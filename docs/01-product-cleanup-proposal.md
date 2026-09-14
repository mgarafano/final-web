# UMS — Product Data Cleanup Proposal

**Status: PROPOSAL. Nothing has been executed.** Product data is store-wide, not
theme-scoped — the moment it changes, it changes on the live site. Nothing in this
document runs until Raheem approves it.

Audited against live Shopify data on 2026-09-13. All 45 products reviewed.

---

## 1. What the catalog actually contains

The brief estimated "~33 `uptown-blanks` + ~8 `uptown-service` ≈ 41 real products,
plus a handful of stray placeholders." The real numbers:

| Group | Count | Reality |
|---|---|---|
| `uptown-blanks` | 33 | 29 sellable, 3 archived (0 stock, $0), 1 draft (0 stock) |
| `uptown-service` | 8 | In-store decoration service SKUs — see §2 |
| `Sample Product` | 4 | "Example product" × 4, $100, 0 stock — **live on the storefront right now** |
| **Total** | **45** | Matches the "Products" collection exactly |

The arithmetic in the brief resolves cleanly: 33 + 8 + 4 = 45. The "stray items" are
the 4 example products.

### Two duplicate collections
`Uptown Blanks` and `POS Products` are byte-identical smart collections — same rule
(`tag = uptown-blanks`), same 33 products. One of them is redundant.

---

## 2. BLOCKER: the 8 "service" products contradict the brief

The brief instructs that the storefront catalog be the ~41 products (33 blanks +
8 services). But the 8 `uptown-service` products are, on inspection, **the custom
decoration business the brief says is discontinued**:

| Product | Variants | What it actually sells |
|---|---|---|
| DTF Services | 30 | Per-placement DTF print pricing; "BYO merch", customer-supplied tees |
| Embroidery Services | 7 | Custom hat embroidery, "BYO hat", per-letter pricing |
| Embroidery Setup and File Services | 3 | Digitizing fees ($40 / $25 / $100) |
| Heat Press Vinyl | 8 | Cut-vinyl names/numbers, "customer merch or transfer" |
| Custom Stickers | 7 | Sticker runs by size/qty |
| Window Decals | 5 | Storefront vinyl, per-sq-ft graphics |
| Step and Repeat / Banners | 10 | Event backdrops; 5 variants are $0.00 "quote" placeholders |
| Quote Request | 5 | $0.00 checkout used as a lead form |

Selling these online conflicts with **five separate confirmed decisions** in the brief:

1. **§4 — no customization.** "Customers are not choosing/customizing; they're buying
   finished, pre-decorated items." DTF/embroidery/vinyl services are exactly customization.
   The DTF description even says *"Artwork should be uploaded through the custom print
   order form or product personalizer"* — the discontinued model, verbatim.
2. **§3 — remove all ESP content.** `Quote Request` has a live variant
   **"ESP catalog quote request"** (SKU `QUOTE-ESP`), and its description references
   "outsourced ESP catalog work."
3. **§5.5 / §9 — no customer confirmation email.** `Quote Request`'s own description
   states: *"after checkout, Shopify will send the customer an order confirmation."*
   A $0 checkout fires a Shopify confirmation email today.
4. **§5 — Organizations has no cart or checkout.** `Quote Request` includes a
   **"Bulk order quote request"** variant — a competing bulk lead path that runs
   *through the cart*, directly undercutting the new intake form.
5. **§4 — fixed-price only.** Several variants are priced $0.00 as quote placeholders.

### Recommendation
**Do not delete them** — they are almost certainly live in-store POS SKUs, and deleting
would break register operation. Instead: **remove them from the Online Store sales
channel only, keeping Point of Sale.** Reversible, preserves in-store use, keeps the
website consistent with the brief.

Note: 6 of the 8 are currently published to Online Store **and** POS; `Embroidery Setup
and File Services` and `Custom Stickers` are published to Online Store only — if those
are used at the register, they need adding to POS before their online listing is removed.

**This needs Raheem's decision before the storefront catalog scope is final.**

---

## 3. URGENT: 4 fake products are live right now

