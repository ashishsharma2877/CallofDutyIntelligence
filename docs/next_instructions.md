We are continuing the CallofDutyIntelligence project.

Milestone 1 created:
- a validated official Call of Duty patch/update temporal spine
- a complete patch-note corpus
- deterministic corpus-analysis tooling
- analytical inventories of concepts found in patch notes

We have deliberately NOT created a knowledge graph or finalized an ontology.

The broader goal is now to derive an ontology from MULTIPLE independent
official Call of Duty corpora rather than allowing patch notes alone to
define the game world.

MILESTONE 2A — OFFICIAL GAMEPLAY GUIDES CORPUS

Do NOT analyze the guide corpus yet.
Do NOT merge guide concepts with patch-note concepts.
Do NOT modify cod_change_history.csv.
Do NOT modify the existing patch corpus.
Do NOT create an ontology.
Do NOT build a graph.
Do NOT use an LLM or external AI API.

Our task is ONLY to discover, inventory, download, and validate the official
Call of Duty gameplay-guide corpus.

--------------------------------------------------
1. REPOSITORY ORGANIZATION
--------------------------------------------------

First inspect the existing repository.

Refactor directory organization only where necessary to cleanly support
multiple independent corpora.

The conceptual organization should be something like:

data/
  raw/
    patch_pages/
    guide_pages/

  processed/
    cod_change_history.csv
    guide_index.csv

  analysis/
    patches/
    guides/

docs/
  analysis/
    patches/
    guides/

Do NOT blindly move files if doing so will break existing scripts.

If existing paths differ, update scripts/references carefully and verify that
the existing patch ingestion and patch analysis still work after any refactor.

Preserve all existing work.

--------------------------------------------------
2. OFFICIAL GUIDE DISCOVERY
--------------------------------------------------

Discover official Call of Duty guide pages using ONLY official
callofduty.com sources.

Start from:

https://www.callofduty.com/guides

Also inspect:

- official guide hub pages
- internal guide navigation
- official sitemap(s)
- links between official guide pages

Relevant game families currently include at least:

- Modern Warfare III
- Black Ops 6
- Black Ops 7
- Modern Warfare 4
- Warzone

But do NOT assume that is the complete set.

Discover what the official site actually exposes.

We are interested in GAMEPLAY KNOWLEDGE, not every page containing the word
"guide".

Potentially relevant material includes:

- getting started / COD 101
- multiplayer
- Warzone
- Zombies
- Campaign
- maps
- modes
- weapons/loadouts
- movement
- progression
- Operators
- equipment
- perks
- streaks
- vehicles
- contracts
- loot/economy
- controls/settings
- social/squads
- other player-facing gameplay systems

Do not impose this taxonomy during discovery.

--------------------------------------------------
3. DISCOVERY INVENTORY
--------------------------------------------------

Before deciding which pages belong in the corpus, create an inventory of ALL
candidate official guide URLs discovered.

For every candidate capture where deterministically available:

url
page_title
discovery_source
hub_or_title_family
language_or_locale
http_status
canonical_url
content_type_guess
include_candidate
exclusion_reason

"content_type_guess" is discovery metadata only and must NOT become ontology.

Potential exclusions include:

- localization duplicates
- navigation-only pages
- unrelated marketing pages
- patch notes
- news/blog articles
- legal/privacy pages
- duplicate canonical URLs
- pages outside gameplay knowledge

Do not silently discard candidates.

Every discovered candidate should either be included or have an explicit
reason for exclusion.

--------------------------------------------------
4. DOWNLOAD RAW CORPUS
--------------------------------------------------

Download included official guide pages into:

data/raw/guide_pages/

Preserve the original HTML.

Use:
- reasonable request pacing
- descriptive User-Agent
- retries for transient failures
- logging

Do not bypass access controls, bot protections, authentication, or rate
limits.

Raw HTML remains ignored by Git.

--------------------------------------------------
5. GUIDE INDEX
--------------------------------------------------

Create:

data/processed/guide_index.csv

One row per canonical included guide page.

Initial columns:

guide_id
url
canonical_url
page_title
title_family
experience_if_explicit
guide_category_if_explicit
publication_or_update_date_if_explicit
discovery_source
source_file
retrieved_at

IMPORTANT:

Only populate title_family, experience, category, or dates when explicitly
supported by the source.

Leave unknown values null.

Do not infer ontology classifications.

--------------------------------------------------
6. VALIDATION
--------------------------------------------------

Validate the corpus before any analysis.

Report:

- total candidate URLs discovered
- included canonical guide pages
- excluded pages
- duplicate/canonicalized pages
- pages downloaded successfully
- failed downloads
- breakdown by title family where explicitly identifiable
- breakdown by explicit guide category if available
- pages with missing titles
- pages with questionable classification
- sitemap-only pages
- hub/navigation-only discoveries
- any inaccessible pages

Manually validate at least 20 diverse included pages against their raw HTML.

The validation sample should deliberately cover as many different areas as
available, such as:

- different titles
- Warzone
- Multiplayer
- Zombies
- Campaign
- training/getting started
- maps
- modes
- weapons/loadouts
- progression
- other unusual guide types

--------------------------------------------------
7. DISCOVERY COMPLETENESS
--------------------------------------------------

Assess whether we have a reasonably complete official gameplay-guide corpus.

Compare:

- guide hub discovery
- sitemap discovery
- internal-link discovery

Identify URLs found by one method but missed by others.

Rate:

A. Discovery completeness
B. Download completeness
C. Metadata accuracy
D. Suitability of the collected pages as an official gameplay-guide corpus

Use:

HIGH CONFIDENCE
MEDIUM CONFIDENCE
LOW CONFIDENCE

Explain each rating.

--------------------------------------------------
8. OUTPUTS
--------------------------------------------------

Create:

data/processed/guide_index.csv

and:

docs/validation/guides-corpus-validation.md

Update README.md only as necessary to document the new ingestion capability.

Add ingestion code under the existing source organization in a way consistent
with the project.

Do NOT create guide corpus-analysis outputs yet.

--------------------------------------------------
9. FINAL REPORT AND STOP
--------------------------------------------------

At completion report:

- candidate URLs discovered
- pages included
- pages excluded
- pages successfully downloaded
- title-family breakdown
- explicit category breakdown
- earliest/latest explicit dates if meaningful
- questionable records
- validation results
- confidence ratings

Show 20 representative rows from guide_index.csv.

Then STOP.

Do NOT:
- analyze guide vocabulary
- extract entities
- compare guides with patch notes
- modify the patch ontology analysis
- design ontology
- build Neo4j
- create synthetic players
- create telemetry
- use GenAI for extraction
- commit or push