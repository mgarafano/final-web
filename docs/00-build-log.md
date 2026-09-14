# Build log

## Environment facts (verified, not assumed)

| Thing | Value |
|---|---|
| Store | Uptown Merch Solutions — uptownmerch145.com, Shopify plan, USD, EDT |
| **Live theme** | **"Dawn" — ID `162803220706`, role MAIN, published 2026-09-13 23:47 UTC** |
| Build theme | "UMS Rebuild 2026" — ID `162803613922`, role UNPUBLISHED |
| Dawn version | 16.0.0 |
| Old live theme | "UMS logo homepage Live Version" (`160521519330`) — now unpublished |
| Backup | "Copy of UMS logo homepage Live Version" (`162803089634`) |
| Staged dupe | "UMS site - Create Your Brand Uptown (staged)" (`162397749474`) |
| Sales channels | Online Store, Point of Sale, Shop, Snapchat Ads, Inbox |

## What this session's tooling can and cannot do

| Capability | Status |
|---|---|
| Read all products, collections, themes, files | ✅ |
| Write theme files to an **unpublished** theme | ✅ verified |
| Duplicate a theme | ✅ |
| Create a theme from a remote zip | ❌ blocked — `themeCreate` returns "Src is empty" |
| Write theme files to the **live/MAIN** theme | ❌ blocked by policy |
| **Publish a theme** | ❌ blocked — Raheem must click Publish in admin |
| Update products, collections, metafields | ✅ |
| Read installed apps | ❌ `appInstallations` — access denied |
| Fetch `cdn.shopify.com` from this container | ❌ egress proxy denies it |

The publish restriction is a good thing here: it makes it impossible for this
session to put anything in front of customers by accident. Go-live is a
deliberate human action.

## Progress

- **2026-09-13** — Audited all 45 products. Created build theme by duplicating the
  clean Dawn. Pushed `assets/ums-brand.css` (palette + nav weighting + cart
  suppression tokens). Wrote `docs/01-product-cleanup-proposal.md`.

- **2026-09-14 — Phase 2, navigation and chrome.**
  - Created menu `ums-main-menu` (Storefront / Organizations / About / Contact).
    The live theme reads `main-menu`, which is **untouched**, so the live site's
    navigation is unchanged.
  - Created pages `/pages/about` (approved copy from brief §6) and
    `/pages/organizations` (placeholder; built in a later phase).
  - Created smart collection `ums-storefront` (rule: tag = `uptown-blanks`, 33 products).
  - Theme settings: brand colour schemes, Archivo/Barlow typography, `cart_type: drawer`,
    squared 2px radii, currency-code suffix off, vendor hidden, social links wired.
  - Header: points at `ums-main-menu`; country and language selectors **off**
    (brief §8/Mobile); announcement bar now carries pickup address and hours.
  - Footer: hunter-green (scheme-3), "Follow on Shop" off, country/language off,
    blocks for address + hours + phone, the all-sales-final policy, and a browse list.
  - Added `sections/ums-globals.liquid` — brand tokens, the Organizations nav
    weighting (desktop pill + mobile filled row, matched on href so it survives
    menu edits), and conditional cart-icon suppression on Organizations pages.

## Additional tooling limits found

| Capability | Status |
|---|---|
| Delete a theme file (`themeFilesDelete`) | ❌ blocked by policy |
| Reach the storefront/preview from this container | ❌ egress proxy denies it — **Raheem must eyeball previews** |

Shopify validates theme files on upsert and writes **nothing** when validation fails.
Confirmed it checks setting ranges/steps, font-picker handles, and section block types.
