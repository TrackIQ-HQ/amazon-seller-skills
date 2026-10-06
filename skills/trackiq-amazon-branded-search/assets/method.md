# Method

## 1. Normalise

Lowercase the query, collapse whitespace, strip punctuation except hyphens.
Normalise the brand and competitor terms the same way. Then **sum rows that
normalise to the same query** — the report returns near-duplicates
("demo outdoor 48ft" and "demo outdoor  48ft") as separate rows.

## 2. Classify, in this order

1. **Own product pages** — the query matches `^b0[a-z0-9]{8}$` and is one
   of the brand's own ASINs (pull 5). This is brand defence on the brand's
   detail pages and belongs with branded spend: report it as its own line
   inside the branded bucket. It is often larger than the spend on branded
   keywords.
2. **Product targeting** — any other ASIN query.
3. **Branded** — the query contains any brand term or misspelling as a whole
   word or whole phrase. Product-line names count as branded.
4. **Competitor** — the query contains any competitor brand term.
5. **Generic** — everything else.

A query containing both a brand and a competitor term is **branded** — the
shopper named the brand.

Whole-word matching matters. A brand called "Glow" must not claim
"glow in the dark stickers"; check the ten largest branded queries by eye
and add exclusions to account.md when it misfires. The same goes for
competitor names that are also plain descriptions ("Pure", "True", "Raw"):
match them only as the full brand phrase, or they pull generic searches into
the competitor bucket.

## 3. Per bucket, per channel

Spend, sales, orders, ROAS, ACOS, share of channel spend, share of channel
sales. Then a combined **spend-only** view across SP and SB.

- **Generic ROAS** is the headline.
- **Blended ROAS** is shown beside it, labelled, for reference.
- **The brand lift**: blended ROAS minus generic ROAS. This is how much brand
  search is flattering the account average.

## 4. Is the brand spend defence?

For the ten branded queries with the most spend, read the brand's purchase
share (`pur_brand_share`) from Search Query Performance, week by week. It
counts organic and paid purchases together, so it measures how much of the
search the brand already wins, not how much it would win without ads. Skip
weeks marked thin.

| Purchase share on its own name | Reading |
|---|---|
| 80% or more, no competitor in the branded queries | Mostly harvesting. Recommend a two-week test at reduced bids on exact brand terms, measuring total brand sales, not ad sales. |
| 50–80% | Mixed. Keep it and watch. |
| Under 50%, or a competitor appears in the branded queries | Defence. Keep it. |

Never recommend a cut. Recommend a test with a stated success measure.

## 5. Competitor conquesting

Competitor-bucket ROAS against generic ROAS. Conquesting usually converts
worse; the question is whether it recruits new customers. If
`trackiq-amazon-amc-ntb-campaigns` has been run, cite the new-to-brand share
of the conquest campaigns. Otherwise say it is unknown.

## 6. Brand keywords with no search volume

From `get_targets`: enabled keywords that contain a brand term but match no
query in the window. Usually harmless, sometimes a sign the brand name is
spelled a way shoppers do not use.
