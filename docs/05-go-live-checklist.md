# Go-live checklist and redirect map

Phase 9 working document. **Updated 2026-09-14 after Raheem's decisions:** the old pages
are unpublished and 32 redirects exist (section 3 shows status per row). What remains for
the publish moment is small and listed in section 2. Every step marked
**(Raheem)** is a click in admin; every step marked **(session)** runs through the API
on an explicit "go" and is reversible unless the row says otherwise.

Publishing the theme is the only irreversible-feeling step, and even that has a one-click
rollback (republish the current "Dawn" theme, ID `162803220706`).

## 1. Before publishing (Raheem)

From `docs/04-store-settings-todo.md`:

- [x] §2 Pickup instructions on the stocked location — done through the API.
- [ ] **Hide 17 collections from the Online Store (Raheem, admin).** This connection's
      safety policy refuses every collection-unpublish mutation, so: Products →
      Collections → select the 17 listed in section 3 → bulk action to remove them from
      the Online Store sales channel ("Unpublish" / "Make unavailable", depending on the
      admin version). Or open each one → Sales channels → Manage → untick Online Store.
      Their redirects already exist and start working the moment this is done.
- [ ] §4 Checkout branding in Settings → Checkout → Customize (values ready to paste).
- [ ] §6 Forwarding rule from orders@ to mgarafano@, then one test through each form.
- [ ] §7 Shop Pay Installments off, if the product page still shows the "Pay in 4" line.
- [ ] Phone pass on the preview (`?preview_theme_id=162803613922`), any last fixes.
- [x] The four open decisions — answered (section 4).

## 2. Go-live sequence

Total time from first click to done: a few minutes. Best done outside the store's
busiest hour, but no downtime is involved.

1. **(Raheem)** Online Store → Themes → "UMS Rebuild 2026 — in progress, do not
   publish" → ⋯ → **Publish**. Then rename it (⋯ → Rename) to something like
   "UMS 2026 — live". The old "Dawn" stays in the theme library as the rollback.
2. **(Raheem)** Say "go" here.
3. **(session)** Unpublish `/pages/order-form` and `/pages/bulk-catalog` — the two
   old pages still in the live menu — and create their redirects to
   `/pages/organizations`. Repoint `/pages/custom-print-order` straight to
   `/pages/organizations`.
4. **(Raheem)** Remove `uptown-blanks` from the Online Store sales channel (same admin
   step as the 17 above — the API is blocked for this). The session creates its
   redirect to `/collections/ums-storefront` at the same time as step 3, so the order
   between 3 and 4 does not matter.
5. **(session)** Read everything back through the API and report: page states, the
   full redirect list.

## 3. Redirect map

Old URLs become redirects the moment their page or collection stops resolving. Targets
follow one rule: a shopper lands on the closest live equivalent, never on a 404.

### Old pages — unpublish, then redirect

| Old path | What it is | Target | Status |
|---|---|---|---|
| `/pages/order-form` | Old custom-order page: neon styling, links to service variants that no longer sell online | `/pages/organizations` | at publish |
| `/pages/bulk-catalog` | "Events and Promotional Products" — carries the **ESP link twice** and a `body{background:#101820}` rule (the brief's dark-gradient source). Must not survive go-live. | `/pages/organizations` | at publish |
| `/pages/screen-printing` | Title "Order Form"; a script that bounces to `/pages/order-form` | `/pages/organizations` | done: unpublished + redirect |
| `/pages/direct-to-garment` | Old DTG service page with a mailto order form, "Free 1 Week Shipping", "Hub92Prints" copy | `/pages/organizations` | done: unpublished + redirect |
| `/pages/embroidery` | Old embroidery page with a mailto order form and `contact@` / `dtftransfers@` addresses | `/pages/organizations` | done: unpublished + redirect |
| `/pages/embroidered-patches` | Old patch order form (mailto `designs@`) | `/pages/organizations-patches` | done: unpublished + redirect |
| `/pages/vinyl-signs` | Old vinyl sign order form (mailto) | `/pages/organizations` | done: unpublished + redirect |
| `/pages/custom-apparel` | Empty | `/pages/organizations` | done: unpublished + redirect |
| `/pages/dtf-transfers` | Empty | `/pages/organizations` | done: unpublished + redirect |
| `/pages/build-your-own-gang-sheet` | Gang sheet builder pitch, links to a product that no longer sells online | `/pages/contact` | done: unpublished + redirect |
| `/pages/dtf-gang-sheets-order` | Already unpublished; redirect only | `/pages/contact` | done: unpublished + redirect |
| `/pages/locations` | Empty | `/pages/contact` | done: unpublished + redirect |
| `/pages/men` | Empty | `/collections/ums-storefront` | done: unpublished + redirect |
| `/pages/women` | Empty | `/collections/ums-storefront` | done: unpublished + redirect |
| `/pages/our-work` | Placeholder gallery — literally "[Add embroidery photo here]" | `/pages/about` (see decision A) | done: unpublished + redirect |
| `/pages/ums-urban-beach` | Empty body; its template exists only in the old theme | `/` (see decision B) | done: unpublished + redirect |
| `/pages/ums-learning-lab` | Empty body; its template exists only in the old theme | `/` (see decision B) | done: unpublished + redirect |

Kept as-is: `/pages/contact`, `/pages/about`, and every `/pages/organizations*` page.

### Old collections — Raheem hides them in admin; redirects already exist

| Old path | Products | Target | Status |
|---|---|---|---|
| `/collections/uptown-blanks` | 29 — the same products as UMS Storefront | `/collections/ums-storefront` | at publish (in the live menu) |
| `/collections/pos-products` | 29 — Point of Sale grouping, was never meant to be public | `/collections/ums-storefront` | redirect done; hide in admin |
| `/collections/pos-services` | 8 — Point of Sale services, not sold online | `/pages/organizations` | redirect done; hide in admin |

### Empty placeholder collections — hide in admin (decision C: never delete); redirects done

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

## 4. Open decisions — answered 2026-09-14

A: unpublish Our Work (done). B: unpublish both for now (done). C: hide, never delete
(redirects done; hiding is an admin step, see section 1). D: "do whatever is best" —
pickup instructions set on the stocked location; "Shop location" left active pending the
POS check in `docs/04` §2.

Original questions, for the record:

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
