# Before you send it

## 1. No revenue anywhere

- **No ROAS, no ACOS, no sales, no revenue column on the page.** Search the HTML
  for those words; the only acceptable occurrence is the sentence explaining
  they are unavailable.
- The report states plainly that segment-level revenue attribution is not in
  this feed, and points at `trackiq-amc-media-mix` for the revenue view.
- No figure on the page is derived from a revenue number.

## 2. No sums, no shares

- **No total row on any dimension table.**
- No percentage-of-total anywhere.
- No sentence of the form "audience X drove N% of DSP".
- The overlap is explained where a reader would first try to add a column up —
  beside the table, not in a footnote at the bottom.

## 3. The overlap grouping

- Segments within 5% on impressions **and** matching CTR to three decimals are
  grouped and labelled as overlapping.
- The group counts as one finding, not four.
- Nothing in the "cut" list is a lone member of an overlap group without a note
  saying its impressions are shared.

## 4. The dimensions

- Every dimension was called separately — `dimension` is a required argument.
- A dimension that returned no rows is stated as empty, not omitted.
- Each section is labelled with the dimension it came from.
- Nothing is compared across dimensions.

## 5. The arithmetic

- Cost per NTB purchase is the headline metric.
- Comparisons use the **median** of the dimension, not the mean.
- Rows below the volume floor (50,000 impressions, 100 clicks) are in the full
  table but out of the ranked findings, and the count held back is stated.
- No division by zero produced an infinity or a blank on the page — a segment
  with zero NTB purchases shows as "no NTB purchases", not as a number.

## 6. The recommendations

- Every "fix" item names the funnel step that failed and says the fix is not a
  budget change.
- Every "cut" item has the volume to support it.
- Nothing is applied. The report says a human applies these in the DSP console.

## 7. Render check

```js
({ overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
   tables: document.querySelectorAll('table').length,
   rows: [...document.querySelectorAll('table')].map(t => t.querySelectorAll('tbody tr').length),
   logos: [...document.images].map(i => i.naturalWidth > 0),
   // must be zero: no revenue language may survive into the tables
   revenue: [...document.querySelectorAll('th')]
              .filter(t => /roas|acos|revenue|sales/i.test(t.textContent)).length })
```

`overflows` false, `logos` all true, **`revenue` zero**. Then look at it; if it
will not paint, say the check was structural.

## 8. Ship

Save as `<client>-dsp-performance-<YYYY-MM-DD>.html`.

Lead the message with the cost per new-to-brand purchase and the one segment
worth scaling. If the honest answer is that the funnel breaks at the detail page
rather than in the media, lead with that instead — it is the more valuable
finding and it is not a DSP problem.
