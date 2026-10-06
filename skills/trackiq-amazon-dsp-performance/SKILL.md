---
name: trackiq-amazon-dsp-performance
description: Breaks Amazon DSP down by audience, creative, inventory source, technology and geography to show which segments actually recruit customers and which burn impressions. Ranks on new-to-brand purchases, detail page views and cost per action rather than ROAS, because DSP revenue is not returned at these dimensions. Use when the user asks about DSP performance, which audiences work, creative performance, DSP audiences, supply or inventory sources, where DSP budget is going, or why DSP is or is not working.
---

# DSP Audience & Creative Performance

`get_dsp_performance` takes a `dimension` argument that almost nothing uses:
`audience`, `creative`, `inventory`, `technology`, `geography`. That is a whole
data surface sitting unexamined in most accounts.

**Which audience segments convert, which creatives carry them, and which supply
sources waste impressions.**

Output is a branded HTML report, one section per dimension.

## Requires

- The TrackIQ MCP, for `list_marketplaces` and `get_dsp_performance`.
- **A DSP account with spend in the window.** Not every account runs DSP. Check
  before promising a report.
- Nothing else. No filesystem, no shell, no internet.
- **Without the MCP:** works from a DSP report export broken out by the same
  dimensions.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/pulls.md` — the dimensions, and the two ways this data lies
- `assets/method.md` — what to rank on when there is no revenue
- `assets/checks.md` — what to verify before anything is sent

Copy `assets/report-template.html` and replace every `{{TOKEN}}`.

## Non-negotiables

1. **`sales` is 0.0 and `units` is "0" on every row at these dimensions.** ROAS
   comes back as 0 and ACOS as null. This is not an account with no sales — it
   is revenue that is not attributed at the segment level. **Never show a ROAS,
   an ACOS or a revenue figure in this report.** If a number would imply
   revenue, it does not belong on the page.
2. **Never sum segments to a total.** Audiences overlap heavily — on the account
   this was built against, four segments returned 5.29M to 5.37M impressions
   with an *identical* 0.8540 CTR, which is the same inventory attributed to
   several segments at once. Summing them produced several times the real spend.
   There is no total row to check against, because `dimension` is mandatory.
3. **Rank on new-to-brand purchases first.** `ntb_purchases` is the metric DSP
   exists for. Orders, DPV and ATC are supporting evidence.
4. **Report cost per action, not efficiency ratios.** `spend / ntb_purchases`,
   `spend / dpv`, `spend / atc`. These are computable and honest. Anything
   dividing by revenue is not.
5. **Compare within a dimension, never across.** An audience and a creative are
   not comparable rows; each dimension gets its own section and its own ranking.
6. **`dimension` is a required argument.** Calling without it errors. Pull each
   dimension separately and label each section with the one it came from.
7. **Say what could not be measured.** The report states plainly that revenue
   attribution is unavailable at segment level, so "which audience made the most
   money" is a question this data cannot answer. Offer the AMC Media Mix skill
   for the revenue view.
8. **Nothing is changed.** Recommendations are for a human to apply in the DSP
   console.
9. **Never print `account_id`.**

## What it pairs with

`trackiq-amc-media-mix` works at the path and channel level and *does* carry
conversion value — it answers whether DSP is worth running at all. This skill
answers what to do inside DSP once that is settled. Run the media mix first; if
DSP is not earning its place, tuning audiences is the wrong conversation.

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

`trackiq-amazon-dsp-performance` v1.0.1 (2026-09-21).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-dsp-performance`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
