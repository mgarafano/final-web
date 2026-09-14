# Store settings that need Raheem in admin

These are store-level settings, not theme files. Some are blocked on this connection;
all of them affect the live site, so none were changed unilaterally.

## 1. Refund policy — does not exist (required by brief §4)

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

## 3. Shipping must be impossible, not just unmentioned

The brief requires pickup to be the only fulfillment method. Worth confirming in
**Settings → Shipping and delivery** that no shipping rates are active for the
storefront products, so a customer cannot reach a shipping option at checkout.

## 4. Checkout branding (brief §7)

**Settings → Checkout → Customize** is a separate system from the theme. The brand
palette, logo, and the Archivo/Barlow pairing need applying there too, or checkout
will still look like default Shopify after the theme goes live.

## 5. The cart's shipping line (phase 7)

Dawn's cart renders "Taxes, discounts and shipping calculated at checkout" from a
translation string, not a theme setting. Correcting it to pickup-only wording means
overriding that key in `locales/en.default.json`. Handled in the cart and checkout
phase.

## 6. Form submissions go to one address — and it's still the misspelled one

Re-checked after Raheem's test submission on 2026-09-14: the store contact email is
**still** `Dtftranfers@uptownmerch145.com` (both `email` and `contactEmail`). That is
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
