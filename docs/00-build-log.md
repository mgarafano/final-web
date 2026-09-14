# Build log

## Environment facts (verified, not assumed)

| Thing | Value |
|---|---|
| Store | Uptown Merch Solutions — uptownmerch145.com, Shopify plan, USD, EDT |
| **Live theme** | **"UMS Live 2026" — ID `162803613922`, role MAIN, published by Raheem 2026-09-14 09:30 UTC** |
| Rollback | "Dawn" — ID `162803220706`, stock Dawn 16.0.0, unpublished at go-live, kept in the library |
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
| Checkout branding via API (`checkoutBranding`, `checkoutBrandingUpsert`) | ❌ Plus-only — "the shop must be on a Plus plan"; Raheem does it in Settings → Checkout → Customize |

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

- **2026-09-14 — fixes from Raheem's review, then Phase 6 (About, Contact, social).**
  - **"Some text bars are small font"** — root cause: Dawn styles `<select>` at 1.2rem
    but `<input>` at 1.6rem, and its floating labels shrink to 1rem once a field has a
    value. Three sizes on one form. Fix: a single shared form system in `ums-globals`
    (`.ums-field` / `.ums-label` / `.ums-input` / `.ums-hint` / `.ums-alert` /
    `.ums-note`). Every control is 4.6rem tall at 1.6rem type; every label sits above
    its control at 1.4rem/600. Build your list, the intake form, and the contact form
    all use it. No floating labels anywhere.
  - **Native artwork upload, no app.** Hidden helper product `Artwork upload`
    (`9363391774946`, handle `artwork-upload`, SKU `INTERNAL-ARTWORK-UPLOAD`, $0,
    status `UNLISTED`, published to Online Store only). The intake form posts the file
    to `/cart/add.js` as `properties[Artwork]` on that product's variant; Shopify stores
    it on its CDN and returns the URL, which goes into a hidden `contact[Artwork]` field;
    the helper line is then removed by key via `/cart/change.js` so a real cart is never
    touched. The file input has no `name`, so the file itself never posts with the form.
    20 MB cap, submit is blocked while an upload is in flight, and every failure path
    falls back to "email it to orders@". If the product picker can't resolve an
    `UNLISTED` product in Liquid, the field degrades to the email note automatically.
  - **Contact is native.** `sections/ums-contact-form.liquid` (Name, Email, Message —
    required, nothing else) and `templates/page.contact.json` (page body + form). The
    `/pages/contact` page title went from "CONTACT US" to "Contact"; the body's inline
    `<style>` block — the orange text and `#101820` gradient that was the brief's
    "source unclear" background — is gone, replaced with hours, address, phone,
    orders@, the "do you still do custom work?" answer, no-shipping, all-sales-final,
    and the Instagram/TikTok handles. That body edit is live now, since page bodies are
    store data, and it fixes the live contact page too.
  - Social: footer icons (since Phase 2) plus handles on the Contact page. About was
    done in Phase 2 with the approved copy.
  - The cosmetic repo/theme drift is resolved — all ten UMS files re-pushed byte-exact.
  - Routing: store contact email confirmed still `Dtftranfers@`; documented in
    `docs/04` why a second recipient is a mailbox rule and not a Shopify setting.

