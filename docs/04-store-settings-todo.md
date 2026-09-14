# Store settings that need Raheem in admin

These are store-level settings, not theme files. Some are blocked on this connection;
all of them affect the live site, so none were changed unilaterally.

## 1. Refund policy — DONE 2026-09-14

**All six policies now exist in admin** (Contact, Legal notice, Privacy, Refund,
Shipping, Terms), so the footer's policy links render. The original note is kept below
for the record.

### Original note

`shopPolicies` is **completely empty**. There is no refund policy, no privacy policy,
and no terms of service on the store.

That matters twice over: the brief requires the all-sales-final policy to be stated
clearly on a native Shopify Refund Policy page, and the new footer has policy links
switched on — with nothing to link to, that footer area renders empty.

Creating it is blocked here: `shopPolicyUpdate` returns *"Access denied … requires
`write_legal_policies`"*.

**Settings → Policies → Refund policy.** Text, ready to paste:

> All sales are final. Uptown Merch Solutions does not offer refunds or exchanges on
> any item.
>
> Every order is picked up in store at 241 W 145th St, Harlem. Please check your item
> before you leave the shop.
>
> If you have a question about an order, call 646-398-8178 or email
> orders@uptownmerch145.com.

Deliberately says nothing beyond the in-store policy — no damage window, no exception
period. Those would be new commitments the brief never authorized.

Shopify will also prompt for a privacy policy and terms of service. Its generated
templates are a reasonable starting point for both.

## 2. Local pickup — DONE 2026-09-14 on both locations

The stocked location, **Uptown Merch Solutions**, carries the pickup instructions (set
through the API on Raheem's "do whatever is best"):

> Orders are usually ready within 24 hours. We'll email you when yours is ready. Pick up
> at 241 W 145th St, Harlem, Tuesday–Saturday, 11am–8pm. Bring your confirmation email.

Pickup window stays "usually ready in 24 hours". This is live at checkout now.

**"Shop location" no longer offers pickup** — disabled through the API on 2026-09-14, on
Raheem's "fix all issues identified", and read back as having no pickup settings. It holds
no inventory and has no address, so the only thing it could do at checkout was show its
old typo'd instructions; the stocked location is now the only pickup point. The location
itself is still active and was *not* deactivated: if the POS register is tied to it,
deactivating would break in-store sales. Re-enabling pickup is one click in Settings →
Locations → Shop location if it is ever needed.

To retire the location entirely, check **Point of Sale → Locations** (or the POS app's
settings) for which location the register uses. If it is "Uptown Merch Solutions", then
"Shop location" can be deactivated in Settings → Locations. If it is "Shop location", the
right fix is to move the register to the stocked location first.

## 3. Shipping — DONE 2026-09-14, pickup is the only method

On Raheem's go-ahead, both shipping zones (Domestic with five flat rates, International
with USPS and DHL Express) were deleted from the General profile. Verified afterwards:
the profile has no zones and the store ships to no countries. Checkout can only offer
local pickup now. Bulk-order shipping is arranged outside the website.

Still worth deciding: whether "Shop location" (no inventory, pickup now off) should
exist at all — see §2.

## 4. Checkout branding — DONE by Raheem 2026-09-14 (not readable from here)

Raheem applied the branding in Settings → Checkout → Customize. The API cannot read it
back on this plan (the write was also tried and refused: Plus-only), so the check is
visual: one item in the cart, open checkout, nothing orange or purple, logo top left.

Original instructions kept below.

The API route is closed: `checkoutBranding` returns *"Access denied … the shop must be
on a Plus plan or a Development store plan."* The checkout editor itself is available on
this plan, but only by hand. Until this is done, checkout still looks like default
Shopify after the theme goes live (brief §7).

**Settings → Checkout → Customize** (opens the checkout editor) → the **Branding**
panel (paintbrush icon). Enter:

| Setting | Value | Why |
|---|---|---|
| Logo | `UMS_logo_transparent.png` from Files, left-aligned, size Small or Medium | Matches the header (130 px wide there) |
| Favicon | same file | Matches the theme |
| Background (page and main area) | `#FFFFFF` | scheme-1 |
| Order summary background | `#F6F5F5` | scheme-2, the site's light gray surface |
| Text | `#1B1B1B` | Brand ink |
| Accent / links / primary button | `#355E3B` | Hunter green |
| Primary button text | `#FFFFFF` | |
| Borders and dividers | `#A9A5A4` or the default light gray | Brand gray |
| Heading font | **Archivo**, weight 700 | Same as the theme |
| Body font | **Barlow**, weight 400 | Same as the theme |
| Corner radius | Small | Theme uses 2 px everywhere |

