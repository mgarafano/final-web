# Uptown Merch Solutions (UMS) — Website Rebuild Reference Brief

**Status: discovery/spec only. Nothing described here has been built yet.** This document is the packaged output of a requirements-gathering conversation between Raheem (owner, UMS) and Claude. It is meant to be handed to a separate future project as the complete, self-contained reference for actually building the new Shopify site. Anyone (or any Claude instance) reading this cold should have everything needed to build without re-asking the questions already answered here.

Store: Uptown Merch Solutions, physical location 241 W 145th St, Harlem, NYC. Shopify domain: uptownmerch145.com.

---

## 1. Business model (the most important thing to get right)

UMS has **two distinct, clearly-separated business lines** living on one unified site:

1. **UMS Storefront** — the physical store's online presence. Static, fixed-price retail inventory only. No in-store customization anymore (that service is being discontinued). Pickup-only, no shipping. Standard Shopify checkout, real prices, real cart.
2. **UMS for Organizations** — the bulk/group branded-merch business. Package-based, no visible pricing (quote-only), no cart/checkout at all — it's an explainer + intake questionnaire that generates a lead for Raheem's team to quote and follow up on manually.

**These two must feel like one unified brand, not a split site.** The previous live homepage's two-tile "split screen" approach was explicitly rejected as bad ("pathetic"). The chosen solution: a shared nav bar with clearly labeled, distinctly weighted entries (see Section 3), not a visual 50/50 split.

**UMS for Organizations is the primary business focus going forward** and should be weighted as such in navigation/hierarchy, while UMS Storefront must still be clearly, easily findable — not buried.

**Current transitional state:** the physical store currently exists mainly to **liquidate existing inventory** (blank apparel bought before the business model changed) as quickly as possible. Designs are being printed onto this existing stock before sale. Long-term, if the bulk side grows enough, the physical store could become more of a showroom — but that is not the case today and shouldn't be assumed in the build.

---

## 2. Brand identity

