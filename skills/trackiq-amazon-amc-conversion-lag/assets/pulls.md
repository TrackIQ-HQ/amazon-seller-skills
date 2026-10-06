# The pull sequence

## 0. Account

`list_marketplaces` first. Never print `account_id`. **More than one TrackIQ
MCP can be connected at once, with identical tool names and different brands
behind them.** Call `list_marketplaces` on each and match on `name`.

## 1. The window

The three most recent **complete** calendar months. Add the same month a year
earlier if the next event is seasonal and AMC has it.

## 2. The pulls

| # | Call | Arguments | Gives you |
|---|---|---|---|
| 1–3 | `get_amc_time_to_conversion` | one call per month, `group_by='position'` | nine rows: purchases per time bucket |
| 4 | `get_amc_time_to_conversion` | focus month, `group_by='campaign'`, `limit=500` | purchases per campaign — volume only |
| 5 | `get_campaigns` | `ad_type='all'`, `state='all'`, focus month | Sponsored Ads spend by channel, for context |

## 3. The fields

`group_by='position'` rows carry `month_start`, `month_end`, `position`
(1–9), `time_to_conversion`, `purchases`, `total_brand_purchases`, and
`ntb_total_brand_purchases`, `total_product_sales`, `ntb_total_product_sales`,
`total_units_sold`, `ntb_total_units_sold`.

The nine buckets, in `position` order:

| position | bucket |
|---|---|
| 1 | < 1 MIN |
| 2 | 1 - 10 MIN |
| 3 | 10 - 30 MIN |
| 4 | 30 - 60 MIN |
| 5 | 1 - 2 HRS |
| 6 | 2 - 12 HRS |
| 7 | 12 - 24 HRS |
| 8 | 1 - 7 DAYS |
| 9 | 7+ DAYS |

## 4. How the data misleads

1. **Only the purchase counts are real.** `total_product_sales`, units and
   every `ntb_` column come back as zero. They are not "no sales"; the tool
   does not populate them. Leave them out.
2. **`purchases` versus `total_brand_purchases`.** `purchases` counts the
   advertised product; `total_brand_purchases` counts anything from the
   brand. Use `total_brand_purchases` for the lag curve — a shopper who saw an
   ad for one product and bought another still converted on the ad — and say
   which you used.
3. **Numbers arrive as strings.** Cast before arithmetic.
4. **`group_by='campaign'` has no timing.** One row per campaign with its
   purchase count. It cannot say which campaign converts faster.
5. **One row per month per bucket.** Never add months together.
