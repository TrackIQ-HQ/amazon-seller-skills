# TrackIQ Heritage Sage — email-safe token set (Weekly Executive Report)

Same palette as every other TrackIQ send. Email clients strip external CSS,
so every value below is an inline hex literal — never a `var()`, a class,
or a stylesheet reference.

## Palette

| Role | Hex | Where it goes |
|---|---|---|
| Primary sage | `#17533F` | brand bar, decision panel, section rules, positive KPI values, best-line highlights |
| Sage hover/deep | `#123F31` | reserved; not used in email |
| Olive | `#778867` | mid-tier bars, secondary series |
| Mocha | `#8A6A4F` | section eyebrows, footer accent, "watch" callouts, unavailable-data notes |
| Sand | `#C4A574` | brand-bar accent, "this week" bars, current-period highlight |
| Pale sand | `#E6DFCE` | oversized section numerals (01/02/03) |
| Ink | `#1F2420` | headlines, table values |
| Body | `#586258` | all body/commentary copy |
| Muted | `#6E7269` | eyebrow labels, table headers, sub-labels |
| Faint | `#A8ABA3` | pending/unknown values, legal line |
| Page bg | `#F3F1EA` | body behind the card |
| Card bg | `#FDFBFA` | email wrapper |
| Surface | `#FFFFFF` | inner cards and tables |
| Soft surface | `#F7F5EF` | table header rows, muted panels |
| Border | `#EFEAE3` | all 1px borders and dividers |
| Row divider | `#F3F1EA` | table row separators |

## Status

| Role | Text | Background | Border/rail |
|---|---|---|---|
| Success | `#2F7A5A` | `#EEF7F1` | `#2F7A5A` |
| Danger | `#C65345` | `#FFF3F1` | `#C65345` |
| Warning | `#8A6A4F` text on `#FFF7E6` | `#FFF7E6` | `#D89B35` |

Warning TEXT is mocha, never `#D89B35` — gold fails contrast on pale gold.
`#D89B35` is legal only as a border or fill.

## Inventory bands

Reuse status colors for the days-of-cover table: `Healthy` = success,
`Tight` = warning, `Critical` = danger. The band boundaries come from the
account's own configured thresholds — never hardcode 21/42 days, ask for
or read the account's actual critical/tight cutoffs.

## Type

Stack: `-apple-system,'Segoe UI',Arial,sans-serif`. No webfont — it will
not survive email clients.

| Element | Size / line-height / weight | Tracking |
|---|---|---|
| Section title | 24-27 / 29-32 / 700 | -0.7 to -0.9px |
| Section numeral | 44 / 32 / 700 | -2px |
| Report title | 26 / 31 / 700 | -0.6px |
| Executive headline | 28-31 / 34-36 / 700 | -1 to -1.1px |
| Decision-panel statement | 17 / 26 / 400 | — |
| Big KPI (cover strip) | 30-32 / 34-36 / 700 | -1px |
| Lever-card metric | 24-30 / 28-34 / 700 | -0.7 to -0.9px |
| Card headline | 15-17 / 21-23 / 700 | -0.2 to -0.3px |
| Body copy | 14-15 / 21-24 / 400 | — |
| Table value | 12-13 / — / 400-700 | — |
| Sub-label sentence | 12-13 / 18-20 / 400 | — |
| Eyebrow (UPPERCASE) | 10-11 / 14 / 700 | 1.2-2px |

**12px is the floor for anything that reads as a sentence.** 10px is legal
only for UPPERCASE letterspaced eyebrows.

## Geometry

Wrapper 640px (wider than Snacks' 600px — this report carries denser
tables). Inner content width 584px (640 − 2×28px pad). Radius: 16px
wrapper, 12px cards/tables, 10px action cards. Shadow:
`0 8px 24px rgba(31,36,32,0.06)`. Section rule: 3px solid `#17533F`. Card
gap: 10px. Section gap: 24px.

Mobile: stack any two-column table at 620px, `.hed` drops to 26px, tables
with more than 4 numeric columns get `overflow-x:auto` on a wrapping
`<div>` (rare in email, acceptable degradation — state totals in prose
above the table so the number survives even if the table clips).

## Logo

Two files ship with the skill, both white, because both placements sit on
sage. The ink and sage variants live in the TrackIQ brand-standards
bundle; add one here only if a light-background placement is introduced.

| File | Where | Size |
|---|---|---|
| `assets/trackiq-logo-white.png` | masthead, on the `#17533F` bar | 140x38 |
| `assets/trackiq-bug-white.png` | footer, on the sage bar | 40x28 |

The lockup stops being legible below about 120px wide — the letterforms
inside the braces close up — so the masthead runs at 140px and anything
smaller takes the bug instead. The bug is a signature, never scaled up to
stand in for the lockup.

## Against the brand standard

These files are the email-safe subset of the TrackIQ Heritage Sage
standard. Three points differ deliberately; everything else matches.

**No webfont.** The standard specifies Inter and Inter Tight from Google
Fonts. Email clients strip `@import` and most ignore `@font-face`, so the
system stack above is used instead. This is the only typography deviation.

**Danger red splits by size.** `#C65345` is 4.31:1 on the card background
and fails AA for body copy. Use `#B84636` (5.13:1) for any red text under
18.66px; keep `#C65345` for rails, borders, fills and chart marks, where
contrast rules do not apply.

**Muted stays darker than the standard.** The standard's Muted `#8B8F86`
measures 3.20:1 on the card and fails at every size used here. Email
eyebrows run 10-12px, so this set keeps `#6E7269` (4.76:1). Do not
"correct" it upward.