- **Full name:** Uptown Merch Solutions. **Tagline (site-wide): "Bringing Brands to Life."** Lean into this tagline, including within the UMS for Organizations section.
- **Logo — created, mark only (no wordmark text below it, per Raheem).** Two files produced by recoloring the actual reference logo pixel-for-pixel (extracted from the reference PDF at 300 DPI, not an AI reinterpretation — exact letterforms preserved), cropped to the "UMS" mark alone — the "UPTOWN MERCH SOLUTIONS" text that ran underneath it in the original artwork has been removed. A solid version (green "UMS" mark on a gray background) and a transparent-background version (green letters with a gray outline, no background fill) for flexible use in the header/favicon/etc. **`UMS_logo_solid.png`** and **`UMS_logo_transparent.png`**. **Color mapping: what was black is now green; what was white is now gray** — the letters themselves are green, the outline/background is gray. Colors used: hunter green `#355E3B` (standard reference value — the awning photo's own green read as teal-shifted, likely a lighting/fading artifact, so it wasn't used directly) and the lighter of the two sampled grays, `#a9a5a4` (see palette note below). No Canva version needed — confirmed.
- **Color palette (updated — gray replaces cream):** deep hunter green (**`#355E3B`**), white, and **gray** as the secondary/neutral tone. Earlier discovery rounds assumed cream/brick based on the exterior awning photo; Raheem has since corrected this against a real photo of the store interior. **Two grays were pixel-sampled directly from the interior photo** (not estimated): a lighter, warmer one from the floor (**`#a9a5a4`** — confirmed as the primary gray to use) and a darker, cooler one from the walls (`#838388` — available as a secondary/accent tone if a deeper contrast gray is useful, e.g. for text or secondary surfaces). **On the green specifically:** `#355E3B` is a standard reference value for "hunter green" (the awning photo's own green read as teal-shifted, likely a lighting/fading artifact, so it wasn't used directly) — **explicitly confirmed by Raheem as final**, no longer just an implicit approval. Interior reference: warm light-gray flooring, mid-tone cool-gray walls, black ceiling tiles stenciled with a repeating white "UMS" logo pattern, black display fixtures (wire grid panels, glass display counters), and one red-brick accent wall (brick is a minor physical texture only — gray is the actual secondary brand tone to use, not brick/cream). Exterior awning remains green with white lettering. **No orange or purple anywhere** — the current live site uses an unrelated orange (#d96300-ish) and Shopify-brand purple throughout buttons/prices/accents, which does not match the real brand at all and must be fully replaced.
- **Typography:** current theme uses "Basic Commercial" (headers) and "Assistant" (body) — open for the build project to revisit, not explicitly locked by Raheem either way.
- Header/browser-tab branding should use **the logo mark itself** (the "UMS" mark, as delivered — the wordmark text is not part of the final logo file, see above). If the full "Uptown Merch Solutions" name needs to appear alongside it anywhere (e.g., a larger footer lockup), that would be a separate text treatment, not baked into the logo file.
- **Favicon — confirmed (content was previously only referenced as "confirmed," not written down; restored here):** a simplified crop of the "UMS" mark alone, sized/simplified appropriately for legibility at tiny sizes (browser tab). Use the transparent-background logo file as the source.

---

## 3. Site navigation (confirmed structure)

```
[Logo]     UMS Storefront   |   UMS FOR ORGANIZATIONS (weighted/button style)   |   About   |   Contact
```

- **"UMS for Organizations"** should be visually weighted heavier than the others (e.g., filled pill/button style) since it's the primary business line. **This applies on mobile too** — confirmed requirement — not just the desktop nav; the mobile menu needs its own distinct treatment for this item (e.g., a highlighted row), not plain text matching the rest of the stacked list.
- **"UMS Storefront"** is the confirmed name for the physical retail section (final — went through several rounds: "Shop" → "Off the Rack" → **"UMS Storefront"**, which is the locked name).
- No more "Blanks," "Services," or "Events and Promotional Products" as nav labels (these are current live-site labels being replaced).
- **Remove entirely:** the external ESP (uptownmerchsolutions.espwebsite.com) link and any ESP catalog content. This must not appear anywhere on the new site.
- Any copy that concatenates the store/section name into a sentence must be checked for natural grammar (e.g., "Pickup at UMS Storefront" — not a template that produces awkward phrasing).
- **Footer content — confirmed (content was previously only referenced as "confirmed," not written down; restored here):** social links (TikTok/Instagram, see Section 6), policy links (including the Refund Policy page, see Section 4), store hours and location, and standard payment method icons. Nothing beyond standard content is needed — no distinctive design requirement was given for the footer specifically.
- **Cart icon on "UMS for Organizations" pages — confirmed (same restoration):** hide or visually de-emphasize the cart icon while browsing that section, since there's no cart/checkout function there at all — showing an active cart icon would be misleading.

---

## 4. UMS Storefront (physical store) — detailed spec

- **Static, fixed-price inventory only.** No customer-facing customization tools. In-store decoration methods used to produce the static inventory: embroidery, DTF transfers, vinyl, screen printing — but customers are not choosing/customizing; they're buying finished, pre-decorated items.
- **Pickup-only.** No shipping option should be offered or implied for store products. Confirm in the build project that local pickup is the only configured fulfillment method in Shopify settings, and that no "shipping calculated at checkout" language appears anywhere in the cart/checkout for these products.
- **Returns policy — confirmed:** a strict **no refunds, no exchanges, all sales final** policy (per in-store signage) carries over unchanged to the online store, and must be stated clearly on the site. **Recommended placement:** a native Shopify Refund Policy page (Settings > Policies — standard, auto-linkable from the footer), plus a short callout near the pickup-info area on product pages and in the cart, so it's visible before checkout rather than buried in a policy page alone. (Earlier drafts of this doc pointed to "Section 9" for this detail; that placement recommendation was lost during a later rewrite of that section and has been restored here directly.)
- **Current inventory (starting catalog):** use what's already listed and in stock in Shopify — ~33 products tagged "uptown-blanks" + ~8 tagged "uptown-service" (≈41 products). **Note the arithmetic:** the "Products" collection shows ~45 total, a few more than these two tag groups account for — the difference is a handful of stray items (an oddly-named single-product "Home page" collection, and a small number of "example"-style products spotted during the original audit that looked like placeholder/demo junk, not real catalog items). **The build project should audit the full product list and exclude anything that isn't genuinely part of the uptown-blanks/uptown-service catalog** rather than assuming the entire "Products" collection is the real starting catalog. Ignore any additional stock that exists physically but isn't properly documented in Shopify yet. This catalog (the genuine ~41, once confirmed) is a liquidation/transitional batch, not the permanent lineup — designs are currently being printed onto this existing stock as part of selling it off quickly; a separate, future round of new stock will get its own designs later once this batch sells through.
- **Photography — confirmed: clean product-only shots**, not lifestyle/on-model photography. Applies here and to the 3–5 example photos per bulk package in Section 5.3.
- **Low-stock display:** show the real remaining unit count whenever inventory for an item is **under 8 units** (e.g., "Only 3 left"). Native Dawn theme capability, just needs enabling with threshold set to 8.
- **Quick-add-to-cart: enabled** (currently off in the live theme) — lets shoppers add an item straight from the product grid without a full page tap-through, on both mobile and desktop.
- **"Drop"/scarcity framing: not needed, confirmed resolved.** Raheem confirmed the low-stock count indicator alone ("only X left") is sufficient as the scarcity mechanism — no additional "current drop" copy layer required. (This bullet previously read as still undecided; that was stale — it was resolved earlier in the discovery process and is settled.)

### 4.1 Product data standard (naming + descriptions)

**Problem found:** live product titles are raw, unedited import strings, e.g. `UPTOWN BLANKS ZS4010 ARCTIC BLUE`, `UPTOWN BLANKS 4527 5 PANEL DESIGNER PLAID COTTON BASEBALL CAP` — all caps, vendor-prefixed, internal style codes exposed to customers. The vendor field on every product still literally reads "Uptown Blanks" (undermines the one-brand goal). Variant option values contain data-entry errors — e.g., one product's "Color" option is literally labeled **"January"** (a bulk-import bug). Some product descriptions still reference the discontinued customization model (e.g., "...easy to wear front-panel forward for embroidery or patches" — implies the item is a decorator's blank, which contradicts the new static/finished-goods model).

