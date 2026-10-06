# The deck

Eleven slides. If a slide cannot earn its place from the data, cut it rather
than filling it.

| # | Slide | What it has to earn |
|---|---|---|
| 1 | Cover | client, month, the one-line verdict |
| 2 | The month in four numbers | revenue, spend, ACOS, units — against last month and last year |
| 3 | Revenue shape | the daily curve, this month against last |
| 4 | Paid and organic | the split, and whether the organic base is growing |
| 5 | Category mix | where the money came from — **one taxonomy only** |
| 6 | Products | top movers up and down, with the cause named |
| 7 | Advertising | portfolios, efficiency, what changed |
| 8 | What worked | two or three things, each with its number |
| 9 | What did not | the same, honestly |
| 10 | Risks | stock cover, listing changes, rank exposure |
| 11 | Next month | three items, each with an owner and a metric |

## Slide 1 — the verdict

One sentence that a reader could repeat from memory. "Revenue up 9% on a flat
ad budget, carried by grill accessories" is a verdict. "A month of mixed performance
with several notable developments" is filler, and it tells the client you did
not look.

If the month was bad, say it was bad on slide 1. A deck that buries the bad
month on slide 9 does not survive contact with a finance director.

## Slide 2 — the four numbers

Revenue, spend, ACOS, units. Each with month-on-month and year-on-year.

**Year-on-year advertising figures only appear if the prior-year data is real.**
See the test in `assets/pulls.md`. Where it is not, the cell says "not
available" and the slide carries one line explaining that ad history for that
period predates the platform connection. It does not show a dash and hope
nobody asks.

## Slide 4 — paid and organic

`organic_sales / total_revenue`, this month against last.

This is the most important slide in the deck for a brand that is trying to stop
buying its own customers, and the one most often left out. A rising organic
share on flat revenue is a better month than rising revenue on a rising ad
budget, and the deck should say so.

Do not draw the year-on-year version of this slide when the prior year shows
100% organic — that is the missing-data artefact, not a result.

## Slide 5 — category mix

**One taxonomy.** The response carries both Pacvue-native categories and
TrackIQ `(tiq)` tags with identical figures; using both doubles the month.

State on the slide which system is shown. If the client thinks in the `(tiq)`
tags because that is what they see in the platform, use those.

The categories must sum to the month's spend on slide 2. Print the sum.

## Slide 6 — products

Top five up and top five down by **dollars moved**, not percent. Each with its
cause from the four-factor decomposition — traffic, conversion, basket, price.
`trackiq-sales-movers` produces exactly this; use its output rather than
recomputing.

Never name buy box as a cause. It is not in the data.

## Slides 8 and 9 — what worked, what did not

Two or three items each, every one with the number that proves it. An item
without a number is an opinion and belongs in the email, not the deck.

Slide 9 is the one that earns the retention. A client who only ever sees slide 8
stops believing slide 8.

## Slide 11 — next month

Three items. Each with:

- what will be done
- who does it — agency or client, named
- the metric it moves, and by when

Three items with owners beat nine without. If there are genuinely more than
three priorities, the month had no priorities.

## Voice

Editorial, not corporate. Short sentences. The reader is a brand manager who has
eleven minutes and will forward this to someone more senior.

- No "leveraged", no "synergies", no "double-clicking".
- Numbers in the sentence, not in a bracket after it.
- No footnotes. If it matters, it goes in the body.
- Never say "significant" without the figure.
