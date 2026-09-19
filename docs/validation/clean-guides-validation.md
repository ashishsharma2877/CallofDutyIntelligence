# Clean Guide Corpus Validation

Generated: 2026-09-18T20:45:32.633782

## Scope

This prototype processes only pages assigned a unique, chrome-free safe root by the existing content-boundary diagnostic. It does not clean unresolved pages, use semantic rules, modify raw HTML, or modify `guide_index.csv`.

## Corpus Counts

- Total original inputs: **564**
- Cleaned: **408**
- Unresolved: **134**
- Landing/index: **12**
- Non-HTML/binary: **10**
- Failed: **0**

## Clean Corpus Size

- Total clean size: **8.515 MB**
- Total characters: **3,897,690**
- Total words: **666,442**
- Estimated total tokens: **974,580**
- Mean tokens per guide: **2,388.68**
- Median tokens per guide: **1,750**
- P90 tokens per guide: **4,149**
- P95 tokens per guide: **6,194**
- P99 tokens per guide: **10,926**
- Largest guide: `call-of-duty-modern-warfare-III-campaign-play-guides-weapons-loadouts-1a06c20d01.html` (13,576 estimated tokens)
- Smallest non-empty guide: `multiplayer-pre-game-802f5f9952.html` (16 estimated tokens)

Token approximation: `estimated_tokens = ceil(clean_characters / 4)`. No external tokenizer or API was used.

## Lightweight Validation

- Zero-text extractions: **0**
- Extremely small extractions (<20 estimated tokens): **2**
- Retention-ratio outliers (>3 standard deviations): **10**
- Pages missing all headings: **0**
- Extraction failures: **0**

### Ten-Page Targeted Sample

The sample covers the largest structural groups, available selector variants, and size/retention extremes. Structural checks verified that source wording was carried through unchanged, headings/lists/tables were represented when present in the selected root, and the resolver accepted no root containing its detected global chrome markers.

| Source file | Selector | Blocks | Headings | Lists | Tables | Wording preserved | Chrome in root |
|---|---|---:|---:|---:|---:|---|---|
| `ak-27-430cf6e3f8.html` | `.body-content` | 187 | 19 | 54 | 0 | yes | no |
| `call-of-duty-guide-modern-warfare-iii-multiplayer-map-meat-378e5b95d4.html` | `.body-content` | 66 | 9 | 14 | 0 | yes | no |
| `call-of-duty-guides-black-ops-6-multiplayer-map-guide-babylon-9f697c270a.html` | `.body-content` | 59 | 15 | 8 | 0 | yes | no |
| `call-of-duty-guides-modern-warfare-iii-mode-gunfight-a2a8945833.html` | `.body-content` | 47 | 6 | 7 | 0 | yes | no |
| `call-of-duty-guides-black-ops-6-level-unlocks-player-level-1-55-5d94162452.html` | `.body-content` | 142 | 1 | 0 | 0 | yes | no |
| `zombies-828cf9ab65.html` | `.content` | 6 | 3 | 0 | 0 | yes | no |
| `multiplayer-pre-game-802f5f9952.html` | `.atvi-rich-text` | 3 | 2 | 0 | 0 | yes | no |
| `call-of-duty-modern-warfare-III-campaign-play-guides-weapons-loadouts-1a06c20d01.html` | `.body-content` | 624 | 85 | 90 | 0 | yes | no |
| `call-of-duty-guides-black-ops-6-multiplayer-beta-everything-you-need-to-know-ac6946f582.html` | `.body-content` | 472 | 231 | 59 | 0 | yes | no |
| `gobblegums-67000e556a.html` | `.body-content` | 571 | 108 | 91 | 0 | yes | no |

## Status Accounting

Every original input appears exactly once in `data/processed/clean_guide_index.csv` with one of: `cleaned`, `unresolved`, `landing_index`, `non_html`, or `failed`.

## Obvious Systematic Problems

- Coverage is intentionally incomplete: unresolved pages were not given fallback heuristics.
- The strict resolver excludes roots with detected navigation/header/footer/locale/cookie/related-content markers, so some structurally usable pages remain unresolved by design.
- Token counts are approximations based on character count, not tokenizer output.
- No semantic extraction or gameplay classification was performed.

## Output Files

- `data/clean/guides/*.json`: one structured file per cleaned guide.
- `data/processed/clean_guide_index.csv`: one status row for all original inputs.
- `src/clean_guides.py`: reproducible structural cleaner.

**Status: prototype clean corpus complete; unresolved pages intentionally accepted.**
