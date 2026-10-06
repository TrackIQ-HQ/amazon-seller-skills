---
name: trackiq-amazon-daily-snacks-email
description: Build TrackIQ Snacks — a short, editorial daily email for an Amazon seller account, written like a newsletter rather than a report. One lead story with a takeaway, quick bites, a scoreboard, charts, product-line rankings, rank/BSR, a business-insight snack fact, and a to-do list. Use when asked for TrackIQ Snacks, a snack email, a fun/reader-friendly daily update, a daily digest with personality, a newsletter-style version of the daily check-up, or a daily Amazon
  advertising email for a brand.
---

# TrackIQ: Amazon Daily Snacks Email

An internal daily email. Same Heritage Sage palette as the formal daily
check-up, opposite posture: this one argues a point. It is read start to
finish in three minutes by someone who will act on it today.

Self-contained `.html`: table-based, inline styles, 600px wrapper,
system-font stack, one media query at 620px.

## Requires

- The TrackIQ MCP, for `get_account_overview`, `get_campaigns`,
  `get_product_performance` and `get_bsr`. Ask which brand and marketplace
  before pulling anything.
- Nothing else. No filesystem, no shell, no internet.
- **Without the MCP:** ask the user to paste yesterday's spend, sales,
  orders, ACOS and rank figures, then build the email from those. Every
  number that is missing is simply omitted — see non-negotiable 3.

## First run

Before the first send, ask these five and fill in a copy of
`assets/account.example.md` saved as account.md beside the skill. Every
later run reads it and asks nothing, and every other TrackIQ skill reads
the same file.

1. **Brand name** as it should appear in the eyebrow, and the account
   name for the footer line
2. **Marketplace** — US, UK, DE, and so on
3. **Hero ASINs** — the three to five products that get shelf cards
4. **Product lines** — how ASINs group for the ranked section, since no
   API knows your groupings
5. **Send day convention** — which weekday the settled day usually falls
   on for this account
6. **Delivery** — in-chat, file, Slack, n8n or email, and the target for
   whichever is chosen

If the runtime has no filesystem — Claude web, ChatGPT — print the same
five answers as a short block and tell the user to paste it into their
project instructions once. Same effect, different storage.

Re-run this only when the user says the account changed. Never re-ask
mid-send.

## Read first

- `assets/voice.md` — how it is written. Read this before writing a word.
- `assets/structure.md` — the section order and what each one is for
- `assets/charts.md` — how to build bars that render correctly in email
- `assets/tokens.md` — palette, type scale, geometry, as inline hex
- `assets/build.md` — the per-send checklist
- `assets/account.example.md` — the first-run answers, filled in once
- `assets/trackiq-logo-white.png` — the masthead lockup
- `assets/trackiq-bug-white.png` — the footer bug

Copy `assets/template.html` and replace its content. Do not rebuild the
shell.

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

1. **Never name a platform other than TrackIQ or Amazon.** No vendor,
   tool, or data-provider names appear anywhere — not in copy, not in a
   caveat, not in a footnote. When a source is unavailable, the email says
   "not verified this run" and stops there. Amazon's own surfaces
   (Sponsored Products, Sponsored Brands, DSP, Buy Box, Amazon's Choice,
   FBA, BSR, ASIN, new-to-brand) are permitted — that is the marketplace
   being reported on. TrackIQ is the only platform in view.
2. **Every aggregate must survive the detail printed beneath it.** A
   summary tile saying "4 of 5 hold #1" above cards showing a #2 is the
   single most embarrassing failure this format has. Count from the cards.
3. **Never invent a data point to fill a chart slot.** A line with no
   incremental spend has no position on a per-incremental-dollar axis —
   leave it off and say why in the caption.
4. **12px minimum for anything that reads as a sentence.** 10px only for
   UPPERCASE letterspaced eyebrows.
5. **No emoji.** The reference format uses them; TrackIQ does not. Color
   rails, numerals, and type weight do the wayfinding.
6. **Nothing is said twice.** Every chart caption, quick bite, and bullet
   must carry a number that appears nowhere else in the email.
7. **Internal email.** No unsubscribe, no preferences link, no postal
   address.
8. **Under 100KB.** Absolute `https://` logo URLs before sending.

## Relationship to the daily check-up

Snacks is not a summary of the formal daily — it is a different edit of the
same data, and it must be self-sufficient. Every number a reader needs to
act is in Snacks. What Snacks omits is per-campaign detail: the specific
campaign names to pause, the full DSP table, the 28-day view. When both
ship, Snacks makes the argument and the check-up carries the evidence.

## Version

`trackiq-amazon-daily-snacks-email` v1.1.1 (2026-09-17).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-daily-snacks-email`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
