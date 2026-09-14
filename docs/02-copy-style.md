# UMS copy style

Applied across product data, theme copy, pages, and collections. Written down so
the remaining phases stay consistent rather than drifting.

## Capitalization

| Where | Style | Example |
|---|---|---|
| Product titles | Title Case, em dash before the color | `Oversized Tee — Arctic Blue` |
| Section headings | Sentence case | `In the shop right now` |
| The tagline | Title Case — it's a brand asset | `Bringing Brands to Life.` |
| Tagline inside prose | Sentence case, as approved | `Bringing brands to life, straight from Harlem.` |
| Buttons and CTAs | Sentence case in the data | `Start your order` |
| Nav labels | As locked in the brief | `UMS Storefront`, `UMS for Organizations` |
| Color option values | Title Case, one flat word | `Burgundy`, `Charcoal`, `Natural` |

Buttons are uppercased by CSS (`text-transform`), never by typing them in caps.
That keeps the underlying text readable to screen readers and correct if the
transform is ever removed.

**Note on the brief.** Section 4.1 calls the title format "sentence case," but every
approved example in that same section is Title Case (`Oversized Tee — Arctic Blue`,
`Youth Tee — White`). The examples won, since they're the concrete approved artifact
and Title Case is the retail norm for product names.

## Spelling

**American English throughout** — `Gray`, not `Grey`; `color`, not `colour`.

The brief's one worked example used "Grey," but the store's own existing data used
"Gray" in the headwear options, and a Harlem storefront selling to US schools and
companies should read as American. Mixing "Grey" in a title with "color" in the
description below it would have been the worst of both.

## Punctuation

- **Oxford comma**, always. The approved About copy uses it ("embroidered, printed,
  and finished in-house"), so the rest of the site matches.
- **Em dash** (—) for the color separator in product titles and for parenthetical
  asides. Spaced, not tight.
- **En dash** (–) for ranges: `Tuesday–Saturday`, `11am–8pm`.
- Description bullets are fragments with **no terminal period**. The lead sentence
  above them **does** end with a period.

## Recurring words

| Use | Not |
|---|---|
| `241 W 145th St` (everywhere) | `241 W 145th Street` |
| `Tuesday–Saturday, 11am–8pm` | `Tuesday to Saturday`, `11am - 8pm` |
| `Pickup only` (noun/adjective) | `Pick up only` |
| `picked up in store` (verb) | `pickup in store` |
| `All sales are final.` | `All sales final.` |
| `UMS for Organizations` | `UMS For Organizations` |

## Product descriptions

One sentence saying what it is, then 2–4 short bullets covering fabric weight, fit,
and standout construction. Never:

- the vendor name or an internal style code
- language implying the item is a blank for further decoration — no "built for
  embroidery," "a strong blank option," "cotton facing for printing"

## Image alt text

`<Product name> in <Color>` — e.g. `Oversized Tee in Arctic Blue`. Describes the
photo for screen readers and search without repeating the title verbatim.
