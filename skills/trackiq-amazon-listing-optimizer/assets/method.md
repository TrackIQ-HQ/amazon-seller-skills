# Method

## 1. Where the terms come from

Three sources, in priority order. **A term goes in the copy only if it comes
from one of them**, and the source is shown beside it.

| Source | What it proves | Tool |
|---|---|---|
| **Converts already** | real demand, real match | `get_search_terms` — orders > 0 |
| **Volume and relevance** | demand the listing is not winning | `get_search_query_performance` |
| **Client's own list** | strategy, a new positioning | supplied |

Terms that convert beat terms with volume. A term that already produces orders
has proven the product matches the intent; a high-volume term has only proven
people type it.

**SQP is weekly, Sunday to Saturday, and ingestion is intermittent** — missing
weeks inside a month are normal. Say which weeks were present.

Rank the candidate terms by orders first, then by volume, and take the top
eight to twelve. More than that will not fit naturally in the copy, and forcing
them produces exactly the stuffed listing this skill exists to replace.

## 2. The five questions

The useful test in 2026 is not keyword density. It is whether the page answers
what a shopper would ask before buying — because that is what both a human
skimming and an assistant summarising are looking for.

1. **What is it?** — the product, plainly, in the first bullet
2. **Who is it for?** — the use case and the person
3. **What makes it different?** — the one thing competitors cannot say
4. **How is it used?** — quantity, frequency, occasion, storage
5. **What is the objection?** — the thing the negative reviews keep raising

Build the five bullets around those five questions, in that order. The search
terms ride **inside** the answers, in natural sentences. A bullet that reads as
a list of keywords answers nothing and now ranks worse for it.

## 3. The title

```
[Brand] [Primary term] [Key differentiator] [Size / count / variant]
```

Rules that survive Amazon changing its mind:

- **The brand and the primary term inside the first ~80 characters.** That is
  roughly what a phone shows before truncating, and it is where the value sits.
- **Report the character count** against a stated threshold. Limits vary by
  category and change; state the one used rather than quoting a rule.
- No ALL CAPS except an established brand mark.
- No promotional language — "sale", "free shipping", "best".
- No competitor brand names.
- Size, count or variant at the end, because that is where shoppers look for it.

Show the current title's length and the proposed one's, side by side.

## 4. The bullets

Five. Each:

- **Leads with a capitalised benefit phrase**, then a sentence that explains it.
  The lead phrase is what gets skimmed; the sentence is what gets matched.
- Under about 200 characters, so it does not truncate on mobile.
- Carries at most **two** search terms, worked into a real sentence.
- Says something the other four do not.

If the current listing has more than five bullets, say which is invisible and
which five the rewrite keeps.

## 5. The description

Written as prose that answers the five questions again in longer form, for the
reader who scrolled. Not a repeat of the bullets.

**Say what the scraped `description` field actually contained** before proposing
a replacement — it is a concatenation of the description, A+ text and brand
story (see `assets/fields.md`). If the user needs the true description field,
ask them to paste it from Seller Central.

## 6. Backend search terms

250 bytes, no commas needed, no repetition of anything already in the title or
bullets — repeating wastes the allowance.

**There is no way to read the current backend terms.** Not in the scrape, not in
the MCP. So the proposal is a **recommendation the user must reconcile against
what is already there**. Say that on the page, beside the list, every time.

Good candidates: misspellings, synonyms, Spanish equivalents for US listings,
use-case phrases, and terms that convert but do not fit the visible copy.

## 7. Objections, from reviews

The negative reviews name what the page failed to say. A complaint that the
product "sticks to teeth" is an objection the bullets can pre-empt honestly —
not by denying it, but by setting the expectation.

`get_reviews` returns about **eight** reviews and they skew positive (see
`assets/fields.md`). Treat them as a prompt for what to look into, never as a
survey. Use `rating_stars_distribution` for the quantitative picture and
`trackiq-review-miner` when a real corpus is needed.

## 8. Compliance pass — run it last, on the proposed copy

Flag and remove:

- health or medical claims ("treats", "cures", "prevents", "heals")
- superlatives needing substantiation ("#1", "best", "clinically proven")
- competitor brand names
- promotional language in the title
- anything about shipping, price or guarantees
- **any factual claim not present in the current listing or confirmed by the
  user** — inventing a size, material or ingredient is what gets a listing
  suppressed

Also flag risky claims **already in the current copy**. That is often the most
valuable finding in the document and nobody was looking for it.

## What this skill does not do

- **No A+ or video audit.** Neither is visible to the tools. Say so.
- **No backend term reading.** Only proposing.
- **No publishing.** A human reviews and uploads.
- **No image work.** It counts images; it does not judge them.
