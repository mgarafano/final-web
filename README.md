# UMS Website Rebuild

Rebuild of the Uptown Merch Solutions Shopify storefront (uptownmerch145.com).

- `docs/` — the authoritative requirements brief, plus working proposals that need
  Raheem's sign-off before anything is executed against the live store.
- `theme/` — source of truth for the Shopify theme **"UMS Live 2026"** (theme ID
  `162803613922`), published on 2026-09-14. Every file here matched the live theme at
  go-live (checksums for code, content for JSON).

## Ground rules

- The live store serves real customers. Nothing is published without explicit approval.
- Product data (titles, vendor, options, descriptions) is **store-wide, not theme-scoped**.
  Changing it changes the live site immediately, so every product change is proposed in
  `docs/` and executed only on approval.
- SKUs, variant IDs and inventory quantities are never altered during the rename work.

## What lives where in `theme/`

- `sections/ums-*.liquid`, `snippets/ums-*.liquid` — every UMS customization. These
  files are ours; Dawn never ships them.
- `templates/*.json`, `sections/*-group.json`, `config/settings_data.json` — Dawn
  templates and settings as configured for UMS.
- **Modified Dawn files** (the only stock files edited, each edit marked `UMS:` inline):
  - `sections/main-cart-footer.liquid` — pickup-only note replaces the tax/shipping
    line; express checkout buttons removed.
  - `snippets/cart-drawer.liquid` — pickup-only note replaces the tax/shipping line.
  - `config/settings_schema.json` — one settings group appended ("UMS cart note").
  - `locales/en.default.json` — two strings changed: the low-stock line reads
    "Only N left" (brief §4), and the caption under a product's price reads "Pickup
    only at 241 W 145th St, Harlem — we don't ship." (linked to the Shipping policy)
    instead of Dawn's "Shipping calculated at checkout." The file carries Shopify's
    auto-generated comment header above the JSON, exactly as Shopify stores it.
- Everything else on the theme is stock Dawn 16.0.0 and is not mirrored here.

## Pushing theme files

- **The theme is live, and the API refuses writes to a live theme.** To change anything
  now: duplicate the live theme (Online Store → Themes → ⋯ → Duplicate), push the changed
  files to the duplicate, read them back, check the preview, then publish the duplicate
  from admin. The previous live copy stays in the library as the rollback.

- Push `sections/*.liquid` and `snippets/*.liquid` first, in their own
  `themeFilesUpsert`; push JSON templates and section groups in a second call. Shopify
  validates a JSON template against the section schema at write time and silently drops
  any setting the schema does not have yet.
- Read every file back after a push. Code files: compare `checksumMd5` with the local
  `md5sum`. JSON files: Shopify reformats them and adds an auto-generated comment, so
  compare the parsed content instead.
- `config/settings_data.json` is deliberately not pushed; the theme editor owns it.
- Muted text in UMS sections (eyebrows, hints, "(optional)") is colored with an explicit
  foreground alpha, never `opacity`. Dawn paints body text at 75% already; stacking
  opacity on top drops small text below the 4.5:1 contrast floor. Measured values are
  in the comment at the top of `sections/ums-globals.liquid`.
- Section CSS loads **before** Dawn's `base.css` (Shopify injects the bundle through
  `content_for_header`). A UMS rule on an element that also carries a Dawn class
  (`page-width`, `button`, `link`, the header menu item) must out-rank Dawn's rule or it
  loses the tie: write `.ums-pkg.page-width`, not `.ums-pkg`.
