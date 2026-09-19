# CMS Content Boundary Analysis

Generated: 2026-09-18T10:59:56

## Scope

This diagnostic uses DOM structure, byte signatures, class/ID naming, and container relationships only. It does not clean files, extract gameplay content, classify text, modify `guide_index.csv`, or delete inputs.

## 1. Input Validation

| Structural classification | Count | Percentage |
|---|---:|---:|
| valid_content_page | 542 | 96.10% |
| non_html_or_binary_asset | 10 | 1.77% |
| valid_landing_or_index_page | 12 | 2.13% |

### Non-content and Uncertain Inputs

**non_html_or_binary_asset** (10):
- `COD-INCLINE-VIDEO-001-encoded.mp4-7552e74178.html` (3708108 bytes, 38 DOM tags, 11406 null bytes)
- `COD-INCLINE-VIDEO-002-encoded.mp4-4bfa1f6307.html` (4559890 bytes, 72 DOM tags, 14235 null bytes)
- `COD-INCLINE-VIDEO-003-encoded.mp4-d06d463064.html` (4581543 bytes, 148 DOM tags, 14112 null bytes)
- `DERELICT-TOWER-DIVE.mp4-4ef50f1a61.html` (11751923 bytes, 70 DOM tags, 31528 null bytes)
- `MOVEMENT-CORNER-SLICE.mp4-30c4902439.html` (10903193 bytes, 106 DOM tags, 29087 null bytes)
- `MOVEMENT-INTELLIGENT-MOVEMENT.mp4-65564a67f5.html` (16436033 bytes, 129 DOM tags, 41107 null bytes)
- `MOVEMENT_Omnimovement.mp4-9d5a3b06c6.html` (17509085 bytes, 246 DOM tags, 41455 null bytes)
- `REWIND-BETA.mp4-2cfd2401df.html` (14712004 bytes, 228 DOM tags, 38665 null bytes)
- `SKYLINE-SECRUITY.mp4-cfbbdbbc88.html` (17249376 bytes, 102 DOM tags, 48196 null bytes)
- `SWIMMING.mp4-b88ffdebed.html` (9767453 bytes, 122 DOM tags, 23869 null bytes)

**valid_landing_or_index_page** (12):
- `blackops6-98afa6baff.html` (230535 bytes, 1839 DOM tags, 0 null bytes)
- `blackops6-e014fa303c.html` (230535 bytes, 1839 DOM tags, 0 null bytes)
- `blackops7-1f82d077fe.html` (217256 bytes, 1794 DOM tags, 0 null bytes)
- `blackops7-26b6917e35.html` (217256 bytes, 1794 DOM tags, 0 null bytes)
- `mobile-bc714ae296.html` (121264 bytes, 986 DOM tags, 0 null bytes)
- `mobile-dde8973b1a.html` (121264 bytes, 986 DOM tags, 0 null bytes)
- `modernwarfare3-389c8bb50b.html` (236749 bytes, 1923 DOM tags, 0 null bytes)
- `modernwarfare3-fdd28e9b8c.html` (236749 bytes, 1923 DOM tags, 0 null bytes)
- `warzone-edf617f6fc.html` (128684 bytes, 1047 DOM tags, 0 null bytes)
- `warzone-f4b44f8712.html` (128684 bytes, 1047 DOM tags, 0 null bytes)
- `weapons-580378482b.html` (186343 bytes, 1587 DOM tags, 0 null bytes)
- `weapons-a444dd623c.html` (186343 bytes, 1587 DOM tags, 0 null bytes)

## 2. CMS Marker Inventory

| Marker | Pages | Coverage | Avg occurrences/page | Median occurrences/page |
|---|---:|---:|---:|---:|
| `article-layout` | 256 | 47.23% | 1.00 | 1 |
| `article-layout-content` | 256 | 47.23% | 1.00 | 1 |
| `article-header-container` | 256 | 47.23% | 1.00 | 1 |
| `article-body-container` | 256 | 47.23% | 1.00 | 1 |
| `body-content` | 410 | 75.65% | 1.00 | 1 |
| `body-content-parsys` | 410 | 75.65% | 1.00 | 1 |
| `article-rich-text` | 256 | 47.23% | 79.19 | 58 |
| `cmp-text` | 532 | 98.16% | 46.71 | 16 |
| `main-content` | 410 | 75.65% | 1.00 | 1 |

### Additional Structurally Named Markers

