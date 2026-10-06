# Before you send it

## 1. No proportion came from the bodies

**The check that matters.** Every percentage, share and comparison on the page
traces to `rating_stars_distribution` or `reviews_count` — never to the ~8
bodies.

Read each number and ask: could this have been computed from eight reviews? If
yes, it is wrong.

## 2. The ceiling is stated up front

- The report says near the top that about **eight review bodies per product**
  are retrievable, and that they skew positive.
- The total number of bodies read is stated.
- The number of ASINs sampled, and their share of revenue, are stated.
- Seller Central export is named as the route to a full corpus.

## 3. Every theme carries its count and denominator

- Format: "N of M reviews read", with M being **bodies read**, not total reviews
  on the products.
- No theme says "frequently", "many customers" or "customers report" without the
  count beside it.
- Between five and twelve themes. Fewer is too broad; more is reviews with
  labels.

## 4. The four-way split exists

- Praise and complaint separated.
- Own and competitor separated.
- The **competitor-complaint** quadrant is populated — it is the positioning
  asset and it is the one most often left empty.

## 5. Page-answers check

- Each complaint theme is classified: answered and still complained about / not
  answered / unanswerable.
- The classification was made against the **actual current bullets**, pulled in
  this run.

## 6. New themes

- If a previous run's file was supplied, new and grown themes are flagged, with
  its date.
- If not, the report says the comparison **starts next run** — it does not show
  a zero.
- New themes are described as **worth investigating**, never diagnosed.

## 7. Language discipline

- No verbatim review quote appears in any proposed copy.
- No reviewer names anywhere. No review IDs anywhere.
- No sentiment score.
- No claim about product quality, manufacturing or a supplier.
- Competitor comparisons are hedged to the sample: "more often in this sample",
  not "worse".

## 8. The outputs are traceable

- Every bullet direction names the theme behind it.
- Every A+ direction names the theme behind it.
- Every negative keyword names the complaint theme **and** the search term it
  matched.

## 9. Render check

```js
({ overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
   themes: document.querySelectorAll('[data-theme]').length,
   counted: document.querySelectorAll('[data-theme][data-count]').length,
   logos: [...document.images].map(i => i.naturalWidth > 0),
   tokens: (document.body.innerHTML.match(/\{\{[A-Z0-9_]+\}\}/g) || []).length,
   // must be zero: no reviewer names or IDs may survive into the output
   pii: (document.body.innerText.match(/\bR[A-Z0-9]{12,}\b/g) || []).length })
```

`overflows` false, `logos` all true, `tokens` zero, `pii` **zero**, and `themes`
equal to `counted` — every theme must carry its sample size.

## 10. Ship

Save as `<client>-review-miner-<YYYY-MM>.html`. Named by month; reviews
accumulate slowly and a weekly cadence wastes credits without adding signal.

Lead with the competitor-complaint quadrant. It is the one thing in the report a
brand manager cannot get anywhere else, and it writes the next bullet for them.