**Approved standard, confirmed by Raheem:**

- **Title format:** `[Fit/audience] [Garment type] — [Color]`, sentence case. Drop the vendor name and internal style code from the customer-facing title (the style code stays correctly in the SKU field — see below). **Note on the examples below:** two of them ("Heather Crewneck Tee," "Plaid Floral Baseball Cap") use a fabric/pattern descriptor in that first slot instead of a fit/audience word, because the product doesn't have a meaningful fit/audience distinction to make — that's fine and expected, not every product will fill that slot the same way; the format is a guideline, not a rigid template every title must literally satisfy.
- **Description format:** one sentence on what it is/who it's for, then 2–4 short bullets (fabric weight, fit, standout features). No leftover language implying the item is meant for further customer decoration.
- **Examples (approved):**
  - `Oversized Tee — Arctic Blue` (was: UPTOWN BLANKS ZS4010 ARCTIC BLUE)
  - `Heather Crewneck Tee — Grey` (was: UPTOWN BLANKS ZS1002 GREY HEATHER)
  - `Women's Crop Long Sleeve — Black` (was: UPTOWN BLANKS ZS2103 BLACK)
  - `Youth Tee — White` (was: UPTOWN BLANKS ZS2001 WHITE)
  - `Plaid Floral Baseball Cap — Red Floral` (was: UPTOWN BLANKS 4527 5 PANEL DESIGNER PLAID COTTON BASEBALL CAP, color mislabeled "January")

**Data-modeling note worth flagging for the build project:** the last example's "color" is really a pattern ("Red Floral"), not a flat color the way "Black" or "Arctic Blue" is. If Color is used as a filterable product option, a patterned item's value there will read strangely next to solid colors, and filtering by "Red" wouldn't obviously surface a floral print the way it would a solid red item. Worth considering a separate Pattern attribute (distinct from Color) for items like this, rather than folding pattern descriptions into the Color field — a decision for the build project, not something Raheem has weighed in on specifically.

**Critical build requirement — data integrity:** when renaming titles, **the correct SKU/style code must be preserved accurately in the SKU field** for every product. Nothing about internal inventory tracking should break during the rename pass. Garment type and color should also exist as real filterable product data (options/tags), not just words in the title.

**Full catalog data audit required.** The "January" bug is very likely not isolated to one product — treat this as a full pass across every product's title, vendor field, color/variant option values, and description, not a one-off fix.

- **Vendor field:** update away from "Uptown Blanks" on every product (final vendor label TBD by build project — likely "Uptown Merch Solutions" or hidden entirely).

---

## 5. UMS for Organizations (bulk program) — detailed spec