- `skip-to-main-content-link`: 540 valid content pages
- `nav-expand-content`: 540 valid content pages
- `cmp-text`: 532 valid content pages
- `main-content`: 410 valid content pages
- `body-content`: 410 valid content pages
- `body-content-parsys`: 410 valid content pages
- `article-image`: 408 valid content pages
- `article-image-component`: 408 valid content pages
- `article-image-container`: 408 valid content pages
- `intel-card__content`: 282 valid content pages
- `article-layout`: 256 valid content pages
- `article-layout-content`: 256 valid content pages
- `article-header-container`: 256 valid content pages
- `article-body-container`: 256 valid content pages
- `article-rich-text`: 256 valid content pages
- `article-related-posts-component`: 184 valid content pages
- `atvi-rich-text`: 162 valid content pages
- `article-related-posts-container`: 160 valid content pages
- `table-component`: 140 valid content pages
- `table__content`: 140 valid content pages
- `reader-drawer__content`: 120 valid content pages
- `drawerContent`: 120 valid content pages
- `guide-drawer__content`: 120 valid content pages
- `guide-content`: 120 valid content pages
- `map-rich-text`: 120 valid content pages
- `map-rich-text-component`: 120 valid content pages
- `marker-drawer__content`: 120 valid content pages
- `markerContent`: 120 valid content pages
- `marker-content`: 120 valid content pages
- `marker-content-header`: 120 valid content pages

## 3. Candidate Root Coverage

| Candidate root | Pages | Coverage | Exactly one | Multiple | Chrome inside | Avg text chars | Avg headings | Avg paragraphs | Avg tables | Avg rich-text components |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.article-body-container` | 256 | 47.23% | 256 | 0 | 2 | 7993 | 25.39 | 99.97 | 0.01 | 158.90 |
| `.body-content` | 410 | 75.65% | 410 | 0 | 6 | 10046 | 20.56 | 102.60 | 0.00 | 106.93 |
| `.body-content-parsys` | 410 | 75.65% | 410 | 0 | 6 | 9929 | 20.56 | 100.36 | 0.00 | 106.93 |
| `.article-layout-content` | 256 | 47.23% | 256 | 0 | 256 | 8230 | 27.02 | 101.97 | 0.01 | 158.90 |
| `#main-content` | 410 | 75.65% | 410 | 0 | 260 | 10392 | 23.55 | 103.85 | 0.00 | 106.93 |
| `.main-content` | 0 | 0.00% | 0 | 0 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 |
| `main#main-content` | 410 | 75.65% | 410 | 0 | 260 | 10392 | 23.55 | 103.85 | 0.00 | 106.93 |
| `.guide-content` | 120 | 22.14% | 0 | 120 | 120 | 5614 | 13.07 | 30.40 | 0.00 | 21.30 |
| `.map-page` | 120 | 22.14% | 120 | 0 | 120 | 6984 | 16.07 | 68.25 | 0.00 | 21.30 |
| `.map-overlay` | 310 | 57.20% | 122 | 188 | 120 | 1540 | 2.92 | 18.79 | 0.00 | 4.12 |
| `.map-rich-text-component` | 120 | 22.14% | 0 | 120 | 0 | 4915 | 11.07 | 22.37 | 0.00 | 0.00 |
| `.article-rich-text` | 256 | 47.23% | 0 | 256 | 2 | 5545 | 14.34 | 82.85 | 0.01 | 79.19 |
| `.atvi-rich-text` | 162 | 29.89% | 6 | 156 | 4 | 11328 | 13.73 | 83.26 | 0.00 | 19.14 |
| `.article-layout` | 256 | 47.23% | 256 | 0 | 256 | 9387 | 27.93 | 129.64 | 0.01 | 158.90 |
| `.article-content` | 0 | 0.00% | 0 | 0 | 0 | 0 | 0.00 | 0.00 | 0.00 | 0.00 |
| `.content` | 2 | 0.37% | 2 | 0 | 0 | 456 | 5.00 | 3.00 | 0.00 | 0.00 |
| `main` | 410 | 75.65% | 410 | 0 | 260 | 10392 | 23.55 | 103.85 | 0.00 | 106.93 |

Chrome markers found inside candidate roots are counted structurally, not judged semantically:

