# Final review — every requirement in the brief, checked against the store

Reviewed 2026-09-14 against the theme files actually on Shopify (not just the repo),
the live catalog and settings, and the UMS code line by line. Every repo file was
compared to its theme copy by MD5 and matched.

Legend: **done** = built and verified · **admin** = needs Raheem in admin ·
**decision** = needs Raheem's call · **fixed** = found in this review and corrected.

## §1 Business model

| Requirement | Status | Evidence |
|---|---|---|
| Two lines, one brand, no 50/50 split | done | Homepage: hero → two weighted panels → storefront grid. Organizations first and filled green, Storefront outlined. |
| Organizations weighted as primary | done | Nav pill, mobile green row, first hero button, larger panel. |
| Storefront easy to find | done | Nav item, hero button, homepage panel, homepage product grid with "View all". |

## §2 Brand

| Requirement | Status | Evidence |
|---|---|---|
| Tagline "Bringing Brands to Life." | done | Homepage hero heading; About page closing line. |
| Logo mark in header, favicon from transparent file | done | `logo` and `favicon` both `UMS_logo_transparent.png`, width 130 (104 on phones). |
| Palette: hunter green, white, gray; no orange, no purple | done | Five schemes: white, `#F6F5F5`, green, ink, `#838388`. Nothing orange or purple in any file. |
| Typography revisited | done | Archivo 700 headings, Barlow 400 body. |

## §3 Navigation

| Requirement | Status | Evidence |
|---|---|---|
| Storefront · Organizations (weighted) · About · Contact | done | Menu `ums-main-menu` in that order; Organizations styled as a filled pill on desktop, filled row on mobile. |
| Old labels gone; ESP gone from the new site | done | New theme has no ESP reference. The old ESP page was unpublished and redirected at go-live on 2026-09-14. |
| Footer: social, policies, hours/location, payment icons | done | Footer group: visit block, pickup block, menu, social on, policies on, payments on, newsletter in footer only. |
| Cart icon hidden on Organizations pages | done | `ums-globals` hides it on every `/pages/organizations*` path, server-side. |

## §4 Storefront

| Requirement | Status | Evidence |
|---|---|---|
| Fixed-price finished goods, no customization language | done | 29 products; descriptions scanned for custom/blank/decorate/DTF/print/ship language: none. |
| Pickup only, no shipping anywhere | done | Zero shipping zones, ships to no countries. Cart, drawer, product page, footer, announcement all say pickup. Checkout's Ship tab is a plan limitation Raheem accepted (docs/04 §8). |
| All-sales-final on product page and cart, plus Refund policy | done | Product `pickup_note` block, cart note, footer, Refund policy live. |
| Catalog audited, strays excluded | done | 29 storefront products active and online; 8 service products POS-only; helper product unlisted. |
| Low-stock count under 8 | done | Inventory block, threshold 8, quantity shown. |
| Quick add on, desktop and mobile | done | Collection grid and homepage grid, `quick_add: standard`. |
| Product photos: clean product-only shots | done | Every product has an image (supplier product shots). |

### §4.1 Product data standard

| Requirement | Status | Evidence |
|---|---|---|
| Titles `Garment — Color`, no vendor or style code | done | All 29 follow it. Multi-color headwear (four caps/beanies) keeps color as a variant option instead of in the title, which is the correct modelling. |
| SKUs preserved | done | Every variant has its SKU; none altered. |
| Vendor changed | done | All 29 read "Uptown Merch Solutions"; vendor hidden everywhere in the theme. |
| "January" and other option errors | done | No option value errors remain; caps carry real Color values. |
| Descriptions: one sentence + bullets, no decoration language | done | Scanned all 29. |
| Garment type and color as filterable data | done | Product type on all 29. Color is now a real option on all 29: 12 headwear products already had it; the 17 soft goods got a one-value option in the final review (decision A). |

## §5 Organizations