Four products titled **"Example product"**, priced **$100.00**, 0 inventory, are
`ACTIVE` and published to the Online Store. They are visible on uptownmerch145.com
today, and they sit in a "Default example products" collection.

Recommended immediate action: set all four to **DRAFT**. That removes them from the
storefront instantly, is completely reversible, and touches nothing else.

| Product ID | Title | Price |
|---|---|---|
| 9284977262818 | Example product | $100.00 |
| 9284977328354 | Example product | $100.00 |
| 9284977361122 | Example product | $100.00 |
| 9284977426658 | Example product | $100.00 |

---

## 4. Proposed renames — all 33 `uptown-blanks` products

Format per brief §4.1: `[Fit/audience] [Garment type] — [Color]`, sentence case,
vendor name and style code dropped from the title.

**Every SKU is left untouched.** Titles, vendor, product type, descriptions and
option *labels* change; SKU fields, variant IDs and inventory quantities do not.

### Apparel — 21 products
Colour lives in the title here because each colour is its own product (Size is the
only variant axis).

| # | ID | Current title | → Proposed title |
|---|---|---|---|
| 1 | 9219808657634 | UPTOWN BLANKS ZS4010 ARCTIC BLUE | Oversized Tee — Arctic Blue |
| 2 | 9219808854242 | UPTOWN BLANKS ZS4010 MINT | Oversized Tee — Mint |
| 3 | 9219808919778 | UPTOWN BLANKS ZS1002 GREY HEATHER | Heather Crewneck Tee — Grey |
| 4 | 9219809050850 | UPTOWN BLANKS ZS2103 BLACK | Women's Crop Long Sleeve — Black |
| 5 | 9219809116386 | UPTOWN BLANKS ZS2103 WHITE | Women's Crop Long Sleeve — White |
| 6 | 9219809214690 | UPTOWN BLANKS ZS2001 WHITE | Youth Tee — White |
| 7 | 9219809280226 | UPTOWN BLANKS ZS2001 GREY HEATHER | Youth Tee — Grey |
| 8 | 9219812196578 | UPTOWN BLANKS ZS1701 WHITE | Heavyweight Tee — White |
| 9 | 9219812720866 | UPTOWN BLANKS ZS1701 BLACK | Heavyweight Tee — Black |
| 10 | 9219812819170 | UPTOWN BLANKS ZS1003 WHITE | Tank Top — White |
| 11 | 9219812884706 | UPTOWN BLANKS ZS1003 NEW NAVY | Tank Top — Navy |
| 12 | 9219812983010 | UPTOWN BLANKS ZS1201 PFD | Garment-Dyed Oversized Tee — Natural |
| 13 | 9219813146850 | UPTOWN BLANKS ZS4080 PFD | Oversized Hoodie — Natural |
| 14 | 9219815637218 | UPTOWN BLANKS ZS4007 VINTAGE DENIM | Mineral Wash Shorts — Vintage Denim |
| 15 | 9219815702754 | UPTOWN BLANKS ZS4009 BUBBLE GUM | Tie-Dye Joggers — Bubble Gum |
| 16 | 9219815801058 | UPTOWN BLANKS ZS4009 SKY BOMB | Tie-Dye Joggers — Sky Bomb |
| 17 | 9219815899362 | UPTOWN BLANKS ZS4009 BLACK SMOKE | Tie-Dye Joggers — Black Smoke |
| 18 | 9219815538914 | UPTOWN BLANKS ZS4007 VINTAGE BLACK | Mineral Wash Shorts — Vintage Black *(stays DRAFT — 0 stock)* |
| 19 | 9219813245154 | UPTOWN BLANKS ZS4004 BUBBLE GUM | *leave as-is — ARCHIVED, 0 stock, $0* |
| 20 | 9219814588642 | UPTOWN BLANKS ZS4004 PINK MARBLE | *leave as-is — ARCHIVED* |
| 21 | 9219815342306 | UPTOWN BLANKS ZS4004 SKY BOMB | *leave as-is — ARCHIVED* |

