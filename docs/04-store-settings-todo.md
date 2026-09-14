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

## 2. Local pickup — instructions DONE 2026-09-14; one location question left

The stocked location, **Uptown Merch Solutions**, now carries pickup instructions (set
through the API on Raheem's "do whatever is best"):

> Orders are usually ready within 24 hours. We'll email you when yours is ready. Pick up
> at 241 W 145th St, Harlem, Tuesday–Saturday, 11am–8pm. Bring your confirmation email.

Pickup window stays "usually ready in 24 hours". This is live at checkout now.

**Still open — "Shop location".** It holds no inventory, ships nothing, and only carries
the old typo'd pickup text. It was *not* deactivated: if the POS register is tied to
it, deactivating would break in-store sales. Check **Point of Sale → Locations** (or
the POS app's settings) for which location the register uses. If it is "Uptown Merch
Solutions", then "Shop location" can be deactivated in Settings → Locations. If it is
"Shop location", the right fix is to move the register to the stocked location first.

## 3. Shipping — DONE 2026-09-14, pickup is the only method

On Raheem's go-ahead, both shipping zones (Domestic with five flat rates, International
with USPS and DHL Express) were deleted from the General profile. Verified afterwards:
the profile has no zones and the store ships to no countries. Checkout can only offer
local pickup now. Bulk-order shipping is arranged outside the website.

Still worth deciding: whether "Shop location" (no inventory) should exist at all, and
the pickup instructions in §2.

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

## 7. Shop Pay Installments messaging (brief §7)

The brief wants the "Pay in 4 interest-free installments" line removed from product
pages with the native toggle, not custom code. Dawn 16 renders that line in the price
block of `sections/main-product.liquid` whenever Shop Pay Installments is active on the
store; nothing in the theme settings controls it. This session cannot read whether it
is active.

**Settings → Payments → Shopify Payments → Manage → Shop Pay → Shop Pay Installments →
turn off.** If a product page on the build theme shows the installments line under the
price, it is still on.