| Requirement | Status | Evidence |
|---|---|---|
| Package-based, no catalog, no cart | done | Hub with six packages, three steps, minimum note; cart icon hidden. |
| Six packages | done | Uniforms, team/spirit, corporate, events, patches, something else. |
| Package page = who it's for, examples, minimum, one button | done, one gap | Description and typical-pieces list, 8-per-style minimum, "Start your order". Example *photos* are a text list until photography exists (open since Phase 5). |
| No pricing, no turnaround anywhere | done | Checked hub, packages, list tool, form, confirmation copy. |
| Build your list: separate step, 8-per-style blocking, prefills form | done | `ums-build-list`: Continue refuses under 8; list carried via sessionStorage into "Exact products" and the quantity. |
| Intake fields and required/optional per §5.5 | done | All eleven fields, required flags as specified, structured contact fields. |
| Artwork upload, native, no app | done | File → hidden $0 helper product → Shopify CDN URL → hidden field. 20 MB cap, fallback to email. Second review: the picker setting had been lost on the theme (see below); restored, with the variant ID also stored as a text setting. |
| Multiple product types per submission | **fixed** | Ticked boxes shared one field name and Shopify keeps only the last one, so a two-type request would have arrived as one. Now joined into a single hidden field ("Team and spirit wear, Custom patches"). |
| Routing to orders@ and mgarafano@ | done / admin | Store email is orders@ (verified). Forwarding rule to mgarafano@ is still Raheem's. |
| Distinct confirmation screen, no customer email | done | Form is replaced by a confirmation state; nothing is sent to the customer. |
| Helper product not purchasable by accident | **fixed** | Its product page now uses a template that shows "Nothing for sale here" with two buttons instead of a $0 buy button. |

## §6 About, Contact, social

| Requirement | Status | Evidence |
|---|---|---|
| About copy as approved | done | Page body matches the brief, with one change Raheem asked for in the final review: "founded in 2024" (was 2023). |
| Contact: Name, Email, question, required | done | Native form; no app. POWR not used. |
| Contact page content: hours, address, phone, email, policy note, social | done | Page body carries all of it plus the "still do custom work?" answer. |
| Social: TikTok and Instagram @145uptownmerch | done | Footer icons and Contact page handles. |

## §7 Cart and checkout

| Requirement | Status | Evidence |
|---|---|---|
| Real drawer with backdrop | done | `cart_type: drawer`. |
| Single green Check out; no express buttons on cart or product | done | Removed from cart footer; product page `show_dynamic_checkout: false`. |
| Installments messaging off | done | Disabled by Raheem in Payments. |
| No shipping copy in cart | done | Pickup note replaces Dawn's line in cart and drawer. |
| Dead block and newsletter under checkout gone | done | Neither exists in Dawn 16. |
| Brand palette through checkout | done (unverifiable here) | Applied by Raheem in the checkout editor. |
| Pickup details and hours in the cart | done | Cart note carries address, hours, "we don't ship", all sales final. |

## §8 Mobile

Selectors off, green Organizations row, two-column grid with quick add, drawer, full-width
buttons, restacked list rows, 80% logo. Raheem's phone pass is the final check.

## Store settings and go-live

| Item | Status |
|---|---|
| Six policies exist | done — five wording nits, see decision C |
| Store email orders@ | done |
| Pickup instructions on stocked location | done |
| Shipping zones removed | done |
| Old pages unpublished, 32 redirects, 17 collections hidden | done |
| Three live-menu items (order form, ESP page, Uptown Blanks) | done at go-live 2026-09-14: pages unpublished, collection hidden, all three redirected |
| Forwarding rule + test submissions | admin |
| Phone pass | admin |

## Fixed in this review

1. Intake form: multiple order types now all arrive (was: only the last one).
2. Hero heading is escaped like every other text setting.
3. The artwork helper product's page no longer offers a $0 purchase.
4. Repo copy of the policies: American spelling and en-dash ranges (see decision C).

## Decisions — answered 2026-09-14

- **A. Color as a filter — done.** A one-value Color option was added to the 17
  single-color soft goods (Arctic Blue, Mint, Gray, Black, White, Navy, Natural,
  Vintage Denim, Bubble Gum, Sky Bomb, Black Smoke), position 2 after Size, variant
  strategy "leave as is". Tested on one product first: every SKU, price, and inventory
  quantity unchanged; variant titles read "M / Arctic Blue". Then the other 16, no
  errors. Every storefront product now has Color as real option data.
- **B. About page — done.** "Founded in 2023" → "founded in 2024", per Raheem: 2024 is
  when it opened. Live now (page bodies are store data).
- **C. Policy wording — optional, still open.** Five word-level edits (spelling and
  dash style, not fonts). Listed in `docs/04` §9. Cosmetic; can be skipped.
- **D. Customer accounts — done by Raheem.** Verified: `DISABLED`. The header's login
  icon disappears with it.
- **E. "Home page" collection — done by Raheem.** Verified off the Online Store.
- **F. Collection filters.** Still worth a glance on the storefront page after
  publishing; remove a "Vendor" filter if one shows.
- **G. POWR — deleted by Raheem.**

## Not verifiable from here, by design

