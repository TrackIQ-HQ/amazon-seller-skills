---
name: trackiq-amazon-amc-conversion-lag
description: Reads Amazon Marketing Cloud's time-to-conversion data to show how long shoppers take between their first ad touch and purchase — the share that buys within the hour, the day and the week, and how that shifts month to month — then turns it into two decisions: which attribution window to report on, and how many days ahead of a sales event to start upper-funnel spend. Use when the user asks about time to conversion, conversion lag, attribution window, lookback window, how long customers take to buy, consideration cycle, 7 versus 14 day attribution, or when to start Prime Day or holiday ads.
---

# AMC Conversion Lag & Attribution Window

How long does it take a shopper to buy after they first see an ad? Amazon
Marketing Cloud counts it in nine time buckets. This skill turns those buckets
into two decisions every brand makes by habit: which attribution window its
reports should use, and how far ahead of an event the spend should start.

Run it quarterly, and six weeks before any major sales event.

## Requires

- The TrackIQ MCP, for `list_marketplaces`, `get_amc_time_to_conversion` and
  `get_campaigns`.
- **AMC enabled on the account.** If the focus month returns no rows, stop and
  say so.
- Nothing else. No filesystem or internet needed.
- **Without the MCP:** works from an AMC time-to-conversion export by month.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/pulls.md` — the pulls, the nine buckets, and the zero columns
- `assets/method.md` — cumulative shares, the window, the event lead time
- `assets/checks.md` — what to verify before anything is sent
- `assets/report-template.html` — the report. Replace every `{{TOKEN}}`.

## Non-negotiables

1. **Purchases only.** The tool's sales, units and new-to-brand columns come
   back as zero. Never report them, never chart them, and say once why they
   are absent.
2. **The buckets are uneven.** "< 1 MIN" and "1 - 7 DAYS" are not the same
   width. Show cumulative shares, never a bar chart that implies equal spacing.
3. **"7+ DAYS" is open-ended.** It cannot say whether those shoppers took eight
   days or thirty. Any window longer than seven days is a judgement, and the
   report says so.
4. **This tool cannot rank campaigns by speed.** `group_by='campaign'` returns
   purchase counts per campaign and no timing. Use it for volume context by
   channel only. Never say which campaign "closes fastest".
5. **Never sum AMC rows across months.** Compare the months side by side.
6. **Connect the window to the reports people already read.** Sponsored
   Products reports on a 7-day window; Brands, Display and DSP on 14. The share
   of purchases landing after 7 days is the share a Sponsored Products report
   cannot see.
7. **Never print `account_id`.**

## What it pairs with

`trackiq-amazon-amc-media-mix` uses one of these months on a single slide;
this is the full read. `trackiq-amazon-budget-pacing` is where the event
lead time turns into a spend plan.

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

`trackiq-amazon-amc-conversion-lag` v1.1.0 (2026-09-21).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-amc-conversion-lag`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
