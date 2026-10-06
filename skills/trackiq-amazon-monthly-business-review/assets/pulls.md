# The pull sequence

## 0. Account and the three windows

`list_marketplaces` first — several TrackIQ MCPs can be connected with
identical tool names. Never print `account_id`.

Three windows, always:

| Window | Range |
|---|---|
| **This month** | the month just ended, whole |
| **Last month** | the calendar month before it |
| **Last year** | the same calendar month, previous year |

Whole calendar months. A "month to date" MBR compares 30 days to 31 and the
difference gets read as performance.

## 1. The daily curve, three times

```
get_account_overview(account_id, start_date, end_date)    # once per window
```

Daily rows: `total_revenue`, `attributed_sales`, `organic_sales`,
`total_spend`, and the split by ad type — `sp_`, `sb_`, `sbv_`, `sd_`.

This is the backbone of slides 2, 3 and 4.

## 2. The year-on-year trap — test before you draw it

On the account this was built against, September the previous year returned:

```
total_revenue    22,681.10      real
attributed_sales      0.00      not real
total_spend           0.00      not real
```

Revenue is there. **Every advertising field is exactly zero.** That is not a
year in which the brand did no advertising — it is ad history that predates the
account's connection to the platform.

A year-on-year deck built without checking would report:

- spend up from $0 — infinite growth
- organic share down from 100% to 62% — a collapse that never happened
- ACOS appearing from nowhere

All three are fabrications, and all three are the kind a client repeats in a
board meeting.

**The test, before any year-on-year ad figure is drawn:**

```
prior_year_spend = sum(total_spend over the prior-year window)
if prior_year_spend == 0:
    compare revenue only
    state on the slide that advertising data for that period is not available
```

Revenue year-on-year is still worth showing and is still true. Say which
comparison is present and which is not, on the slide, not in a note.

Apply the same test to `attributed_sales`. Organic share is only meaningful when
both halves are real.

## 3. Products

```
get_product_performance(account_id, start_date, end_date,
                        group_by='product', limit=200)   # once per window
```

`revenue`, `units`, `sessions`, `orders`, `conversion_rate` per SKU.

**Roll up to ASIN** — rows arrive per SKU and the same ASIN appears several
times (FBM shadows, multipacks). Derive price as `revenue / units`; there is no
price field. There is no buy-box field at all.

`granularity="daily"` is silently ignored by this tool, so the month is one
aggregate per window, not a series.

## 4. Categories — two taxonomies in one response

```
get_product_categories_performance(account_id, start_date, end_date, limit=100)
```

The response mixes **two overlapping category systems**:

| category_id | title | spend |
|---|---|---|
| 14 | Grill Accessories | 52,209.92 |
| 54 | (tiq) Waterproof Grill Cover XL | 52,209.92 |

Identical figures, same campaigns, counted twice. The `(tiq)` prefix marks the
TrackIQ-side tags; the unprefixed rows are the Pacvue-native categories.

**Pick one.** Filter on the prefix, state which system the slide uses, and never
sum across both. A category mix slide built from everything will come to roughly
double the month's real spend, and it will not tie to slide 2.

## 5. Advertising detail

```
get_campaigns(account_id, start_date, end_date, limit=200)     # granularity total
get_portfolios(account_id, start_date, end_date, limit=100)
```

Campaign and portfolio totals for the month. Note that
`get_campaigns(granularity="daily")` drops the campaign dimension entirely and
returns an account-level curve — use `get_account_overview` for the curve and
these for attribution.

`get_portfolios` returns `in_budget` (0/1), the only budget-related signal in
the product. It is a flag, not an amount.

## 6. Optional, where the story needs it

- `get_inventory_snapshot` — for the risks slide. Cover must be computed per
  ASIN, never per SKU; see `trackiq-restock-priority`.
- `get_amc_attribution_paths` — if the client has AMC and the deck needs the
  channel story. That is the AMC media mix skill's territory; link to it rather
  than rebuilding it here.
- `get_search_query_performance` — weekly, Sunday to Saturday, and ingestion is
  intermittent. Missing weeks in a month are normal; do not present a partial
  month of SQP as the month.
