---
name: trackiq-amazon-competitor-teardown
description: Puts one Amazon product page side by side with the three or four beating it on the shelf — title structure, image count, bullet construction, price and price per unit, coupons, rating and review depth, and rank — then says what to change and in what order. Compares content, not slots. Use when the user asks how we compare to competitors, a competitor teardown, competitive analysis, why competitors outrank us, what competitors do better, or a listing comparison.
---

# Competitor Listing Teardown

`trackiq-share-of-shelf` counts **slots**. This compares **content**.

**How does our page compare to the ones beating us, and what do we change
first?**

Output is a branded HTML report: a comparison grid, then a ranked list of gaps.

## Requires

- **The Oxylabs scraper**, for `get_product` and `get_reviews`.
- The TrackIQ MCP, for `list_marketplaces` and `get_product_performance` — to
  know which of our ASINs is worth the comparison.
- **A competitor set** — three to five ASINs. Ask, or take them from
  `trackiq-share-of-shelf`, which already identifies who holds page one.
- Nothing else. No filesystem, no shell.
- **Without Oxylabs:** cannot see any page. Do not guess at a competitor's
  listing from memory.

## First run

Fill in a copy of `assets/account.example.md` saved as account.md beside the
skill. Every TrackIQ skill reads the same file, so an account already set up
for another TrackIQ report needs nothing added here.

If the runtime has no filesystem, print the same block and ask the user to
paste it into their project instructions once.

## Read first

- `assets/fields.md` — what can and cannot be compared, and the two fields that
  lie
- `assets/method.md` — the comparison grid and how gaps are ranked
- `assets/checks.md` — what to verify before anything is sent

Copy `assets/report-template.html` and replace every `{{TOKEN}}`.

## Non-negotiables

1. **A+ content and video cannot be detected.** There is no A+ flag and no video
   flag in the scrape. The A+ *text* leaks into the `description` field, which
   is a hint and not a check. **Any row about A+ modules or video must be marked
   "by eye" and actually looked at**, or left out. Never report a gap that was
   never measured.
2. **`description` is not the description.** It is a concatenation of the
   description, A+ comparison-table labels and brand-story copy, with no marker
   between them. Comparing its length across competitors compares noise.
   Say what it contains; do not diff it.
3. **`bullet_points` is one newline-joined string.** Split on newline to count.
   More than five means some are invisible on the detail page — a real finding on
   either side of the comparison.
4. **Compare price per unit, not price.** `_oxylabs_bonus.price_per_unit` is
   returned and is what a shopper comparing a 30-count to a 50-count actually
   sees. A raw price comparison across different pack sizes is meaningless.
5. **Filter `buybox_raw`.** It contains rows with `price: -1` — these are
   subscribe-and-save delivery frequencies, not offers. Including them produces
   nonsense price ranges.
6. **Review depth beats rating.** A 4.6 on 2,816 reviews outranks a 4.8 on 40 in
   every way that matters. Compare `reviews_count` and the one-star share, not
   the headline star.
7. **Rank the gaps by what is cheap and what matters**, not by how many there
   are. A teardown listing nineteen differences gets none of them fixed.
8. **Never name a competitor brand in proposed copy.** Comparative claims on
   Amazon are a policy risk. The gaps inform the copy; the copy does not mention
   them.
9. **This is one brand's page against its rivals.** No portfolio views, no
   multi-client comparisons.
10. **Never print `account_id`.**

## What it pairs with

`trackiq-share-of-shelf` finds who to tear down. `trackiq-listing-optimizer`
writes the fix this skill specifies. `trackiq-review-miner` says what buyers say
about the same set of products — content and sentiment are different questions
and the answers often disagree.

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

`trackiq-amazon-competitor-teardown` v1.0.1 (2026-10-06).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-amazon-competitor-teardown`, and if it is newer, give them the download link
and the one-line changelog. Do not fetch at any other time.