- `.article-body-container`: {'Navigation': 2}
- `.body-content`: {'Navigation': 6}
- `.body-content-parsys`: {'Navigation': 6}
- `.article-layout-content`: {'article-related-posts-component': 184, 'article-related-posts-container': 160, 'related-wrapper': 256, 'article-related-posts': 72, 'Navigation': 2}
- `#main-content`: {'article-related-posts-component': 184, 'article-related-posts-container': 160, 'related-wrapper': 256, 'article-related-posts': 72, 'Navigation': 6}
- `main#main-content`: {'article-related-posts-component': 184, 'article-related-posts-container': 160, 'related-wrapper': 256, 'article-related-posts': 72, 'Navigation': 6}
- `.guide-content`: {'cookie-settings': 120, 'locale-panel': 120, 'locale-panel-header': 120, 'locale-panel-inner-container': 120, 'locale-selector-list': 120, 'locale-selector-toggle': 120, 'locale-string': 120}
- `.map-page`: {'cod-header_cta': 120, 'cod-header_cta-desktop': 120, 'cod-header_cta-mobile': 120, 'cod-header_desktop-nav_links': 120, 'cod-header_global-list': 120, 'cod-header_inner-container': 120, 'cod-header_mobile-button': 120, 'cod-header_mobile-dropdown': 120, 'cod-header_mobile-dropdown-inner-container': 120, 'cod-header_mobile-menu': 120, 'cod-header_mobile-primary-menu': 120, 'cod-header_mobile-secondary-menu': 120, 'cod-header_mobile-sidebar': 120, 'cod-header_mobile-sidebar-inner-container': 120, 'cod-header_mobile-sidebar_header': 120, 'cod-header_mobile-sidebar_header-back': 120, 'cod-header_mobile-sidebar_header-close': 120, 'cod-header_mobile-sidebar_links': 120, 'cod-header_mobile-sidebar_secondary': 120, 'cod-header_mobile-sidebar_sso': 120, 'cod-header_mobile-sso': 120, 'cod-header_primary-logo': 120, 'cod-header_secondary-logo': 120, 'cod-header_sso': 120, 'cod-header_top-nav': 120, 'cookie-settings': 120, 'locale-panel': 120, 'locale-panel-header': 120, 'locale-panel-inner-container': 120, 'locale-selector-list': 120, 'locale-selector-toggle': 120, 'locale-string': 120, 'nav-ellipsis-dropdown': 120, 'nav-ellipsis-dropdown-menu': 120, 'nav-ellipsis-dropdown-toggle': 120, 'nav-expand-content': 120}
- `.map-overlay`: {'cod-header_cta': 120, 'cod-header_cta-desktop': 120, 'cod-header_cta-mobile': 120, 'cod-header_desktop-nav_links': 120, 'cod-header_global-list': 120, 'cod-header_inner-container': 120, 'cod-header_mobile-button': 120, 'cod-header_mobile-dropdown': 120, 'cod-header_mobile-dropdown-inner-container': 120, 'cod-header_mobile-menu': 120, 'cod-header_mobile-primary-menu': 120, 'cod-header_mobile-secondary-menu': 120, 'cod-header_mobile-sidebar': 120, 'cod-header_mobile-sidebar-inner-container': 120, 'cod-header_mobile-sidebar_header': 120, 'cod-header_mobile-sidebar_header-back': 120, 'cod-header_mobile-sidebar_header-close': 120, 'cod-header_mobile-sidebar_links': 120, 'cod-header_mobile-sidebar_secondary': 120, 'cod-header_mobile-sidebar_sso': 120, 'cod-header_mobile-sso': 120, 'cod-header_primary-logo': 120, 'cod-header_secondary-logo': 120, 'cod-header_sso': 120, 'cod-header_top-nav': 120, 'cookie-settings': 120, 'locale-panel': 120, 'locale-panel-header': 120, 'locale-panel-inner-container': 120, 'locale-selector-list': 120, 'locale-selector-toggle': 120, 'locale-string': 120, 'nav-ellipsis-dropdown': 120, 'nav-ellipsis-dropdown-menu': 120, 'nav-ellipsis-dropdown-toggle': 120, 'nav-expand-content': 120}
- `.article-rich-text`: {'Navigation': 2}
- `.atvi-rich-text`: {'Navigation': 4}
- `.article-layout`: {'article-related-posts-component': 184, 'article-related-posts-container': 160, 'cod-footer': 232, 'cod-header_cta': 256, 'cod-header_cta-desktop': 256, 'cod-header_cta-mobile': 256, 'cod-header_desktop-nav_links': 256, 'cod-header_global-list': 256, 'cod-header_inner-container': 256, 'cod-header_mobile-button': 256, 'cod-header_mobile-dropdown': 256, 'cod-header_mobile-dropdown-inner-container': 256, 'cod-header_mobile-menu': 256, 'cod-header_mobile-primary-menu': 256, 'cod-header_mobile-secondary-menu': 256, 'cod-header_mobile-sidebar': 130, 'cod-header_mobile-sidebar-inner-container': 130, 'cod-header_mobile-sidebar_header': 130, 'cod-header_mobile-sidebar_header-back': 130, 'cod-header_mobile-sidebar_header-close': 130, 'cod-header_mobile-sidebar_links': 130, 'cod-header_mobile-sidebar_secondary': 130, 'cod-header_mobile-sidebar_sso': 130, 'cod-header_mobile-sso': 256, 'cod-header_primary-logo': 256, 'cod-header_secondary-logo': 256, 'cod-header_sso': 256, 'cod-header_top-nav': 256, 'cookie-settings': 232, 'locale-panel': 232, 'locale-panel-header': 232, 'locale-panel-inner-container': 232, 'locale-selector-list': 232, 'locale-selector-toggle': 232, 'locale-string': 232, 'nav-ellipsis-dropdown': 256, 'nav-ellipsis-dropdown-menu': 256, 'nav-ellipsis-dropdown-toggle': 256, 'nav-expand-content': 256, 'related-wrapper': 256, 'article-related-posts': 72, 'cod-header_locale-selector': 2, 'cod-header_search': 2, 'Navigation': 2}
- `main`: {'article-related-posts-component': 184, 'article-related-posts-container': 160, 'related-wrapper': 256, 'article-related-posts': 72, 'Navigation': 6}