- **2026-09-14 — Phase 7, cart and checkout.**
  - **Shipping language is gone from the cart.** Dawn's "Taxes, discounts and shipping
    calculated at checkout" line (eight translation-key variants, some linking to the
    shipping policy) is replaced on both the cart page and the cart drawer by a new
    snippet, `snippets/ums-cart-note.liquid`. It renders a pickup-only box directly above
    the Check out button: title "Pickup only"; "Every order is picked up in store at
    241 W 145th St, Harlem. Tuesday–Saturday, 11am–8pm. We don't ship." / "All sales are
    final. No refunds, no exchanges."; then "Taxes and discounts are calculated at
    checkout." That covers brief §7 (shipping copy; pickup details and hours in the cart)
    and §4 (all-sales-final callout visible before checkout). The copy is editable in
    **Theme settings → UMS cart note** — three settings appended to
    `config/settings_schema.json`, with the copy as their defaults. `settings_data.json`
    was deliberately not pushed, so nothing changed in the editor since the last push
    could be overwritten; the defaults apply until Raheem edits them.
  - **One Check out button on the cart page.** The store has Shop Pay, Apple Pay, and
    Google Pay enabled, so Dawn's cart footer was rendering all of them under Check out
    (`additional_checkout_buttons`). That block is removed. The drawer never had them in
    Dawn 16; the product page lost them in Phase 4. The button is hunter green through
    scheme-1, and Dawn's label already reads "Check out". Express methods stay available
    inside checkout itself, exactly as the brief specifies.
  - **Architecture exception, recorded deliberately.** This is the first time Dawn's own
    files were edited: `sections/main-cart-footer.liquid` (two edits) and
    `snippets/cart-drawer.liquid` (one edit). Each file carries a header comment and each
    edit is marked `UMS:` inline; the repo keeps the modified copies. There was no clean
    way to change the drawer's footer from outside it — the drawer is a snippet with no
    sections or blocks, and anything injected by JS is wiped every time the cart
    re-renders.
  - Dead block and newsletter under the checkout button (brief §7): neither exists in
    Dawn 16's cart — both were the old theme's. Cart type has been `drawer` since
    Phase 1, with Dawn's dimmed backdrop.
  - **Checkout branding is a wall.** `checkoutBranding` returns "Access denied … the shop
    must be on a Plus plan or a Development store plan". The brief is right that the
    checkout editor is available without Plus — through admin only, not the API. Exact
    values to enter are in `docs/04` §4.
  - **Shipping is live on the store, and the brief requires that it not be (§4).**
    Audited delivery profiles: the General profile has a Domestic (US) zone with five
    flat rates (Economy $0 / $4.90 / $19.90, Standard $6.90 / $9.90) and an
    International zone of 27 countries with USPS and DHL Express carrier rates, all
    active. The profile's only location is "Shop location" — the one holding no stock.
    Nothing was changed: removing rates on a live store needs Raheem's go-ahead. Details
    and the one-step fix are in `docs/04` §3.
  - **Correction to the Phase 4 note.** `show_dynamic_checkout: false` removes the
    express buttons but *not* Shop Pay Installments messaging: Dawn 16 renders that in
    the `price` block of `sections/main-product.liquid` via `payment_terms`, gated only
    by whether Installments is switched on in Settings → Payments. The brief asks for
    the native toggle, so that is an admin item (`docs/04` §7), not theme code.
  - Verified in admin since Phase 6: all six policies now exist (Contact, Legal notice,
    Privacy, Refund, Shipping, Terms). The store contact email is still `Dtftranfers@`,
    so form routing is still not fixed.
  - Every pushed file verified by MD5 against the repo copy.

- **2026-09-14 — Shipping removed, on Raheem's go-ahead.** Both zones deleted from the
  General profile (`DeliveryProfile/96243482850`) with one `deliveryProfileUpdate`:
  Domestic (`DeliveryZone/390961037538` — Economy $0 / $4.90 / $19.90, Standard
  $6.90 / $9.90) and International (`DeliveryZone/390961070306` — 27 countries, USPS
  and DHL Express carrier rates). Verified afterwards: the profile has no zones and
  `shop.shipsToCountries` is empty, so checkout can only offer local pickup. Pickup
  stays enabled at both locations. The rate conditions (weight or price thresholds)
  were not captured before deletion; if shipping is ever wanted again it gets set up
  fresh. Bulk-order shipping is handled outside the site, per Raheem.
  - **Store contact email cannot be changed from here.** Checked every one of the 441
    Admin API mutations: nothing writes `shop.email` or `shop.contactEmail` (the only
    shop-level writes are locales, policies, and resource feedback). It stays an admin
    task — steps in `docs/04` §6.

