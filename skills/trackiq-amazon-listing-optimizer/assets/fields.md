# What the scrape actually returns

`get_product(asin)` via Oxylabs. One credit per call.

## Fields you can trust

| Field | Notes |
|---|---|
| `title` | the live title. Measure its length. |
| `brand` | |
| `images[]` | the image block. Count them; nine is healthy, four is thin. |
| `price`, `currency` | |
| `rating`, `reviews_count` | both reliable |
| `bullet_points` | **one string** — see below |
| `category[].ladder` | the browse node path |
| `bsr_primary`, `sales_rank_ladder` | rank now, no history |
| `buybox` | `price`, `seller`, `stock` |
| `coupon`, `coupon_discount_percentage` | |
| `_oxylabs_bonus.rating_stars_distribution` | the full star split — reliable |
| `_oxylabs_bonus.buy_it_with` | what Amazon pairs it with. Useful for bundles. |
| `_oxylabs_bonus.price_per_unit`, `price_sns` | |

## `bullet_points` is one newline-joined string

Not a list. Split on `\n`.

The ASIN this was built against returned **six** bullets. Amazon displays five
on the detail page, so the sixth is invisible to shoppers while still counting
against the listing.

Count them. If there are more than five, say which one is not being seen and
propose which five survive — that is a real finding and nobody notices it.

## `description` is not the description

This is the trap. The scrape concatenates **the whole lower page** into
`description`:

- the actual product description
- A+ comparison-table cell labels ("4ft Starter", "Grill Covers", "48ft Pro")
- brand-story copy ("With over 300 million bees, 10,000 beehives…")
- certification and marketing blocks

So the field is a mixture of three or four different pieces of content, and
there is no marker saying where one ends and the next begins.

**Consequences:**

- Do **not** diff it between runs as if it were the description field — that is
  `trackiq-listing-monitor`'s job and it has the same problem.
- Do **not** rewrite "the description" from it without telling the user what it
  actually contains.
- **Do** read it for what the page currently claims, which is genuinely useful
  for finding missing answers and for spotting risky claims.

If the user needs the true description field, it is in Seller Central. Ask them
to paste it.

## What is not there at all

- **No A+ content flag.** Cannot tell whether A+ exists or what modules it uses.
  The A+ *text* leaks into `description`, which is a hint and not a check.
- **No video flag.** Cannot tell whether the listing has video.
- **No backend search terms.** Not in the scrape, not in the MCP, nowhere.
- **No variation family.** Siblings are not returned.

Any audit of A+ modules or video presence has to be done **by eye**. Say that
rather than reporting a gap that was never measured.

## `get_reviews` returns about eight reviews

Verbatim from the response on the account this was built against:

> Only the ~8 inline top reviews are returned; the dedicated amazon_reviews
> source is tier-gated on this account.

Eight, against a listing with 2,816 reviews — and skewed: seven of the eight
returned were five-star against a true distribution of 83/9/5/1/2.

**So:**

- `rating_stars_distribution` is the reliable quantitative signal. Use it.
- The eight bodies are a **prompt for what to look into**, never a survey. Do
  not say "customers report X" from one review.
- For real voice-of-customer work, `trackiq-review-miner` samples across the
  catalogue and competitors to build a corpus worth clustering.

## Cost

One credit per `get_product` call, one per `get_reviews`. Optimising a listing
against three competitors is eight calls. Agree the competitor set before
spending them.
