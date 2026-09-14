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