No orange, no purple, no gradients anywhere in checkout. If the font picker does not
list Archivo or Barlow, stop and say so rather than substituting — the pairing is a
brand decision from Phase 1.

While in **Settings → Checkout**, two related toggles worth confirming: customer
contact method set to email (the pickup-ready notification goes there), and no
tipping or extra fields that were never part of the brief.

## 5. The cart's shipping line — DONE in Phase 7

Dawn's "Taxes, discounts and shipping calculated at checkout" line is replaced on the
cart page and in the cart drawer by a pickup-only note (address, hours, no shipping,
all sales final, "Taxes and discounts are calculated at checkout."). The wording lives
in **Theme settings → UMS cart note** if it ever needs changing. Nothing was done in
`locales/` after all — the snippet route kept the change in one place.

## 6. Store email — FIXED 2026-09-14; forwarding and a test still to do

**Verified through the API after Raheem's change: both `shop.email` and
`shop.contactEmail` now read `orders@uptownmerch145.com`.** What remains is the
forwarding rule to mgarafano@ (below) and one test submission per form.

For the record, both fields had been `Dtftranfers@uptownmerch145.com`.
There is **no Admin API mutation that writes either field** (checked all 441 of them on
2026-09-14), so this cannot be done from the build session. Shopify delivers contact
form submissions to one store address, so this is also why mgarafano@ has not been
getting copies.

Two fields to change, both to `orders@uptownmerch145.com`:

