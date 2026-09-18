# Post-Fix Validation Report

This report validates the corrected Call of Duty patch-note ingestion pipeline. No graph, detailed change extraction, synthetic data, or LLM extraction was used.

## 1. Discovery

Discovery now uses the official sitemap as the primary source and the official patch-note archive as a secondary cross-check.

| Discovery method | URLs |
|---|---:|
| Sitemap | 35 |
| Archive | 29 |
| Found by both | 27 |
| Sitemap only | 8 |
| Archive only | 2 |
| Union downloaded | 37 |

All 37 discovered pages downloaded successfully. The eight sitemap-only pages were downloaded and included. The two archive-only pages were also retained.

The eight sitemap-only pages are the previously missed official pages:

- Modern Warfare III Season 6
- Black Ops 6 Preseason
- Black Ops 6 Seasons 01 through 06

The official sitemap was read from `https://www.callofduty.com/sitemap.xml`; the archive cross-check used the official Call of Duty patch-note archive. No access controls or bot protections were bypassed.

## 2. Extraction and Schema

The CSV now contains:

```text
update_date
franchise
title
experience
season
update_title
date_source_type
source_page_title
source_url
source_file
retrieved_at
```

Deterministic extraction recognizes:

- Date-only update headings in `h1` through `h6`
- Structured `p.dateline` elements
- Fragment-link anchors such as `<a href="#nov26">November 26</a>` in update navigation
- Combined evidence when more than one structure supports the same date

No unrestricted prose-date extraction is used.

The `date_source_type` values found in the final CSV are:

| Date source type | Events |
|---|---:|
| `heading` | 77 |
| `dateline` | 4 |
| `anchor` | 73 |
| `heading;dateline` | 20 |
| `dateline;anchor` | 12 |
| `heading;anchor` | 11 |
| `heading;dateline;anchor` | 1 |

## 3. Final Ingestion Results

- Total official patch-note pages discovered: **37**
- Pages successfully downloaded: **37**
- Pages producing at least one update: **37**
- Pages producing zero updates: **0**
- Raw structured events extracted: **199**
- Unique logical update events: **198**
- Duplicate events reconciled: **1**
- Earliest event date: **2024-09-18**
- Latest event date: **2026-09-16**

The eight previously failing Black Ops 7 pages now all produce dated updates:

- Black Ops 7 Beta: 8
- Black Ops 7 Preseason: 8
- Black Ops 7 Season 01: 8
- Black Ops 7 Season 02: 10
- Black Ops 7 Season 03: 8
- Black Ops 7 Season 04: 3
- Black Ops 7 Season 05: 3
- Black Ops 7 Season 06: 1

The previously missing sitemap pages are included in the 37 downloaded pages and contribute events to the regenerated CSV.

## 4. Chronological Gaps

Gap analysis uses the 143 unique dates represented by the 198 logical events, producing 142 intervals.

- Median interval: **4 days**
- Mean interval: **5.127 days**
- Gaps greater than 14 days: **8**
- Gaps greater than 30 days: **0**

Longest gaps:

| Days | From | To |
|---:|---|---|
| 24 | 2025-10-21 | 2025-11-14 |
| 23 | 2025-12-16 | 2026-01-08 |
| 21 | 2025-08-13 | 2025-09-03 |
| 21 | 2025-07-16 | 2025-08-06 |
| 20 | 2024-10-01 | 2024-10-21 |
| 17 | 2025-03-14 | 2025-03-31 |
| 16 | 2025-09-16 | 2025-10-02 |
| 15 | 2024-12-19 | 2025-01-03 |
| 14 | 2025-04-16 | 2025-04-30 |
| 14 | 2026-09-02 | 2026-09-16 |

## 5. Breakdown By Title

| Title | Events |
|---|---:|
| Black Ops 6 | 43 |
| Black Ops 7 | 49 |
| Modern Warfare 4 | 11 |
| Modern Warfare III | 6 |
| Title not reliably specified | 89 |

The null title values are intentional. Warzone page titles often identify the experience but do not reliably identify the underlying title. The parser does not infer Black Ops 6 or Black Ops 7 for those records merely from unrelated or ambiguous URL tokens.

## 6. Breakdown By Experience

| Experience | Events |
|---|---:|
| Warzone | 89 |
| Experience not reliably specified | 109 |

`Warzone` is populated only where the official page title or URL clearly identifies the Warzone experience. Multiplayer is not inferred for title-specific pages, so the remaining experience values are null rather than guessed.

## 7. Duplicate Reconciliation

The same logical event appears on two official Warzone pages:

- Date: `2025-05-28`
- Pages: Black Ops 6 Season 04 and Black Ops 6 Warzone Season 04 Reloaded
- Logical result: one CSV event
- Provenance: both source URLs are retained, joined with ` | `
- Source evidence: `heading;dateline`

The reconciliation key is deterministic:

```text
update_date + franchise + title + experience + normalized update_title
```

