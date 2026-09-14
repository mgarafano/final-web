# Build log

## Environment facts (verified, not assumed)

| Thing | Value |
|---|---|
| Store | Uptown Merch Solutions — uptownmerch145.com, Shopify plan, USD, EDT |
| **Live theme** | **"Dawn" — ID `162803220706`, role MAIN, published 2026-09-13 23:47 UTC** |
| Build theme | "UMS Rebuild 2026" — ID `162803613922`, role UNPUBLISHED |
| Dawn version | 16.0.0 |
| Old live theme | "UMS logo homepage Live Version" (`160521519330`) — now unpublished |
| Backup | "Copy of UMS logo homepage Live Version" (`162803089634`) |
| Staged dupe | "UMS site - Create Your Brand Uptown (staged)" (`162397749474`) |
| Sales channels | Online Store, Point of Sale, Shop, Snapchat Ads, Inbox |

## What this session's tooling can and cannot do

| Capability | Status |
|---|---|
| Read all products, collections, themes, files | ✅ |
| Write theme files to an **unpublished** theme | ✅ verified |
| Duplicate a theme | ✅ |
| Create a theme from a remote zip | ❌ blocked — `themeCreate` returns "Src is empty" |
| Write theme files to the **live/MAIN** theme | ❌ blocked by policy |
| **Publish a theme** | ❌ blocked — Raheem must click Publish in admin |
| Update products, collections, metafields | ✅ |
| Read installed apps | ❌ `appInstallations` — access denied |
| Fetch `cdn.shopify.com` from this container | ❌ egress proxy denies it |

The publish restriction is a good thing here: it makes it impossible for this
session to put anything in front of customers by accident. Go-live is a
deliberate human action.

## Progress

- **2026-09-13** — Audited all 45 products. Created build theme by duplicating the
  clean Dawn. Pushed `assets/ums-brand.css` (palette + nav weighting + cart
  suppression tokens). Wrote `docs/01-product-cleanup-proposal.md`.
