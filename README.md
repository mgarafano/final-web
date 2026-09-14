# UMS Website Rebuild

Rebuild of the Uptown Merch Solutions Shopify storefront (uptownmerch145.com).

- `docs/` — the authoritative requirements brief, plus working proposals that need
  Raheem's sign-off before anything is executed against the live store.
- `theme/` — source of truth for the new Shopify theme. Files here are pushed to the
  unpublished theme **"UMS Rebuild 2026"** (theme ID `162803613922`).

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
- Everything else on the theme is stock Dawn 16.0.0 and is not mirrored here.

## Pushing theme files

- Push `sections/*.liquid` and `snippets/*.liquid` first, in their own
  `themeFilesUpsert`; push JSON templates and section groups in a second call. Shopify
  validates a JSON template against the section schema at write time and silently drops
  any setting the schema does not have yet.
- Read every file back after a push. Code files: compare `checksumMd5` with the local
  `md5sum`. JSON files: Shopify reformats them and adds an auto-generated comment, so
  compare the parsed content instead.
- `config/settings_data.json` is deliberately not pushed; the theme editor owns it.
