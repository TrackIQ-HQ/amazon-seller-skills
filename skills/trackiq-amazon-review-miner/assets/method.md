# Method

## Two layers, kept apart

| Layer | Source | What it can say |
|---|---|---|
| **Quantitative** | `rating_stars_distribution`, `reviews_count`, `rating` | proportions, comparisons, trends |
| **Qualitative** | the ~8 review bodies per ASIN | themes, language, objections |

**Every number comes from the first layer. Every theme comes from the second.**
Mixing them — computing a percentage from eight bodies — is the one failure that
makes this report worthless, and it is easy to do by accident.

## The quantitative spine

Per ASIN, own and competitor:

```
rating, reviews_count
five_star_pct .. one_star_pct        from rating_stars_distribution
negative_pct = one_star_pct + two_star_pct
```

Brand level, weighted by review count:

```
brand_rating = sum(rating x reviews_count) / sum(reviews_count)
```

Weight by review count, not a plain mean — a 5.0 on eleven reviews should not
move the brand average the way a 4.3 on nine thousand does.

Against competitors, the comparison that matters is **negative_pct**, not the
star rating. A 4.6 and a 4.4 are indistinguishable to a shopper; 3% one-star
against 9% one-star is a real difference in how often this product disappoints.

## Building themes

Read every body. For each, extract the **claims**, not the sentences:

- what it is used for ("sore throat", "GERD", "travel")
- what is praised ("taste", "works fast", "natural")
- what is complained about ("sticks to teeth", "price", "packaging")
- who the buyer is ("teacher", "singer", "caught a cold from a grandchild")

Cluster into themes of roughly five to twelve. Fewer and they are too broad to
act on; more and they are individual reviews with labels.

**Every theme carries its count and its denominator:**

```
"Sticks to teeth — 7 of 184 reviews read (4%)"
```

The denominator is the number of **bodies read**, not the number of reviews the
products have. Say which it is. A reader who thinks 4% of 2,816 reviews said
this will act very differently from one who knows it was 7 of 184.

## The four-way split

Praise and complaint, own and competitor. The four quadrants say different
things:

| | **Own** | **Competitor** |
|---|---|---|
| **Praise** | what the copy should lead with | what you must match or dismiss |
| **Complaint** | the objection to pre-empt | **the positioning asset** |

The bottom-right is the one people miss. A complaint competitors get repeatedly
and you do not is the sentence your listing should be making — not by naming
them, but by stating the thing you do that they do not.

## Does the page already answer it?

For each complaint theme, check the current `bullet_points` and `description`:

- **Answered and still complained about** → a communication failure. The copy
  says it but not where anyone reads it. Move it up, say it plainer.
- **Not answered** → a gap. Write it into the bullets.
- **Unanswerable** → a genuine product limitation. Set the expectation honestly
  rather than hiding it; a pre-empted objection produces fewer one-star reviews
  than a surprise.

This distinction is what makes the output a direction rather than a list.

## New themes — the early warning

Where a previous run's file exists:

```
new_themes     = themes now - themes then
grown_themes   = themes whose share of bodies read rose by more than half
```

A new complaint theme appearing across several ASINs is the earliest quality
signal available anywhere in this toolkit — earlier than the star rating, which
moves slowly under the weight of history.

**Flag it as worth investigating. Do not diagnose it.** "Six mentions of
packaging damage across three ASINs, none in the previous run" is a finding.
"The new carton is failing" is a conclusion this data cannot support.

Without a previous run, say the comparison starts next run.

## Copy directions

Three outputs, each traced to a theme:

**Bullet directions.** Which of the five bullets should carry which theme, and
what it should say. Paraphrased — **never a reviewer's words lifted into copy.**

**A+ directions.** Themes that need a picture rather than a sentence — usage,
scale, comparison, what is in the box.

**Negative keywords.** Where a complaint theme matches a search term the brand
is buying, shoppers are arriving with an intent the product does not satisfy.
That is a bulk-file row, not a copy change — hand it to
`trackiq-wasted-spend`'s format.

## What may and may not be claimed

| Allowed | Not allowed |
|---|---|
| "7 of 184 reviews read mentioned X" | "4% of customers say X" |
| "the most common complaint in the sample" | "the most common complaint" |
| "worth investigating" | "there is a quality problem" |
| "competitors are criticised for Y more often in this sample" | "competitors have worse Y" |
| paraphrased themes | verbatim review quotes in copy |

The left column is defensible. The right column will be repeated to a
manufacturer and will not survive the first question.

## What this skill does not do

- **No full review corpus.** ~8 bodies per ASIN; the rest is tier-gated.
- **No sentiment score.** A number derived from eight skewed bodies would look
  precise and mean nothing.
- **No quality diagnosis.** Patterns, not causes.
- **No reviewer identification.** No names, no review IDs, anywhere.
