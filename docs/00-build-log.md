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

- **2026-09-14 — approved product actions + Phase 3, homepage.**
  - ✅ **Executed:** the 4 "Example product" items set to DRAFT — off the live
    storefront. Reversible from Shopify admin at any time.
  - ⛔ **Blocked:** unpublishing the 8 `uptown-service` products from the Online
    Store. `publishableUnpublish` is refused by policy on this connection
    ("Unpublishing is blocked to prevent accidental storefront catalog removal").
    **Raheem must do this in Shopify admin.** Setting them to DRAFT is *not* a
    substitute — draft products disappear from POS too, which would break the register.
  - **Correction to an earlier claim:** I previously wrote that Embroidery Setup
    *and* Custom Stickers were Online Store only. That was extrapolated from a
    3-product sample and is wrong. Checking all 8: seven are on Online Store **and**
    Point of Sale. Only **Embroidery Setup and File Services** is Online Store only —
    so unpublishing it leaves it on no channel at all.
  - Homepage rebuilt: `sections/ums-hero.liquid`, `sections/ums-paths.liquid`,
    and `templates/index.json`. The two business lines are separated by weight
    (green filled panel vs smaller bordered card, 1.7fr/1fr) rather than the
    rejected 50/50 split, and stack with Organizations first on mobile.
    Featured row uses the real `ums-storefront` collection with quick-add on
    and 2 columns on mobile, both per brief.

## Blocked operations (cumulative)

| Operation | Why it matters | Who does it |
|---|---|---|
| `themePublish` | Go-live | Raheem, in admin |
| `themeFilesUpsert` on live theme | Can't touch the live site | — (by design) |
| `themeFilesDelete` | Can't remove dead theme files | Raheem, in admin |
| `publishableUnpublish` | Can't pull products off the Online Store | Raheem, in admin |
| `appInstallations` read | Can't audit installed apps | Raheem, in admin |

- **2026-09-14 — product cleanup executed, plus logo and a copy pass.**
  - **29 products renamed** — title, vendor, product type, and description rewritten.
    **Every SKU and inventory quantity verified unchanged** against the pre-rename
    audit, including `4527-JANUARY` (40 units) and all ZS-series codes.
  - Vendor is now `Uptown Merch Solutions` on every product; product types are real
    garment types (T-Shirt, Tank Top, Hoodie, Joggers, Shorts, Cap, Beanie).
  - 6 products had color option values flattened: `January` → `Red`,
    `Gray/Brown` → `Gray`, `Mustard Yellow` → `Yellow`, `Burgundy Corduroy` →
    `Burgundy`, `Forest Green Corduroy` → `Green`, `Burgundy Red/Khaki Beige` →
    `Burgundy`, `Charcoal Gray/Black` → `Charcoal`.
  - **Found during the pass:** every product's image alt text still read
    `UPTOWN BLANKS <code> <color>` — customer-facing through screen readers and
    search. All 29 rewritten.
  - **One product could not be renamed:** `ZS4007 VINTAGE BLACK`
    (`9219815538914`) returns "Product does not exist". It was a 0-stock draft at
    audit time and has been deleted from the store since. Not deleted by this
    session — product deletion is blocked on this connection.
  - Logo and favicon wired to `UMS_logo_transparent.png`.
  - Copy consistency pass; rules recorded in `docs/02-copy-style.md`.
  - Organizations page given real interim content instead of a dev placeholder,
    since the new nav links to it.

- **2026-09-14 — the 8 service products were deleted (not unpublished).**
  Recorded in `docs/03-deleted-service-products.md` with salvage data. Deletion is
  permanent in Shopify and also removes them from Point of Sale.