## 4. Smallest Evidence-Supported Fallback Chain

Candidate ordering is empirical: coverage first, then fewer obvious chrome markers, then exact-one prevalence.

| Step | Added selector | Newly covered | Cumulative coverage |
|---:|---|---:|---:|
| 1 | `.body-content` | 404 | 74.54% |
| 2 | `.content` | 2 | 74.91% |
| 3 | `.atvi-rich-text` | 2 | 75.28% |

| Target | Smallest chain | Coverage |
|---:|---|---:|
| 80% | not reached by measured unique-root candidates | - |
| 90% | not reached by measured unique-root candidates | - |
| 95% | not reached by measured unique-root candidates | - |
| 99% | not reached by measured unique-root candidates | - |
| unresolved | 134 valid content pages | - |

## 5. Cross-check Against Largest 0.90 Structural Families

### 0.90-1

- Page count: 120
- Dominant root: `(none)`
- Dominant-root coverage: 0.00% of family
- Fallback-chain coverage: 0.00% of family
- Exceptions/unresolved: 120

### 0.90-2

- Page count: 112
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-3

- Page count: 88
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-4

- Page count: 80
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-5

- Page count: 48
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-6

- Page count: 10
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-7

- Page count: 10
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-8

- Page count: 8
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-9

- Page count: 8
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-10

- Page count: 8
- Dominant root: `(none)`
- Dominant-root coverage: 0.00% of family
- Fallback-chain coverage: 0.00% of family
- Exceptions/unresolved: 8

### 0.90-11

- Page count: 0
- Dominant root: `(none)`
- Dominant-root coverage: 0.00% of family
- Fallback-chain coverage: 0.00% of family
- Exceptions/unresolved: 0

### 0.90-12

- Page count: 4
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-13

- Page count: 0
- Dominant root: `(none)`
- Dominant-root coverage: 0.00% of family
- Fallback-chain coverage: 0.00% of family
- Exceptions/unresolved: 0

### 0.90-14

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-15

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-16

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-17

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-18

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-19

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

### 0.90-20

- Page count: 2
- Dominant root: `.body-content`
- Dominant-root coverage: 100.00% of family
- Fallback-chain coverage: 100.00% of family
- Exceptions/unresolved: 0

## 6. Representative Boundary Previews

### 0.90-2 — 1911

- Source file: `1911-8e28f7814b.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-1 — Abyss

- Source file: `abyss-c0e1ea3795.html`
- Root selector: `(unresolved)`
- Before root: `[]`
- Root start: `[]`
- Root end: `[]`
- After root: `[]`

### 0.90-3 — Call of Duty | Guides - Modern Warfare III Multiplayer Map — Meat

- Source file: `call-of-duty-guide-modern-warfare-iii-multiplayer-map-meat-0a5e043c27.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.subtitle', 'h1', 'p', 'p', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `[]`

### 0.90-5 — Call of Duty | Guides - Modern Warfare Zombies Tactics

