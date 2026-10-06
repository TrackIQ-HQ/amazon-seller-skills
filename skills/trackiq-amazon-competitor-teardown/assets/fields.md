# What can and cannot be compared

`get_product(asin)` via Oxylabs, one credit per call.

## Comparable, and reliable

| Field | What it supports |
|---|---|
| `title` | length, structure, what sits in the first ~80 characters |
| `bullet_points` | count and length — **split on newline**, it is one string |
| `images[]` | image count |
| `price`, `currency` | with the caveat below |
| `_oxylabs_bonus.price_per_unit` | **the comparison that matters** |
| `_oxylabs_bonus.price_sns` | subscribe-and-save price |
| `coupon`, `coupon_discount_percentage` | promotional posture |
| `rating`, `reviews_count` | review depth |
| `_oxylabs_bonus.rating_stars_distribution` | the one-star share — the real quality signal |
| `bsr_primary`, `sales_rank_ladder` | rank now, no history |
| `buybox.seller`, `buybox.stock` | who holds it, are they in stock |
| `_oxylabs_bonus.featured_merchant` | FBA or not |
| `_oxylabs_bonus.buy_it_with` | what Amazon pairs it with — bundle intelligence |
| `category[].ladder` | are we even in the same browse node |

## Not available at all

- **No A+ content flag.** Cannot tell whether A+ exists, or which modules.
- **No video flag.** Cannot tell whether the listing has video.
- **No backend search terms.**
- **No variation family.**

These are exactly the rows a client expects in a teardown, so the temptation to
infer them is strong. Do not. **Either open the pages and look, marking the row
"by eye" with the date**, or leave the row out and say it was not measured.

A teardown reporting "competitor has A+ and we do not" when nothing checked is
the kind of error that gets the whole document doubted.

## Two fields that lie

### `description`

A concatenation of the whole lower page — the real description, A+
comparison-table cell labels, and brand-story copy, with no separator. On the
ASIN this was built against it ran to several thousand characters of mixed
content.

**Do not compare its length across competitors.** You would be comparing how
much A+ copy each page has, filtered through a scraper, which is not a finding.

Read it for **what the page claims**. That is genuinely useful — it is where you
find the certifications, the sourcing story and the objections each brand chose
to answer.

### `buybox_raw`

Contains rows with `price: -1`. Those are subscribe-and-save **delivery
frequency** options ("2 weeks", "1 month (Most common)"), not offers.

Filter `price > 0` before computing any price range, or the report will show a
minimum price of -1 and nobody will trust anything else on the page.

## Price: compare per unit

A 30-count at $12.99 and a 50-count at $18.99 cannot be compared on price. The
scrape returns `price_per_unit` with its unit:

```
"price_per_unit": {"currency": "USD", "price": 0.43, "unit": "count"}
```

Use it. Where it is missing, derive it from the pack size in the title and
**say it was derived**.

Show the raw price too — shoppers see both, and a high per-unit price on a small
pack is a legitimate strategy.

## Reviews

`get_reviews(asin)` returns about **eight** bodies — the dedicated review source
is tier-gated. `rating_stars_distribution` is complete.

For a teardown, the useful comparison is:

```
reviews_count        depth — the moat
one_star_pct         how often it disappoints
```

A 4.6 on 2,816 reviews beats a 4.8 on 40 on every dimension that affects a
shopper. Rank on depth, then on one-star share, and treat the headline star
rating as the least informative number of the three.

## Cost

Four ASINs, product and reviews each, is **8 credits** per teardown. Agree the
competitor set first.
