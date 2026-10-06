# Before you send it

## 1. Nothing unmeasured is reported

- **A+ and video rows are either marked "by eye" with today's date, or absent.**
  No blank cells on those rows.
- No claim about a competitor's A+ modules or video was inferred from the
  `description` field.
- Every other row in the grid came from a field that actually exists.

## 2. The fields were read correctly

- `bullet_points` was **split on newline** on every product, not treated as one
  string.
- Bullet counts show **visible / total**, and anything above five is called out
  on whichever side it occurs.
- `description` length is **not** compared across products.
- `buybox_raw` was filtered to `price > 0` — no `-1` reached any price figure.

## 3. Price

- **Price per unit is in the grid** and is the row the analysis leans on.
- Where `price_per_unit` was missing and derived from the pack size, the report
  says it was derived.
- Raw price is shown as well.
- Coupons and subscribe-and-save prices are included — a 10% coupon changes the
  comparison entirely.

## 4. Reviews

- `reviews_count` and **one-star share** are both in the grid.
- The analysis leans on depth and one-star share, not on the headline rating.
- Where the review gap is large, the report **says it cannot be closed with
  copy** and proposes a narrower intent instead.
- No claim is built on the ~8 retrievable review bodies.

## 5. The gaps

- **Three to five gaps total**, not nineteen.
- Each is tiered: this week / this month / this quarter / accept.
- The **Accept** tier is populated. Naming what is not being fixed is what makes
  the rest credible.
- Every gap names the row in the grid it came from.

## 6. Compliance

- **No competitor brand name appears in any proposed copy.**
- No comparative claim is proposed.
- The gaps inform the copy; the copy does not reference them.

## 7. Snapshot honesty

- The report says rank and price are a **snapshot** with no history available.
- The date and time of the scrape are on the page. Prices and coupons move
  daily and a week-old teardown is misleading without its timestamp.

## 8. Render check

```js
({ overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
   cols: document.querySelectorAll('table thead th').length,
   rows: document.querySelectorAll('table tbody tr').length,
   logos: [...document.images].map(i => i.naturalWidth > 0),
   tokens: (document.body.innerHTML.match(/\{\{[A-Z0-9_]+\}\}/g) || []).length,
   blanks: [...document.querySelectorAll('table tbody td')]
             .filter(td => !td.textContent.trim()).length,
   gaps: document.querySelectorAll('[data-gap]').length })
```

`overflows` false, `logos` all true, `tokens` zero, **`blanks` zero** — an empty
cell in a comparison grid reads as "they have nothing there" — and `gaps`
between 3 and 5.

## 9. Ship

Save as `<client>-competitor-teardown-<ASIN>-<YYYY-MM-DD>.html`.

Lead with the one gap in the "this week" tier. A teardown that arrives with a
change someone can make this afternoon gets read; one that opens with a
nineteen-row grid does not.
