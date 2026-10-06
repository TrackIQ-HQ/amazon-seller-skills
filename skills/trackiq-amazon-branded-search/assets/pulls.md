# The pull sequence

## 0. Account and terms

`list_marketplaces` first. Never print `account_id`. If more than one
TrackIQ MCP is connected, call it on each and match on `name`.

Read the Brand terms block from account.md. If it is empty, ask for the brand
name, common misspellings and product-line names before pulling anything.

Window: a trailing 30 days.

## 1. The pulls

| # | Call | Arguments | Gives you |
|---|---|---|---|
| 1 | `get_search_terms` | `ad_type='sp'`, `sort='spend DESC'` | customer query, spend, sales, orders — SP, 7-day window |
| 2 | `get_search_terms` | `ad_type='sb'`, `sort='spend DESC'` | the same for SB, 14-day window |
| 3 | `get_targets` | `record_type='KEYWORD'`, `ad_type='all'`, `state='enabled'` | the keywords the account bids on, to spot brand keywords with no search volume |
| 4 | `get_search_query_performance` | `query_contains` = each brand term, one call per week of the window | the brand's purchase share on its own name |
| 5 | `get_product_performance` | same window | the brand's own ASINs, to recognise its own product pages among product-targeting queries |

## 2. Why SP and SB are separate pulls

`ad_type='all'` returns one ranking with each row tagged by channel — and
one ROAS blending a 7-day and a 14-day attribution window. Summing across
the two inflates SB against SP. Keep two tables, one per channel, and a
spend-only combined view where windows do not matter.

## 3. Paginate — the limit is binding

Search terms are a long tail, and the tail is almost all generic. Page with
`offset` and keep a running spend total. Stop when a call returns fewer rows
than the limit, **or** when the pulled spend reaches 97% of the channel's
spend in `get_campaigns` for the same window — on a large account the last
3% can be thousands of queries under $3 each. Report the share of channel
spend covered. Stopping early makes brand look like a bigger share of spend
than it is.

Do not trust `next_cursor` to end the loop: it can come back `null` on a
page that returned exactly `limit` rows.

## 4. What the search-term report will not tell you

`get_search_terms` returns the query and its metrics — no campaign, ad group
or match type. The split is by what the shopper typed, which is the right
question here. It cannot say which keyword caught the query.

## 5. Search Query Performance

`get_search_query_performance` covers organic and paid together — it is
not an organic figure. The field is `pur_brand_share`: the share of all
purchases on that search that went to the brand.

It is weekly and pins to the **latest week** overlapping the dates you pass,
so one call per week (Sunday to Saturday) is the only way to cover a month.
Show the weeks side by side; never average shares across them.

Brand searches are small. A week with fewer than **20** `market_purchases`
on a query is too thin to read — "100%" on nine purchases says little. Mark
it thin rather than quoting the share. If a query has no SQP row at all, say
so rather than estimating it.