Rendered pages (no storefront access from this environment), checkout branding, and
the email delivery itself. Raheem's phone pass and test submissions cover these.

## Second review — 2026-09-14, rendered pass

Every UMS page rendered locally with Dawn's CSS and the theme's settings, screenshotted
at 1280px and 390px, measured, and checked again against the store.

| Check | Result |
|---|---|
| Home, Organizations hub, package page, Build your list, order form, Contact, cart note (page and drawer), internal product page — desktop and phone | Render correctly; no horizontal overflow at 390px on any page. |
| Column alignment | **Fixed.** Package CTA box and contact form now share the body column exactly (`page-width--narrow`). |
| Text links | **Fixed.** "Edit the list" was browser-default blue; now inherits the text color. Every other anchor carries a class. |
| Post-submit confirmation screens (intake, contact) | **Fixed.** Focus ring and shadow no longer drawn around the "Thanks" block. |
| Artwork upload on the theme | **Fixed.** The theme's `page.order.json` had lost `artwork_product`, so the picker never rendered. Cause: Shopify validates a template against the section schema when the template is written; a template pushed alongside a schema change loses the new setting. Restored, plus `artwork_variant_id` as a second source; read back with both present. |
| Theme files | 12 code files match the repo by MD5; 9 JSON templates and groups match in content; `layout/theme.liquid` and every asset are stock Dawn 16 except the superseded `ums-brand.css`. |
| Pages | 24 pages read in full: no `mgarafano@` anywhere; `order-form` and `bulk-catalog` were the last old pages standing and went down at go-live. |
| Helper product | `Artwork upload`: UNLISTED, on the Online Store, $0, available for sale, `product.internal` template. |