Three notes on judgment calls above:
- **"PFD"** (#12, #13) is a mill term — *Prepared For Dye*, i.e. undyed. It means nothing
  to a shopper, so it becomes **Natural**.
- **Evocative colour names are kept in the title** (Bubble Gum, Sky Bomb, Arctic Blue)
  because they are the real colourway names on the garment and the invoice. The *flat*
  colour for filtering is handled separately — see §5.
- **Archived items (#19–21) are deliberately skipped.** They are invisible to the
  storefront, have no stock, no price and no real description. Renaming them is effort
  with no customer-facing benefit.

### Headwear — 12 products
Colour is a real variant option here, so multi-colour products carry no colour in the title.

| # | ID | Current title | → Proposed title | Option value change |
|---|---|---|---|---|
| 22 | 9220148855010 | UPTOWN BLANKS 2552 8 Inch Skull Acrylic Beanie | Skull Beanie — Black | *(none)* |
| 23 | 9220151116002 | UPTOWN BLANKS 2563 Fisherman Beanie 9 Inch | Fisherman Beanie | *(none)* |
| 24 | 9220150067426 | UPTOWN BLANKS 3532 Oil Waxed Unstructured 5 Panel Cap | Oil-Waxed 5-Panel Cap — Brown | *(none)* |
| 25 | 9220148199650 | UPTOWN BLANKS 3533 7 Panel Suede Cap | Suede 7-Panel Cap — Brown | *(none)* |
| 26 | 9220148986082 | UPTOWN BLANKS 4527 5 Panel Designer Plaid Cotton Baseball Cap | Plaid Baseball Cap — **?** | **"January" → ?  (see below)** |
| 27 | 9220151017698 | UPTOWN BLANKS 4531 5 Panel Melton Wool Suede Cap | Melton Wool Suede Cap — Grey | "Gray/Brown" → "Grey" |
| 28 | 9220150624482 | UPTOWN BLANKS 4532 5 Panel Melton Wool Cap With Metal Buckle | Melton Wool Buckle Cap — Grey | "Gray" → "Grey" |
| 29 | 9220150198498 | UPTOWN BLANKS 6527 5 Panel Corduroy Two-Tone Snapback Cap | Two-Tone Corduroy Snapback | "Mustard Yellow" → "Yellow" |
| 30 | 9220148363490 | UPTOWN BLANKS 7528U 5 Panel Unstructured Corduroy Snapback Hat | Unstructured Corduroy Snapback | "Burgundy Corduroy" → "Burgundy"; "Forest Green Corduroy" → "Green" |
| 31 | 9220150329570 | UPTOWN BLANKS 7539 5 Panel Corduroy Rope Trucker Cap | Corduroy Rope Trucker Cap — Burgundy | "Burgundy Red/Khaki Beige" → "Burgundy" |
| 32 | 9220150493410 | UPTOWN BLANKS 8608 6 Panel Fitted Flat Bill Cap | Fitted Flat Bill Cap — Black | *(none)* |
| 33 | 9220148691170 | UPTOWN BLANKS DC112FP 5 Panel Premier Trucker Cap | Premier Trucker Cap | "Charcoal Gray/Black" → "Charcoal" |

### The "January" bug — I need Raheem's eyes on this one
Product #26's Color option is literally **"January"**, and the SKU is **`4527-JANUARY`**.
The brief's example guessed `Red Floral`, but "January" carries no colour information at
all, so that guess cannot be verified from the data. **I will not invent a colour for a
product that will be sold.** Raheem needs to look at the cap (or its photo) and tell me
the colour.

The SKU `4527-JANUARY` is proposed to stay **unchanged** — SKUs are the stable inventory
key and likely match physical tags and POS records. It will read slightly oddly, but
correctness of inventory tracking outranks tidiness. Say the word if you'd rather I
change it.

### Spelling: Grey vs Gray
Live data is inconsistent — apparel uses "GREY HEATHER", headwear uses "Gray".
Standardising on **Grey**, matching the brief's own approved example
(`Heather Crewneck Tee — Grey`).

---

## 5. Filterable colour and garment type

The brief (§4.1) requires garment type and colour to exist as real filterable data,
not just words in a title. Current state: neither does.

- **Garment type → native `Product type` field.** Currently "Blanks" / "Blank Apparel"
  (internal jargon that also contradicts the finished-goods model). Proposed real values:
  `T-Shirt`, `Tank Top`, `Hoodie`, `Joggers`, `Shorts`, `Cap`, `Beanie`. Product type is a
  native Shopify filter dimension — no extra machinery needed.

- **Colour → a `Color` metafield**, not tags and not a new variant option.
  - *Not tags*, because Shopify's tag filter exposes **every** tag, and the catalog is
    full of internal ones (`invoice-import`, `headwear-import`, style codes like `zs4010`).
    That filter would be unusable.
  - *Not a new variant option*, because adding an option touches variant structure on a
    live store — exactly where SKU and inventory risk lives.
  - A metafield is zero-risk to variants, keeps the flat one-word values you asked for
    (Blue, Pink, Grey, Natural…), and filters cleanly alongside Product type.

Proposed flat colour values: Arctic Blue → `Blue`, Mint → `Green`, Bubble Gum → `Pink`,
Sky Bomb → `Blue`, Black Smoke → `Black`, Vintage Denim → `Blue`, PFD → `Natural`,
New Navy → `Navy`, Grey Heather → `Grey`.

---

## 6. Vendor and description rewrites

- **Vendor:** all 33 blanks currently read `UPTOWN BLANKS` → set to
  `Uptown Merch Solutions`, hidden from display in the theme.
- **Product type:** per §5 above.
- **Descriptions:** every one needs work. Two problems run through the whole catalog:
  1. All apparel descriptions open with a bold `UPTOWN BLANKS ZS4010 Arctic Blue` line
     and close with `Style: ZS4010. Color: Arctic Blue.` — vendor name and internal code
     exposed to customers.
  2. **Every headwear description and several apparel ones sell the item as a decorator's
     blank** — "built for embroidery, patches, and custom decoration", "a strong blank
     option for embroidery", "made for durability, comfort, and customization", "100%
     cotton facing for printing". This is the discontinued model, and it is pervasive,
     not the single instance the brief flagged.

New format per §4.1 — one sentence on what it is, then 2–4 short bullets. The genuinely
useful fabric specs already in the data (GSM/oz weights, construction details) are kept.

**Before**
> **UPTOWN BLANKS ZS1701 White**
> Heavy Weight Short Sleeve Tee made for durability, comfort, and customization. Built
> from 186 GSM / 5.5 OZ premium ring-spun combed cotton with ribbed neck band, satin
> tearaway label, shoulder taping, tubular construction, and double needle stitching at
> the sleeve and bottom hem.
> Style: ZS1701. Color: White.

**After**
> A heavier-weight everyday tee built to hold its shape wash after wash.
> - 186 GSM (5.5 oz) premium ring-spun combed cotton
> - Ribbed neckband, shoulder taping, tubular construction
> - Double-needle stitching at sleeve and bottom hem

**Before** (headwear — decoration language)
> A 5-panel corduroy snapback with a two-tone build for extra contrast on the front
> panel. The ribbed corduroy texture **holds embroidery cleanly** and gives the cap a
> warmer, more textured look than a standard twill snapback.

**After**
> A five-panel corduroy snapback with contrast panels and a warmer, textured finish.
> - Ribbed corduroy face, two-tone build
> - Snapback closure
> - Available in yellow and black

---

## 7. Decisions needed before anything runs

1. **The 8 service products** — remove from Online Store (keep POS), as recommended? Or
   something else?
2. **The 4 "Example product" items** — set to DRAFT now? (They are live at $100 today.)
3. **Product #26's real colour** — what colour is the 4527 plaid cap?
4. **SKU `4527-JANUARY`** — leave it, or correct it once the colour is known?
5. **Duplicate collections** — `Uptown Blanks` and `POS Products` are identical. Keep which?
6. **Colour via metafield** — confirm the approach in §5.
