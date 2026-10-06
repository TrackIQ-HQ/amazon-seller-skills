# Method

## 1. The curve, per month

For each month, with `b1..b9` the `total_brand_purchases` per bucket:

```
total          = b1 + ... + b9
within_hour    = (b1 + b2 + b3 + b4) / total
within_day     = (b1 + ... + b7) / total
within_week    = (b1 + ... + b8) / total
after_week     = b9 / total
```

Show the three months side by side. Report the direction of `after_week`
across them — a rising share means a lengthening consideration cycle.

## 2. The attribution window

| Share of purchases after 7 days | Reading |
|---|---|
| under 10% | A 7-day window sees nearly everything. Sponsored Products reports are close to complete. |
| 10–20% | A 7-day window understates ads by roughly that share. Read Sponsored Products next to a 14-day source. |
| over 20% | A long-consideration category. Judge upper-funnel spend on 14-day or AMC figures, never on a 7-day ROAS alone. |

State plainly: "N% of purchases land more than a week after the first ad —
a Sponsored Products report on its 7-day window cannot see them."

## 3. The event lead time

The share that buys within a day is impulse; the week bucket is
consideration. For a sales event:

```
lead_days = 7 if after_week >= 20% else (5 if after_week >= 10% or within_day < 60% else 2)
```

The middle band follows the attribution table above: once a tenth of
purchases land after a week, two days is too short a run-up.

Recommend starting upper-funnel (DSP, Sponsored Display, Sponsored Brands
video) `lead_days` before the event, and say it rests on the open-ended
"7+ DAYS" bucket. Sponsored Products bids can move on the day.

## 4. Volume by channel

From `group_by='campaign'`, sum `total_brand_purchases` by `campaign_type` for the focus
month and show each channel's share of attributed purchases. Context only —
it does not rank campaigns by speed.

## 5. The headline

"X% of shoppers buy within a day of their first ad, and Y% take more than a
week." Name the month.
