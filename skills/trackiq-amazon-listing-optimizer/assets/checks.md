# Before you send it

## 1. Nothing was invented

**The one that matters most.** Read every factual statement in the proposed
copy and confirm it appears in the current listing or was confirmed by the user:

- size, count, weight, dimensions
- materials and ingredients
- certifications and origin
- what it does

An invented attribute is the failure that gets a listing suppressed, and it is
the easiest one to make because the sentence reads well.

## 2. Every term traces to data

- **Each proposed term shows its source and its number** — orders from
  `get_search_terms`, or volume from SQP, or the client's list.
- No term appears because it sounded right.
- Between eight and twelve terms total. More means stuffing.
- Which SQP weeks were present is stated — ingestion is intermittent.

## 3. The fields were read correctly

- `bullet_points` was **split on newline**, not treated as one string.
- The bullet count is stated. If the current listing has more than five, the
  invisible one is named.
- The report says what the scraped `description` field actually contained — a
  concatenation of description, A+ text and brand story — before proposing a
  replacement.
- Nothing claims to have audited **A+ modules or video**. Neither is visible.

## 4. The title

- Character counts shown for both current and proposed.
- The threshold used is stated, not quoted as a universal rule.
- Brand and primary term inside the first ~80 characters.
- No ALL CAPS, no promotional language, no competitor names.

## 5. The bullets

- Exactly five.
- Each answers one of the five questions, in order.
- Each under about 200 characters.
- At most two search terms each, inside real sentences.
- No two bullets say the same thing.

## 6. Backend terms

- The proposal says **in the same block** that current backend terms cannot be
  read and the user must reconcile against what is already there.
- Under 250 bytes — **count bytes, not characters**.
- Nothing repeated from the title or bullets.

## 7. Compliance

- The compliance pass was run on the **proposed** copy: no health claims, no
  unsubstantiated superlatives, no competitor names, no shipping or price
  language.
- **Risky claims already in the current copy are flagged.** This is often the
  most valuable finding in the document.

## 8. Reviews

- No sentence of the form "customers report…" is built on the eight inline
  reviews.
- The star distribution is used for anything quantitative.
- The review sample size is stated where reviews informed a change.

## 9. Render check

```js
({ overflows: document.documentElement.scrollWidth > document.documentElement.clientWidth,
   bullets: document.querySelectorAll('.proposed-bullet').length,
   logos: [...document.images].map(i => i.naturalWidth > 0),
   tokens: (document.body.innerHTML.match(/\{\{[A-Z0-9_]+\}\}/g) || []).length,
   // every proposed term must carry its source
   terms: document.querySelectorAll('[data-term]').length,
   sourced: document.querySelectorAll('[data-term][data-source]').length })
```

`overflows` false, `logos` all true, `tokens` zero, `bullets` exactly 5, and
`terms` equal to `sourced`. Then look at it; if it will not paint, say the check
was structural.

## 10. Ship

Save as `<client>-listing-optimizer-<ASIN>-<YYYY-MM-DD>.html`.

Send it with the compliance flags first if there are any — a risky claim already
live is more urgent than a better bullet. Then the title, because it is the
single change with the most effect and the easiest to approve.
