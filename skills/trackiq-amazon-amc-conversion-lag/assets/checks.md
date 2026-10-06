# Before you send it

## 1. Only real columns

- No sales, units or new-to-brand figure from this tool appears anywhere.
- The report says once why they are absent.
- The report says whether the curve uses `purchases` or
  `total_brand_purchases`.

## 2. Honest shape

- Shares are cumulative. No chart implies the nine buckets are equal width.
- The "7+ DAYS" limitation is stated wherever a window longer than seven
  days is recommended.

## 3. Months are never added

- Every figure names its month.

## 4. No campaign speed claims

- Nothing says which campaign converts fastest. The channel table is labelled
  volume only.

## 5. Render check

```js
({ overflows: document.documentElement.scrollWidth > window.innerWidth,
   rows: [...document.querySelectorAll('table')].map(t => t.querySelectorAll('tbody tr').length),
   tokens: (document.body.innerText.match(/\{\{[A-Z_]+\}\}/g) || []).length })
```