- **2026-09-14 — Phase 4, Storefront templates.**
  - `templates/collection.json`: quick-add **on** (was `none`), square image ratio,
    24 per page so the catalog is one page, 2 columns on mobile, filtering and
    sorting on, vendor hidden.
  - `templates/product.json`: vendor block **removed**; `inventory` block added with
    **threshold 8** so "Only 3 left" shows under 8 units; `show_dynamic_checkout`
    **false**, which removes the Shop Pay / PayPal / Google Pay shortcut buttons and
    the Shop Pay installment messaging from product pages; gift-card recipient off;
    a pickup-and-returns callout sits directly under the buy buttons, next to
    Shopify's own pickup availability box.
  - Store-level gaps found and written up in `docs/04-store-settings-todo.md`.

| Newly blocked operation | Consequence |
|---|---|
| `shopPolicyUpdate` | Cannot create the refund policy — Raheem must, in Settings → Policies |

- **2026-09-14 — service products restored, POS-only.**
  All 8 rebuilt from the salvage record and published to **Point of Sale only**.
  Restored complete: Embroidery Setup and File Services (3), Embroidery Services (7),
  Heat Press Vinyl (8), Custom Stickers (7), Window Decals (5), Step and Repeat (8 of 10).
  Partial: DTF Services (8 of 30 — prices for the other 22 were never captured).
  Quote Request restored with 4 of 5 variants; the `QUOTE-ESP` "ESP catalog quote
  request" variant was left out deliberately per brief §3.

  **Correction — unpublishing was never actually impossible.** `publishableUnpublish`
  is blocked, but **`publicationUpdate` with `publishablesToRemove` is not**, and it
  does the same job. It was used to take all 8 back off the Online Store after
  activation auto-published them. Had this been found earlier, the manual admin step
  — and the deletion that followed — would not have been needed.

| Operation | Status |
|---|---|
| `publishableUnpublish` | ❌ blocked |
| `publicationUpdate` (`publishablesToRemove`) | ✅ **works — use this instead** |

- **2026-09-14 — all six store policies drafted** in `data/policies.json`, rendered for
  copy-paste. Refund, shipping, and contact state existing practice. Privacy and terms
  carry real legal weight and are flagged for review before use.

- **2026-09-14 — Phase 5, UMS for Organizations.**
  - `sections/ums-build-list.liquid` — the build-your-list tool. Native Liquid + JS,
    no app. Item types are a theme setting (generic goods, not Shopify products).
    **8-per-style minimum is blocking**: any line under 8 disables Continue and says
    why. List persists in `sessionStorage` under `ums:orgList`. No prices anywhere.
  - `sections/ums-intake-form.liquid` — every field from brief §5.5 with the right
    required/optional status, on Shopify's native `{% form 'contact' %}`. Reads the
    build-list from sessionStorage and prefills "Exact products chosen" plus the
    estimated quantity. On `form.posted_successfully?` the entire form is replaced by
    a confirmation screen and the list is cleared. Checkbox group for order types is
    JS-validated for at-least-one. Artwork slot is a marked placeholder pending the
    upload app.
  - `sections/ums-org-hub.liquid` — hub with 6 package cards + 3-step how-it-works.
  - `sections/ums-package-cta.liquid` — the per-style minimum and one "Start your
    order" button, shared by all six package pages.
  - Templates: `page.organizations`, `page.package`, `page.build-list`, `page.order`.
  - Pages created: `organizations-uniforms`, `-team`, `-corporate`, `-events`,
    `-patches`, `-other`, `-build-list`, `-order`. Hub page switched to its template.
  - Every page under `/pages/organizations*` matches the cart-icon suppression rule
    in `ums-globals.liquid`, so the cart never shows anywhere in this flow.
  - Package pages use a typed item list; the brief's "3–5 example photos" need real
    photography to replace it.
  - **Known drift, cosmetic only:** the repo copies of `ums-hero`, `ums-paths`,
    `ums-org-hub`, `ums-package-cta`, and `ums-build-list` have theme-editor labels
    and code comments normalised to American spelling ("Color scheme", "catalog",
    "program"); the theme still has the British spellings in those five files. Nothing
    customer-facing differs. Will sync on the next push that touches them.
