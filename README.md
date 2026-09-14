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
  - `locales/en.default.json` — three strings changed: the low-stock line reads
    "Only N left" (brief §4); the caption under a product's price reads "Pickup only at
    241 W 145th St, Harlem — No Shipping." (linked to the Shipping policy) instead of
    Dawn's "Shipping calculated at checkout." (Raheem's wording, applied through Edit
    default theme content); and the quick-add button on product cards says "Add to
    cart" for every product — Dawn says "Choose options" on products with variants,
    which put two different labels in one grid. The file carries Shopify's
    auto-generated comment header above the JSON, exactly as Shopify stores it.
- Everything else on the theme is stock Dawn 16.0.0 and is not mirrored here.

## Pushing theme files

- **The theme is live, and the API refuses writes to a live theme.** Changes go into a
  new unpublished theme that Raheem publishes from admin; the previous live copy stays in
  the library as the rollback. Two ways to make that theme:
  1. **From this repo, no admin click needed** (used for "UMS Live 2026 v2" on
     2026-09-14): `python3 scripts/build-theme-zip.py <dawn-v16.0.0-checkout> out.zip`
     builds the complete theme (stock Dawn v16.0.0 plus `theme/`, which is everything
     the live theme has that Dawn does not). Upload the zip to the store's Files with
     `stagedUploadsCreate` + `fileCreate`, run `themeCreate` with the file's CDN URL
     (`themeCreate` needs a URL that serves the zip with a content length — GitHub
     archive links fail with "Src is empty"), wait until `processing` is false, read
     every file back (checksums for code, parsed content for JSON), then delete the zip
     from Files. The API refuses `themePublish`, so the last step is Raheem's.
  2. Duplicate the live theme in admin (Online Store → Themes → ⋯ → Duplicate), push the
     changed files to the duplicate with `themeFilesUpsert`, read them back.

- Push `sections/*.liquid` and `snippets/*.liquid` first, in their own
  `themeFilesUpsert`; push JSON templates and section groups in a second call. Shopify
  validates a JSON template against the section schema at write time and silently drops
  any setting the schema does not have yet.
- Read every file back after a push. Code files: compare `checksumMd5` with the local
  `md5sum`. JSON files: Shopify reformats them and adds an auto-generated comment, so
  compare the parsed content instead.
- `config/settings_data.json` is deliberately not pushed; the theme editor owns it.
- A JSON template may only carry keys the section's schema defines; Shopify drops
  anything else silently at write time. Dawn 16's featured collection takes
  `quick_add` ("none" / "standard" / "bulk"), not `enable_quick_add` — the homepage
  template carried the wrong key until the fifth review, so the live homepage grid has
  no quick add.
- Muted text in UMS sections (eyebrows, hints, "(optional)") is colored with an explicit
  foreground alpha, never `opacity`. Dawn paints body text at 75% already; stacking
  opacity on top drops small text below the 4.5:1 contrast floor. Measured values are
  in the comment at the top of `sections/ums-globals.liquid`.
- Section CSS loads **before** Dawn's `base.css` (Shopify injects the bundle through
  `content_for_header`). A UMS rule on an element that also carries a Dawn class
  (`page-width`, `button`, `link`, the header menu item) must out-rank Dawn's rule or it
  loses the tie: write `.ums-pkg.page-width`, not `.ums-pkg`.
- Product cards are stretched by `ums-globals` (grid item → card wrapper → card as flex
  items) so the quick-add button sits at the bottom of every card in a row. Dawn relies
  on a `height: 100%` chain for this, which iOS Safari does not resolve; on the phone the
  buttons drifted by a line whenever a title wrapped. The photo box is 4:5 in every grid
  template (collection, homepage, related products, search) with `object-fit: contain`,
  so nothing is cropped and rows stay even.
