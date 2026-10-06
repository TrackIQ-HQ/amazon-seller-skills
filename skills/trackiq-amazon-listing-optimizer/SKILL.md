---
name: trackiq-amazon-listing-optimizer
description: Rewrites one Amazon listing — title, bullets, description and backend terms — against the terms it should rank for and the questions shoppers actually ask, producing a side-by-side of current and proposed copy with the reason for every change. Built for how Amazon matches intent and answers questions in 2026, not for keyword stuffing. Use when the user asks to optimise a listing, rewrite a title or bullets, improve a product page, listing copy, Rufus or COSMO readiness, or how to make a listing rank better.
---

# Listing Optimizer

The catalogue is full of skills that measure. **This one writes the fix.**

One ASIN in, a rewritten title, five bullets, a description and backend terms
out — each change traced to a search term that earns it or a question it answers.

Output is a branded HTML document: current beside proposed, with reasons.

## Requires

- **The Oxylabs scraper**, for `get_product` and `get_reviews` — the live page
  and what buyers say about it.
- The TrackIQ MCP, for `list_marketplaces`, `get_search_query_performance` and
  `get_search_terms` — the terms worth ranking for and the ones that already
  convert.
- Nothing else. No filesystem, no shell.
- **Without the MCP:** works from the live page plus a keyword list the user
  supplies. Without Oxylabs it cannot see the page and should not guess —
  ask the user to paste the current title, bullets and description.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/fields.md` — what the scrape actually returns, and the two fields that
  are not what they look like
- `assets/method.md` — where the terms come from and how the copy is built
- `assets/checks.md` — what to verify before anything is published

Copy `assets/document-template.html` and replace every `{{TOKEN}}`.

## Non-negotiables

1. **`bullet_points` is one newline-joined string, not a list.** Split on
   newline. The ASIN this was built against had **six** bullets where Amazon
   displays five — count them, and if there are more than five say which one is
   not being seen.
2. **`description` is not the description.** The scrape concatenates the whole
   lower page — A+ comparison-table labels and brand-story copy land in the same
   field. Never diff it as if it were the description, and never rewrite "the
   description" from it without telling the user what it actually contains.
3. **There are no backend search terms in any tool.** Not in the scrape, not in
   the MCP. Proposed backend terms are a **recommendation the user must check
   against what is already there**, because duplicating existing terms wastes
   the 250-byte allowance. Say so every time.
4. **Measure the title, do not assert a rule.** Report the character count and
   flag it against a stated threshold. Amazon's limits vary by category and
   change; the durable facts are that the first ~80 characters are what a phone
   shows, and that the brand and the primary term belong inside them. State the
   threshold used rather than quoting a rule as if it were universal.
5. **Every proposed term traces to data.** A term appears in the rewrite because
   it converts (`get_search_terms`) or has volume and relevance
   (`get_search_query_performance`) — not because it sounds right. Show the
   source and the number beside each one.
6. **Answer questions, do not stuff keywords.** The useful test in 2026 is
   whether the page answers what a shopper would ask: what is it, who is it for,
   what makes it different, how is it used, what are the objections. Build the
   bullets around those five, with the terms carried naturally inside them.
7. **Objections come from reviews.** The negative reviews name the thing the
   page failed to say. `get_reviews` returns only ~8 inline reviews — see
   `assets/fields.md` — so treat them as a prompt, not as a survey.
8. **No claims the brand cannot make.** No health or medical claims, no
   superlatives that need substantiating, no competitor names, no "#1" or "best
   seller" language. If the current copy has them, flag them as a risk.
9. **Never invent a product attribute.** Every factual statement in the rewrite
   must appear in the current listing or be confirmed by the user. Making up a
   size, a material or an ingredient is the one failure that gets a listing
   suppressed.
10. **Nothing is published.** This produces copy a human reviews and uploads.
11. **Never print `account_id`.**

## Overlaps with `rufus-readiness`

A `rufus-readiness` skill exists in the local library and **scores** a page.
This one **rewrites** it. If both are installed, run the scorer first and feed
its gaps in here. Do not ship both as answers to the same question — one
measures, one fixes.

## What it pairs with

`trackiq-category-priority-keywords` supplies the terms worth ranking for.
`trackiq-search-visibility-audit` says where the listing under-converts rather
than under-ranks — a page that ranks and does not convert needs this skill, and
a page that converts and does not rank needs advertising.

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

`trackiq-amazon-listing-optimizer` v1.0.0 (2026-09-18).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-listing-optimizer`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
