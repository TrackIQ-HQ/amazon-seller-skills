---
name: trackiq-amazon-weekly-executive-report
description: Build the TrackIQ Weekly Executive Report — a client-ready week-over-week recap for an Amazon account, covering the scorecard, pacing against the brand's own trailing four-week average, per-product-line marginal return, an Amazon DSP/programmatic breakout, keyword economics, and an inventory days-of-cover watch, closed out with a short list of this week's decisions. Pulls both the current and prior week from the TrackIQ MCP on the same day so the comparison is like-for-like, ties every aggregate to the detail beneath it, and renders as one self-contained HTML email. Use when asked for the weekly executive report, the weekly recap, the Monday client send, a week-over-week pacing report, a weekly brand summary, or a client-facing weekly Amazon report.
---

# TrackIQ: Amazon Weekly Executive Report

A client-facing weekly recap, read in under five minutes by someone who
did not watch the account this week and needs to leave the email knowing
what happened and what happens next. Same Heritage Sage brand as every
other TrackIQ send; opposite register from Snacks — this one is the
prepared brief, not the colleague thinking out loud.

Self-contained `.html`: table-based, inline styles, 640px wrapper,
system-font stack, one media query at 640px.

## Requires

- The TrackIQ MCP, for account overview, product/line performance, ad
  performance, DSP performance, inventory, keyword and search-query
  tools. Ask which brand, marketplace, and week-anchor (most accounts are
  Sunday-Saturday) before pulling anything.
- Nothing else. No filesystem, no shell, no internet.
- **Without the MCP:** ask the user to paste this week's and last week's
  retail, ad spend, ad sales, DSP figures and line-level breakdown, then
  build the report from those. A section whose figures were not provided
  is simply omitted — see non-negotiable 6.

## First run

Before the first send, fill in a copy of `assets/account.example.md` saved
as account.md beside the skill. Every later run reads it and asks nothing.
It is the same file the other TrackIQ skills read, so an account already
set up for the daily send needs only the week anchor and the inventory
bands added.

1. **Brand name** for the eyebrow, and the account line for the footer
2. **Marketplace** — US, UK, DE
3. **Week anchor** — most accounts are Sunday-Saturday
4. **Product lines** — how ASINs roll up, since no API knows your grouping
5. **Inventory bands** — the account's own days-of-cover cutoffs
6. **Delivery** — in-chat, file, Slack, n8n or email, and the target for
   whichever is chosen

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

Re-run this only when the user says the account changed. Never re-ask
mid-send.

## Read first

- `assets/voice.md` — how it is written; read before writing a word
- `assets/structure.md` — the fixed section order and what each is for
- `assets/build.md` — the methodology: what to pull, how to roll it up,
  every formula, and the tie-outs to run before sending
- `assets/charts.md` — how to build bars that render correctly in email
- `assets/tokens.md` — palette, type scale, geometry, as inline hex
- `assets/account.example.md` — the first-run answers, filled in once

Copy `assets/template.html` and replace its content. Do not rebuild the
shell. The template also references `assets/trackiq-logo-white.png` and
`assets/trackiq-bug-white.png`.

## Delivery

The report is always produced in the chat first. Delivery is the last
step, and the method comes from the Delivery block in account.md — never
ask per send.

| Method | What to do | Needs |
|---|---|---|
| `in-chat` | Return the HTML. The default, and the fallback for every other method. | nothing |
| `file` | Write it beside the skill as `<name>-<YYYY-MM-DD>.html`. | a filesystem |
| `slack` | Post the lead headline and the decision list as text, then upload the HTML as a file attachment. Slack will not render the email markup inline — never paste raw HTML into a message. | a connected Slack tool |
| `n8n` | POST the HTML as the request body to the configured webhook, `Content-Type: text/html`. Report the status code back. | network access |
| `email` | Hand it to the connected mail tool with the subject line from the masthead. | a connected mail tool |

Three rules:

1. **Confirm before the first outward send of a session.** Slack, n8n and
   email all publish outside the chat. Show the recipient or channel and
   wait for a yes. In-chat and file need no confirmation.
2. **Fall back loudly.** If the configured method is not available in this
   runtime, return the report in-chat and say which method was skipped and
   why. Never fail silently, and never substitute a different outward
   channel.
3. **Delivery config is not report content.** Naming Slack or n8n here does
   not breach the rule against naming platforms — that rule governs what
   appears inside the rendered email, which never mentions any of them.

## Non-negotiables

1. **Pull both weeks on the same day.** Attribution matures for several
   days after a week closes, so a prior week pulled last Monday and a
   current week pulled today are not comparable. State this in the
   pacing section.
2. **Pick sponsored-only or all-in for the headline, once, and hold it.**
   If DSP is material, all-in (sponsored + DSP) is almost always right —
   a sponsored-only headline next to a channel table that includes DSP
   will contradict itself. Never print a "full-funnel" total that is
   headline-plus-DSP on top of an already-all-in headline; that
   double-counts DSP.
3. **Marginal return only where spend actually increased.** A line that
   cut spend and grew retail has no position on that axis by definition.
   A marginal-return figure built on a small dollar change produces a
   wild, meaningless ratio — flag it as noise in the same sentence, never
   present it as a finding.
4. **Roll retail up from the per-product pull, not an ad-only or
   category endpoint.** The latter returns ad spend and ad sales, not
   total retail, and mixing the two produces a scorecard that does not
   tie.
5. **DSP is its own channel.** Never fold it into the sponsored subtotal,
   and never allocate it across product lines unless the account can
   actually attribute DSP campaigns to a line by name.
6. **Never state a number that is not in the data, and never invent a
   section to fill a gap.** A section with nothing behind it this week
   self-hides — no placeholder, no apology paragraph.
7. **Read inventory as days of cover, not raw units.** Rising on-hand
   units do not mean the risk is over if sell-through rose faster.
8. **Never name a platform other than TrackIQ or Amazon.** No vendor,
   tool, or data-provider name anywhere in the report.
9. **Every aggregate must survive the detail beneath it**, and every
   number in prose must match a cell in a table somewhere in the report.
   Run the tie-outs in `assets/build.md` before sending, not after.
10. **12px minimum for anything that reads as a sentence**, no emoji, and
    under 100KB with absolute `https://` logo URLs before sending.

## Version

`trackiq-amazon-weekly-executive-report` v1.0.0 (2026-09-16).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-weekly-executive-report`, and if it is newer, give them the
download link and the one-line changelog. Do not fetch at any other time.
