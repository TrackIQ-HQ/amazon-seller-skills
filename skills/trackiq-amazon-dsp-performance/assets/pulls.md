# The pull sequence

## 0. Account

`list_marketplaces` first — several TrackIQ MCPs can be connected with
identical tool names. Never print `account_id`.

## 1. One call per dimension

```
get_dsp_performance(account_id, start_date, end_date, dimension=<d>, limit=100)
```

**`dimension` is required.** Calling without it returns a validation error, not
a default. The values to try:

| dimension | What the rows are |
|---|---|
| `audience` | in-market, lifestyle, demographic and lookalike segments |
| `creative` | the ad units |
| `inventory` | supply sources — Amazon-owned, third-party exchanges |
| `technology` | device and environment |
| `geography` | location |

Not every dimension is populated on every account. Call each one; if it returns
no rows, say that dimension was empty rather than omitting it silently.

Use a **30-day window** as the default. DSP delivers at scale, so a month is
plenty, and shorter windows make the overlap problem below worse.

## 2. The fields

```
target, segment, impressions, clicks, spend, sales, orders, units,
dpv, atc, ntb_purchases, acos, roas, cpc, ctr, cvr
```

- `dpv` — detail page views
- `atc` — add to cart
- `ntb_purchases` — new-to-brand purchases, the metric DSP is bought for
- `target` — often `"untargeted"`; not a useful column on its own

## 3. Trap one: there is no revenue here

**`sales` is 0.0 and `units` is "0" on every row.** Consequently `roas` is 0.0
and `acos` is null.

This is not an account that made no money. It is revenue that is not attributed
down to the segment level in this feed. The distinction matters because a report
showing "ROAS 0.00" beside every audience reads as a catastrophe and is simply
wrong.

**Do not put a revenue, ROAS or ACOS column on the page.** Rank and compare on
the fields that are real: `ntb_purchases`, `orders`, `dpv`, `atc`, `spend`,
`impressions`, `clicks`.

If the client wants the revenue view of DSP, that is `trackiq-amc-media-mix`,
which works at the path and channel level where conversion value does exist.

## 4. Trap two: the segments overlap, so nothing sums

On the account this was built against, the audience dimension returned:

| Segment | Impressions | CTR |
|---|---|---|
| Demo – Amazon Reach Segment | 5,366,013 | 0.8540 |
| LS – Seller Central Lookalikes | 5,365,760 | 0.8540 |
| LS – (seasonal lookalike) | 5,290,621 | 0.8540 |
| IM – Health & Household | 5,232,314 | 0.8549 |

Four segments, near-identical volumes, an identical click-through rate. That is
**one pool of impressions attributed to several overlapping segments**, not four
independent audiences. A user can sit in three of these at once.

Consequences:

- **Never add segment spend together.** The sum on that account came to several
  times the real DSP spend.
- **Never present a segment's share of total**, because there is no honest
  denominator.
- There is no total row available to sanity-check against, because `dimension`
  is mandatory — you cannot ask for the ungrouped figure.
- **Do compare segments to each other** on rate metrics: cost per NTB purchase,
  DPV rate, ATC rate. Those are valid per row and are what the report is for.

Say this on the report. A client who adds the column up themselves and gets a
number three times their invoice will lose faith in everything else on the page.

## 5. Spotting the near-duplicates

Flag any group of segments whose impressions are within 5% of each other **and**
whose CTR matches to three decimal places. That is the overlap signature. Group
them visually and label the group rather than listing them as separate findings
— four rows saying the same thing is not four insights.