Within a page, multiple representations of the same date are reduced to one event while retaining all supported `date_source_type` values. Across pages, matching logical events are merged while retaining source URLs, filenames, titles, seasons, and retrieval timestamps. No duplicate-looking source page is simply deleted.

Final duplicate checks found:

- Duplicate logical event keys: **0**
- Same source URL/date duplicates: **0**
- Date values outside `2024-09-01` through `2026-09-17`: **0**
- Null franchise values: **0**
- Null update titles: **0**

## 8. Manual Raw HTML Validation

Twenty representative events were checked directly against the preserved raw HTML. Every sample passed.

| Category | Date | Title | Experience | Season | Source type |
|---|---|---|---|---|---|
| Modern Warfare 4 Beta | 2026-08-20 | Modern Warfare 4 | null | Beta | heading;anchor |
| Modern Warfare III season | 2024-09-18 | Modern Warfare III | null | Season 6 | heading |
| Modern Warfare III Warzone | 2024-09-18 | null | Warzone | Season 6 | heading |
| Black Ops 6 Preseason | 2024-10-23 | Black Ops 6 | null | Preseason | anchor |
| Black Ops 6 season | 2024-11-15 | Black Ops 6 | null | Season 01 | anchor |
| Black Ops 6 ordinary update | 2025-04-08 | Black Ops 6 | null | Season 03 | anchor |
| Black Ops 6 Warzone | 2025-03-31 | null | Warzone | Season 03 | heading |
| Black Ops 6 Reloaded | 2025-04-30 | null | Warzone | Season 03 Reloaded | heading |
| Black Ops 7 Beta | 2025-10-02 | Black Ops 7 | null | Beta | anchor |
| Black Ops 7 Preseason | 2025-11-14 | Black Ops 7 | null | Preseason | anchor |
| Black Ops 7 season | 2026-02-06 | Black Ops 7 | null | Season 02 | anchor |
| Black Ops 7 Warzone | 2026-02-04 | null | Warzone | Season 02 | heading |
| Structured dateline | 2024-10-21 | null | Warzone | Season 6 | heading;dateline |
| Preseason anchor | 2024-10-24 | Black Ops 6 | null | Preseason | anchor |
| Season dateline | 2024-10-25 | Modern Warfare III | null | Season 6 | heading;dateline |
| Preseason anchor | 2024-10-26 | Black Ops 6 | null | Preseason | anchor |
| Preseason anchor | 2024-10-29 | Black Ops 6 | null | Preseason | anchor |
| Preseason anchor | 2024-11-01 | Black Ops 6 | null | Preseason | anchor |
| Preseason anchor | 2024-11-04 | Black Ops 6 | null | Preseason | anchor |
| Dateline and anchor | 2024-11-08 | Black Ops 6 | null | Preseason | dateline;anchor |

The sample deliberately covers Modern Warfare III, Black Ops 6, Black Ops 7, Modern Warfare 4, Warzone, preseason/launch material, seasons, Reloaded material, ordinary dated updates, and every supported date-source type.

## 9. Questionable Records and Remaining Limitations

- The 89 null title values are expected where Warzone pages do not clearly name the underlying title. They are preferable to unsupported inference.
- The 109 null experience values are expected where the page does not explicitly distinguish Multiplayer, Warzone, Zombies, Campaign, or another surface.
- The official sitemap and archive may evolve after this run; discovery completeness is relative to the public indexes observed during ingestion.
- The index captures dated update boundaries, not individual weapons, maps, modes, balance changes, fixes, or other detailed bullets.
- `date_source_type` identifies the structural evidence used, not the semantic type of the update.

## 10. Final Assessment

### A. Page Discovery Completeness: HIGH CONFIDENCE

The sitemap is now primary, the archive is a secondary cross-check, both sources are compared, and the full 37-page union downloaded successfully. All eight previously missed sitemap pages are present. Residual risk is limited to official pages absent from both public indexes.

### B. Date Extraction Accuracy: MEDIUM CONFIDENCE

All 37 pages now produce structured dated events, the eight Black Ops 7 failures are resolved, and all 20 manual samples match raw HTML. Confidence remains medium because official page templates may contain future structured date patterns not represented in this sample.

### C. Title/Experience Classification Accuracy: MEDIUM CONFIDENCE

The model no longer conflates the game title with the experience surface and leaves ambiguous values null. Explicit title and Warzone classifications are supported by page metadata. Confidence is not high because many official pages do not state both dimensions clearly.

### D. Suitability As the Authoritative Temporal Spine: MEDIUM CONFIDENCE

The index now has broad page coverage, structured extraction evidence, logical deduplication, raw provenance, and validated chronology. It is suitable as the temporal spine for the next phase, provided downstream users treat null title/experience values as unknown and do not interpret this ledger as detailed change extraction.

The regenerated outputs are:

- Raw pages: `data/raw/patch_pages/`
- Processed ledger: `data/processed/cod_change_history.csv`
- Ingestion audit log: `data/processed/ingestion.log`
