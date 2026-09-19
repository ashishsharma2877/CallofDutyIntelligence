# DOM Structure Analysis of the Call of Duty Guide Corpus

Generated: 2026-09-18T09:48:26

## Scope and Method

This is a diagnostic of HTML/DOM structure only. It does not clean pages, extract gameplay content, classify semantic content, or modify `guide_index.csv`.

- HTML pages analyzed: **564**
- Exact structural fingerprints: **286**
- Fingerprints use ordered DOM tag shape, normalized class/ID tokens, element counts, heading levels, container presence, depth, and parent-child tag pairs.
- Text nodes, page titles, URLs, dates, and content names were excluded from fingerprints.
- Near-family counts use connected components over pairwise structural cosine similarity.

## Similarity Diagnostics

| Similarity threshold | Structural families | Largest family | Pages in largest family |
|---:|---:|---:|---:|
| 0.95 | 98 | 1 | 98 (17.38%) |
| 0.90 | 47 | 1 | 120 (21.28%) |
| 0.80 | 19 | 1 | 250 (44.33%) |
| 0.70 | 14 | 1 | 256 (45.39%) |

### Exact Fingerprint Distribution

- Pages represented in exact duplicate groups (size >= 2): 554
- Exact groups of size >= 2: 276
- Singleton exact fingerprints: 10

### Coverage of Largest Near-Families

| Largest families included | Corpus covered |
|---:|---:|
| 1 | 21.28% |
| 3 | 56.74% |
| 5 | 79.43% |
| 10 | 87.23% |
| 20 | 92.20% |

### Families Needed for Coverage

| Target coverage | Families needed |
|---:|---:|
| 80% | 6 |
| 90% | 14 |
| 95% | 28 |
| 99% | 42 |

## Structural Family Size Distribution

### Threshold 0.95

- Families: 98
- Largest: 98 pages
- Median: 2 pages
- Singleton families: 10
- Top 10 sizes: [98, 84, 80, 44, 28, 20, 12, 8, 8, 6]

### Threshold 0.90

- Families: 47
- Largest: 120 pages
- Median: 2 pages
- Singleton families: 10
- Top 10 sizes: [120, 112, 88, 80, 48, 10, 10, 8, 8, 8]

### Threshold 0.80

- Families: 19
- Largest: 250 pages
- Median: 1 pages
- Singleton families: 10
- Top 10 sizes: [250, 154, 120, 12, 8, 4, 2, 2, 2, 1]

### Threshold 0.70

- Families: 14
- Largest: 256 pages
- Median: 1 pages
- Singleton families: 10
- Top 10 sizes: [256, 176, 120, 2, 1, 1, 1, 1, 1, 1]

## Largest Structural Families

### 0.90-1

- Pages: **120** (21.28% of corpus)
- Representative guide: **Abyss**
- Representative URL: `https://www.callofduty.com/guides/blackops7/multiplayer-maps/s03/abyss`
- Representative source file: `abyss-c0e1ea3795.html`
- Title families: {'(blank)': 88, 'Black Ops 7': 32}
- Guide categories: {'(blank)': 86, 'Map': 34}
- Experiences: {'(blank)': 88, 'Multiplayer': 32}
- Publication years: {'(unknown)': 120}
- DOM characteristics: {'element_count': 1091, 'max_depth': 21, 'main_count': 0, 'article_count': 0, 'section_count': 0, 'container_count': 214, 'top_tags': [('div', 209), ('a', 140), ('li', 121), ('span', 100), ('p', 75), ('button', 50), ('path', 46), ('img', 44), ('ul', 34), ('symbol', 28), ('i', 24), ('style', 22)], 'top_classes': [('expand-arrow', 30), ('aem-gridcolumn', 25), ('aem-gridcolumn--default--#', 25), ('custom-arrow', 20), ('slick-sr-only', 20), ('nav-expand-content', 13), ('map-rich-text', 12), ('cmp-text', 12), ('map-rich-text-component', 12), ('dd', 12), ('icon-btn', 10), ('map-media-carousel', 10)], 'heading_counts': {'h1': 2, 'h2': 11, 'h3': 4}}

