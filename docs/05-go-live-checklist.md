# Go-live checklist and redirect map

Phase 9 working document. Nothing in here has been executed. Every step marked
**(Raheem)** is a click in admin; every step marked **(session)** runs through the API
on an explicit "go" and is reversible unless the row says otherwise.

Publishing the theme is the only irreversible-feeling step, and even that has a one-click
rollback (republish the current "Dawn" theme, ID `162803220706`).

## 1. Before publishing (Raheem)

From `docs/04-store-settings-todo.md`:

- [ ] §2 Pickup instructions on the **Uptown Merch Solutions** location (the one with stock).
- [ ] §4 Checkout branding in Settings → Checkout → Customize (values ready to paste).
- [ ] §6 Forwarding rule from orders@ to mgarafano@, then one test through each form.
- [ ] §7 Shop Pay Installments off, if the product page still shows the "Pay in 4" line.
- [ ] Phone pass on the preview (`?preview_theme_id=162803613922`), any last fixes.
- [ ] Decide the four **open decisions** in section 4 below.

## 2. Go-live sequence

Total time from first click to done: a few minutes. Best done outside the store's
busiest hour, but no downtime is involved.

1. **(Raheem)** Online Store → Themes → "UMS Rebuild 2026 — in progress, do not
   publish" → ⋯ → **Publish**. Then rename it (⋯ → Rename) to something like
   "UMS 2026 — live". The old "Dawn" stays in the theme library as the rollback.
2. **(Raheem)** Say "go" here.
3. **(session)** Unpublish the old pages listed in section 3. Unpublishing is
   reversible (the pages keep their content; they just stop resolving).
4. **(session)** Take the old collections off the Online Store sales channel (section
   3). Also reversible.
5. **(session)** Delete the 15 empty placeholder collections — *only if the decision in
   section 4 is yes.* Deletion is permanent, but they hold no products.
6. **(session)** Create the redirects in section 3 and repoint the one existing
   redirect. Shopify only fires a redirect when the old path no longer resolves, which
   is why steps 3–5 come first.
7. **(session)** Read everything back through the API and report: page states,
   collection publication, the full redirect list.

## 3. Redirect map

Old URLs become redirects the moment their page or collection stops resolving. Targets
follow one rule: a shopper lands on the closest live equivalent, never on a 404.

### Old pages — unpublish, then redirect