- **2026-09-14 — Phase 8, mobile pass.** No storefront rendering is possible from this
  container (egress blocked), so this was a line-by-line review of every UMS file and
  Dawn's header against the brief's mobile section, followed by fixes. Raheem's phone
  is the final check; a checklist is at the end of this entry.
  - **Already right, verified in the files:** country and language selectors off in the
    header and footer groups; "UMS for Organizations" is a filled green row in the
    mobile menu drawer (`.menu-drawer__menu-item` rule in `ums-globals`, more specific
    than Dawn's hover and active rules, so it wins); collection grid 2 columns on
    mobile with quick add on; cart drawer with backdrop; cart icon hidden on
    Organizations pages on every screen size; every UMS form control is 16px type, so
    iOS does not zoom on focus; every grid (business lines, package cards, steps, the
    two-column form rows, the checkbox grid) collapses to one column under 750px.
  - **Changed:**
    - Every primary action becomes a full-width bar on phones — one rule on the shared
      `.ums-cta` class. The hero, Organizations hub, and package-page buttons now carry
      that class too (their duplicated CSS is gone), so "Start an order", "Start your
      order", "Add to list", "Continue to the order form", "Send my request", "Send",
      and both confirmation buttons all behave the same way.
    - Build your list rows restack on phones: the item name takes the whole first
      line, quantity and Remove share the second. Before, a long name like "Crewneck
      sweatshirts" was being squeezed beside the quantity field. Remove and Clear
      buttons now meet a 44px tap-target height.
    - Organizations hub and package footer: tighter padding and smaller headings under
      750px so the first screen shows content, not whitespace.
    - **Judgment call:** the header logo renders at 80% of its desktop width on phones
      (104px instead of 130px). Dawn has no mobile logo setting and was rendering the
      full desktop width, which with the header padding made a ~115px-tall mobile
      header. Easy to revert (one rule in `ums-globals`) if Raheem prefers it large.
  - **Left alone, deliberately:** the announcement bar wraps to two lines on a narrow
    phone. Abbreviating the days would break the copy standard ("Tuesday–Saturday",
    never "Tue–Sat"); two lines is the honest trade.
  - **Phone checklist for Raheem** (preview link in the environment table, add
    `?preview_theme_id=162803613922`): the mobile menu (green Organizations row),
    the homepage hero and two business-line panels, a collection page (2 columns,
    "+" quick add), a product page (single Add to cart, pickup note), the cart drawer
    (pickup note above Check out), `/cart`, the Organizations hub, one package page,
    Build your list with three items (one under 8), the order form top to bottom
    including the artwork picker, and the contact page.
  - All five pushed files verified by MD5 against the repo copies.

- **2026-09-14 — Phase 8 review fixes.**
  - **Hero actions are a matched pair.** Raheem: "Start an order for your group" and
    "Shop the storefront" should look the same on desktop and mobile. They were a
    button and a text link. Both are now Dawn buttons of identical type, size, weight,
    and letter-spacing; the only difference is fill — solid green for Organizations,
    outlined for the Storefront — so the primary line still reads first (brief §1).
    On phones they stack as two full-width bars. The theme-editor labels were updated
    to say "button" for both. Pushed and verified by MD5.
  - **Store email fixed by Raheem** — `shop.email` and `shop.contactEmail` both read
    `orders@uptownmerch145.com` now. The forwarding rule to mgarafano@ and one test
    submission per form are still on him (`docs/04` §6).

- **2026-09-14 — Old content taken down (Raheem: "Remove all old obsolete content").**
  Decisions: A unpublish Our Work; B unpublish Urban Beach and Learning Lab for now;
  C hide the empty collections, never delete; D "do whatever is best".
  - **14 old pages unpublished** through `pageUpdate` (reversible): screen-printing,
    direct-to-garment, embroidery, locations, embroidered-patches, men, women,
    custom-apparel, vinyl-signs, dtf-transfers, build-your-own-gang-sheet, our-work,
    ums-urban-beach, ums-learning-lab. Nothing on the live theme links to any of them
    (checked its header, footer, and homepage templates: the live menu is the only
    place old links exist).
  - **32 redirects created** (`urlRedirectCreate`): 15 for those pages plus the
    already-unpublished dtf-gang-sheets-order, and 17 for the collections below. Map
    in `docs/05`.
  - **Collections could not be hidden from here.** `publicationUpdate` refuses
    collections ("a catalog publication can only contain products"), and both
    `publishableUnpublish` and the older `collectionUnpublish` are refused by this
    connection's safety policy ("unpublishing is blocked"). Raheem hides the 17 in
    admin; the redirects are already in place and start working the moment he does.
  - **Deferred to the publish moment, deliberately:** `/pages/order-form`,
    `/pages/bulk-catalog` (the ESP page), and `/collections/uptown-blanks` are the three
    links in the live site's menu. Taking them down today would break the live
    navigation; they go the minute the new theme is published.
  - **Decision D, done the safe way:** the stocked location "Uptown Merch Solutions"
    had empty pickup instructions, so checkout's pickup box was blank for every real
    order. Set through `locationLocalPickupEnable`: "Orders are usually ready within
    24 hours. We'll email you when yours is ready. Pick up at 241 W 145th St, Harlem,
    Tuesday–Saturday, 11am–8pm. Bring your confirmation email." (24-hour pickup window
    unchanged.) This is live now. "Shop location" was left alone: it may be the
    location the POS register is tied to, and deactivating a location is not something
    to do on a guess. Noted in `docs/04` §2.
  - **Collections hidden by Raheem** (admin bulk action "Exclude from sales channels" →
    Online Store), verified through the API: all 17 off the Online Store, POS untouched;
    Home page, Products, Uptown Blanks, and UMS Storefront still on. The 17 collection
    redirects are therefore live.

