# TrackIQ Heritage Sage — email-safe token set (Snacks)

Email clients strip external CSS. Every value below must be written as an
inline hex literal. Never emit a var(), class, or stylesheet reference.

## Palette

| Role | Hex | Where it goes |
|---|---|---|
| Primary sage | `#17533F` | brand bar, One Thing panel, Focus panel, section titles, 3px section rules, positive KPI values |
| Sage hover/deep | `#123F31` | reserved; not used in email |
| Olive | `#778867` | mid-tier bars in the daily-retail chart |
| Mocha | `#8A6A4F` | section eyebrows, footer wordmark accent, "drifted" deltas, unavailable-data headlines |
| Sand | `#C4A574` | brand-bar accent, latest-settled-day bar, organic half of the revenue-source bar |
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

## Type

Stack: `-apple-system,'Segoe UI',Arial,sans-serif` — resolves to SF Pro on
Apple Mail, Segoe UI in Outlook, Arial everywhere else. No webfont: Inter
cannot be relied on in email, and @import is stripped.

| Element | Size / line-height / weight | Tracking |
|---|---|---|
| Section title | 27 / 32 / 700 | -0.9px |
| Section numeral | 44 / 32 / 700 | -2px |
| Email title | 26 / 31 / 700 | -0.6px |
| One Thing statement | 20 / 27 / 600 | -0.3px |
| Big KPI | 32 / 36 / 700 | -1px |
| Strip KPI | 21 / 25 / 700 | -0.5px |
| Card headline | 15 / 21 / 700 | -0.2px |
| Body copy | 13 / 20 / 400 | — |
| Table value | 12 / — / 400-700 | — |
| Sub-label sentence | 12 / 18 / 400 | — |
| Eyebrow (UPPERCASE) | 10-11 / 14 / 700 | 1.2-1.8px |

**12px is the floor for anything that reads as a sentence.** 10px is legal
only for UPPERCASE letterspaced eyebrows. This rule exists because it was
the single most repeated review note on this design.

## Geometry

Wrapper 600px. Inner content width 544px (600 − 2×28px pad).
Radius: 14px wrapper, 12px cards/tables, 10px action cards and callouts.
Shadow: `0 8px 24px rgba(31,36,32,0.06)` — the only shadow in the email.
Section rule: 3px solid `#17533F`. Card gap: 10px. Section gap: 22px.

## Snacks-specific type

Snacks runs larger than the daily check-up, because it is prose.

| Element | Size / line-height / weight | Tracking |
|---|---|---|
| Lead headline | 31 / 36 / 700 | -1.1px |
| Section title | 24 / 29 / 700 | -0.7px |
| Snack-fact hero | 30 / 34 / 700 | -0.9px |
| Takeaway body | 17 / 26 / 400 | — |
| Body copy | 15 / 24 / 400 | — |
| Card headline | 15-17 / 21-23 / 700 | -0.3px |
| Card body | 14 / 21-22 / 400 | — |
| Chart label / value | 13 / — / 600-700 | — |

Mobile: `.huge` 34px, `.hed` 27px, `.third` stacks full width.

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
