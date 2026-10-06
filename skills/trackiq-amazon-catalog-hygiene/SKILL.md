---
name: trackiq-amazon-catalog-hygiene
description: Sweeps a whole Amazon catalogue for the quiet defects nobody owns — thin image sets, truncating or short titles, bullet counts above or below what displays, orphaned and duplicate SKUs, dead and GUID listings cluttering the inventory, products with no ads and no traffic, and listings that are live but not buyable — ranked by revenue at risk so the list is finite. Use when the user asks for a catalogue audit, listing hygiene, what is broken across our listings, catalogue cleanup, orphan ASINs, or a health check across all products.
---

# Catalog & Variation Hygiene Audit

The housekeeping nobody does, because it is nobody's job and no single item is
urgent.

**What is quietly broken across the catalogue, and which five things are worth
fixing?**

Output is a branded HTML report: the defects, ranked by revenue at risk.

## Requires

- The TrackIQ MCP, for `list_marketplaces`, `get_product_performance`,
  `get_inventory_snapshot` and `get_product_ads`.
- **The Oxylabs scraper** for the page-level checks — `get_product`, one credit
  per ASIN. On a 60-ASIN catalogue that is 60 credits; agree the scope first.
- Nothing else. No filesystem, no shell.
- **Without Oxylabs:** the inventory and performance checks still work and are
  half the value. Say which half is missing rather than implying a full sweep.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/checklist.md` — every check, what it needs, and the four that cannot
  be automated
- `assets/method.md` — how revenue at risk is assigned and how the list is cut
  to size
- `assets/checks.md` — what to verify before anything is sent

Copy `assets/report-template.html` and replace every `{{TOKEN}}`.

## Non-negotiables

1. **Four of the checks a client will expect cannot be automated.** There is no
   A+ content flag, no video flag, no backend search terms and no variation
   family anywhere in the tools. **Mark those rows "needs eyes" and leave them
   unscored**, or open the pages and fill them in by hand with a date. Never
   report a gap that was never measured.
2. **`description` is not the description.** It is a scrape of the whole lower
   page with A+ text and brand-story copy concatenated in. Do not use its
   presence or length as an A+ proxy.
3. **`bullet_points` is one newline-joined string.** Split on newline to count.
   More than five means some are invisible on the detail page; fewer than five
   is wasted space.
4. **Most inventory rows are not products.** On the account this family was
   built against, roughly 70 of 146 snapshot rows were variation parents, FBM
   shadow SKUs, GUID-style ASINs or dead listings. **That is a hygiene finding
   in itself**, not just noise to filter — report the count and the categories.
5. **Never flag a SKU with sales and no stock as dead.** It is the most urgent
   row in the catalogue, and it belongs to `trackiq-restock-priority`.
6. **Rank by revenue at risk, and cut the list to what is finite.** A hygiene
   report with 140 rows changes nothing. Show the top defects by exposure, and
   state how many were found in total.
7. **A defect on a product with no revenue is not urgent, it is tidy.** Keep
   those in a separate low-priority section so the main list stays actionable.
8. **Nothing is changed.** This is a work list a human applies.
9. **Never print `account_id`.**

## What it pairs with

`trackiq-listing-monitor` watches for **changes**; this finds what was already
wrong before anyone was watching. Run this once, fix the list, then let the
monitor keep it clean. `trackiq-listing-optimizer` fixes the individual pages
this skill flags.

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

`trackiq-amazon-catalog-hygiene` v1.0.0 (2026-09-18).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-catalog-hygiene`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