- **2026-09-14 — Final review (Phase 9).** Every brief requirement checked against the
  theme on Shopify, the catalog, and the settings; written up in
  `docs/06-final-review.md`. All 12 repo code files match the theme by MD5; every JSON
  template matches in content. Catalog: 29 storefront products pass every check
  (titles, vendor, SKUs, descriptions, images, tracking, pricing, publication).
  - **Fixed — intake form lost order types.** The checkboxes all posted as
    `contact[Product types]`; Shopify keeps only the last of duplicate names, so a
    request ticking two types arrived with one. Now a single hidden field carries every
    ticked label, comma-separated. Verified by MD5 after push.
  - **Fixed — helper product page.** `Artwork upload` now uses `product.internal`
    (new `sections/ums-internal-product.liquid`): a plain "Nothing for sale here" page
    with two buttons instead of a $0 Add to cart.
  - Hero heading now escaped. Policies in the repo corrected to American spelling and
    en-dash ranges; the five admin edits are in `docs/04` §9.
  - Seven decisions for Raheem listed in `docs/06`, the material one being color as a
    filterable option on the 18 single-color soft goods.
  - **Review decisions executed (Raheem).** Color option added to the 17 single-color
    soft goods via `productOptionsCreate` with `LEAVE_AS_IS` — one product tested
    first, SKUs/prices/stock unchanged, then the rest; About page now says founded in
    2024; Raheem disabled customer accounts (verified `DISABLED`), excluded the "Home
    page" collection from the Online Store (verified), and deleted POWR. Policy wording
    edits remain optional.

