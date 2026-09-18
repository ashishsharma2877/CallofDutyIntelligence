# Call of Duty Intelligence

An experimental platform for exploring how knowledge graphs, analytics,
machine learning, and generative AI can connect game development decisions
to player experiences and outcomes.

## Core Idea

The project models a closed intelligence loop:

Ideation
→ Development
→ Content
→ Release
→ Player Experience
→ Telemetry
→ Insight
→ Decision
→ Next Release

Rather than centralizing all underlying data, the goal is to create a
connected intelligence layer across the entities and relationships that
matter.

## Phase 1: Content Calendar

Build a historical dataset of Call of Duty releases and changes using
publicly available sources.

The initial dataset will cover approximately two years and include:

- Major title releases
- Seasons
- Reloaded / mid-season releases
- Patches and hotfixes
- Maps
- Modes
- Weapons
- Events
- Gameplay and balance changes
- Other significant content changes

Every extracted fact should retain provenance to its original source.

### Official Patch-Note Ingestion

The first Phase 1 asset is a deterministic ledger of individually dated
updates from official Call of Duty patch-note pages. It covers pages from
2024-09-01 through the day the command is run. The official sitemap is the
primary discovery source and the patch-note archive is a secondary cross-check.
Raw HTML is retained in `data/raw/patch_pages/`; the one-row-per-logical-update
CSV is written to `data/processed/cod_change_history.csv`.

The CSV separates `franchise`, `title`, and `experience`. Values are left null
when the official page does not distinguish them reliably. Structured dates
record their discovery method in `date_source_type` (`heading`, `dateline`,
`anchor`, or combinations when multiple structures support the same event).
When the same dated update appears on multiple official pages, the pipeline
keeps one logical event and joins the source provenance with ` | ` in the
source fields rather than dropping either source.

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Run the ingestion from the repository root:

```bash
python src/ingest_patch_notes.py
```

The script uses the official sitemap and archive, a descriptive User-Agent,
one-second request pacing, deterministic HTML parsing, and logs discovery
cross-checks, reconciliation counts, and pages with download or extraction
problems to
`data/processed/ingestion.log`.

## Future Phases

1. Call of Duty content calendar
2. Content knowledge graph
3. Synthetic player population
4. Synthetic player telemetry
5. Player journey analytics
6. Machine-learning experiments
7. Connect player outcomes to content changes
8. Natural-language intelligence layer

## Status

Phase 1 — Content Calendar