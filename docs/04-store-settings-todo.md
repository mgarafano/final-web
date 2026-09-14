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

## 2. Local pickup is configured on the wrong location

There are two locations, and the pickup settings are on the one without stock:

| Location | Holds inventory | Pickup instructions |
|---|---|---|
| Shop location | **No** | "Same day service depending on the size of the order.Bring confirmation email. " |
| Uptown Merch Solutions | **Yes** | *(empty)* |

Every product's stock sits at **Uptown Merch Solutions**, which has **no pickup
instructions at all**. So the pickup box at checkout is blank for real orders, while
the useful text sits on an empty location customers never pull from.

Note the existing text also has a missing space after "order." and a trailing space.

**Settings → Locations → Uptown Merch Solutions → Local pickup.** Suggested:

> Orders are usually ready within 24 hours. We'll email you when yours is ready to
> collect. Bring your confirmation email to the shop at 241 W 145th St.

Then decide whether "Shop location" should exist at all — an inventory-less duplicate
location is a common source of confusion.

## 3. Shipping rates are LIVE — decision needed before go-live

Audited on 2026-09-14 through the delivery profiles API. The brief (§4) requires that
local pickup be the only fulfillment method and that no shipping be offered or implied.
Right now the store can sell shipping:

| Profile | Zone | Rates (all active) |
|---|---|---|
| General profile (default) | Domestic — United States | Economy $0.00, Economy $4.90, Economy $19.90, Standard $6.90, Standard $9.90 |
| General profile (default) | International — 27 countries (CA, GB, AU, DE, FR, JP, …) | USPS (carrier-calculated), DHL Express (carrier-calculated) |

Two more things worth knowing:

- The profile ships from **"Shop location" only** — the location with no inventory.
  "Uptown Merch Solutions", where every unit of stock actually sits, is not in the
  profile at all. Which method Shopify offers a given customer therefore depends on
  how it routes the order between the two locations — not something to leave to chance.
- Local pickup is enabled on **both** locations, with instructions only on the
  empty one (see §2).

**Recommended fix:** delete both zones from the General profile, leaving it with no
shipping rates at all. Checkout then offers pickup only. Nothing else (products,
prices, locations, inventory) is touched.

This is a live-store change that affects every checkout from the moment it runs, so it
waits for a go-ahead. Two ways to do it:

- **In admin:** Settings → Shipping and delivery → General shipping rates → Manage →
  delete the Domestic and International zones (or every rate inside them) → Save.
- **From this session, on a "yes":** one `deliveryProfileUpdate` mutation on profile
  `gid://shopify/DeliveryProfile/96243482850`, removing zones
  `gid://shopify/DeliveryZone/390961037538` (Domestic) and
  `gid://shopify/DeliveryZone/390961070306` (International) from location group
  `gid://shopify/DeliveryLocationGroup/97430077666`.

Also worth deciding: whether "Shop location" should exist at all. An inventory-less
duplicate location is a common source of confusion (it is the reason pickup instructions
and shipping rates are attached to the wrong place).

## 4. Checkout branding — admin only, values ready to enter

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

## 6. Form submissions go to one address — and it's still the misspelled one

Re-checked after Raheem's test submission on 2026-09-14, and again at the end of
Phase 7: the store contact email is **still** `Dtftranfers@uptownmerch145.com` (both
`email` and `contactEmail`). That is
where the test landed.

**Why mgarafano@ didn't get a copy:** Shopify's contact form delivers to exactly one
address — the store contact email. There is no second-recipient setting anywhere in
Shopify, and nothing in the theme can add one. The second inbox is a **mailbox
forwarding rule**, full stop.

The two-step fix:

1. **Settings → Store details → Contact information → Store contact email** →
   `orders@uptownmerch145.com`. Fixes the routing *and* the typo.
2. In the **orders@** mailbox, add a rule that forwards every message to
   `mgarafano@uptownmerch145.com`. On Google Workspace that's Gmail → Settings →
   Forwarding, or a group/alias in the admin console; on other providers it's the
   equivalent forwarding or alias setting.

Then send one more test through `/pages/organizations-order` and one through
`/pages/contact`. Both should arrive in both inboxes, each field labelled, with a
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
