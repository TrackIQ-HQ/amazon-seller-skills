# Method

## Revenue at risk, per defect

A hygiene report's whole problem is that everything on it is true and almost
none of it is urgent. Revenue at risk is what makes the list finite.

```
asin_revenue = revenue over the last 90 days, rolled up to ASIN
at_risk      = asin_revenue x severity
```

| Severity | Defects | Reasoning |
|---|---|---|
| **1.00** | not buyable, buy box lost | the revenue is stopping now |
| **0.30** | traffic with no conversion, rating under 4.0, high one-star | a real and measurable drag |
| **0.15** | thin images, bullets under five, short title | known conversion effects, not catastrophic |
| **0.05** | bullets over five, long bullets, long title | tidy, small effect |
| **0.00** | GUID ASINs, FBM shadows, parents, dead listings | clutter, not revenue |

The severities are **judgement, not measurement.** Say so. They exist to order
the list, and a client who wants to argue about whether thin images cost 15% is
having a more useful conversation than one staring at 140 undifferentiated rows.

**A defect on a zero-revenue product scores zero** and drops to the low-priority
section. It is still worth fixing one rainy afternoon; it is not worth a line in
the main list.

## Cutting the list to size

```
main list        = top 10 defects by revenue at risk
urgent           = anything at severity 1.00, regardless of revenue
low priority     = everything else, counted but not listed individually
```

**State the total found.** "38 defects found across 61 ASINs; the 10 with
revenue exposure are below" is honest and gives the reader the choice. A report
that shows all 38 gets skimmed and none get fixed.

Anything not buyable goes at the top whatever its revenue — a listing that is
dark is losing 100% of something.

## The inventory clutter number

Report it as a headline, before the individual rows:

```
snapshot rows        146
  real, sellable      76
  variation parents   21
  FBM shadows         28
  GUID / broken ASINs  9
  dead listings       12
```

Those numbers are from the account this family was built against. **Roughly
half the catalogue was not products.** That is a finding on its own, it explains
why every other report on the account needed filtering, and nobody had ever
counted it.

Where rows fall into more than one category, count each row once and say which
rule claimed it.

## Grouping by cause, not by ASIN

Twelve ASINs with five images each is **one** finding — "12 products have thin
image sets" — with the ASINs listed underneath and their revenue totalled. Not
twelve findings.

Grouping by cause is what turns the report into a work order. Somebody can brief
a photographer once.

## The "needs eyes" section

A+ content, video, backend terms and variation completeness cannot be measured
(see `assets/checklist.md`). They get their own section, with:

- what the check is
- why no tool can do it
- the list of ASINs to check, ordered by revenue
- space to record what was found and the date

**This section is not scored and does not appear in the totals.** If it is
filled in by hand, the date goes beside it.

## Sequencing the fix

| Order | What | Why first |
|---|---|---|
| 1 | Not buyable, buy box lost | revenue stopping now |
| 2 | Inventory clutter | it makes every other report wrong |
| 3 | Thin images and bullets on high-revenue ASINs | known conversion effect, one briefing |
| 4 | Titles | cheap, and easy to batch |
| 5 | The long tail | a rainy afternoon |

Inventory clutter sits second not because it earns money but because every other
skill in the catalogue silently filters around it. Cleaning it once makes
everything downstream more trustworthy.

## What this skill does not do

- **No A+, video, backend terms or variation family.** Not in the tools.
- **No listing changes.** It produces a work list.
- **No change detection.** That is `trackiq-listing-monitor`; this is the
  one-off sweep you run before installing it.
- **No copy.** It says the bullets are thin; `trackiq-listing-optimizer` writes
  them.
