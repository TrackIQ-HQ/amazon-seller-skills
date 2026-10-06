# Method

## The grid

One column per product, ours first. One row per comparable attribute.

| Row | Ours | Comp A | Comp B | Comp C |
|---|---|---|---|---|
| Price | | | | |
| **Price per unit** | | | | |
| Coupon | | | | |
| Subscribe & save | | | | |
| Title length | | | | |
| Primary term in first 80 chars | | | | |
| Bullets (visible / total) | | | | |
| Mean bullet length | | | | |
| Images | | | | |
| Rating | | | | |
| **Reviews** | | | | |
| **One-star share** | | | | |
| BSR in category | | | | |
| Buy box holder | | | | |
| FBA | | | | |
| In stock | | | | |
| *A+ present* | *by eye* | | | |
| *Video present* | *by eye* | | | |

The bold rows carry the weight. The italic rows **cannot be measured by the
tools** — either look at the pages and mark the row with today's date, or delete
the rows entirely. Do not leave them blank; a blank row reads as "checked, found
nothing".

## Reading the grid

**Price per unit** is the comparison a shopper makes, whether or not they know
it. A product 40% more expensive per unit needs a reason visible on the page,
and if the page does not give one, that is the finding.

**Reviews is the moat.** It is the one row that cannot be fixed this quarter. If
we have 200 and they have 4,000, no amount of copy closes that, and the honest
strategy is to win a narrower intent rather than the head term. Say so — a
teardown that pretends a review gap is a copy problem wastes a quarter.

**One-star share** is the quality signal. Lower than a competitor's is a
positioning asset: the page should make the claim that earns it, without naming
anyone.

**Title first 80 characters** is where the phone truncates. A competitor whose
brand and primary term both land inside it and ours does not is a cheap,
immediate fix.

**Bullets visible against total.** More than five means some are invisible on
the detail page. Check both sides — a competitor wasting their sixth bullet is
worth knowing, and so is ours.

## Ranking the gaps

Not by size. By **effect divided by effort**:

| Tier | What qualifies | Timescale |
|---|---|---|
| **This week** | title order, bullet order, an invisible sixth bullet, a missing coupon | copy change, no new assets |
| **This month** | rewritten bullets, images to shoot, a price-per-unit story to tell, A+ modules | needs production |
| **This quarter** | review depth, pack size or price architecture, a new variation | needs a plan and a budget |
| **Accept** | a gap that cannot be closed and does not matter | say so explicitly |

**Three to five gaps total, across all tiers.** A teardown listing nineteen
differences gets none of them fixed. The discipline of choosing is the product.

The **Accept** row matters more than it looks. Naming the gaps you are choosing
not to close is what makes the rest of the list credible.

## What not to do with the findings

**Never name a competitor in proposed copy.** Comparative claims are a policy
risk on Amazon and the downside is a suppressed listing, not a stern email.

The gaps inform the copy. The copy states what our product is, in terms that
happen to be where they are weak. "Individually wrapped for travel" is fine;
"unlike Brand X, individually wrapped" is not.

## One caveat about rank

`bsr_primary` and `sales_rank_ladder` are **point in time**. Neither the scrape
nor the MCP carries rank history — `get_bsr` returns one `tracked_date`
regardless of the range requested.

So the grid shows where everyone ranks today. It cannot show who is climbing,
which is usually the more interesting question. Say the reading is a snapshot,
and if the client wants the trend, run this monthly and keep the files.

## What this skill does not do

- **No A+ or video detection.** Not in the data. By eye or not at all.
- **No rank history.**
- **No keyword-level comparison.** That is `trackiq-share-of-shelf` and the rank
  skills.
- **No copy.** It specifies the gap; `trackiq-listing-optimizer` writes the fix.
