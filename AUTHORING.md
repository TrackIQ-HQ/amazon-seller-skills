# The TrackIQ Skill Standard

Every skill we publish follows these rules. They exist so one skill file
runs unchanged in Claude, ChatGPT, Codex and anything else that reads the
Agent Skills format — and so a user who installed it in March still gets
value from it in December.

---

## 1. One canonical format, no vendor forks

A skill is a folder:

```
trackiq-snacks-email/
├── SKILL.md          required — instructions + YAML frontmatter
├── skill.json        TrackIQ metadata (version, requires). Agents ignore it.
└── assets/           templates, references, logos, scripts
```

Frontmatter carries **`name` and `description` only.**

```yaml
---
name: trackiq-snacks-email
description: Build TrackIQ Snacks — a short editorial daily email for an
  Amazon seller account… Use when asked for TrackIQ Snacks, a snack email,
  or a newsletter-style daily update.
---
```

Other keys (`version`, `license`, `allowed-tools`, `metadata`) are
supported unevenly across platforms and a stricter validator will reject
the whole upload. Version lives in `skill.json` and in a one-line footer in
the body. Nothing else goes in frontmatter.

## 2. The description is the product

It is the only part of the skill that is always in context. It has one job:
make the agent load the skill at the right moment and not at any other.

Write it third person, and cover both halves — **what it does** and **when
to use it** — including the words a user would actually type. Max 1024
characters; use 300–600.

```
✗  description: Helps with daily Amazon reporting.
✓  description: Builds a one-page daily Amazon advertising check-up email
   from TrackIQ MCP data — spend, sales, ACOS, rank movement and a
   prioritized to-do list. Use when the user asks for a daily check-up,
   morning report, "how did we do yesterday", or a daily email for a brand.
```

## 3. Name it once, never rename it

The `name` is the skill's identity across every install. Renaming it does
not update anyone — it creates a second skill sitting next to the stale
one. Pick the name at publish time and treat it as permanent.

Rules: lowercase, numbers and hyphens, ≤64 chars, and it may **not** contain
"claude" or "anthropic" — Anthropic's validator rejects those outright. Ours
are all prefixed `trackiq-`, which doubles as shelf space in a user's skill
list.

## 4. Assume nothing about the runtime

A skill that only works in Claude Code is half a product. Before shipping,
assume the runtime has **no filesystem, no shell, no internet, and no MCP
connected** and check that the skill still does something useful.

- **Scripts are an accelerant, never a dependency.** If `scripts/build.py`
  can't run, the instructions must still describe the work. Say "run
  `scripts/x.py`" *and* keep the method in prose.
- **Name tools defensively.** "Pull the last 14 days with the TrackIQ MCP
  `get_account_overview` tool. If it isn't connected, ask the user to paste
  the same figures and continue."
- **Forward slashes in every path.** Always `assets/voice.md`.
- **No absolute local paths**, no `~/Documents`, no container paths.

## 5. Progressive disclosure, one level deep

`SKILL.md` stays under 500 lines — ideally under 150. Everything else goes
in `assets/` and gets linked **from SKILL.md directly**. Never a chain
(SKILL.md → structure.md → tokens.md); agents read the first hop and stop.

Bundled files cost zero tokens until read. A 70KB template costs nothing to
ship and everything to inline.

## 6. Non-negotiables get numbered

The body's job is not to explain the domain — the model already knows
Amazon advertising. Its job is to encode the things it would otherwise get
wrong: our voice, our palette, the aggregate that must match the detail
below it, the vendor names that never appear. Write those as a numbered
list of hard rules, not paragraphs of context.

Cut anything that a competent analyst would do anyway.

## 7. Every skill declares what it needs

Top of the body, four lines max:

```markdown
## Requires
- TrackIQ MCP connected (`get_account_overview`, `get_campaigns`)
- Nothing else. No filesystem or internet needed.
- Without the MCP: works from figures the user pastes in.
```

This is the single biggest driver of "it didn't work for me" support
tickets. Users install a skill and never learn it needed a connector.

## 8. Ship an update path inside the skill

Zip-installed skills cannot auto-update. So the skill tells the agent how to
check. Every SKILL.md ends with:

```markdown
## Version

trackiq-snacks-email v1.2.0 (2026-09-16).
If the user asks whether this skill is current, fetch
https://trackiq.com/skills/registry.json, compare the `version` field for
`trackiq-snacks-email`, and if it is newer give them the download link and
the one-line changelog. Do not fetch at any other time.
```

Cheap, self-contained, and it turns every install into something that can
tell its owner it went stale. Git-based installs (the plugin marketplace)
update on their own and ignore this.

## 9. Semantic versions, and a changelog line users can read

`MAJOR.MINOR.PATCH` in `skill.json`.

- **PATCH** — wording, a fixed typo, a tightened rule
- **MINOR** — a new section, a new asset, a new capability
- **MAJOR** — the output changes shape, or a new requirement appears

The changelog entry is one sentence in plain language, aimed at the seller
who installed it, not at us: "Adds week-over-week rank deltas to the
scoreboard." That sentence ships on the website and in the update check.

## 10. Test it cold, three times

Before publish, in a fresh session with no other context:

1. **Trigger test** — say what a user would say. Does it load unprompted?
2. **Bare test** — run it with the MCP disconnected. Does it degrade or
   flail?
3. **Cross-platform test** — upload the same zip to ChatGPT and run it. Any
   instruction that assumed Claude's tooling will fail loudly here.

A skill that passes those three is worth putting a version number on.

---

## The maintainer loop

```
edit skills/ → python scripts/validate.py → bump skill.json →
python scripts/build.py → commit → tag → CI publishes zips + registry.json
```

Git users get the update automatically. Zip users get told about it the
next time they ask.
