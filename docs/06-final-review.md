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
| Old labels gone; ESP gone from the new site | done | New theme has no ESP reference. The old ESP page is unpublished at publish (it is in the live menu until then). |
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
| Garment type and color as filterable data | **decision** | Product type is set on all 29 (T-Shirt, Tank Top, Hoodie, Shorts, Joggers, Cap, Beanie). Color is a real option only on the 11 headwear products; the 18 tees, tanks, hoodie, shorts, and joggers carry color in the title only. See decision A. |

## §5 Organizations

| Requirement | Status | Evidence |
|---|---|---|
| Package-based, no catalog, no cart | done | Hub with six packages, three steps, minimum note; cart icon hidden. |
| Six packages | done | Uniforms, team/spirit, corporate, events, patches, something else. |
| Package page = who it's for, examples, minimum, one button | done, one gap | Description and typical-pieces list, 8-per-style minimum, "Start your order". Example *photos* are a text list until photography exists (open since Phase 5). |
| No pricing, no turnaround anywhere | done | Checked hub, packages, list tool, form, confirmation copy. |
| Build your list: separate step, 8-per-style blocking, prefills form | done | `ums-build-list`: Continue refuses under 8; list carried via sessionStorage into "Exact products" and the quantity. |
| Intake fields and required/optional per §5.5 | done | All eleven fields, required flags as specified, structured contact fields. |
| Artwork upload, native, no app | done | File → hidden $0 helper product → Shopify CDN URL → hidden field. 20 MB cap, fallback to email. |
| Multiple product types per submission | **fixed** | Ticked boxes shared one field name and Shopify keeps only the last one, so a two-type request would have arrived as one. Now joined into a single hidden field ("Team and spirit wear, Custom patches"). |
| Routing to orders@ and mgarafano@ | done / admin | Store email is orders@ (verified). Forwarding rule to mgarafano@ is still Raheem's. |
| Distinct confirmation screen, no customer email | done | Form is replaced by a confirmation state; nothing is sent to the customer. |
| Helper product not purchasable by accident | **fixed** | Its product page now uses a template that shows "Nothing for sale here" with two buttons instead of a $0 buy button. |

## §6 About, Contact, social

| Requirement | Status | Evidence |
|---|---|---|
| About copy as approved | done | Page body matches the brief word for word. The approved text says "opened in 2024" and "founded in 2023"; flagged in Phase 6, unchanged on purpose — decision B. |
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
| Three live-menu items (order form, ESP page, Uptown Blanks) | at publish |
| Forwarding rule + test submissions | admin |
| Phone pass | admin |

## Fixed in this review

1. Intake form: multiple order types now all arrive (was: only the last one).
2. Hero heading is escaped like every other text setting.
3. The artwork helper product's page no longer offers a $0 purchase.
4. Repo copy of the policies: American spelling and en-dash ranges (see decision C).

## Decisions for Raheem

- **A. Color as a filter for the soft goods.** The brief wants color as real product data. Today the collection page can filter by product type, size, price, availability, and color for headwear only. Adding a one-value Color option to the 18 tees, tanks, hoodie, shorts, and joggers (e.g. "Arctic Blue") makes the color filter cover everything. Reversible, SKUs untouched, adds one "Color" pill on those product pages. Recommend yes; one API pass on a go-ahead.
- **B. About page dates.** "Opened in 2024" and "founded in 2023" read as a contradiction to a customer. The copy is approved as-is, so it stays unless Raheem wants one of them changed.
- **C. Policy wording.** The pasted policies use "enquiry", "fulfil", and "Tuesday to Saturday, 11am to 8pm" in a few places; the site standard is "inquiry", "fulfill", and "Tuesday–Saturday, 11am–8pm". Five small edits in Settings → Policies, listed in docs/04 §9. Cosmetic.
- **D. Customer accounts.** New customer accounts are enabled, so the header shows an account icon and login link. Not in the brief either way. Keep, or turn off login links in Settings → Customer accounts.
- **E. "Home page" collection.** Shopify's default collection, published, holds one product, and appears on the unlinked `/collections` page. Recommend excluding it from the Online Store like the other 17.
- **F. Collection filters.** The filter set is controlled by Shopify's Search & Discovery app, not the theme. If a "Vendor" filter shows on the storefront page, remove it there — it has one value.
- **G. Obsolete apps.** POWR Form Builder is no longer used. The brief expected removal of two obsolete apps; app data is not readable from here. Uninstall in Apps when convenient.

## Not verifiable from here, by design

Rendered pages (no storefront access from this environment), checkout branding, and
the email delivery itself. Raheem's phone pass and test submissions cover these.
