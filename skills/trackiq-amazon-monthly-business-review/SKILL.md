---
name: trackiq-amazon-monthly-business-review
description: Builds the month-end client deck for one Amazon brand — revenue and spend against the previous month and the same month last year, the organic and paid split, category and product mix, what moved and why, and a prioritised plan for next month. Checks that last year's ad data actually exists before drawing a year-on-year comparison. Use when the user asks for a monthly business review, MBR, month-end deck, monthly client report, end of month summary, or the monthly review presentation.
---

# Monthly Business Review

The retention artifact. **The month in one deck**, in a form a brand manager can
forward to their own leadership without editing it.

Output is a branded 1920x1080 HTML deck, same format as the AMC media mix deck.

## Requires

- The TrackIQ MCP, for `list_marketplaces`, `get_account_overview`,
  `get_product_performance`, `get_campaigns`, `get_portfolios` and
  `get_product_categories_performance`.
- Nothing else. No filesystem, no shell, no internet.
- **Without the MCP:** works from monthly exports of sales, spend and ASIN
  performance for the three periods being compared.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/pulls.md` — the calls, the year-on-year trap, and the duplicate
  category taxonomy
- `assets/narrative.md` — the slide order and what each slide has to earn
- `assets/checks.md` — what to verify before anything is sent, including the
  footer safe-zone measurement

Copy `assets/deck-template.html` and replace every `{{TOKEN}}`.

## Non-negotiables

1. **Check that last year's ad data exists before drawing any year-on-year
   comparison of it.** On the account this was built against, the same month a
   year earlier returned real `total_revenue` but `total_spend` of exactly 0.00
   and `attributed_sales` of 0.00 — advertising history that predates the
   platform connection, not a year without advertising. A naive year-on-year
   would report spend up from zero and organic share down from 100%. Both are
   fabrications. **Test `total_spend > 0` in the prior-year window; if it is
   zero, compare revenue only and say why the ad comparison is absent.**
2. **`get_product_categories_performance` returns two overlapping taxonomies in
   one response.** Pacvue-native categories and TrackIQ `(tiq) …` tags return
   identical spend and sales for the same campaigns — to the cent. **Summing all
   rows double-counts.** Pick one taxonomy, say which, and filter the other out.
3. **Revenue reconciles across every slide.** The month's total on slide 2 is the
   same number as the sum of the category mix on slide 5 and the product table
   on slide 6. If they differ, a filter is wrong. Never ship a deck whose totals
   disagree with each other.
4. **No slide content below the footer safe zone.** 1920x1080, 96px margins,
   104px reserved at the bottom. This is invisible in source and has to be
   measured — `assets/checks.md` has the script.
5. **Three comparisons, no more:** this month, last month, same month last year.
   A deck with five comparison columns does not get read.
6. **Every claim on a narrative slide traces to a number on a data slide.** No
   assertion that cannot be pointed at.
7. **The plan slide is three items, each with an owner and a metric.** A plan of
   nine things is a list, not a plan.
8. **No footnotes.** If it matters, it goes in the body.
9. **Never print `account_id`.**

## What it pairs with

This deck is the monthly assembly of what the other skills produce weekly.
`trackiq-sales-movers` supplies the "what moved and why" slide, `trackiq-budget-pacing`
the spend story, `trackiq-restock-priority` the risks slide. Run those first and
this becomes editing rather than analysis.

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

`trackiq-amazon-monthly-business-review` v1.0.0 (2026-09-18).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-monthly-business-review`, and if it is newer, give them the download
link and the one-line changelog. Do not fetch at any other time.