1. **Settings → Store details → Profile → Store email** (Shopify's "where we contact
   you" address). Fixes the typo at the source.
2. **Settings → Notifications → Sender email** (the address customers see, and the one
   Shopify uses to deliver contact-form submissions). Shopify sends a verification link
   to the new address; the change takes effect once it's clicked. If admin also asks to
   authenticate the domain (SPF/DKIM), it will be the same domain that was already in
   use, so it usually passes as-is.

Then, in the **orders@** mailbox, add a rule that forwards every message to
`mgarafano@uptownmerch145.com`. On Google Workspace: Gmail → Settings → Forwarding and
POP/IMAP, or a group/alias in the admin console. On other providers, the equivalent
forwarding or alias setting.

Finally, send one test through `/pages/organizations-order` and one through
`/pages/contact`. Both should land in both inboxes, each field labelled, with a
`Source` line saying which form it came from.

`mgarafano@` is not listed anywhere on the site and never will be — verified by
searching every theme file. `orders@` is the only address shown to customers.

## 7. Shop Pay Installments — DONE by Raheem 2026-09-14

Disabled in Settings → Payments. The "Pay in 4" line no longer renders on product pages.
Original note kept below.

The brief wants the "Pay in 4 interest-free installments" line removed from product
pages with the native toggle, not custom code. Dawn 16 renders that line in the price
block of `sections/main-product.liquid` whenever Shop Pay Installments is active on the
store; nothing in the theme settings controls it. This session cannot read whether it
is active.

**Settings → Payments → Shopify Payments → Manage → Shop Pay → Shop Pay Installments →
turn off.** If a product page on the build theme shows the installments line under the
price, it is still on.

## 8. The "Ship" tab in checkout cannot be removed on this plan — ACCEPTED by Raheem 2026-09-14

Decision: leave it as is. The Ship tab is a dead end (no rates), Pick up is the only path
that completes. The optional wording edit below remains available at any time.

Raheem saw a "Shipping method" box in checkout ("Enter your shipping address to view
available shipping methods") after all shipping rates were deleted.

Why it is there: Shopify's checkout always renders the delivery method chooser with a
**Ship** tab beside **Pick up** whenever local pickup is available. Deleting the rates
made shipping impossible to complete — a customer who stays on Ship and enters an
address gets "no shipping methods available" and cannot continue — but the tab itself
is not removable. Hiding or reordering delivery methods needs Shopify Functions or
checkout UI extensions on the shipping step, which Shopify limits to Plus (confirmed in
the developer docs on 2026-09-14). Every storefront product is a tracked, physical item
stocked at the pickup-enabled location, so the Pick up tab is offered.

Two mitigations, both without Plus:

1. **Rewrite the strings inside the Ship tab** so the dead end explains itself.
   Online Store → Themes → the build theme → ⋯ → Edit default theme content →
   *Checkout & system* tab → search "shipping". Suggested:
   - "Enter your shipping address to view available shipping methods." →
     "We don't ship. Choose Pick up above to collect your order at 241 W 145th St."
   - the "no shipping rates / can't be shipped to this address" message →
     "This shop is pickup only. Select Pick up above."
   These are store-wide checkout translations, not theme code, and take effect on save.
2. **Mark products as not requiring shipping.** Removes the delivery step entirely, but
   also removes Shopify's local-pickup flow (pickup instructions at checkout, the
   ready-for-pickup email, the pickup orders tab in POS) — not recommended; the brief
   asks to keep the pickup pattern.

## 9. Policy wording — four edits left (Settings → Policies)

Raheem made the spelling edits (inquiry, fulfill) on 2026-09-14. What remains is the dash
style in three policies and one cross-reference. The API cannot make them: on 2026-09-14
`shopPolicyUpdate` was refused again (*"Access denied … requires `write_legal_policies`"*),
so they are admin edits. `data/policies.json` carries the final text of all six policies
if pasting a whole policy is easier than editing in place.

| Policy | Find | Replace with |
|---|---|---|
| Contact information | `Tuesday-Saturday, 11am-8pm` | `Tuesday–Saturday, 11am–8pm` |
| Shipping policy | `Tuesday-Saturday, 11am-8pm` | `Tuesday–Saturday, 11am–8pm` |
| Terms of service | `Tuesday-Saturday, 11am-8pm` | `Tuesday–Saturday, 11am–8pm` |
| Terms of service | `See our Return and refund policy.` | `See our Refund policy.` |

The last one matters a little more than the dashes: the page customers land on is titled
"Refund policy" (`/policies/refund-policy`), so the Terms should call it that. The en dash
(–) is Option-hyphen on a Mac, Alt+0150 on Windows, or copy it from this table.

## 10. Product page caption "Shipping calculated at checkout" — DONE 2026-09-14 (Raheem, language editor)

Raheem, with a product page screenshot: "There is no shipping … replace this with some
other more intuitive line." Dawn prints `products.product.shipping_policy_html` under the
price whenever a Shipping policy exists (the quick-add modal shows it too, since it loads
the same section). The repo's `locales/en.default.json` now reads:

> Pickup only at 241 W 145th St, Harlem — <a href="{{ link }}">we don't ship</a>.

The link goes to the Shipping policy, as the word "Shipping" did before. The API refuses
writes to the live theme, so getting it live is one of:

1. **Edit default theme content on the live theme.** Online Store → Themes → UMS Live
   2026 → ⋯ → Edit default theme content → search "calculated at checkout" → replace the
   *Shipping policy html* value with the line above, `<a>` tag included → Save. Takes
   effect immediately. Shopify writes it into the theme's own `en.default.json`, so the
   live theme still matches the repo; read the file back afterwards to confirm.
2. **Duplicate → push → publish** (README workflow): duplicate the live theme in admin,
   push the locale file to the duplicate, read it back, publish the duplicate.

Looked for a way to do it without Raheem: `themeFilesCopy` cannot read from another theme
(its input has no source theme), `themeCreate` needs a public zip of the complete theme,
and writes to the live theme are refused. So the live step is Raheem's.

**Applied by Raheem through route 1**, with his own wording: "Pickup only at 241 W 145th
St, Harlem — No Shipping." Read back from the live theme; the repo now carries that exact
string, and nothing else in the file changed. One optional nit: the site's copy standard
(`docs/02`) is sentence case, so "no shipping" would match the rest of the page; same
editor, same field, if wanted.

## 11. After the fifth review — theme-editor and admin items, none blocking

Everything below is a setting or store-data change, not code. Where it is a theme-editor
setting it can be made on the live theme directly (Online Store → Themes → Customize),
no duplicate needed; the repo copy gets synced afterwards.

| # | Item | Where | What |
|---|---|---|---|
| 1 | Product photos are cropped in the grids | **Superseded by §12** | v2 (published) used "Adapt to image", which made rows ragged; v3 uses one 4:5 box that every photo fills, on Raheem's direction that photos must all be the same size. |
| 2 | Collection page splits 29 products over two pages | **DONE in "UMS Live 2026 v2"** | Products per page 24 → 36. One page. |
| 3 | Product page says "Pickup only" three times | **DONE in "UMS Live 2026 v2"** | The text block under the buy button now reads "All sales are final — no refunds or exchanges." The caption under the price (§10) and Dawn's pickup-availability line carry the pickup message. |
| 4 | Homepage grid has no quick add | Customize → Homepage → Featured collection → Quick add | Optional: **Standard**, to match the collection page. The template carried a key Dawn 16 does not have, so the setting never took. |
| 5 | Products carry no product category | Products → select all 29 → bulk edit → Category | Set Apparel & Accessories › Clothing (T-shirts, Hoodies, Shorts, Pants) and › Clothing Accessories › Hats. Shopify Tax uses the category to apply New York's clothing exemption under $110; without it, full sales tax can be charged on every tee. Check **Settings → Taxes → United States** for how NY clothing is set up. Can also be set through the API on request. |
| 6 | The 12 hats are not on Point of Sale | **DONE 2026-09-14 (API, `publishablePublish`)** | All 12 hats are now on Point of Sale as well as the Online Store; no errors, read back. |
| 7 | "POS Products", "POS Services", "Uptown Blanks" are on no channel at all | Collection → Publishing → Point of Sale | Their descriptions call them POS tile collections. If the register's smart grid used them, the tiles are dead; re-add them to **Point of Sale only** (not the Online Store). |
| 8 | No social sharing image | Online Store → Preferences → Social sharing image | A 1200×630 image (logo on brand green). Without it, links shared in messages and social apps show no preview. |
| 9 | "No Shipping" capitalization | Edit default theme content → Products → Shipping policy html | Optional: "no shipping" (sentence case, `docs/02`). |
| 10 | Old "Main menu" still exists | Navigation → Main menu | Not used by the new theme (header and footer use "UMS main menu"), but it still lists Services, Blanks, Events and Promotional Products, Contact Us. Delete or empty it so it can never be picked by mistake. |

Live tests still worth one run each: a pickup checkout (order → cart → checkout → Pick up),
the contact form, the organizations order form **with an artwork file attached** (the
upload is verified in code and locally, never yet on the live store), and the
confirmation email that arrives.

**How the v2 theme was made (2026-09-14).** Raheem: "please fix 1,3,5,6". Items 1, 5 and 6
are theme templates, so they need a new theme: built from stock Dawn v16.0.0 plus this repo's
`theme/` folder (`scripts/build-theme-zip.py`), uploaded to Files, created with
`themeCreate`, and read back file by file — all 360 files identical to the package
(checksums for code, parsed content for JSON); the only difference from the live theme apart
from the three template edits is that the dead `assets/ums-brand.css` is gone. Nothing in the
live theme changed after 10:00 UTC, so v2 carries every editor setting. **To go live:**
Online Store → Themes → "UMS Live 2026 v2" → ⋯ → Preview (check the storefront grid, a
product page, the homepage), then ⋯ → Publish. "UMS Live 2026" becomes the rollback.

## 12. Product cards: buttons out of line and two different labels — DONE in "UMS Live 2026 v3", 2026-09-14

Raheem published v2 and sent three phone screenshots of the storefront grid: quick-add
buttons in the same row sitting at different heights, and "Add to cart" on some cards next
to "Choose options" on others.

- **Buttons.** Dawn pins the button to the bottom of the card through a chain of
  `height: 100%` rules; iOS Safari does not resolve it, so a card with a two-line title
  (or, under "adapt", a taller photo) pushed its button lower than its neighbour's.
  `ums-globals` now stretches grid item → card wrapper → card as flex items, which needs no
  percentage heights. Verified in a local rebuild of Dawn's grid: every button in a row at
  the same pixel, at 390px and 1280px.
- **Labels.** Dawn says "Add to cart" on single-variant products and "Choose options" on
  the rest. The locale string is now "Add to cart" for all; on a product with sizes the
  button opens the size chooser, then adds.
- **Photo box.** All four grid templates (collection, homepage featured collection,
  related products, search) use the 4:5 "portrait" box and every photo fills it edge to
  edge (`object-fit: cover`), so every photo in the grid is exactly the same size. The
  first cut of v3 fitted the photo inside the box instead, which left the square hat shots
  visibly smaller than the apparel shots; Raheem rejected it ("they can not be smaller or
  larger than others") and it was corrected in place. The crop at 4:5 is about 8% off the
  top and bottom of an apparel shot and 10% off each side of a hat shot — margin in the
  supplier photos. `templates/search.json` joins the repo for the box setting.
- **Button size.** Besides the one label, every card button is full width and one line
  (`white-space: nowrap`), so all are the same size.

v3 was built from the repo (`scripts/build-theme-zip.py`), created through `themeCreate`,
and read back file by file. **To go live:** Online Store → Themes → "UMS Live 2026 v3" →
⋯ → Preview (storefront grid on the phone), then ⋯ → Publish. v2 becomes the rollback.