### 5.1 Model
Package-based, not raw product browsing. No individual product catalog is shown on this side (that's what UMS Storefront is for) — these must stay **visibly, structurally distinct** from each other so a school/org customer never confuses this with a normal add-to-cart shop.

### 5.2 Confirmed package categories (starting list)
1. School & work uniforms *(group/organizational clientele only, not individuals)*
2. Team / spirit wear (sports, clubs)
3. Corporate & staff apparel
4. Event / fundraiser merch
5. Custom patches (for groups)
6. Other / not sure yet (catch-all)

### 5.3 Package page content (kept intentionally simple, per Raheem)
Each package page = 4 things only:
1. A short 1–2 sentence description of who the package is for.
2. 3–5 example photos/icons illustrating typical item types for that package (curated per-package, not one shared master product list across all packages — "the packages should make sense based on what they're ordering").
3. The **8-piece-per-style minimum** stated plainly.
4. One clear **"Start your order"** button.

- **No pricing shown anywhere** in this section, at any stage, until Raheem's team sends a quote.
- **No turnaround time stated** (explicitly — don't add estimated production/turnaround language).
- Further product-level detail (exact colors, sizes, specifics) is sorted out manually by Raheem *after* the intake form is submitted — the website's job is to capture broad interest + a working list, not deep configuration.
- **Minimum order quantity — finalized:** **8 pieces per style** (changed from an earlier 10-per-order draft), and **enforced/blocking** — the build-your-list tool must not let a customer submit with any single style under 8 units, not just display the number as information.

### 5.4 "Build your list" tool
- Its own **separate step**, not embedded inside the intake form itself.
- Lets the customer add product types + quantities to a running list (no pricing shown).
- **Must enforce the 8-piece-per-style minimum (Section 5.3) — blocking, not just informational.** Any single style added to the list below 8 units should prevent the customer from proceeding/submitting until corrected.
- Once complete, that list **automatically carries into / pre-fills the intake form** on submission.
- Should feel like a real, polished tool — "clean and polished" was explicitly emphasized.
- **Build approach (confirmed): native custom-built functionality inside the Shopify theme** (Liquid + JavaScript), part of the same site build — **not** a separate installed/hosted Shopify App. Raheem explicitly confirmed "Option A": no separate app, no separate hosting/maintenance commitment, no OAuth install — just a well-built custom feature living in the same theme as everything else. This does not need its own project; it's part of the main site build.
- File upload (artwork) is the one piece native Shopify contact forms can't do out of the box — the build project will need to solve this within the custom-built approach (e.g., native Shopify line-item property file upload on a hidden/zero-price product mechanism, or another native-feeling method). Evaluate at build time; must not require a separate hosted app per the Option A decision above.

### 5.5 Intake/questionnaire form — final field list, with required/optional status resolved
- **Organization name** (required)
- **Contact info — decided:** separate structured fields, not one open field — **Name and Email (required), Phone (optional).** Reasoning: Raheem has consistently valued clean, structured, professional data over free-text blobs throughout this whole process (the product naming/data standard in Section 4.1, preferring real filterable options over text-in-title, the simple-but-structured package pages) — structured contact fields let his team act on a submission immediately (email a quote, call if needed) rather than parsing free text. Email is required since that's the primary follow-up channel; phone is optional since not everyone wants to be called.
- **Artwork upload** (**optional**)
- **Event/deadline date** (**optional**)
- **Estimated budget** (**optional**)
- **Estimated quantity** (required)
- **Product type(s)** (required)
- **Exact products chosen** (required if the customer used the build-your-list tool; not applicable otherwise)
- **Preferred decoration method** (**optional**)
- **How did you hear about us** (**optional**)

**Submission routing — confirmed:** every intake form submission must go to **orders@uptownmerch145.com** and **mgarafano@uptownmerch145.com**. This is the mechanism that closes the loop after a customer submits — the build project needs to wire form submissions to email both addresses. Exactly how depends on which technical mechanism gets chosen for this form — see Section 9's one open item.

**Post-submission experience — revised, confirmation email removed by Raheem's explicit decision:** the customer is taken to **a distinct confirmation screen/page** thanking them for their submission — not just an inline message on the same page. **No confirmation email is sent to the customer.** The only email in this flow is the internal orders@/mgarafano@ notification above; nothing goes back to the customer's inbox.

This same treatment (confirmation screen only, no customer email) applies to **both** the Organizations intake form and the general Contact Us form — see Section 6.

**This removes the technical obstacle flagged in earlier review passes — the build project should return to the original Option A plan (Section 5.4), fully native, no app needed for this form.** The previous concern was specifically about automatically emailing the *customer* a confirmation, which isn't something pure theme code can do without a server-side piece. With that requirement gone, everything left is achievable natively: **(1)** the confirmation screen is a straightforward redirect/page-swap after submission — ordinary theme functionality, no backend needed. **(2)** the internal notification to two addresses is achievable through Shopify's own native contact-form mechanism (which supports custom hidden fields for structured data beyond just name/email/message — a common, well-established pattern for capturing extra fields through Shopify's built-in submission pipeline) or, if the intake form isn't built on that mechanism, a plain email-forwarding rule on the receiving mailbox — either way, no custom email-sending code required. **The file-upload piece (Section 5.4) is a separate, still-open technical question, unrelated to this change** — evaluate that natively at build time as already noted; removing the confirmation email doesn't resolve that one.

### 5.6 Order fulfillment & payment (bulk) — clarified, changes what the website needs to do

**UMS manages the entire bulk order process — quoting, supplier sourcing, and payment — through ASI's ESP platform (ESP Web / ESP+), an existing, separate, industry-standard tool for the promotional products business.** This is not something the new Shopify site needs to handle at all. The website's job stops at capturing the lead and confirming receipt: package browsing → build-your-list → intake form → **email notification to orders@ and mgarafano@, plus a confirmation screen for the customer (no confirmation email — explicitly removed from scope)** (see Section 5.5). Everything downstream — quoting, invoicing, payment collection, supplier ordering, production — happens in ESP, entirely outside Shopify, managed manually by Raheem's team. **This meaningfully simplifies the build project's scope**: no draft-order/payment-link mechanism needs to be built for the bulk side, and — now that customer email confirmation is out of scope — no app or serverless piece is needed either; the intake form + internal notification + native confirmation screen is the complete deliverable for that flow.

**On Claude/ESP compatibility (Raheem asked directly):** there is no existing Anthropic/Claude connector or integration with ASI's ESP platform — checked directly against the MCP connector registry, nothing matches. This doesn't block anything here since the website only needs to email a lead, not integrate with ESP directly. If UMS wants deeper automation later (e.g., auto-creating ESP records from web submissions), that would be a separate initiative — ASI does offer some API/developer tooling on their end ("ESP Direct Connect" for supplier data sync was mentioned in their own materials), but a proper Claude-ESP integration doesn't exist today and would need its own scoping, not something to assume as part of this website build.

---

## 6. About Us / Contact Us / Social

- **About Us and Contact Us pages required.** About Us is built natively in Shopify (it's just static content — see below). Contact Us is **not** native — it runs on POWR Form Builder, per the decision below; this line previously said both were "built natively where possible," which is now stale and has been corrected.
- **About Us — approved, final:**

  > **Our Story**
  >
  > Uptown Merch Solutions opened its doors in Harlem in 2024, built on a simple idea: this neighborhood deserved a merch shop that actually understood it.
  >
  > UMS was founded in 2023 by someone who grew up right here in Harlem — this isn't just a business located in the community, it's built from it.
  >
  > Today, that shows up in two ways. The shop carries ready-to-wear pieces, embroidered, printed, and finished in-house. For schools, teams, and organizations that need something bigger, UMS for Organizations turns an idea into real branded gear for a whole group.
  >
  > Bringing brands to life, straight from Harlem.

  No founder name, no street address — kept out of this narrative copy deliberately (address can still appear functionally elsewhere, e.g. footer/pickup confirmation). **Approved by Raheem — ready for the build project to use as-is.**
- **Contact Us — finalized, revised to remove the customer confirmation email:** purpose is to be a low-volume catch-all for questions that don't fit either dedicated flow (buying directly from UMS Storefront, or submitting the UMS for Organizations intake form) — it is **not** a returns/support desk (the store's sales are final, see Section 4) and **not** a primary conversion path. Because of that, it doesn't need a dropdown or heavy structure. **The form itself: Name and Email (required) plus the "describe your question" field (required).** Email is still required here even without a confirmation email — it's how Raheem's team actually replies to the person, which is the more important reason anyway. **Build mechanism: POWR Form Builder (free plan), already installed on the store** — originally chosen partly for its autoresponder feature, which is **no longer needed and should not be configured/enabled.** The remaining reasons to keep using it: its custom post-submission message/redirect cleanly satisfies the distinct-confirmation-screen requirement (see Section 5.5), and admin notification on submission. **Honest note: with the confirmation-email need gone, a fully native Shopify contact form is a more viable alternative than it was before** — this is now closer to a preference than a technical necessity. Since POWR is already installed at no cost and already solves the confirmation-screen requirement cleanly, the default here is to keep using it rather than redo the work to revert to native, but reverting is a real option if Raheem would rather not depend on any app at all for something this simple. **Page structure:** the Contact Us page itself is a normal native Shopify page — POWR is only the form widget, embedded within that page alongside natively-built informational content (hours, address, phone/email, social links, and a brief policy note) around it. POWR does not host or replace the whole page. **Styling — expanded per Raheem's explicit instruction to customize as much as possible, not just colors:** the embedded POWR widget should be made to look like a native part of the site, not recognizable as a third-party form at all. Beyond the color mapping (`#355E3B` buttons/accents, `#a9a5a4`/`#838388` borders/secondary text/backgrounds, confirmed available on POWR's free plan via its Custom CSS panel — verified directly against POWR's own pricing page), also match: **typography** (the site's fonts — "Basic Commercial"/"Assistant," or whatever the build project settles on per Section 2 — applied to labels, input text, and button text, not POWR's default font); **button shape and spacing** (border-radius, padding, and sizing consistent with the rest of the site's buttons, e.g. the single hunter-green "Check out" button style already specified in Section 7); **input field styling** (border color/weight, focus states, corner radius matching the site's other form-like elements, such as the quantity fields in cart/build-your-list); and **overall spacing/layout density** matching the rest of the page rather than POWR's own default form padding. The goal is that a visitor lands on Contact Us and has no visual cue they've left the native theme. This lets the most common questions (hours, location, "do you still do custom work") be self-served without submitting anything at all. **Phone number: 646-398-8178** (this is the store's in-store line, confirmed). Any important client information relayed by phone should still make its way to **both orders@uptownmerch145.com and mgarafano@uptownmerch145.com** — the same two addresses as the form-submission routing in Section 5.5, not mgarafano@ alone. Note: POWR's free tier includes only 1 email administrator, so it may only notify one address directly in-app — set it to notify orders@, then add a simple forwarding rule on that mailbox so a copy also reaches mgarafano@, rather than needing a paid tier just for this. **Post-submission:** a distinct confirmation screen thanking them for their message, natively provided by POWR's redirect/custom-message feature — **no confirmation email is sent to the customer.**
- **Social media section required**, listing:
  - TikTok: **@145uptownmerch**
  - Instagram: **@145uptownmerch**

---

## 7. Cart & checkout — confirmed fixes

Verified directly against the live site's actual settings and real screenshots (not guesses):

- **Switch from cart notification popup to a real slide-out drawer.** The live theme is currently set to `cart_type: notification` (a small popup, not a drawer) — confirmed broken/unpolished (a real screenshot showed the popup overlapping/obscuring other on-page text like "Continue shopping" with no backdrop). Fix: real slide-out drawer with a proper dimmed backdrop.
- **Express payment buttons — precise distinction, clarified by Raheem.** Remove the Shop Pay / PayPal / Google Pay shortcut buttons that currently clutter the cart and product pages — that visual clutter was the actual complaint. **Keep them available as normal payment methods within Shopify's actual hosted checkout page itself** — that's just a fast, secure way to pay once someone's already checking out, not clutter. So: cart/product pages show a single "Check out" button only (styled in brand hunter green, currently orange); the real checkout page beyond that can still offer Apple Pay/Google Pay/etc. as payment options.
- **Remove Shop Pay "pay over time" installment messaging** from product pages (native toggle, not custom code) — irrelevant for a small pickup-only local store.
- **Fix shipping copy:** cart/checkout currently reads "Taxes, discounts and shipping calculated at checkout" — must be replaced with pickup-only messaging (no shipping implied) for store products.
- **Remove the large empty/dead block** currently present in the cart page footer area (visually broken, unused whitespace with nothing in it).
- **Move the newsletter signup out of the checkout flow** — currently sits directly under the checkout buttons, interrupting the path to purchase. Belongs in the footer only.
- Apply the corrected brand palette (hunter green/gray/white, no orange, no purple) consistently through cart, checkout, and Shopify's separate **Checkout branding editor** (colors/logo/fonts — a distinct system from the theme itself, native to Shopify, available without Plus).
- Confirm pickup details are clearly communicated in the cart, not just on the product page — including store hours (Tuesday–Saturday, 11am–8pm) now that they're set.

---

## 8. Full visual audit findings (current live site, by section)

### Homepage
Currently a single hardcoded custom-liquid block: two large logo tiles ("Uptown Blanks" → blank-apparel collection, "Uptown Merch Solutions" → order-form page) plus a bottom bar linking out to the external ESP site. Problems: no headline/story/trust content, two unrelated background photos floating behind the right tile without integrating into the page, generic filler label copy, ESP link (being removed per Section 3), no reflection of it being a real Harlem storefront. **This entire homepage needs to be rebuilt** to reflect the unified nav/brand structure in Section 3 — not patched.

### Header / navigation
Plain black-on-white Dawn default ("scheme-1") — zero brand color anywhere in the header. Flat 4-item menu with non-descriptive labels ("Services," "Blanks," "Events and Promotional Products," "Contact Us") that give a visitor no signal about which path is the store vs. the bulk program. One item still points at the leftover ESP catalog page. No "About" link existed. **Fixed by:** the nav structure in Section 3.

### Product grid / collection page
Flat gray Dawn cards, no borders/radius. Real products pulled from the live catalog show the raw-SKU-title and stale-vendor problems described in Section 4.1. Plain white-background supplier product photos with no lifestyle treatment, nothing tying visually to the brand, no visual distinction between product types at a glance. (Correction: filtering and sorting are already enabled in the theme's actual settings, verified later during the mobile pass — that part doesn't need fixing, only the visual/data problems above.)

### Product page (verified against a real screenshot)
- A dark brown/black gradient background covers the entire page (header + body) — doesn't match the brand and isn't even Dawn's plain default; source unclear, likely a global site-wide background that needs to be found and removed everywhere, not just on this page.
- Logo slot at the top is empty/not displaying.
- Three uncoordinated backgrounds compete on one screen (dark gradient page, white photo panel, cream info panel).
- Title is the raw multi-line all-caps import string (see Section 4.1).
- Color variant mislabeled "January" (data bug, see Section 4.1).
- Orange price / orange "Add to cart" / purple "Buy with Shop" — none of these colors match the real brand.
- Shop Pay installment messaging present (remove, see Section 7).
- Description contains leftover custom-decoration language (remove, see Section 4.1).
- Pickup messaging ("Pickup available... usually ready in 24 hours") is present and works well — **keep this pattern**, just fix the grammar/name reference per Section 3 and extend similar messaging to the cart.

### Cart page (verified against a real screenshot)
All of Section 7's fixes apply here. Additionally confirmed: same dark gradient background, same raw title/vendor/"January" bugs surfacing again in the cart line item, four clashing button colors in the checkout block, dead empty block, shipping copy contradicting pickup-only, cart notification overlap/legibility bug on "Continue shopping."

### Mobile (verified against real theme settings, not assumed)
- **Country selector and language selector — both confirmed for removal.** Verified enabled in the header's actual settings. Raheem confirmed the realistic customer base is English- and Spanish-speaking, but decided against building real localization for it — anyone needing another language can use their browser/Google Translate, so both selectors get removed rather than built out. The country selector had no functional purpose to begin with either way (pickup-only, single location, no shipping/currency variation).
- **"UMS for Organizations" must keep its primary visual weight in the mobile menu too — confirmed.** Not plain text like the other rows in the stacked list; needs its own distinct treatment (e.g., a highlighted background or button-style row) so the "this is the primary path" signal that works via button styling on desktop still reads clearly in a mobile drawer.
- **Collection grid — resolved.** Keep 2 columns on mobile — it's the standard, clean choice for a mobile shopping grid and was never really the problem. The actual issue was the old all-caps, multi-line SKU titles wrapping badly at that card width, which the naming system in Section 4.1 already fixes. **Quick-add-to-cart: turn on** (currently off, confirmed decision) — removes the extra full-page tap-through just to add an item from the grid.
- The cart-drawer decision (Section 7) pays off doubly on mobile — a proper slide-out drawer is a much better small-screen pattern than the tiny corner notification popup that was actually live.
- The old two-tile homepage stacks vertically on mobile (confirmed by how Dawn's grid sections reflow), forcing a long scroll before reaching any real content — moot since the whole homepage is being rebuilt (Section 8, Homepage), but additional evidence for why.
- **Scope confirmation:** every fix already agreed on for desktop (Sections 2–7: brand colors, naming system, cart drawer, single checkout button, pickup/policy messaging, everything) applies equally to mobile. Mobile is the same site, not a reduced or separate design pass.

---

## 9. Open items and review history

**Still open: none.** The one remaining item (the bulk intake form's technical build mechanism) is resolved below — Raheem's decision to drop the customer confirmation email removed the exact problem that item existed to solve.

**Major update: customer confirmation email removed from scope entirely, per Raheem's explicit decision.** This was not a small tweak — it removed the core technical problem driving the last open item in this document. Consequences, worked through fully:
- **Contact Us (Section 6):** confirmation email dropped from POWR's configuration (don't enable the autoresponder). POWR is kept for the confirmation-screen and admin-notification features, which are still useful, but its original strongest justification (customer email) is gone — noted honestly as now closer to a preference than a necessity, with reverting to a fully native Shopify contact form named as a real alternative if Raheem would rather not depend on any app for something this simple.
- **Bulk intake form (Sections 5.5, 5.6):** this is the bigger consequence. The previous "still open" item existed entirely to solve automatic customer-email-sending under a pure-native build — the one piece plain theme code genuinely couldn't do alone. With that requirement gone, **the build project returns cleanly to the original Option A plan: fully native, no app, no serverless piece needed for this form.** The confirmation screen is a native redirect; the internal two-address notification is achievable through Shopify's native contact-form mechanism or simple mailbox forwarding. The three previously-proposed paths (POWR paid tier, POWR-as-email-backend via hidden fields, or a custom serverless function) are no longer needed for this reason and are moot.
- **File upload (Section 5.4) remains a separate, still-open technical question**, unrelated to this change — removing the confirmation email doesn't resolve that one; it still needs to be evaluated natively at build time.

**Resolved earlier this session — the four business-logic gaps found on the third review pass:**
- **Intake form fields:** artwork, deadline, and budget are all optional; contact info is structured as Name + Email (required) and Phone (optional) — see Section 5.5 for the reasoning.
- **Minimum order quantity:** changed to 8 pieces per style, enforced/blocking in the build-your-list tool — see Sections 5.3 and 5.4.
- **Post-submission experience:** a distinct confirmation screen (no longer a confirmation email — see above), for both the Organizations intake form and Contact Us — see Sections 5.5 and 6.
- **Green hex:** explicitly confirmed final by Raheem — see Section 2.

**Everything else raised across this entire discovery process is resolved** — business model, navigation, brand palette, logo files, the Storefront spec and product naming standard, the Organizations/bulk program spec including the ESP finding and fulfillment model, About/Contact/social content, cart & checkout fixes, and the mobile-specific pass. Sections 2–8 reflect the current, correct state directly.

**Review history (for provenance, not action):** this document went through six increasingly critical review passes after the initial discovery process. Pass one caught a factual error (product grid filtering) and two broken/stale references. Pass two found that three confirmed decisions (footer, cart icon on Organizations pages, favicon) had been marked "confirmed" without their actual content ever being written down, a product-count arithmetic error masking stray placeholder products in the catalog, and a naming-standard inconsistency between the stated format and its own examples. Pass three verified claims against ground truth rather than just re-reading (pixel-sampled the actual delivered logo files, scanned for markdown syntax errors, cross-checked every repeated fact for transposition errors — all clean) and surfaced four business-logic gaps. Pass four resolved those four gaps based on Raheem's direct answers. Pass five traced the newly-added confirmation-email requirement through to its actual consequences and found the Contact Us form had no email field at all (fixed) plus a real technical-feasibility risk in sending customer confirmation emails under a pure-native build (flagged). Pass six checked the document for staleness after the POWR decision was added and found Section 6's opening line still claimed Contact Us would be "built natively," directly contradicting the POWR decision specified two sentences later — fixed, plus added POWR as a tracked dependency in Section 10. Raheem then installed POWR on the store (Sections 6, 9, 10 updated accordingly). Pass seven went past "is POWR installed" into how it actually integrates with the rest of the site, and found three real gaps: whether Contact Us is a native page with POWR embedded or POWR-hosted entirely (clarified: native page, POWR is just the widget), a missing requirement to restyle POWR's default appearance to match the brand palette (added), and an understated technical complexity in one of the three proposed paths for the bulk form (flagged). **Then Raheem removed the customer confirmation email requirement entirely** — traced through above, this simplified the bulk intake form's mechanism back to fully native, the exact outcome Option A called for from the start.

---

## 10. Technical / Shopify environment notes

- Shopify plan: Shopify (standard tier). Currency: USD. Timezone: EDT.
- Live/published theme: **"UMS logo homepage Live Version"** — theme ID `160521519330`, role `MAIN`.
- Unpublished staged theme: **"UMS site - Create Your Brand Uptown"** — theme ID `162397749474`, role `UNPUBLISHED`. Confirmed by Raheem to be a documentation-only duplicate of the live site (see Section 9) — **the rebuild should use a brand-new theme, not this one and not the current live theme.**
- Current live theme is a customized Shopify Dawn theme.
- Current main nav handle: `main-menu`.
- Current collections of note: "Uptown Blanks" (33 products, tag `uptown-blanks`), "POS Services" (8 products, tag `uptown-service`), "Products"/all (45 total). Numerous other collections exist but are empty placeholders (DTF, DTG, Stickers, Banners & Posters, Custom Patches, School & Work Uniforms, DTF Gang Sheets, DTF By Size, Banners, Garment Type, Fees, UMS Customer Kiosk) — leftover from an earlier, abandoned plan. **Confirmed by Raheem for removal** (see Section 9) — not yet deleted, since this discovery project hasn't made live changes to the store.
- **App dependency: POWR Form Builder (free plan) — installed and confirmed, used for Contact Us only.** See Section 6. Its autoresponder feature should not be enabled — the customer confirmation email was removed from scope (see Section 9). The bulk intake form does not depend on this app; it's built fully native (Section 5.4/5.5), since removing the confirmation-email requirement eliminated the only reason an app was being considered for that form.
- **Note for the build project (not a Raheem decision, just good practice):** as URLs change (old nav paths like `/pages/order-form`, the `/collections/uptown-blanks` handle, etc. get replaced by the new structure in Section 3), set up 301 redirects from the old paths to their new equivalents rather than leaving them to 404 — avoids broken links from anything already indexed or bookmarked.