- Source file: `call-of-duty-guide-modern-warfare-zombies-tactics-481a4ce521.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.subtitle', 'h1', 'p', 'p', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `[]`

### 0.90-14 — Call of Duty | Guides - Black Ops 6 Level Unlocks: Player Level 1-55

- Source file: `call-of-duty-guides-black-ops-6-level-unlocks-player-level-1-55-563871bcd0.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'p', 'h4']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-15 — Call of Duty | Guides - Black Ops 6 Multiplayer Beta — Everything You Need to Know

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-beta-everything-you-need-to-know-ac6946f582.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-16 — Call of Duty | Guides - Black Ops 6 Multiplayer Guide — COD 101 - READ THIS FIRST

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-guide-cod-101-read-this-first-8084da5b9e.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-17 — Call of Duty | Guides - Black Ops 6 Multiplayer: How to Play

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-how-to-play-379fac00d4.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h1', 'p']`
- Root end: `['p', 'h2', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-18 — Call of Duty | Guides - Black Ops 6 Multiplayer Guide — Leveling Up and Progression

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-leveling-up-and-progression-5389470c33.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-4 — Call of Duty | Guides - Black Ops 6 Multiplayer Map Guide — Babylon

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-map-guide-babylon-9f697c270a.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-6 — Call of Duty | Guides - Black Ops 6 Multiplayer Mode Guide — Domination

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-mode-domination-3dda7a93fa.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['h3', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-7 — Call of Duty | Guides - Black Ops 6 Multiplayer Mode Guide — Control

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-mode-guide-control-334f07851a.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-19 — Call of Duty | Guides - Black Ops 6 Multiplayer Mode Guide — Kill Order

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-mode-kill-order-2bc2655337.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'p', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-20 — Call of Duty | Guides - Black Ops 6 Multiplayer: Pre-Game — Weapons & Loadouts

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-pre-game-weapons-and-loadouts-9fd8e38841.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h1', 'h1']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-21 — Call of Duty | Guides - Black Ops 6 Multiplayer Training — Controls

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-training-controls-0f886d6cf1.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'h2']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-22 — Call of Duty | Guides - Black Ops 6 Multiplayer Training — Movement

- Source file: `call-of-duty-guides-black-ops-6-multiplayer-training-movement-d3a05f8c7c.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h1', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-8 — Call of Duty | Guides - Black Ops 6 Round Based Zombies — Citadelle des Morts

- Source file: `call-of-duty-guides-black-ops-6-round-based-zombies-citadelle-des-morts-68184148ce.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-23 — Call of Duty | Guides - Black Ops 6 Round Based Zombies Directed Mode — Reckoning

- Source file: `call-of-duty-guides-black-ops-6-round-based-zombies-directed-mode-reckoning-b37e970768.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-24 — Call of Duty | Guides - Black Ops 6 Round Based Zombies — Liberty Falls

- Source file: `call-of-duty-guides-black-ops-6-round-based-zombies-liberty-falls-8908fbbf8c.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p', 'p']`
- After root: `['div.side-cta-wrapper']`

### 0.90-25 — Call of Duty | Guides - Black Ops 6 Round Based Zombies — GobbleGums

- Source file: `call-of-duty-guides-black-ops-6-zombies-gobblegums-11c7f3bdc3.html`
- Root selector: `.body-content`
- Before root: `['div.side-nav-wrapper']`
- Root start: `['p.dateline', 'p.byline', 'p.subtitle', 'h2', 'p']`
- Root end: `['p', 'p', 'p', 'p.sku', 'p']`
- After root: `['div.side-cta-wrapper']`

## 7. Failure Modes

- **no_unique_candidate_content_root**: 8
- **multiple_competing_roots_or_nodes**: 538
- **candidate_root_includes_obvious_chrome**: 380
- **landing_or_index_page**: 12
- **non_html_or_binary**: 10
- **root_appears_to_omit_headings**: 192
- **root_appears_to_omit_tables**: 540
- **root_appears_to_omit_rich_text**: 312

## Decision

**TEMPLATE-SPECIFIC EXTRACTION REQUIRED**

The best single root covers 75.65% of valid content pages. The measured safe fallback chain reaches not reached at not reached selectors and leaves 134 valid content pages unresolved. Root behavior still varies across structural families, so fallback handling is required.

### Direct Answers

1. Valid content pages: **542** of 564.
2. Landing/index pages: **12**.
3. Malformed/non-HTML/binary assets: **10**.
4. Best single root: `.body-content` at **75.65%**.
5. Best single-root coverage: **75.65%**.
6. Smallest chain for 80%: **not reached**.
7. Smallest chain for 90%: **not reached**.
8. Smallest chain for 95%: **not reached**.
9. Smallest chain for 99%: **not reached**.
10. Valid content pages unresolved by the measured safe chain: **134**.
11. Largest structural-family result: `.body-content` generalizes across the largest non-map families; the 120-page map family requires a different boundary and its unique candidate contains global chrome.
12. Systematic loss risk: yes. Repeated rich-text components, map-family chrome, and pages without a unique chrome-free root are enumerated above rather than corrected.

No cleaner was implemented and no corpus files were modified.
