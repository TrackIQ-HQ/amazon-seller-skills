# TrackIQ Skills for Amazon Sellers

Agent Skills that turn TrackIQ data into the things you'd otherwise build
by hand — a daily email, a weekly recap, a client-ready deck. They run in
Claude and ChatGPT from the same folder.

A **skill** is a folder of instructions an AI assistant loads only when
it's relevant. A **connector** (MCP) is where the data comes from. TrackIQ
supplies both: the connector holds your account, the skills know what to do
with it.

---

## Powered by the TrackIQ MCP

[![TrackIQ MCP — connect your AI assistant to Amazon data. 16 tools, full MCP access, $69/mo. Works with Claude, ChatGPT and Cursor.](.github/trackiq-mcp-banner.png)](https://trackiq.com/mcp)

These skills read your live Amazon account through the
**[TrackIQ MCP](https://trackiq.com/mcp)** — 16 tools connecting your AI
assistant to Amazon data:

Sales & Traffic · Orders · Inventory · Returns · Sponsored Products · Sponsored
Brands · Sponsored Display · Amazon DSP · AMC Cloud · Keywords · Search Terms ·
Targeting · Search Query Performance · Organic Rank · Best Seller Rank · Buy Box
History · Brand Analytics · Export


Works with Claude, ChatGPT and Cursor. **[Get access →](https://trackiq.com/mcp)**

---

## Install everything, one command

```
/plugin marketplace add TrackIQ-HQ/amazon-seller-skills
/plugin install trackiq-amazon-daily-snacks-email@trackiq
/plugin install trackiq-amazon-weekly-executive-report@trackiq
/plugin install trackiq-amazon-category-priority-keywords@trackiq
/plugin install trackiq-amazon-amc-media-mix@trackiq
/plugin install trackiq-amazon-search-visibility-audit@trackiq
```

Installed this way, skills update themselves. Run
`/plugin marketplace update` to force a check.

Not on Claude Code? Each skill ships a `.zip` for manual upload to Claude
web, Claude desktop or ChatGPT — see the skill's own README.

## The catalog

| Skill | What you get | Needs |
|---|---|---|
| [**TrackIQ: Amazon Daily Snacks Email**](https://github.com/TrackIQ-HQ/trackiq-amazon-daily-snacks-email) | A three-minute editorial daily email — lead story, quick bites, scoreboard, charts, to-do list | TrackIQ MCP |
| [**TrackIQ: Amazon Weekly Executive Report**](https://github.com/TrackIQ-HQ/trackiq-amazon-weekly-executive-report) | A client-ready weekly recap — scorecard, pacing, marginal return by line, DSP, keyword economics, inventory cover | TrackIQ MCP |
| [**TrackIQ: Amazon Category Priority Keywords**](https://github.com/TrackIQ-HQ/trackiq-amazon-category-priority-keywords) | The 25 search terms per product category worth tracking organic rank on, priced, with a rank-tracker gap check | TrackIQ MCP + SQP |
| [**TrackIQ: Amazon AMC Media Mix**](https://github.com/TrackIQ-HQ/trackiq-amazon-amc-media-mix) | A twelve-slide media mix deck — attribution paths, what DSP is worth, cost per new customer, one reallocation | TrackIQ MCP + AMC + DSP |
| [**TrackIQ: Amazon Search Visibility Audit**](https://github.com/TrackIQ-HQ/trackiq-amazon-search-visibility-audit) | Where your ASINs appear in search — owned, doubled, bought or absent per query, plus the priced gap | TrackIQ MCP |

Every skill degrades gracefully: with no connector attached, it asks you to
paste the figures and builds from those.

Each skill lives in its own repository. This one holds only the catalog, the
authoring standard, and the template for new skills.

## Staying current

| How you installed | How you update |
|---|---|
| Plugin marketplace | Automatic. `/plugin marketplace update` forces it. |
| Uploaded `.zip` | Ask your assistant *"is my TrackIQ Snacks skill current?"* — the skill checks the registry and tells you. Then re-upload. |

Versions are semantic. A MAJOR bump means the output changed shape or the
skill needs something new connected; everything else is safe to take
blind.

## Writing a skill

Start from [`templates/skill-template/`](templates/skill-template) and read
[AUTHORING.md](AUTHORING.md) first. It is short, and every rule in it comes
from something that broke.

Adding a skill to this catalog is one entry in
[`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json)
pointing at its repository:

```json
{
  "name": "trackiq-your-skill",
  "source": { "source": "github", "repo": "TrackIQ-HQ/trackiq-your-skill" }
}
```

## License

MIT. See [LICENSE](LICENSE).
