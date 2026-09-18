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
/plugin install trackiq-amazon-rank-readiness@trackiq
/plugin install trackiq-amazon-share-of-shelf@trackiq
/plugin install trackiq-amazon-listing-monitor@trackiq
```

Installed this way, skills update themselves. Run
`/plugin marketplace update` to force a check.

Not on Claude Code? Each skill ships a `.zip` for manual upload to Claude
web, Claude desktop or ChatGPT — see the skill's own README.

## The catalog

Twenty-five skills across five areas. Each lives in its own repository and
is referenced here by github source.

### Amazon Advertising

*Where the ad money goes, and what it buys.*

| Skill | What it does | Needs |
|---|---|---|
| [**AMC Media Mix**](https://github.com/TrackIQ-HQ/trackiq-amazon-amc-media-mix) | A twelve-slide Amazon Marketing Cloud deck arguing one case — where the budget goes versus where new customers come from | MCP |
| [**Budget Pacing and Month-End Forecast**](https://github.com/TrackIQ-HQ/trackiq-amazon-budget-pacing) | Builds a mid-month Amazon advertising pacing report — month-to-date spend against the plan, a day-weighted projection to month end, the gap in… | MCP |
| [**DSP Audience and Creative Performance**](https://github.com/TrackIQ-HQ/trackiq-amazon-dsp-performance) | Breaks Amazon DSP down by audience, creative, inventory source, technology and geography to show which segments actually recruit customers and… | MCP |
| [**Search-Term Harvester**](https://github.com/TrackIQ-HQ/trackiq-amazon-search-term-harvester) | Finds the Amazon search terms that already convert above break-even but have no keyword of their own, and turns them into an upload-ready… | MCP |
| [**Wasted-Spend Sweeper**](https://github.com/TrackIQ-HQ/trackiq-amazon-wasted-spend) | Finds Amazon advertising spend that is not paying for itself — keywords that spent and sold nothing, keywords bidding above what they return, the… | MCP |

### Amazon Search & SEO

*Which terms to track, where you rank, and what the gap is worth.*

| Skill | What it does | Needs |
|---|---|---|
| [**Category Priority Keywords**](https://github.com/TrackIQ-HQ/trackiq-amazon-category-priority-keywords) | Groups an Amazon catalogue into product categories, then picks the 25 search terms per category worth tracking organic rank on — each with weekly… | MCP |
| [**Organic Rank Movement Tracker**](https://github.com/TrackIQ-HQ/trackiq-amazon-rank-movement) | Tracks weekly organic rank movement across a brand's priority keyword set by sampling live search results, compares it to the previous run, and… | MCP **+ scraper** |
| [**Rank Readiness**](https://github.com/TrackIQ-HQ/trackiq-amazon-rank-readiness) | Decides which search terms deserve advertising spend or seeding on a single ASIN, by testing whether a bought organic rank would survive the money… | MCP |
| [**Search Visibility Audit**](https://github.com/TrackIQ-HQ/trackiq-amazon-search-visibility-audit) | Audits where an Amazon brand's ASINs actually appear in search — organic rank per revenue-bearing query, the terms bought but not ranked, the… | MCP |
| [**Share of Shelf**](https://github.com/TrackIQ-HQ/trackiq-amazon-share-of-shelf) | Measures how much of Amazon page one a brand owns for the keywords that carry its revenue — organic slots, sponsored slots and Amazon's Choice… | MCP **+ scraper** |

### Amazon Listing Management & Optimization

*Keeping listings intact, compliant and converting.*

| Skill | What it does | Needs |
|---|---|---|
| [**Catalog and Variation Hygiene Audit**](https://github.com/TrackIQ-HQ/trackiq-amazon-catalog-hygiene) | Sweeps a whole Amazon catalogue for the quiet defects nobody owns — thin image sets, truncating or short titles, bullet counts above or below what… | MCP **+ scraper** |
| [**Competitor Listing Teardown**](https://github.com/TrackIQ-HQ/trackiq-amazon-competitor-teardown) | Puts one Amazon product page side by side with the three or four beating it on the shelf — title structure, image count, bullet construction,… | MCP **+ scraper** |
| [**Listing Monitor**](https://github.com/TrackIQ-HQ/trackiq-amazon-listing-monitor) | Watches a brand's listings daily and alerts only when something actually moved — a rewritten title or bullet, a lost image, a missing A+… | MCP **+ scraper** |
| [**Listing Optimizer**](https://github.com/TrackIQ-HQ/trackiq-amazon-listing-optimizer) | Rewrites one Amazon listing — title, bullets, description and backend terms — against the terms it should rank for and the questions shoppers… | MCP **+ scraper** |
| [**Review and Voice-of-Customer Miner**](https://github.com/TrackIQ-HQ/trackiq-amazon-review-miner) | Builds a voice-of-customer picture for a brand by sampling reviews across its own catalogue and its competitors, clustering what buyers praise and… | MCP **+ scraper** |

### Amazon Inventory

*Cover, replenishment and the cost of running out.*

| Skill | What it does | Needs |
|---|---|---|
| [**Demand Forecast and Reorder Plan**](https://github.com/TrackIQ-HQ/trackiq-amazon-demand-forecast) | Turns trailing sales and last year's seasonal shape into a week-by-week demand forecast per Amazon product, then converts it into order quantities… | MCP |
| [**Excess and Aged Inventory Plan**](https://github.com/TrackIQ-HQ/trackiq-amazon-excess-inventory) | Finds the Amazon inventory sitting too long — products with cover far beyond target, stock stranded on SKUs that no longer sell, and unfulfillable… | MCP |
| [**Inventory Risk → Ad Spend Throttle**](https://github.com/TrackIQ-HQ/trackiq-amazon-inventory-ad-throttle) | Finds the Amazon campaigns still paying to advertise products that are about to run out of stock, and produces an upload-ready bulk file that… | MCP |
| [**Restock Priority**](https://github.com/TrackIQ-HQ/trackiq-amazon-restock-priority) | Works out which Amazon products to ship next and in what order — days of cover at the current sales rate, the date each one runs out, the date a… | MCP |
| [**Stockout Impact and Recovery**](https://github.com/TrackIQ-HQ/trackiq-amazon-stockout-impact) | Measures what a completed Amazon stockout actually cost — lost units and revenue against the pre-stockout run rate, how far sessions and… | MCP **+ scraper** |

### Amazon Management & Operations

*The reporting cadence a team actually runs on.*

| Skill | What it does | Needs |
|---|---|---|
| [**Daily Snacks Email**](https://github.com/TrackIQ-HQ/trackiq-amazon-daily-snacks-email) | A three-minute editorial daily email for an Amazon account — one lead story with a takeaway, quick bites, a scoreboard, charts and a to-do list | MCP |
| [**Launch Scorecard**](https://github.com/TrackIQ-HQ/trackiq-amazon-launch-scorecard) | Grades a newly launched Amazon ASIN week by week through its first twelve weeks — units and revenue against a target curve, session growth,… | MCP **+ scraper** |
| [**Monthly Business Review**](https://github.com/TrackIQ-HQ/trackiq-amazon-monthly-business-review) | Builds the month-end client deck for one Amazon brand — revenue and spend against the previous month and the same month last year, the organic and… | MCP |
| [**Sales Movers and Root Cause**](https://github.com/TrackIQ-HQ/trackiq-amazon-sales-movers) | Ranks an Amazon catalogue by how much each product's revenue moved between two periods and decomposes every mover into its cause — traffic,… | MCP |
| [**Weekly Executive Report**](https://github.com/TrackIQ-HQ/trackiq-amazon-weekly-executive-report) | A client-ready week-over-week Amazon recap — scorecard, pacing against the brand's own trailing four-week average, per-line marginal return, DSP… | MCP |

Every skill degrades gracefully: with no connector attached, it asks you to
paste the figures and builds from those. The exceptions are the skills marked **+ scraper** above, which need a
scraper connection to observe the public page and say so rather than
approximating it.

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