Still optional, unchanged from the first review: policy wording (Contact and Terms use
hyphens in "Tuesday-Saturday, 11am-8pm"; Shipping still says "Tuesday to Saturday, 11am
to 8pm"), Dawn's "Low stock: N left" wording, the "Powered by Shopify" footer link, a
homepage title and meta description, the staff "New order" notification recipient, a
preview of the order confirmation email for pickup, the Vendor filter in Search &
Discovery, deleting the old themes after go-live, SKU `4527-JANUARY`. One new copy
nit: the About page says "2024" in two consecutive sentences ("opened its doors in
Harlem in 2024" and "was founded in 2024"); dropping the second date reads better.

## Third review — 2026-09-14, brief re-read, Theme Check, contrast, catalog

| Check | Result |
|---|---|
| Brief §1–§10 re-read line by line against the build | Two gaps found and closed: the tagline was absent from the Organizations section (§2), and the low-stock line did not use the brief's "Only N left" wording (§4). |
| Shopify Theme Check on the complete theme (110 text files pulled from Shopify) | No errors or warnings in UMS code apart from the expected shared-class notices; remaining notices are in stock Dawn files. |
| WCAG AA contrast, measured on all ten rendered pages | **Fixed.** 15 small-text elements were between 3.6:1 and 4.4:1; every one now passes (explicit alpha instead of stacked opacity). |
| Copy consistency (hours, address, phone, final-sale line) across theme, pages, policies, pickup instructions | Consistent. Footer pickup line now scoped to storefront orders. |
| Catalog, product by product | 29 storefront products pass every check; 8 POS-only services off the Online Store; helper product unlisted. |
| Navigation, redirects, blog, collections, policies, files, themes, locations | All as planned; 33 redirects match the go-live map; live theme untouched. |
| Pages | 24 pages: the new pages published, the old ones unpublished, `order-form` and `bulk-catalog` waiting for go-live. |

Left as they are, for Raheem: the Contact page FAQ wording on shipping, the doubled
"2024" on About, hyphens versus en dashes in the policies, the "Products" collection
at `/collections`, a purpose-made favicon crop, local pickup still enabled on "Shop
location", the forwarding rule, and photographs for the package pages.

## After Raheem's desktop screenshots — 2026-09-14

| Check | Result |
|---|---|
| "UMS for Organizations" pill on the Organizations pages | **Fixed.** Text stays white on the current page; Dawn's active-item color and underline are out-ranked. |
| Package page box against the footer | **Fixed.** 64px of white below the box on desktop, 48px on phones. |
| Same cause elsewhere | **Fixed.** Order form, build list, contact form, internal page and business-line cards regain their vertical spacing; the two forms return to a 72–76rem column on desktop. |
| Root cause | Section CSS loads before Dawn's `base.css`; equal-weight rules on shared elements lost the tie. Documented in `ums-globals` and the README. |

## Final review after go-live — 2026-09-14

Run against the live theme and the live store, not a preview.

| Check | Result |
|---|---|
| Live theme file for file against the repo | All 12 code files and the locale match by checksum; all 10 JSON templates and groups match in content; nothing edited in the theme editor since the last push. |
| Rendered audits on the live files | Contrast: every page passes WCAG AA. No horizontal overflow at phone width. Package box and contact form share the body column exactly. Box clears the footer by 64px (48px on phones). Nav pill white on its own page. Forms hold their 72–76rem column. Theme Check: nothing in UMS code. |
| Checkout inputs | Shipping profile has no zones, so no shipping rate can be offered; local pickup on the stocked location with the corrected instructions; accounts disabled; store email and contact email are orders@. |
| Content and navigation | 11 pages published, every old page down; `ums-main-menu` in header and footer; 36 redirects; Online Store collections are UMS Storefront and the built-in Products listing; helper product unlisted, addable, untracked. |
| Rollback | "Dawn" unpublished in the library; one click restores it. |

Open, all Raheem's call: the Contact page shipping answer, the doubled "2024" on About,
policy hyphens, a purpose-made favicon, "Shop location" still offering pickup with its old
instructions and no stock, the forwarding rule, photos for the package pages, and deleting
the four old themes once the new site has settled.

## Fixes applied — 2026-09-14, after the final review

Raheem: "please fix all issues identified." Everything the API can reach is done and read
back; the rest is listed with the exact steps.

| Item | Result |
|---|---|
| Contact page, "Do you ship?" | **Done.** Now reads "No — storefront orders are picked up in store. Group orders are arranged directly with our team, including how you'll receive them." Same line of thought as the footer and the Shipping policy. |
| About page, "2024" twice | **Done.** Second sentence now "UMS was founded by someone who grew up right here in Harlem…"; the opening year stays in the first sentence. |
| "Shop location" offering pickup | **Done.** Local pickup disabled on that location (no stock, no address, old instructions); read back as no pickup settings. The stocked location is the only pickup point. The location itself stays active — `docs/04` §2. |
| Policy hyphens and the Terms cross-reference | **Admin.** `shopPolicyUpdate` refused (`write_legal_policies`). Four find-and-replace edits in `docs/04` §9; `data/policies.json` matches. |
| Favicon | **Admin, needs an image.** The favicon is the full 1958×1434 logo; at 32px it reads as a smudge. Needs a square crop of the logo's main mark, without any small lettering, exported as a 512×512 PNG on a transparent background, then Online Store → Themes → Customize (UMS Live 2026) → Theme settings → Favicon. That is a theme-editor setting, not a code push, so it needs no duplicate theme. No image bytes are reachable from this session, so the crop cannot be made here. |
| Homepage meta description | **Done by Raheem** (read back as the shop description on 2026-09-14): "Custom merch printed and embroidered in-house in Harlem. Ready-to-wear pieces for pickup at 241 W 145th St, and branded gear for schools, teams, and companies." |
| Photos for the package pages | **Raheem.** 3–5 example photos per package (brief §5). The typed list stands in until they exist. |
| Forwarding rule orders@ → mgarafano@ | **Raheem.** In the orders@ mailbox — `docs/04` §6. Then one test submission through each form. |
| Old themes | **Two deleted by Raheem** ("UMS site - Create Your Brand Uptown (staged)" and "UMS logo homepage Live Version"). Left: "Copy of UMS logo homepage Live Version" (delete when ready) and "Dawn", the one-click rollback. |
| "Products" collection at `/collections` | **Left as is, on purpose.** Hiding the built-in `all` collection would break `/collections/all` links; it lists the same 29 products. |

## Product page caption — 2026-09-14

Raheem: the "Shipping calculated at checkout" line under every product price contradicts
the pickup-only store. It is Dawn's `products.product.shipping_policy_html` string, printed
whenever a Shipping policy exists. Replaced in the repo with "Pickup only at 241 W 145th
St, Harlem — we don't ship.", "we don't ship" linked to the Shipping policy. Not yet live:
the API refuses writes to the live theme; the two ways to apply it are in `docs/04` §10.

## Fifth review — 2026-09-14, the most critical pass

Aimed at what a rendered check cannot show: stock Dawn behavior driven by store data (the
shipping caption was one of those), catalog data as the theme will display it, channel
and publication state, and the live theme measured against Dawn itself.

| Check | Result |
|---|---|
| Live theme against stock Dawn v16.0.0, every file | 345 Dawn files present and identical by checksum, apart from the four known edits (`settings_schema`, `en.default.json`, `main-cart-footer`, `cart-drawer`); 16 UMS additions; JSON files differ only by Shopify's reformatting — 15 templates, groups and config compared as parsed content: identical to the repo, except the caption string (Raheem's wording, repo synced) and one dead key (below). |
| Repo vs live | `templates/index.json` carried `enable_quick_add`, a key Dawn 16 does not have; Shopify dropped it, so the homepage grid has no quick add. Key removed from the repo; enabling it is a theme-editor choice (`docs/04` §11). |
| Store | Password protection off. Primary domain `uptownmerch145.com` with SSL, www and the myshopify domain alongside. Shop name "Uptown Merch Solutions" (drives the title tag and the copyright line). Store and contact email orders@. Meta description set. Customer accounts disabled. Ships to no countries. |
| Pages | 11 published; every template each page names exists in the live theme; 17 old pages unpublished. |
| Redirects | 36; every target is a live page, collection, or the homepage; no chains. |
| Helper product | Status `UNLISTED` — Shopify itself keeps it out of search, collections and recommendations, and out of `/collections/all`; published to the Online Store so the cart endpoint accepts it; `internal` template. |
| Catalog, 29 products | Sizes in the right order on every product (XS…3X, YXS…YL); one image each with "<Name> in <Color>" alt; no compare-at prices, so no false sale badges; inventory tracked, no overselling; one sold-out variant (Women's Crop Long Sleeve — White, XS) shows as unavailable, correctly. Descriptions carry no shipping, custom or blank-goods language. Size labels differ between families ("2X, 3X" on the Heavyweight Tees, "2XL" on the Garment-Dyed Tee) — cosmetic, both read fine. |
| Catalog, found | **Photos are cropped in every grid**: apparel shots are portrait, cards are square with cover-fit, so a sixth is cut top and bottom. **Pagination**: 24 per page splits 29 products across two pages. **No product category** on any product (Shopify Tax's NY clothing exemption depends on it). **Hats not on Point of Sale** (12 of 29). Three POS tile collections on no channel. All in `docs/04` §11 with the one-setting fixes. |
| Product page | Now says "Pickup only" three times (caption under the price, the text block under the buy button, Dawn's pickup-availability line). Trim the block to the all-sales-final sentence — a theme-editor edit. |
| Forms | Intake and contact forms re-read line by line: required fields, Shopify's error list, the artwork upload's size cap, failure message, and cleanup of the $0 helper line, and the submit guard while an upload is in flight. Nothing to change. The upload has been verified in code and locally, not yet on the live store — one live test with a file attached is the remaining step. |
| Locations | Stocked location: full address, phone, pickup instructions, 24-hour window. "Shop location": pickup off, still active for POS. |
| Themes | Two old themes gone (Raheem). "Copy of UMS logo homepage Live Version" and the "Dawn" rollback remain. |
| Social preview | No social sharing image is set (Preferences); shared links show no image. |

## After "fix 1, 3, 5, 6" — 2026-09-14

| Item | Result |
|---|---|
| 1. Cropped grid photos | In "UMS Live 2026 v2": image ratio "adapt" on the collection grid, homepage featured collection, and related products. |
| 3. Hats off Point of Sale | **Live.** All 12 published to POS through the API, read back. |
| 5. Tripled pickup line | In v2: the product-page text block now reads "All sales are final — no refunds or exchanges." |
| 6. Two-page collection | In v2: 36 products per page. |

v2 was built from stock Dawn v16.0.0 plus the repo (`scripts/build-theme-zip.py`), created
with `themeCreate`, and verified file by file (360 of 360). It is unpublished until Raheem
publishes it; the live theme is untouched.

## Product cards — 2026-09-14, after v2 went live

Raheem's phone screenshots: quick-add buttons in one row at different heights, and two
different labels ("Add to cart" / "Choose options"). Cause and fix in `docs/04` §12. Fixed
in "UMS Live 2026 v3" (unpublished until Raheem publishes it): cards stretched without
percentage heights, one label at one size, and the photos exactly as V1 showed them (a 4:5
box, fitted and then filled, was tried and rejected; Raheem asked for the V1 photos back).
Measured in a local rebuild of Dawn's grid with the store's settings: buttons level in
every row at phone and desktop widths. Theme Check clean.

Raheem then deleted v3 and narrowed the ask to the buttons only, uploaded to the theme
named "UMS Live 2026". Done in place (two files), read back; that theme's photos are
untouched. Details in `docs/04` §12, "Final state".