| Old path | What it is | Target |
|---|---|---|
| `/pages/order-form` | Old custom-order page: neon styling, links to service variants that no longer sell online | `/pages/organizations` |
| `/pages/bulk-catalog` | "Events and Promotional Products" — carries the **ESP link twice** and a `body{background:#101820}` rule (the brief's dark-gradient source). Must not survive go-live. | `/pages/organizations` |
| `/pages/screen-printing` | Title "Order Form"; a script that bounces to `/pages/order-form` | `/pages/organizations` |
| `/pages/direct-to-garment` | Old DTG service page with a mailto order form, "Free 1 Week Shipping", "Hub92Prints" copy | `/pages/organizations` |
| `/pages/embroidery` | Old embroidery page with a mailto order form and `contact@` / `dtftransfers@` addresses | `/pages/organizations` |
| `/pages/embroidered-patches` | Old patch order form (mailto `designs@`) | `/pages/organizations-patches` |
| `/pages/vinyl-signs` | Old vinyl sign order form (mailto) | `/pages/organizations` |
| `/pages/custom-apparel` | Empty | `/pages/organizations` |
| `/pages/dtf-transfers` | Empty | `/pages/organizations` |
| `/pages/build-your-own-gang-sheet` | Gang sheet builder pitch, links to a product that no longer sells online | `/pages/contact` |
| `/pages/dtf-gang-sheets-order` | Already unpublished; redirect only | `/pages/contact` |
| `/pages/locations` | Empty | `/pages/contact` |
| `/pages/men` | Empty | `/collections/ums-storefront` |
| `/pages/women` | Empty | `/collections/ums-storefront` |
| `/pages/our-work` | Placeholder gallery — literally "[Add embroidery photo here]" | `/pages/about` (see decision A) |
| `/pages/ums-urban-beach` | Empty body; its template exists only in the old theme | `/` (see decision B) |
| `/pages/ums-learning-lab` | Empty body; its template exists only in the old theme | `/` (see decision B) |

Kept as-is: `/pages/contact`, `/pages/about`, and every `/pages/organizations*` page.

### Old collections — remove from the Online Store channel, then redirect

| Old path | Products | Target |
|---|---|---|
| `/collections/uptown-blanks` | 29 — the same products as UMS Storefront | `/collections/ums-storefront` |
| `/collections/pos-products` | 29 — Point of Sale grouping, was never meant to be public | `/collections/ums-storefront` |
| `/collections/pos-services` | 8 — Point of Sale services, not sold online | `/pages/organizations` |

### Empty placeholder collections — delete (decision C), then redirect

`shirts`, `shirts-1`, `garment-type` → `/collections/ums-storefront`
`custom-patches` → `/pages/organizations-patches`
`school-work-uniforms` → `/pages/organizations-uniforms`
`dtf`, `dtg`, `stickers`, `banners`, `banners-posters`, `dtf-gang-sheets`, `dtf-by-size` → `/pages/organizations`
`fees`, `ums-customer-kiosk`, `asset-pack-41806364674-example-products` → `/` (internal names, redirect is belt-and-braces)

Left alone: `/collections/all` (Shopify's built-in) and `/collections/frontpage` (Shopify's default "Home page" collection, one product, unlinked).

### Existing redirect to repoint

`/pages/custom-print-order` currently → `/pages/order-form`. After go-live that would
chain through two hops. Repoint it straight to `/pages/organizations`.

### Not needed

The eight service products restored to Point of Sale only already return 404 on the
storefront today, so go-live changes nothing for their old `/products/…` URLs. Redirects
for those can be added later if search traffic shows up for them.

## 4. Open decisions (Raheem)

- **A. `/pages/our-work`.** It is a published placeholder with bracketed "[Add … photo
  here]" text and is not in the new navigation. Recommendation: unpublish and redirect
  to About. Alternative: keep it unpublished with no redirect and finish it later.
- **B. `/pages/ums-urban-beach` and `/pages/ums-learning-lab`.** Both have empty bodies
  and custom templates that only exist in the old theme, so under the new theme they
  would render as blank pages. They are not in the brief. Recommendation: unpublish and
  redirect to the homepage. If they are client projects you still need, say so and
  they stay as they are.
- **C. The 15 empty collections.** The brief treats deleting them as decided; the rule
  here is to confirm before anything destructive. Recommendation: delete (nothing is
  lost — they hold no products). Alternative: remove from the Online Store channel only,
  which is reversible and gets the same public result.
- **D. The "Shop location" location.** Holds no inventory and is the source of the
  pickup-instructions mix-up in `docs/04` §2. Recommendation: fix the instructions on
  the stocked location first, then deactivate "Shop location" in Settings → Locations
  once nothing references it. Not part of go-live; flagged so it does not get lost.

## 5. After publishing (Raheem, phone and desktop)

- [ ] Homepage, menu, footer — nothing from the old theme leaks through.
- [ ] Product → Add to cart → drawer → Check out: delivery shows **pickup only**, no
      shipping step, the pickup instructions read correctly.
- [ ] Organizations: hub → package → Build your list → order form → confirmation screen.
      Email arrives at orders@ and (via forwarding) mgarafano@ with every field labelled.
- [ ] Contact form → confirmation screen → email arrives.
- [ ] Type `/pages/order-form` and `/collections/uptown-blanks` into the address bar:
      both should land on the new pages, not a 404.
- [ ] Search the site for "espwebsite" in the browser's view-source on the homepage and
      Organizations page: zero hits.

## 6. Rollback

If anything is wrong: Online Store → Themes → "Dawn" → Publish. That restores the old
site in one click. Then say "roll back" here and the session republishes the old pages,
puts the collections back on the channel, and deletes the redirects — the same
mutations in reverse, all reversible except the collection deletions in decision C (if
taken, those would need recreating by hand; they are empty, so that is a name and a
handle each).
