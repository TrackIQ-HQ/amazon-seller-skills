# Every check

## A. Inventory hygiene — from `get_inventory_snapshot`

Paginate; it caps at 100 rows.

| Check | Test | Why it matters |
|---|---|---|
| **GUID ASINs** | ASIN is not a `B0…` code | a broken or placeholder listing |
| **FBM shadows** | `_FBM` suffix, zero stock, null title | clutter that breaks every join |
| **Variation parents** | SKU contains `parent`, `-P`, `Set`; generic title; no stock | not sellable; counted as products by mistake |
| **Dead listings** | `total == 0` and no sales in 90 days | should be closed or removed |
| **Stranded stock** | stock on a SKU with no sales while a sibling SKU sells | capital stuck on the wrong SKU |
| **Unfulfillable** | `unfulfillable > 0` | already lost; remove or dispose |
| **Duplicate SKUs** | two SKUs, same ASIN, both with stock and sales | usually a migration that never finished |

**The count itself is the finding.** On the account this family was built
against, roughly **70 of 146 snapshot rows** were parents, FBM shadows, GUID
ASINs or dead listings. Nobody knew. Report the count and the split before
listing individual rows.

**Never flag a SKU with sales and zero stock as dead.** That is the most urgent
row in the catalogue and it belongs to `trackiq-restock-priority`.

## B. Commercial hygiene — from `get_product_performance` and `get_product_ads`

| Check | Test |
|---|---|
| **No traffic** | sessions under 30 in 90 days on a live listing |
| **No support** | revenue but zero ad spend in 90 days |
| **Traffic, no conversion** | sessions above 200, conversion under 2% |
| **Advertised, not selling** | ad spend above $100, zero orders in 90 days |
| **Sells without a listing check** | revenue but the ASIN never appears in the ad feed |

"No traffic" and "no support" together usually mean a product nobody has
thought about for a year. That is the single most common real finding in this
report.

## C. Page hygiene — from Oxylabs `get_product`, 1 credit per ASIN

| Check | Test | Note |
|---|---|---|
| **Thin images** | fewer than 6 | 7–9 is healthy |
| **Short title** | under 80 characters | the phone shows ~80; under it is wasted |
| **Long title** | over the stated threshold | state the threshold; limits vary by category |
| **Bullets over five** | split on newline, count > 5 | the sixth is invisible on the page |
| **Bullets under five** | count < 5 | wasted space |
| **Long bullets** | any bullet over ~250 characters | truncates on mobile |
| **No coupon while rivals run one** | `coupon_discount_percentage` empty | optional, needs a competitor set |
| **Not buyable** | `buybox.stock` not "In Stock" | urgent |
| **Buy box lost** | `buybox.seller` is not the brand | urgent |
| **Low rating** | `rating` under 4.0 with 15+ reviews | |
| **High one-star** | one-star share above 10% | from `rating_stars_distribution` |

## D. The four that cannot be automated

There is **no A+ flag, no video flag, no backend search terms and no variation
family** anywhere in either tool.

| Check | Status |
|---|---|
| A+ content present, and which modules | **needs eyes** |
| Video present | **needs eyes** |
| Backend search terms populated and unique | **needs Seller Central** |
| Variation family complete, no orphan children | **needs Seller Central** |

Two honest options, per row:

1. **Mark it "needs eyes"**, leave it unscored, and list the ASINs to check.
2. **Open the pages and fill it in**, marking the row with the date it was
   checked by hand.

Do not infer A+ from the `description` field. It contains A+ text concatenated
with the description and brand story, so a long `description` means "this page
has a lot of words", not "this page has A+".

A hygiene report that silently omits A+ reads as "checked and clear". That is
the failure to avoid.

## E. Cost

One Oxylabs credit per ASIN for section C. A 60-ASIN catalogue is 60 credits.

If that is too many, run section C on the ASINs carrying the top 80% of revenue
and say the tail was not page-checked. Sections A and B cost nothing and cover
the whole catalogue.
