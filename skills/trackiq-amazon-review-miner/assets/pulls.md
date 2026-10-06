# The pull sequence

## 0. Account and the competitor set

`list_marketplaces` first. Never print `account_id`.

Ask for **three to five competitor ASINs**, or take them from a recent
`trackiq-share-of-shelf` run, which already identifies who holds page one.

## 1. Choose the ASINs worth sampling

```
get_product_performance(account_id, start_date=<90 days ago>, end_date=<yesterday>,
                        group_by='product', limit=200)
```

Roll up to ASIN and take the ones that carry the revenue — typically the top 15
to 20, or everything above 1% of catalogue revenue. Sampling a long tail of
products nobody buys adds reviews and no signal.

State how many ASINs were sampled and what share of revenue they represent.

## 2. The reviews

```
for each ASIN (own and competitor):
    get_reviews(asin)          # 1 credit
```

Returns:

```
reviews_count_total, rating_overall, rating_stars_distribution,
reviews_returned, reviews[{rating, title, body, date, verified_purchase,
                           helpful_votes, variant, reviewer_name, review_id}]
```

### The ceiling — read this before designing anything

**`reviews_returned` is about 8.** The response says so itself:

> Only the ~8 inline top reviews are returned; the dedicated amazon_reviews
> source is tier-gated on this account.

Eight, on a product with 2,816 reviews.

**And they are skewed.** On the ASIN this was built against, seven of the eight
were five-star, against a true distribution of 83/9/5/1/2. They are Amazon's
*most helpful* selection, not a random sample. A five-star rate computed from
the bodies would read 88% against a true 83% — close by luck, and there is no
reason to expect that to hold.

So:

- **Never compute a proportion from the bodies.**
- **Always compute proportions from `rating_stars_distribution`**, which is
  complete and reliable.
- The bodies give you **language and themes**. That is what they are for.

### Getting to a corpus

Twenty own ASINs plus four competitors is 24 calls and roughly **190 review
bodies**. That is enough to cluster into themes with the sample size stated
beside each one. One ASIN's eight is not.

This is why the skill is brand-level. Scope it that way and say so.

## 3. The product pages

```
for each ASIN:
    get_product(asin)          # 1 credit
```

For `rating`, `reviews_count`, `price`, `bullet_points` and
`_oxylabs_bonus.rating_stars_distribution`.

The bullets matter here: a complaint the page **already answers** is a different
finding from one it ignores. The first is a communication failure, the second is
a gap.

## 4. Cost

One credit per call. Twenty own ASINs plus four competitors, reviews and product
each, is **48 credits** per run. Agree the scope before spending them, and do not
re-run it weekly — reviews accumulate slowly and monthly is the useful cadence.

## 5. Connecting complaints to search

```
get_search_query_performance(account_id, start_date, end_date, limit=200)
```

Where a complaint theme matches a search term the brand is buying — shoppers
arriving on a term the product does not satisfy — that term is a **negative
keyword candidate**, not a copy problem.

That connection is the most actionable output this skill produces, because it
turns a qualitative theme into a bulk-file row.

SQP is weekly, Sunday to Saturday, and ingestion is intermittent. Say which
weeks were present.

## 6. The previous run

Ask for the previous report file. Theme-over-theme comparison is the early
quality warning this skill exists for, and there is no review history in any
tool — the only way to have it is to have written it down last time.

Without one, say the comparison starts next run. Do not show a zero.
