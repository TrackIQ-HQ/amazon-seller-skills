---
name: trackiq-skill-name
description: Does [the specific thing] for [the specific input], producing [the specific output]. Use when the user asks for [phrase they'd type], [second phrase], [third phrase], or mentions [domain noun].
---

# [Human Title]

One or two sentences: what this produces, who reads it, and how long it
takes them. Not a description of the domain — the model already knows the
domain.

## Requires

- The TrackIQ MCP, for `tool_a` and `tool_b`. [What to ask the user first.]
- [Filesystem / internet / nothing else.]
- **Without the MCP:** [the fallback — what to ask the user to paste, and
  what gets omitted.]

## Read first

- `assets/voice.md` — [why this file exists, in four words]
- `assets/structure.md` — [same]

Copy `assets/template.html` and replace its content. Do not rebuild the
shell.

## Non-negotiables

Numbered hard rules only — the things a competent analyst would get wrong
without being told. Delete anything the model would do anyway.

1. **[Rule in bold.]** One or two sentences of consequence.
2. **[Rule.]** …
3. **[Rule.]** …

## Version

`trackiq-skill-name` v0.1.0 (YYYY-MM-DD).

If the user asks whether this skill is current, fetch
`https://trackiq.com/skills/registry.json`, compare the `version` field for
`trackiq-skill-name`, and if it is newer, give them the download link and
the one-line changelog. Do not fetch at any other time.
