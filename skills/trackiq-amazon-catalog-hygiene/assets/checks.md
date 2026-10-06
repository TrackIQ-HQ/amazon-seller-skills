# Before you send it

## 1. Nothing unmeasured is scored

- **A+, video, backend terms and variation completeness are in the "needs eyes"
  section**, unscored and outside the totals.
- That section explains **why** no tool can do them.
- Nothing infers A+ from the `description` field.
- If any of those rows was filled in by hand, it carries the date.

## 2. The scope is stated

- How many ASINs were page-checked with Oxylabs, and how many credits that cost.
- If only the top revenue band was page-checked, the report says the tail was
  not.
- Which sections ran without Oxylabs, if it was unavailable.

## 3. The inventory count

- **The clutter headline is present** — total snapshot rows split into real,
  parents, FBM shadows, GUID ASINs and dead listings.
- Each row is counted **once**, and the rule that claimed it is stated.
- **No SKU with sales and zero stock is listed as dead.** Check this explicitly;
  it is the most dangerous false positive in the report.

## 4. The fields were read correctly

- `bullet_points` was **split on newline**, not counted as one.
- Bullet findings distinguish over-five (invisible) from under-five (wasted).
- Title length thresholds are **stated**, not quoted as universal rules.
- `buybox_raw` price rows of `-1` were filtered out of anything price-related.

## 5. The ranking

- Defects are ranked by **revenue at risk**.
- Severities are labelled **judgement, not measurement**.
- Anything not buyable is at the top regardless of revenue.
- Zero-revenue defects are in the low-priority section, not the main list.
- **The total number of defects found is stated**, even though only the top ten
  are listed.

## 6. Grouping

- Findings are grouped **by cause**, not one row per ASIN.
- Each group lists its ASINs and totals their revenue.
- Twelve thin-image products are one finding, not twelve.

## 7. The sequence

- A fix order is given, with inventory clutter second and the reason stated —
  it makes every other report on the account wrong until it is cleaned.
- The first item is something someone could start today.

## 8. Render check

```js
({ overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
   tables: document.querySelectorAll('table').length,
   rows: [...document.querySelectorAll('table')].map(t => t.querySelectorAll('tbody tr').length),
   logos: [...document.images].map(i => i.naturalWidth > 0),
   tokens: (document.body.innerHTML.match(/\{\{[A-Z0-9_]+\}\}/g) || []).length,
   // the needs-eyes rows must carry no score
   unscored: [...document.querySelectorAll('[data-needs-eyes]')]
               .filter(e => e.querySelector('[data-at-risk]')).length })
```

`overflows` false, `logos` all true, `tokens` zero, **`unscored` zero** — a
"needs eyes" row carrying a revenue-at-risk figure means something unmeasured
was scored. Then look at it; if it will not paint, say the check was structural.

## 9. Ship

Save as `<client>-catalog-hygiene-<YYYY-MM-DD>.html`.

Lead with the inventory clutter count. "Half your catalogue rows are not
products" is the sentence that makes someone read the rest, and it is usually
true and always news.
