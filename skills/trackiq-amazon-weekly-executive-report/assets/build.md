# Producing one send

## 1. Confirm the account and the week

Get the account, marketplace, product-line breakdown (how retail rolls up
into lines — usually by ASIN), and the recipient(s) before pulling
anything. A report about the right numbers on the wrong account is the
single worst outcome this skill can produce, and the one a client always
notices.

The reported week is the just-completed Sunday-to-Saturday week (or
whatever anchor the account uses — ask if unstated). Compare it against
the week immediately before.

## 2. Pull BOTH weeks on the same day

Attribution matures for several days after a week closes. A prior week
pulled last Monday and a current week pulled today are not comparable —
pull both today so the comparison is like-for-like, even though the
absolute level of each is still provisional. Say so in the pacing section
("both weeks were pulled today; next week's send will restate this week
upward").

If a prior-week figure the client already saw has since restated, that is
a fact worth stating once in passing, not something to smooth over.

## 3. Roll retail up from the per-line pull, not a category endpoint

Line/category retail belongs in the report from whatever endpoint returns
total retail per product or per SKU, rolled up by the account's own
line-to-ASIN mapping — never from an ad-only or category-spend endpoint,
which returns ad spend and ad sales but not total retail. Mixing the two
is the fastest way to produce a scorecard that does not tie.

If a product's fulfillment rows duplicate (the same ASIN appearing twice
with different SKUs, or a "_FBM" suffix), sum across the duplicate rows
per ASIN — never take the first match, and never leave the duplicate in
as a second row.

## 4. Headline convention: pick one and state it once

Decide up front whether the headline KPI is sponsored-only or all-in
(sponsored + DSP), and hold that convention through every number derived
from it — ACoS, ROAS, TACoS, the scorecard, the cover strip. If DSP is
material to the account, all-in is almost always the right headline,
because a sponsored-only number next to a channel table that already
includes DSP will visibly contradict itself two sections later. State the
convention once, in the channel-panel caption, and never re-derive a
different blend for a different section.

If the headline is all-in, do not also print a "full-funnel" row computed
as headline-plus-DSP — that silently double-counts DSP. Compute the
channel-level sponsored total plus DSP total and confirm it equals the
headline before publishing; if it does not, the headline is not actually
all-in and the report is inconsistent.

## 5. Marginal return: only where spend actually moved

```
marginal return = Δ retail ÷ Δ ad spend
```

Only meaningful for a line whose spend increased week over week — a line
that cut spend and grew retail is a win, but it has no position on this
axis by definition; cover it in the line panel, not the chart. And a
marginal-return figure built on a small dollar change ($50-100 of spend
delta) produces a wild ratio that says nothing about elasticity — flag it
as noise in the same sentence rather than treating the number as a
finding. See `voice.md`.

## 6. Pacing against the trailing average, not a target

```
baseline = sum(retail, trailing 4 weeks ending the PRIOR week's end) ÷ 4
vs. baseline % = this week's retail ÷ baseline − 1
```

Pull the trailing sum fresh in the same pull as the two reported weeks,
not from old saved figures, for the same attribution-maturity reason as
step 2. This is a pace-against-your-own-history number, not a
target-vs-actual number — never imply the client set this baseline as a
goal unless line-level goals are actually configured.

## 7. Amazon DSP is a separate channel

Never fold DSP spend or sales into the sponsored subtotal, and never
allocate DSP spend across product lines unless the account can actually
attribute DSP campaigns to a specific line by name — most cannot, and a
forced allocation invents a number. Report DSP as its own block, bucketed
however the account's own campaign naming or grouping actually buckets it
(by objective, by format, by funnel stage) — do not invent a taxonomy the
account does not use.

A channel that can carry sales after its spend drops to zero (a campaign
that ended mid-window but still has attributed sales in its window) is
real and should be included, not treated as an error.

## 8. Inventory: read days of cover, not raw units

```
days of cover = on-hand units ÷ (units sold this week ÷ 7)
```

Rising on-hand units do not mean the risk is over if velocity rose faster
— compute cover every time, never eyeball on-hand alone. Use the
account's own configured critical/tight/healthy thresholds; if none are
configured, ask rather than inventing a cutoff. A listing whose cover
*fell* even though its stock grew is a real, useful finding — say so
explicitly rather than only reporting the stock increase.

## 9. Search-query and other lagging data: label the week it covers

Search-query and similar weekly-ingested feeds usually lag the reported
week by one to three weeks. State the actual week the data covers, every
time it appears, in the section itself — never let it read as if it
covers the reported week just because it sits next to sections that do.

## 10. Keyword economics

Classify a term as "brand" only when it names the brand itself — a
category term the account happens to dominate is not brand, and lumping
it in overstates brand share by an order of magnitude. Split by brand vs.
non-brand and by match type; surface a short list of terms converting
well on trivial spend (the "under-funded winners") rather than a full
keyword table, which nobody reads end to end.

## 11. Placement/bid efficiency, if available

Group by placement type (automatic discovery, product, category, audience)
rather than implying keyword-level specificity the underlying data does
not carry — some ad types return no target text for automatic or category
targeting, and naming a placement more precisely than the data supports is
worse than grouping it plainly.

## 12. Tie-outs before anything ships

Before finishing, confirm:
- Summed line retail (+ any unattributed remainder) equals account retail
- Summed line ad spend equals the sponsored total
- Summed DSP-bucket spend equals the DSP total
- The cover strip's ad-spend figure equals the channel table's all-in total
- Every number quoted in prose matches a cell in a table somewhere in the
  same report

If a tie-out fails, the fix is always in the pull or the rollup — never
edit a total to make it match a detail, or a detail to make it match a
total. Reconcile the inputs.

## 13. De-duplicate

Read the finished report top to bottom and delete any number stated
twice. Adding a chart usually orphans a line panel; adding an inventory
row usually orphans a bullet elsewhere. This is the most common defect in
long-form reports like this one.

## 14. Ship checks

- No platform named but TrackIQ and Amazon
- Every aggregate agrees with the detail printed beneath it
- Every chart bar proportional; label columns clear of the bars
- Headline convention (sponsored-only vs. all-in) is stated once and held
  throughout
- No text under 12px except uppercase eyebrows
- No footer content beyond the brand bug and the account/week line
- Under 100KB; logos absolute `https://`