### 0.90-2

- Pages: **112** (19.86% of corpus)
- Representative guide: **1911**
- Representative URL: `https://callofduty.com/guides/blackops7/weapons/pistol/s03/1911`
- Representative source file: `1911-8e28f7814b.html`
- Title families: {'(blank)': 112}
- Guide categories: {'(blank)': 112}
- Experiences: {'(blank)': 112}
- Publication years: {'(unknown)': 112}
- DOM characteristics: {'element_count': 2439, 'max_depth': 33, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 1374, 'top_tags': [('div', 1367), ('style', 188), ('li', 178), ('p', 175), ('a', 123), ('span', 108), ('b', 88), ('ul', 60), ('meta', 24), ('script', 22), ('img', 21), ('link', 19)], 'top_classes': [('aem-gridcolumn', 194), ('aem-gridcolumn--default--#', 194), ('aem-grid', 190), ('aem-grid--#', 190), ('aem-grid--default--#', 190), ('table__cell', 188), ('table__cell--col-#', 188), ('table__cell--row-#', 188), ('table__cell--value', 184), ('article-rich-text', 170), ('cmp-text', 170), ('table__row', 83)], 'heading_counts': {'h1': 1, 'h6': 2, 'h2': 8, 'h4': 18}}

### 0.90-3

- Pages: **88** (15.60% of corpus)
- Representative guide: **Call of Duty | Guides - Modern Warfare III Multiplayer Map — Meat**
- Representative URL: `https://www.callofduty.com/guides/multiplayer-maps/call-of-duty-guide-modern-warfare-iii-multiplayer-map-meat`
- Representative source file: `call-of-duty-guide-modern-warfare-iii-multiplayer-map-meat-0a5e043c27.html`
- Title families: {'Modern Warfare III': 88}
- Guide categories: {'Map': 88}
- Experiences: {'Multiplayer': 88}
- Publication years: {'(unknown)': 88}
- DOM characteristics: {'element_count': 1018, 'max_depth': 23, 'main_count': 1, 'article_count': 0, 'section_count': 3, 'container_count': 209, 'top_tags': [('div', 196), ('a', 172), ('li', 170), ('p', 126), ('span', 80), ('img', 60), ('ul', 43), ('button', 24), ('b', 24), ('script', 23), ('meta', 21), ('link', 16)], 'top_classes': [('aem-gridcolumn', 28), ('aem-gridcolumn--default--#', 28), ('link-icon', 16), ('expand-arrow', 16), ('dd', 15), ('article-image-container', 12), ('lazy', 11), ('visually-hidden', 10), ('atvi-rich-text', 10), ('cmp-text', 10), ('aem-grid', 8), ('aem-grid--#', 8)], 'heading_counts': {'h2': 8, 'h1': 5}}

### 0.90-4