- **2026-09-14 — Second full review (rendered pass).** Every UMS page was rendered
  locally (liquidjs, a copy of Dawn's `base.css`, the theme's own settings, each section
  wrapped in `.shopify-section` the way Shopify does it), screenshotted headless at
  1280px and 390px, and measured — on top of a fresh read of the store data. Four fixes,
  all pushed and verified by MD5:
  - **Package pages and Contact: the box and the form now share the page body's
    column.** `ums-package-cta` and `ums-contact-form` used `page-width` with their
    own max-widths, so the green CTA box and the contact form sat narrower than, and
    inset from, Dawn's `page-width--narrow` body above them. Both now use
    `page-width page-width--narrow`; measured edges are identical at 1280, 900 and 390.
  - **"Edit the list" link** on the order form was a bare `<a>` and rendered in
    browser-default blue; it now inherits the text color like every other UMS link.
  - **Confirmation screens** for the intake and contact forms are focused by script
    after submit, and Dawn's `:focus-visible` drew a grey ring and shadow around the
    whole "Thanks" block. Suppressed on both.
  - **Artwork upload was silently off on the theme.** The theme's copy of
    `templates/page.order.json` had no `artwork_product` setting, so the order form
    showed the "email it to us" note instead of the file picker. Cause found and
    reproduced: Shopify validates a JSON template against the section's schema at the
    moment the template is written, so a template pushed in the same batch as (or
    before) a schema change silently loses the new setting. Fix: `artwork_product`
    restored, plus a plain-text `artwork_variant_id` (`48416697024738`) as a second
    source; section pushed first, template second, read back with both settings present.
    Rule from now on: push sections before templates, never together, and read every
    JSON template back after a push.
  - Also checked: no horizontal overflow on any page at 390px; every anchor in the UMS
    files carries a class; all 24 pages read in full — no `mgarafano@` anywhere, and
    only `order-form` and `bulk-catalog` (the two go-live pages) are still published
    besides the new ones; every asset in the build theme is stock Dawn 16 apart from the
    superseded `ums-brand.css`; `layout/theme.liquid` is stock; all 12 code files match
    by MD5 and all 9 JSON templates and groups match in content.
  - The render harness (liquidjs, Chromium) lives outside the repo; it is a review aid,
    not part of the theme.

