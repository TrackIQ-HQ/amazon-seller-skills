---
name: trackiq-amazon-review-miner
description: Builds a voice-of-customer picture for a brand by sampling reviews across its own catalogue and its competitors, clustering what buyers praise and complain about into themes, and turning those into bullet and A+ copy directions plus negative keywords. Uses the full star distribution for anything quantitative because only about eight review bodies are retrievable per product. Use when the user asks about customer reviews, what customers are saying, voice of customer, review themes, complaints, why the rating dropped, or what to put in the copy.
---

# Review & Voice-of-Customer Miner

The only skill in the set that produces **creative direction** rather than
another number.

**What do buyers actually say, and what should the page say back?**

Output is a branded HTML report: themes, praise against complaint, own against
competitor, and the copy directions that follow.

## Requires

- **The Oxylabs scraper**, for `get_reviews` and `get_product`.
- The TrackIQ MCP, for `list_marketplaces`, `get_product_performance` (to pick
  the ASINs worth sampling) and `get_search_query_performance` (to connect
  complaints to search terms).
- **A competitor set** — three to five ASINs. Ask, or take them from
  `trackiq-share-of-shelf`.
- Nothing else. No filesystem, no shell.
- **Without Oxylabs:** cannot see reviews at all. Ask the user to export them
  from Seller Central rather than guessing.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/pulls.md` — the sampling plan and the eight-review ceiling
- `assets/method.md` — how themes are built and what may be claimed from them
- `assets/checks.md` — what to verify before anything is sent

Copy `assets/report-template.html` and replace every `{{TOKEN}}`.

## Non-negotiables

1. **`get_reviews` returns about eight review bodies per ASIN.** The response
   says so itself: *"Only the ~8 inline top reviews are returned; the dedicated
   amazon_reviews source is tier-gated on this account."* On a product with
   2,816 reviews that is 0.3% of them.
2. **And those eight are skewed.** On the ASIN this was built against, seven of
   the eight returned were five-star, against a true distribution of 83/9/5/1/2.
   They are the *most helpful* reviews, which is not the same as a sample.
   **Never compute a percentage from the bodies.**
3. **`rating_stars_distribution` is complete and reliable.** It is the
   quantitative backbone — the real split of five to one star, per ASIN. Every
   number on the report comes from there or from `reviews_count`. The bodies
   supply language, not proportions.
4. **This is a brand-level skill, not a per-ASIN deep dive.** Eight reviews from
   one product is an anecdote. Eight from each of twenty own ASINs and four
   competitors is roughly two hundred — a corpus worth clustering. Scope it
   that way and say how many were read.
5. **Say the sample size beside every theme.** "Mentioned in 7 of 184 reviews
   read" is honest and useful. "Customers frequently report" from three
   mentions is not.
6. **Praise and complaint are separated, and so are own and competitor.** The
   four-way split is where the value is: a complaint competitors get and you do
   not is a positioning asset; one you get and they do not is a product problem.
7. **A new complaint theme is an early quality warning.** Where a previous run's
   file exists, diff the themes and flag anything new. Without it, say the
   comparison starts next run.
8. **Do not diagnose product quality from reviews.** Report what is said and how
   often. A pattern worth investigating is a finding; a conclusion about the
   manufacturing is not.
9. **Never quote a review verbatim in client-facing copy.** Reviews are the
   reviewer's words. Paraphrase in the themes, and never lift a phrase into
   proposed bullet copy.
10. **No reviewer names, no review IDs** in any output.
11. **Never print `account_id`.**

## The honest ceiling, stated up front

This skill reads the reviews Amazon shows inline. It is a **qualitative
instrument with a quantitative spine** — themes from a couple of hundred
bodies, proportions from the full star distributions.

If a client needs true review mining at scale, that is a Seller Central export
or an upgraded Oxylabs tier, and the report should say so rather than implying
the corpus was complete.

## What it pairs with

`trackiq-listing-optimizer` consumes the objections this skill finds and writes
them into the bullets. `trackiq-competitor-teardown` compares the pages; this
compares what buyers say about them.

## Delivery

The output is produced in the chat first. Delivery is the last step and the
method comes from the Delivery block in account.md — never ask per run.

| Method | What to do | Needs |
|---|---|---|
| `in-chat` | Return the report. The default, and the fallback for every other method. | nothing |
| `file` | Write it beside the skill, dated. | a filesystem |
| `slack` | Post the headline findings as text, then upload the file. | a connected Slack tool |
| `n8n` | POST it to the configured webhook. | network access |
| `email` | Hand it to the connected mail tool. | a connected mail tool |

Confirm before the first outward send of a session, fall back to in-chat
loudly when a method is unavailable, and never substitute a different
outward channel.

## Version

`trackiq-amazon-review-miner` v1.0.1 (2026-10-06).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-review-miner`, and if it is newer, give them the download link and the
one-line changelog. Do not fetch at any other time.