- Pages: **80** (14.18% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Map Guide — Babylon**
- Representative URL: `https://callofduty.com/guides/blackops6/multiplayer-maps/call-of-duty-guides-black-ops-6-multiplayer-map-guide-babylon`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-map-guide-babylon-9f697c270a.html`
- Title families: {'Black Ops 6': 80}
- Guide categories: {'Map': 80}
- Experiences: {'Multiplayer': 80}
- Publication years: {'(unknown)': 80}
- DOM characteristics: {'element_count': 886, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 250, 'top_tags': [('div', 243), ('li', 112), ('a', 104), ('p', 71), ('span', 70), ('img', 66), ('ul', 32), ('script', 25), ('link', 22), ('meta', 21), ('style', 21), ('button', 18)], 'top_classes': [('aem-gridcolumn', 34), ('aem-gridcolumn--default--#', 34), ('article-rich-text', 18), ('cmp-text', 18), ('expand-arrow', 16), ('article-image-container', 16), ('lazy', 13), ('article_rich_text_#-#', 12), ('article-image', 8), ('atvi-image', 8), ('article-image-component', 8), ('img-lazy-container', 8)], 'heading_counts': {'h1': 1, 'h6': 3, 'h2': 11, 'h3': 6}}

### 0.90-5

- Pages: **48** (8.51% of corpus)
- Representative guide: **Call of Duty | Guides - Modern Warfare Zombies Tactics**
- Representative URL: `https://www.callofduty.com/guides/zombies/call-of-duty-guide-modern-warfare-zombies-tactics`
- Representative source file: `call-of-duty-guide-modern-warfare-zombies-tactics-481a4ce521.html`
- Title families: {'(blank)': 12, 'Modern Warfare III': 36}
- Guide categories: {'Mode': 46, 'Operator': 2}
- Experiences: {'Zombies': 12, '(blank)': 32, 'Campaign': 2, 'Multiplayer': 2}
- Publication years: {'(unknown)': 48}
- DOM characteristics: {'element_count': 1337, 'max_depth': 23, 'main_count': 1, 'article_count': 0, 'section_count': 3, 'container_count': 387, 'top_tags': [('div', 374), ('p', 197), ('a', 188), ('li', 176), ('span', 81), ('img', 58), ('ul', 46), ('b', 43), ('h2', 23), ('i', 23), ('script', 22), ('meta', 20)], 'top_classes': [('aem-gridcolumn', 61), ('aem-gridcolumn--default--#', 61), ('atvi-rich-text', 31), ('cmp-text', 31), ('article-image-container', 28), ('link-icon', 16), ('expand-arrow', 16), ('dd', 15), ('article-image', 14), ('atvi-image', 14), ('article-image-component', 14), ('img-lazy-container', 14)], 'heading_counts': {'h2': 23, 'h1': 12}}

### 0.90-6

- Pages: **10** (1.77% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Mode Guide — Domination**
- Representative URL: `https://www.callofduty.com/guides/blackops6/modes/call-of-duty-guides-black-ops-6-multiplayer-mode-domination`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-mode-domination-3dda7a93fa.html`
- Title families: {'Black Ops 6': 10}
- Guide categories: {'Mode': 10}
- Experiences: {'Multiplayer': 10}
- Publication years: {'(unknown)': 10}
- DOM characteristics: {'element_count': 698, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 157, 'top_tags': [('div', 150), ('li', 101), ('a', 99), ('p', 77), ('span', 51), ('ul', 30), ('img', 28), ('b', 26), ('meta', 23), ('script', 22), ('link', 19), ('i', 15)], 'top_classes': [('aem-gridcolumn', 16), ('aem-gridcolumn--default--#', 16), ('expand-arrow', 16), ('tag-item', 9), ('dd', 7), ('nav-expand-content', 7), ('article-rich-text', 7), ('cmp-text', 7), ('aem-grid', 6), ('aem-grid--#', 6), ('aem-grid--default--#', 6), ('article-image-container', 6)], 'heading_counts': {'h1': 3, 'h6': 1, 'h2': 7, 'h3': 15}}

### 0.90-7

- Pages: **10** (1.77% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Mode Guide — Control**
- Representative URL: `https://www.callofduty.com/guides/blackops6/modes/call-of-duty-guides-black-ops-6-multiplayer-mode-guide-control`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-mode-guide-control-334f07851a.html`
- Title families: {'Black Ops 6': 10}
- Guide categories: {'Mode': 10}
- Experiences: {'Multiplayer': 10}
- Publication years: {'(unknown)': 10}
- DOM characteristics: {'element_count': 613, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 142, 'top_tags': [('div', 136), ('a', 95), ('li', 83), ('p', 70), ('span', 44), ('img', 26), ('script', 23), ('ul', 23), ('meta', 20), ('link', 19), ('i', 14), ('h3', 14)], 'top_classes': [('aem-gridcolumn', 17), ('aem-gridcolumn--default--#', 17), ('expand-arrow', 16), ('cmp-text', 8), ('dd', 7), ('nav-expand-content', 7), ('article-rich-text', 7), ('aem-grid', 6), ('aem-grid--#', 6), ('aem-grid--default--#', 6), ('article-image-container', 6), ('line-fade', 5)], 'heading_counts': {'h1': 1, 'h6': 1, 'h2': 8, 'h3': 14}}

### 0.90-8

- Pages: **8** (1.42% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Round Based Zombies — Citadelle des Morts**
- Representative URL: `https://callofduty.com/guides/blackops6/zombies/call-of-duty-guides-black-ops-6-round-based-zombies-citadelle-des-morts`
- Representative source file: `call-of-duty-guides-black-ops-6-round-based-zombies-citadelle-des-morts-68184148ce.html`
- Title families: {'Black Ops 6': 8}
- Guide categories: {'Guide': 6, 'Mode': 2}
- Experiences: {'Zombies': 8}
- Publication years: {'(unknown)': 8}
- DOM characteristics: {'element_count': 1596, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 715, 'top_tags': [('div', 709), ('p', 146), ('li', 141), ('img', 122), ('a', 105), ('style', 97), ('span', 48), ('button', 38), ('ul', 35), ('script', 25), ('link', 21), ('meta', 18)], 'top_classes': [('aem-gridcolumn', 118), ('aem-gridcolumn--default--#', 118), ('cmp-text', 81), ('article-rich-text', 75), ('aem-grid', 48), ('aem-grid--#', 48), ('aem-grid--default--#', 48), ('table__row', 42), ('table__row-#', 42), ('table__cell', 42), ('table__cell--col-#', 42), ('table__cell--row-#', 42)], 'heading_counts': {'h1': 1, 'h6': 3, 'h2': 6, 'h3': 15, 'h4': 9}}

### 0.90-9

- Pages: **8** (1.42% of corpus)
- Representative guide: **Call of Duty | Guides - Modern Warfare III COD 101**
- Representative URL: `https://www.callofduty.com/guides/getting-started/call-of-duty-modern-warfare-iii-play-guides-getting-started-cod-101`
- Representative source file: `call-of-duty-modern-warfare-iii-play-guides-getting-started-cod-101-2294a0becb.html`
- Title families: {'Modern Warfare III': 8}
- Guide categories: {'Mode': 4, 'Weapon': 2, 'Operator': 2}
- Experiences: {'(blank)': 8}
- Publication years: {'(unknown)': 8}
- DOM characteristics: {'element_count': 900, 'max_depth': 23, 'main_count': 1, 'article_count': 0, 'section_count': 3, 'container_count': 159, 'top_tags': [('a', 176), ('li', 157), ('div', 146), ('p', 114), ('span', 76), ('ul', 42), ('img', 31), ('i', 25), ('script', 21), ('meta', 21), ('button', 16), ('b', 15)], 'top_classes': [('aem-gridcolumn', 21), ('aem-gridcolumn--default--#', 21), ('link-icon', 16), ('expand-arrow', 16), ('dd', 15), ('visually-hidden', 10), ('article-image-container', 10), ('aem-grid', 8), ('aem-grid--#', 8), ('aem-grid--default--#', 8), ('nav-expand-content', 7), ('flag-en', 6)], 'heading_counts': {'h2': 6, 'h1': 8}}

### 0.90-10

- Pages: **8** (1.42% of corpus)
- Representative guide: **Call of Duty®: Warzone™ | Warzone Tac Map**
- Representative URL: `https://callofduty.com/guides/tac-atlas-urzikstan`
- Representative source file: `tac-atlas-urzikstan-7fa92103ff.html`
- Title families: {'(blank)': 8}
- Guide categories: {'Map': 8}
- Experiences: {'Warzone': 8}
- Publication years: {'(unknown)': 8}
- DOM characteristics: {'element_count': 1763, 'max_depth': 24, 'main_count': 0, 'article_count': 0, 'section_count': 4, 'container_count': 320, 'top_tags': [('img', 344), ('div', 308), ('li', 300), ('a', 195), ('p', 128), ('button', 96), ('span', 90), ('ul', 71), ('style', 49), ('h4', 47), ('script', 23), ('meta', 21)], 'top_classes': [('lazy', 163), ('map-overlay', 120), ('legend-btn', 65), ('icon-inactive', 65), ('icon-active', 65), ('sector-zone-#', 48), ('zone-item', 48), ('zone-item_image', 48), ('zone-item_description', 48), ('zone-item_title', 47), ('expand-arrow', 30), ('dd', 20)], 'heading_counts': {'h2': 5, 'h1': 1, 'h3': 12, 'h4': 47}}

### 0.90-11

- Pages: **6** (1.06% of corpus)
- Representative guide: **Call of Duty®: Guides | Black Ops 6**
- Representative URL: `https://callofduty.com/guides/blackops6`
- Representative source file: `blackops6-98afa6baff.html`
- Title families: {'Black Ops 6': 2, 'Black Ops 7': 2, '(blank)': 2}
- Guide categories: {'Guide': 4, 'Mode': 2}
- Experiences: {'(blank)': 6}
- Publication years: {'(unknown)': 6}
- DOM characteristics: {'element_count': 1839, 'max_depth': 24, 'main_count': 0, 'article_count': 0, 'section_count': 7, 'container_count': 788, 'top_tags': [('div', 772), ('a', 259), ('li', 215), ('span', 102), ('img', 99), ('ul', 78), ('style', 75), ('p', 73), ('button', 34), ('script', 32), ('link', 24), ('meta', 23)], 'top_classes': [('aem-gridcolumn', 93), ('aem-gridcolumn--default--#', 93), ('guide-grid-item', 68), ('cod-guide-grid-item-component', 68), ('guide-grid-item-container', 68), ('cod-guide-grid-item-component-inner-container', 68), ('cod-guide-grid-item-component__graphic', 68), ('cod-guide-grid-item-component__graphic-overlay', 68), ('cod-guide-grid-item-component__text', 68), ('cod-guide-grid-item-component__text-eyebrow', 68), ('cod-guide-grid-item-component__text-title', 68), ('widescreen-item', 47)], 'heading_counts': {'h2': 7, 'h1': 2, 'h3': 3}}

### 0.90-12

- Pages: **4** (0.71% of corpus)
- Representative guide: **Call of Duty | Guides - Modern Warfare Zombies Bestiary**
- Representative URL: `https://callofduty.com/guides/zombies/call-of-duty-guides-modern-warfare-zombies-missions-and-progression`
- Representative source file: `call-of-duty-guides-modern-warfare-zombies-missions-and-progression-65c4c91cf5.html`
- Title families: {'(blank)': 4}
- Guide categories: {'Mode': 2, 'Guide': 2}
- Experiences: {'Zombies': 2, 'Warzone': 2}
- Publication years: {'(unknown)': 4}
- DOM characteristics: {'element_count': 1595, 'max_depth': 23, 'main_count': 1, 'article_count': 0, 'section_count': 3, 'container_count': 699, 'top_tags': [('div', 686), ('a', 187), ('p', 181), ('li', 167), ('span', 98), ('img', 47), ('ul', 43), ('script', 23), ('meta', 20), ('i', 20), ('link', 16), ('button', 16)], 'top_classes': [('aem-gridcolumn', 89), ('aem-gridcolumn--default--#', 89), ('cmp-text', 65), ('atvi-rich-text', 60), ('table__cell', 55), ('table__cell--col-#', 55), ('table__cell--row-#', 55), ('aem-grid', 52), ('aem-grid--#', 52), ('aem-grid--default--#', 52), ('table__cell--key', 44), ('table__cell--value', 44)], 'heading_counts': {'h2': 10, 'h1': 11, 'h4': 4}}

### 0.90-13

- Pages: **4** (0.71% of corpus)
- Representative guide: **Call of Duty®: Guides | Call of Duty Mobile**
- Representative URL: `https://callofduty.com/guides/mobile`
- Representative source file: `mobile-bc714ae296.html`
- Title families: {'(blank)': 4}
- Guide categories: {'Guide': 4}
- Experiences: {'(blank)': 2, 'Warzone': 2}
- Publication years: {'(unknown)': 4}
- DOM characteristics: {'element_count': 986, 'max_depth': 24, 'main_count': 0, 'article_count': 0, 'section_count': 6, 'container_count': 230, 'top_tags': [('div', 215), ('a', 194), ('li', 174), ('span', 99), ('p', 71), ('ul', 46), ('img', 34), ('script', 30), ('link', 23), ('button', 22), ('meta', 19), ('style', 8)], 'top_classes': [('expand-arrow', 30), ('aem-gridcolumn', 25), ('aem-gridcolumn--default--#', 25), ('dd', 20), ('link-icon', 16), ('nav-expand-content', 13), ('visually-hidden', 10), ('atvi-module-container', 9), ('aem-grid', 8), ('aem-grid--#', 8), ('aem-grid--default--#', 8), ('logged-out', 6)], 'heading_counts': {'h2': 6, 'h1': 2, 'h3': 3}}

### 0.90-14

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Level Unlocks: Player Level 1-55**
- Representative URL: `https://www.callofduty.com/guides/blackops6/getting-started/call-of-duty-guides-black-ops-6-level-unlocks-player-level-1-55`
- Representative source file: `call-of-duty-guides-black-ops-6-level-unlocks-player-level-1-55-563871bcd0.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Guide': 2}
- Experiences: {'(blank)': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 2709, 'max_depth': 24, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 1817, 'top_tags': [('div', 1811), ('p', 178), ('b', 135), ('style', 134), ('a', 109), ('li', 96), ('img', 74), ('span', 58), ('ul', 27), ('script', 22), ('meta', 19), ('link', 19)], 'top_classes': [('aem-grid', 226), ('aem-grid--#', 226), ('aem-grid--default--#', 226), ('table__cell', 224), ('table__cell--col-#', 224), ('table__cell--row-#', 224), ('table__cell--content', 220), ('table__cell--value', 220), ('aem-gridcolumn', 194), ('aem-gridcolumn--default--#', 194), ('table__cell--key', 165), ('article-rich-text', 133)], 'heading_counts': {'h1': 1, 'h4': 1, 'h2': 2}}

### 0.90-15

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Beta — Everything You Need to Know**
- Representative URL: `https://callofduty.com/guides/blackops6/getting-started/call-of-duty-guides-black-ops-6-multiplayer-beta-everything-you-need-to-know`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-beta-everything-you-need-to-know-ac6946f582.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Guide': 2}
- Experiences: {'Multiplayer': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 2082, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 395, 'top_tags': [('div', 389), ('p', 340), ('a', 206), ('li', 193), ('b', 174), ('h4', 164), ('h3', 110), ('br', 99), ('span', 76), ('img', 63), ('ul', 56), ('i', 54)], 'top_classes': [('aem-gridcolumn', 71), ('aem-gridcolumn--default--#', 71), ('article-image-container', 50), ('img-lazy-container', 32), ('cmp-text', 31), ('expand-arrow', 30), ('article-rich-text', 30), ('article-image', 25), ('atvi-image', 25), ('article-image-component', 25), ('lazy', 25), ('align-left', 24)], 'heading_counts': {'h2': 25, 'h1': 1, 'h6': 5, 'h3': 110, 'h4': 164}}

### 0.90-16

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Guide — COD 101 - READ THIS FIRST**
- Representative URL: `https://callofduty.com/guides/blackops6/getting-started/call-of-duty-guides-black-ops-6-multiplayer-guide-cod-101-read-this-first`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-guide-cod-101-read-this-first-8084da5b9e.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Guide': 2}
- Experiences: {'Multiplayer': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 681, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 143, 'top_tags': [('div', 137), ('p', 107), ('a', 105), ('li', 82), ('span', 45), ('script', 26), ('img', 26), ('ul', 21), ('i', 21), ('meta', 20), ('link', 19), ('style', 12)], 'top_classes': [('aem-gridcolumn', 25), ('aem-gridcolumn--default--#', 25), ('expand-arrow', 16), ('article-rich-text', 12), ('cmp-text', 12), ('article-image-container', 10), ('dd', 7), ('nav-expand-content', 7), ('article_rich_text_#-#', 7), ('aem-grid', 6), ('aem-grid--#', 6), ('aem-grid--default--#', 6)], 'heading_counts': {'h1': 1, 'h6': 1, 'h2': 6, 'h3': 8, 'h4': 9}}

### 0.90-17

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer: How to Play**
- Representative URL: `https://callofduty.com/guides/blackops6/training/call-of-duty-guides-black-ops-6-multiplayer-how-to-play`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-how-to-play-379fac00d4.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Guide': 2}
- Experiences: {'Multiplayer': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 1573, 'max_depth': 24, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 561, 'top_tags': [('div', 555), ('p', 198), ('a', 148), ('li', 144), ('b', 119), ('span', 68), ('style', 65), ('h4', 51), ('img', 49), ('ul', 40), ('script', 24), ('link', 20)], 'top_classes': [('aem-gridcolumn', 90), ('aem-gridcolumn--default--#', 90), ('cmp-text', 62), ('article-rich-text', 58), ('article-image-container', 40), ('aem-grid', 34), ('aem-grid--#', 34), ('aem-grid--default--#', 34), ('table__cell', 32), ('table__cell--col-#', 32), ('table__cell--row-#', 32), ('expand-arrow', 30)], 'heading_counts': {'h1': 2, 'h6': 6, 'h2': 10, 'h3': 7, 'h4': 51}}

### 0.90-18

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Guide — Leveling Up and Progression**
- Representative URL: `https://www.callofduty.com/guides/blackops6/training/call-of-duty-guides-black-ops-6-multiplayer-leveling-up-and-progression`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-leveling-up-and-progression-5389470c33.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Progression': 2}
- Experiences: {'Multiplayer': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 694, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 190, 'top_tags': [('div', 184), ('li', 98), ('a', 91), ('p', 74), ('span', 44), ('img', 33), ('ul', 25), ('script', 23), ('i', 21), ('meta', 20), ('link', 19), ('style', 19)], 'top_classes': [('aem-gridcolumn', 33), ('aem-gridcolumn--default--#', 33), ('article-image-container', 20), ('cmp-text', 17), ('expand-arrow', 16), ('article-rich-text', 16), ('article-image', 10), ('atvi-image', 10), ('article-image-component', 10), ('img-lazy-container', 10), ('lazy', 10), ('article_rich_text_#--#', 9)], 'heading_counts': {'h1': 1, 'h6': 2, 'h2': 7, 'h3': 5}}

### 0.90-19

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer Mode Guide — Kill Order**
- Representative URL: `https://www.callofduty.com/guides/blackops6/modes/call-of-duty-guides-black-ops-6-multiplayer-mode-kill-order`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-mode-kill-order-2bc2655337.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Mode': 2}
- Experiences: {'Multiplayer': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 787, 'max_depth': 23, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 223, 'top_tags': [('div', 216), ('a', 99), ('li', 97), ('p', 90), ('span', 52), ('img', 29), ('ul', 28), ('script', 24), ('b', 24), ('meta', 21), ('link', 20), ('style', 16)], 'top_classes': [('aem-gridcolumn', 24), ('aem-gridcolumn--default--#', 24), ('expand-arrow', 16), ('cmp-text', 14), ('article-rich-text', 13), ('aem-grid', 12), ('aem-grid--#', 12), ('aem-grid--default--#', 12), ('tag-item', 10), ('table__cell', 8), ('table__cell--col-#', 8), ('table__cell--row-#', 8)], 'heading_counts': {'h1': 7, 'h6': 1, 'h2': 4, 'h4': 2, 'h3': 16}}

### 0.90-20

- Pages: **2** (0.35% of corpus)
- Representative guide: **Call of Duty | Guides - Black Ops 6 Multiplayer: Pre-Game — Weapons & Loadouts**
- Representative URL: `https://www.callofduty.com/guides/blackops6/pre-game/call-of-duty-guides-black-ops-6-multiplayer-pre-game-weapons-and-loadouts`
- Representative source file: `call-of-duty-guides-black-ops-6-multiplayer-pre-game-weapons-and-loadouts-9fd8e38841.html`
- Title families: {'Black Ops 6': 2}
- Guide categories: {'Weapon': 2}
- Experiences: {'Multiplayer': 2}
- Publication years: {'(unknown)': 2}
- DOM characteristics: {'element_count': 4190, 'max_depth': 22, 'main_count': 1, 'article_count': 0, 'section_count': 2, 'container_count': 2207, 'top_tags': [('div', 2201), ('p', 706), ('style', 342), ('b', 319), ('h4', 119), ('a', 113), ('li', 95), ('span', 54), ('img', 48), ('ul', 29), ('h3', 29), ('script', 23)], 'top_classes': [('aem-gridcolumn', 373), ('aem-gridcolumn--default--#', 373), ('article-rich-text', 330), ('cmp-text', 330), ('aem-grid', 287), ('aem-grid--#', 287), ('aem-grid--default--#', 287), ('table__cell', 281), ('table__cell--col-#', 281), ('table__cell--row-#', 281), ('table__cell--value', 281), ('table__row', 130)], 'heading_counts': {'h1': 12, 'h6': 9, 'h2': 10, 'h3': 29, 'h4': 119}}

## Metadata Association and Interpretation

Metadata was used only after structural grouping to test association; it was not included in fingerprints.

- Exact/near families should be compared with title and guide-category distributions in the machine-readable inventory.
- Largest-family metadata purity at threshold 0.90: {'page_count': 120, 'title_family_purity': 0.733, 'category_purity': 0.717, 'experience_purity': 0.733, 'summary': {'title_families': {'(blank)': 88, 'Black Ops 7': 32}, 'categories': {'(blank)': 86, 'Map': 34}, 'experiences': {'(blank)': 88, 'Multiplayer': 32}, 'publication_years': {'(unknown)': 120}}}
- Largest-family metadata purity at threshold 0.80: {'page_count': 250, 'title_family_purity': 0.52, 'category_purity': 0.464, 'experience_purity': 0.472, 'summary': {'title_families': {'(blank)': 116, 'Black Ops 6': 130, 'Black Ops 7': 4}, 'categories': {'(blank)': 116, 'Guide': 18, 'Progression': 2, 'Map': 82, 'Mode': 30, 'Weapon': 2}, 'experiences': {'(blank)': 118, 'Multiplayer': 114, 'Zombies': 18}, 'publication_years': {'(unknown)': 250}}}

### Difference Diagnosis

- **Shared page shell vs. meaningful layout**: duplicate and high-similarity groups indicate a shared shell where pages differ mainly in content-bearing nodes excluded from the fingerprint.
- **Historical redesigns**: multiple persistent families with distinct container/class structures and year/title mixtures are evidence of more than one shell; publication-year concentrations should be treated as supporting, not definitive, evidence.
- **Title-specific templates**: a family dominated by one title family but structurally distinct from other title families supports title-specific layout variation.
- **Guide-type-specific templates**: category-pure families support map/mode/weapon-specific layouts; mixed families indicate shared shell reuse.
- **Random/inconsistent markup**: singleton-heavy distributions and low-threshold fragmentation indicate residual markup variation or page-specific modules.

## Assessment

**MODERATELY TEMPLATIZABLE**

At the 0.90 diagnostic threshold, 47 structural families were observed and the largest covered 21.3% of pages. The concentration of the largest ten families was 87.2%, while exact fingerprints and lower-similarity fragmentation expose meaningful residual variation.

The number of structural families needed for 80%, 90%, 95%, and 99% coverage is reported above. These are diagnostic structural families, not extraction templates.

## Machine-Readable Output

- `data/analysis/guides/dom-structural-families.json` contains per-page fingerprints, family assignments at all thresholds, representative families, metadata summaries, and coverage statistics.

No cleaning or gameplay extraction was performed.
