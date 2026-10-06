# Before you send it

## 1. The year-on-year is real

- **`total_spend` in the prior-year window was tested and is greater than zero**
  before any year-on-year advertising figure was drawn.
- If it is zero, the deck shows revenue year-on-year only, and says on the slide
  that ad history for that period predates the platform connection.
- Nowhere does the deck report spend "up from $0", an infinite percentage, or an
  organic share falling from 100%.
- The same test was applied to `attributed_sales` before any organic-share
  year-on-year.

## 2. One category taxonomy

- The category slide uses **either** the Pacvue-native categories **or** the
  `(tiq)` tags, never both.
- The slide says which one it is showing.
- **The categories sum to the month's spend on slide 2.** Print the sum. If it
  comes to roughly double, both taxonomies leaked in.

## 3. Everything reconciles

- Month revenue on slide 2 == sum of category revenue on slide 5 == sum of the
  product table on slide 6.
- Spend on slide 2 == sum of portfolio spend on slide 7.
- Any figure appearing twice in the deck is the same figure.
- Percentages are computed from the underlying numbers, not from other
  percentages.

## 4. Whole months

- All three windows are whole calendar months.
- Days in each month are stated where a comparison could be read as performance
  (28 against 31 is an 11% handicap).

## 5. The slides

- **Slide 1 carries a verdict**, not a summary. If the month was bad, slide 1
  says so.
- Slide 9 exists and is not empty.
- Slide 11 has **exactly three** items, each with an owner and a metric.
- No claim on a narrative slide lacks a number on a data slide.
- No footnotes anywhere.
- No ASIN names buy box as a cause.

## 6. Footer safe zone — measure it, do not eyeball it

Overflow past the footer is invisible in source. Run this in the browser:

```js
// Read the scale off the deck itself. Recomputing it from window.innerWidth
// silently yields 0 in a hidden or zero-width viewport, and every slide then
// measures as passing.
const deck = document.getElementById('deck');
const sc = new DOMMatrixReadOnly(getComputedStyle(deck).transform).a;
if (!(sc > 0)) throw new Error('deck not laid out yet — resize the window and re-run');

const res = [...document.querySelectorAll('.slide')].map((s, i) => {
  const top = s.getBoundingClientRect().top;
  let b = 0;
  [...s.children].forEach(c => {
    if (/bug|pnum|close-lockup|title-lockup|title-kicker/.test(c.className)) return;
    b = Math.max(b, (c.getBoundingClientRect().bottom - top) / sc);
  });
  return { slide: i + 1, over: Math.round(b - 976) };
});
({ bad: res.filter(r => !(r.over < 0)), all: res.map(r => r.over) });
```

`bad` must be empty and every value in `all` must be negative. A `null` or `NaN`
is a **failed measurement, not a pass** — re-run it.

To fix an overflowing slide, in this order: apply the `tight` class, shorten the
prose, drop a table row, split the slide. Never shrink the base font.

## 7. Render check

```js
({ slides: document.querySelectorAll('.slide').length,
   logos: [...document.images].map(i => i.naturalWidth > 0),
   tokens: (document.body.innerHTML.match(/\{\{[A-Z0-9_]+\}\}/g) || []).length })
```

`tokens` must be **zero** — an unreplaced `{{TOKEN}}` in a client deck is the
worst single failure this skill can ship. `logos` all true.

## 8. Ship

Save as `<client>-monthly-business-review-<YYYY-MM>.html`. Named by the month
reviewed, not the day it was built.

Send it with the slide 1 verdict as the first line of the email. If the deck
will not open on their machine, that sentence still does the job.
