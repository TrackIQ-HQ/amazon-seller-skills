---
name: trackiq-amazon-branded-search
description: Splits every Amazon Sponsored Products and Sponsored Brands search term into branded, competitor, product-targeting and generic buckets, then shows where the ad money really goes — how much is spent on shoppers who already typed the brand, what generic search returns once brand is taken out, whether competitor conquesting pays — and checks the brand's purchase share on its own name before calling brand spend defence or waste. Use when the user asks about branded vs non-branded, brand vs generic spend, branded search, brand defence, conquesting, competitor keywords, true or non-branded ACOS, or whether ACOS is flattered by brand terms.
---

# Branded vs. Non-Branded Search

Takes the blended ACOS everyone reports and splits it into its honest parts:
brand, competitor, product targeting and generic. Brand search almost always
flatters the average, so the number that says whether advertising is growing
the business is the generic one.

Run it monthly, and before any conversation about "our ACOS is fine".

## Requires

- The TrackIQ MCP, for `list_marketplaces`, `get_search_terms`,
  `get_targets`, `get_search_query_performance`, `get_product_performance`
  and `get_campaigns`.
- **The brand's own terms**, from the Brand terms block in account.md — the
  brand name, its misspellings and its product-line names. Ask once.
- **Competitor brand names**, from the same block. Optional; without them
  competitor search counts as generic, and the report says so.
- **Without the MCP:** works from a search-term report exported from
  Campaign Manager for Sponsored Products and Sponsored Brands.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report only needs the Brand terms block added.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/pulls.md` — the pulls, why SP and SB are pulled separately
- `assets/method.md` — the classifier, the buckets, and the brand-share test
- `assets/checks.md` — what to verify before anything is sent
- `assets/report-template.html` — the report. Replace every `{{TOKEN}}`.

## Non-negotiables

1. **Pull Sponsored Products and Sponsored Brands separately.** `ad_type='all'`
   blends a 7-day and a 14-day attribution window into one ROAS. Report each
   channel's buckets on its own window and label them.
2. **Show the classifier.** The report lists the brand and competitor terms
   used, and the ten largest queries in each bucket, so the client can
   correct a misfile. A split nobody can audit does not get believed.
3. **ASIN queries are their own bucket.** A query like `b0cxxxxxxx` is
   product targeting typed into search, not a generic term.
4. **Never call brand spend waste on ROAS alone.** Brand terms always return
   well. The question is whether the brand would have won the sale anyway —
   check the brand's purchase share on its own name first
   (`assets/method.md` §4), and recommend a controlled test, never a cut.
5. **The headline is generic ROAS, not blended.** Blended ACOS is shown for
   reference, beside it, labelled.
6. **Paginate until a pull returns fewer rows than the limit.** The long tail
   is mostly generic; stopping at the cap overstates the brand share.
7. **Never name a competitor in anything the client might publish.** The
   competitor list is analysis, not copy.
8. **Never print `account_id`.**

## What the account will argue with

Some brands bid on their own name because a competitor is conquesting it.
If the brand's purchase share on its own name is low, or a competitor shows up
in the branded queries' sponsored slots, brand spend is defence — say so
rather than implying it is inflating the numbers for nothing.

## What it pairs with

`trackiq-amazon-wasted-spend` finds generic terms to cut;
`trackiq-amazon-search-term-harvester` finds generic terms to promote. This
one says how big the generic business actually is.

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

`trackiq-amazon-branded-search` v1.1.1 (2026-10-06).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-branded-search`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