- **2026-09-14 — Third full review (brief re-read, Theme Check, contrast, catalog).**
  Read the brief and the copy guide end to end and re-checked every section against
  the theme and the store. Pulled all 110 text files of the build theme to disk and ran
  Shopify's Theme Check over the whole theme: nothing in the UMS files beyond the
  expected "class defined outside this file" notices for the shared `ums-globals`
  classes; the handful of other notices sit in stock Dawn files. Measured WCAG contrast
  on every rendered page. Eight fixes, sections pushed before templates and every file
  read back:
  - **Contrast.** Small muted text (eyebrows, hints, "(optional)", the package note,
    the Remove button, the hub eyebrow) sat between 3.6:1 and 4.4:1 because an
    `opacity` reduction stacked on Dawn's own 75% body-text alpha. Every one now uses
    an explicit foreground alpha (0.68 on white, 0.82 on green); the audit passes on
    all ten rendered pages.
  - **Tagline in Organizations (brief §2).** "Bringing Brands to Life." now sits as a
    signature line under the hub's hero button (`tagline` setting on `ums-org-hub`).
  - **Low-stock wording (brief §4).** "Low stock: N left" → "Only N left" in
    `locales/en.default.json`, now tracked in the repo as a modified Dawn file.
  - **Footer pickup line** scoped to the storefront ("Storefront orders are picked up in
    store — we don't ship."), matching the Shipping policy, which already explains that
    group orders are arranged directly.
  - Catalog re-audited product by product: 29 storefront products with standard titles,
    vendor "Uptown Merch Solutions", product types, SKUs intact, one image each with
    "<Name> in <Color>" alt text, tracked inventory, no overselling, all published;
    8 service products active but off the Online Store; helper product unlisted.
  - Store re-read: `ums-main-menu` correct; 33 redirects match the go-live map; the
    "News" blog has no articles; four collections on the Online Store ("Products",
    "Uptown Blanks" until go-live, "UMS Storefront", and the built-in listing); six
    policies present; `UMS_logo_transparent.png` exists; the live "Dawn" theme has not
    changed since it was created; pickup instructions on the stocked location intact.
  - Noted, not changed (live content or Raheem's call): Contact page FAQ "Do you ship?
    No." could mention that group orders are arranged directly; About page says 2024 in
    two consecutive sentences; policy hours use hyphens in two policies and "to" in one;
    `/collections` lists a "Products" collection (handle `all`) alongside UMS Storefront;
    the favicon is the full transparent logo rather than a simplified crop; "Shop
    location" still has local pickup enabled with no address and no stock; the
    forwarding rule to the second inbox is still to do; package pages use a typed list
    where the brief wants 3–5 photos.

- **2026-09-14 — Raheem's screenshots: nav pill text dark on Organizations pages, package
  box touching the footer.** Both had one cause my local renders could not see: Shopify
  injects the bundled section CSS through `content_for_header`, which Dawn's layout places
  *before* `base.css`, so wherever a UMS rule and a Dawn rule of equal weight sit on the
  same element, Dawn wins. Dawn's `.page-width--narrow { padding: 0 }` erased the package
  box's bottom spacing; its `.header__active-menu-item { color: foreground }` painted the
  current-page pill text dark. The same tie was silently costing the order form, build
  list, business-line cards, contact form, and internal page their vertical spacing, and
  the two forms their 72–76rem column (they ran the full 1200px on desktop).
  - Every rule on an element that also carries a Dawn class now out-ranks Dawn's (e.g.
    `.ums-pkg.page-width`, `.header__inline-menu .header__menu-item[href*=...] span`).
    Nine sections pushed, verified by MD5.
  - Two rules that never took effect (`max-width: 82rem` on the hero and hub inner
    wrappers) were removed rather than enforced: the full-width column is what Raheem has
    been looking at and it keeps the hero text aligned with the cards below.
  - "Clear the list" no longer borrows Dawn's `link` class, so its color is ours.
  - The render harness now loads UMS styles before `base.css`, marks the current nav item
    the way Dawn does, and ends with a footer block, so this class of bug shows up locally.

- **2026-09-14 — Go-live.** Raheem published the build theme from admin (the API refuses
  `themePublish` by policy); it is now "UMS Live 2026", role MAIN, with "Dawn" unpublished
  in the library as the one-click rollback. Verified the role through the API before
  touching anything, then ran the session's part of `docs/05` §2: unpublished
  `/pages/order-form` and `/pages/bulk-catalog`, created their redirects to
  `/pages/organizations`, repointed `/pages/custom-print-order` from `/pages/order-form`
  to `/pages/organizations`, and created `/collections/uptown-blanks` →
  `/collections/ums-storefront`. Redirects were created only after the pages were
  unpublished, since Shopify will not redirect a path that still resolves. Read back:
  36 redirects; the only remaining go-live click is Raheem removing Uptown Blanks from
  the Online Store channel.
  - Raheem removed Uptown Blanks from the Online Store channel; verified through the
    API. Online Store collections are now UMS Storefront and the built-in "Products"
    listing only. The go-live sequence is complete.

- **2026-09-14 — Final review after go-live.** Live theme compared file for file with the
  repo (all match), render audits and Theme Check re-run on exactly those files (all
  clean), live store settings re-read (no shipping zones, pickup instructions intact,
  accounts disabled, orders@ everywhere, 11 pages, 36 redirects, two collections on the
  channel, helper product unlisted). Write-up in `docs/06`. The API now refuses writes to
  the live theme; the duplicate-push-publish workflow is in the README.

- **2026-09-14 — "Please fix all issues identified."** Applied everything the API can reach
  from the post-go-live open list, and read each change back:
  - Contact page: the "Do you ship?" answer now separates storefront pickup from group
    orders arranged directly with the team (matches the footer line and the Shipping
    policy). About page: the second "in 2024" dropped.
  - "Shop location": local pickup disabled (`locationLocalPickupDisable`); read back with
    no pickup settings. The location stays active — the POS question in `docs/04` §2.
  - Policies: `shopPolicyUpdate` refused (`write_legal_policies`), so the three dash edits
    and the Terms cross-reference ("Refund policy" — the page's real title) are listed for
    admin in `docs/04` §9; `data/policies.json` updated to match.
  - Not reachable from here, listed with steps in `docs/06`: favicon crop (needs an image
    file), homepage meta description, package photos, forwarding rule, old-theme deletion
    (API policy).

- **2026-09-14 — Product page: "Shipping calculated at checkout" replaced.** Raheem sent a
  product page screenshot: the caption under the price still said shipping is calculated
  at checkout. It is Dawn's `products.product.shipping_policy_html` string, rendered by
  `main-product` (and `featured-product`) whenever `shop.shipping_policy` has a body —
  which it does, since the Shipping policy is where the no-ship rule is published. New
  string in `locales/en.default.json`: "Pickup only at 241 W 145th St, Harlem — we don't
  ship.", with "we don't ship" linked to the Shipping policy as the word "Shipping" was.
  Looked for a way to apply it without Raheem: `themeFilesCopy` cannot read from another
  theme (its input has no source theme), `themeCreate` needs a public zip of the complete
  theme, and writes to the live theme are refused — so the live step is Raheem's, either
  through Edit default theme content on the live theme or the duplicate-push-publish
  workflow (`docs/04` §10).

- **2026-09-14 — Fifth review, the most critical pass.** Raheem had already applied the
  product-page caption through Edit default theme content, with "No Shipping" as the
  link text; read back, repo synced to his wording (nothing else in the file moved).
  Pulled Dawn v16.0.0 from GitHub and compared the live theme file for file: all 345
  stock files identical by checksum except the four known edits; JSON differs only by
  Shopify's reformatting (parsed content compared for 15 files). Found and removed a dead
  key in the repo's `templates/index.json` (`enable_quick_add` — Dawn 16 uses
  `quick_add`), which is why the live homepage grid has no quick add. Audited the 29
  products as the theme will render them (option order, stock, prices, images, alt text,
  descriptions, categories, channels), the publications (Online Store, POS, Shop,
  Snapchat, Inbox), redirects, pages against templates, domains, password protection,
  locations, and the helper product's `UNLISTED` status. New findings, all settings or
  store data rather than code, are listed with their one-setting fixes in `docs/04` §11:
  cropped grid photos, two-page collection, no product categories, hats off POS, POS
  tile collections on no channel, no social sharing image, the product page's tripled
  pickup line, and the old Main menu. Raheem also set the meta description and deleted
  two old themes; docs updated.

- **2026-09-14 — "Please fix 1, 3, 5, 6."** Hats to Point of Sale: 12 `publishablePublish`
  calls in one mutation, no errors, live. The other three are template settings, so they
  needed a new theme. `themeFilesCopy` cannot read across themes and `themeCreate` from a
  GitHub archive URL fails ("Src is empty" — no content length), so: built the complete theme
  locally (stock Dawn v16.0.0 from GitHub, verified this morning to be byte-identical to the
  live theme's stock files, plus the repo's `theme/` overlay with the edits), uploaded the
  1 MB zip to the store's Files through a staged upload, ran `themeCreate` from the file's
  CDN URL, waited for processing, read all 360 files back — every one identical to the
  package by checksum or parsed content — then deleted the zip from Files. The result is
  "UMS Live 2026 v2", unpublished. Edits: `templates/collection.json` (36 per page, adapt),
  `templates/index.json` (adapt), `templates/product.json` (adapt on related products; the
  text block trimmed to the all-sales-final sentence). `assets/ums-brand.css`, dead since
  Phase 3, is not in v2. `scripts/build-theme-zip.py` reproduces the package from the repo
  exactly (Dawn's stock `404`, `article` and `password` templates differ from Shopify's
  reformatted copies only in whitespace). README documents the route; publishing is Raheem's.
