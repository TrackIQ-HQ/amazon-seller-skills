# Method

## What to rank on when there is no revenue

DSP is bought to recruit customers, not to close them the same day. So the
ranking is a funnel, and every step of it is available:

```
cost_per_ntb  = spend / ntb_purchases          # the headline
cost_per_dpv  = spend / dpv                    # cost of consideration
cost_per_atc  = spend / atc                    # cost of intent
dpv_rate      = dpv / clicks                   # did the click go anywhere
atc_rate      = atc / dpv                      # did the page do its job
ntb_rate      = ntb_purchases / atc            # did the cart close
ntb_share     = ntb_purchases / orders         # how new is this audience
```

**Cost per new-to-brand purchase is the headline.** It is the number DSP is
actually accountable for, and unlike ROAS it is computable from what the feed
returns.

`ntb_share` is the quiet one worth reading. A segment delivering orders that are
mostly *not* new-to-brand is re-buying existing customers — that can be fine for
a retargeting line and is a waste in a prospecting one. Judge it against what
the segment is supposed to be doing.

## Reading down the funnel

The value of the funnel is that it localises the failure:

| Pattern | What broke |
|---|---|
| Low CTR | the creative or the placement, not the audience |
| CTR fine, low `dpv_rate` | clicks are not landing — check the destination |
| `dpv_rate` fine, low `atc_rate` | the detail page, not the media |
| `atc_rate` fine, low `ntb_rate` | price, reviews or checkout — not the media |

Say which step failed rather than calling a segment "bad". A segment that
delivers great DPV and no add-to-carts is a listing problem wearing an audience
costume, and pausing it fixes nothing.

## Comparing within a dimension only

An audience row and a creative row are not comparable. Each dimension gets its
own section, its own ranking and its own median.

Use the **median of the dimension** as the comparison point, not the mean.
Segment distributions are long-tailed and one huge segment drags a mean until
every other row looks good.

```
flag_expensive = cost_per_ntb > 2 x median(cost_per_ntb of this dimension)
flag_efficient = cost_per_ntb < 0.5 x median(...)
```

## The overlap rule

Segments overlap (see `assets/pulls.md`), so:

- **No sums.** Not spend, not impressions, not NTB purchases.
- **No shares of total.** There is no honest denominator.
- **No "this audience drove X% of DSP".** It cannot be known from this feed.
- Rate metrics per row are valid and are the whole basis of the report.

Group segments whose impressions are within 5% **and** whose CTR matches to
three decimals — that is the overlap signature — and treat the group as one
finding.

## Minimum volume

A segment with 200 impressions and one NTB purchase has a cost per NTB that
means nothing. Require, per row:

```
impressions >= 50,000   and   clicks >= 100
```

Below that, list the row in the full table and keep it out of the ranked
findings. State how many rows were held back for volume.

## What to recommend

Three lists, each short:

**Scale.** Efficient cost per NTB, healthy funnel, not volume-capped. Name the
segment and what it is spending now.

**Fix.** The funnel failed at a step that is not the media — a landing or a
listing problem. The recommendation is not a budget change.

**Cut.** Expensive against the dimension median, funnel weak throughout, enough
volume to be sure. Never recommend cutting a segment that is part of an overlap
group without saying that its impressions are shared.

## What this skill does not do

- **No revenue, ROAS or ACOS.** The feed does not carry it at these dimensions
  and inventing it from an account-level ratio would be a fabrication.
- **No totals or shares.** The segments overlap.
- **No budget changes.** Recommendations are applied by a human in the DSP
  console.
- **No cross-dimension attribution.** This data cannot say which creative ran
  against which audience.
