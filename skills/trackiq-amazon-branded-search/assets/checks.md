# Before you send it

## 1. Is the split honest?

- SP and SB are reported on their own attribution windows and labelled.
  No ROAS is computed across both.
- Buckets add up: branded + competitor + product targeting + generic equals
  the channel total, to the dollar.
- The headline is generic ROAS, with blended beside it and labelled.

## 2. Can the client audit it?

- The brand and competitor terms used are printed in the report.
- The ten largest queries in each bucket are shown.
- Read the ten largest branded queries by eye. Anything misfiled goes into
  the exclusions in account.md and the split is rerun.

## 3. Is the brand-spend reading fair?

- Every branded query in the defence table has a purchase share, or
  says it was unavailable.
- The recommendation is a test with a success measure, never a cut.

## 4. Did the pulls finish?

- Both search-term pulls were paged until a call returned fewer rows than
  the limit. If not, the report says the generic share is understated.

## 5. Nothing a client would publish names a competitor

Competitor names appear in the analysis tables only.

## 6. Render check

```js
({ overflows: document.documentElement.scrollWidth > window.innerWidth,
   rows: [...document.querySelectorAll('table')].map(t => t.querySelectorAll('tbody tr').length),
   tokens: (document.body.innerText.match(/\{\{[A-Z_]+\}\}/g) || []).length })
```
