# Call of Duty Patch-Note Corpus Analysis

## Scope and Method

This deterministic analysis covers all **37** HTML pages in `data/raw/patch_pages/` and the **198** logical update events represented by the existing ledger. It does not modify `data/processed/cod_change_history.csv`, extract individual bullet-level changes, use an LLM, or implement an ontology.

Headings retain original labels and are analyzed with normalized whitespace/case. Hierarchies use HTML heading levels and the nearest preceding lower-level heading. Sections are associated with the most recent dated event when the heading label matches the event index.

## Corpus Summary

- Pages analyzed: **37**
- Update events represented: **198**
- Unique normalized section labels: **1554**
- Total heading occurrences: **6270**
- Maximum observed heading depth: **5**
- Recurring labels: **553**

## 1. Document Structure Inventory

The corpus commonly follows `page title > dated update > surface/system > content category > named entity`. Other recurring patterns include `Weapons > weapon family > named weapon`, `Warzone > Maps/Weapons/Playlist/Ranked Play`, and `ZOMBIES > Weapons/Maps/Modes/Stability`.

Top labels:

| Normalized label | Occurrences |
|---|---|
| stability | 140 |
| ui | 134 |
| weapons | 131 |
| maps | 127 |
| modes | 120 |
| multiplayer | 117 |
| zombies | 107 |
| global | 105 |
| challenges | 94 |
| bug fixes | 94 |
| new | 75 |
| adjusted | 75 |
| ranked play | 72 |
| adjustments | 71 |
| general | 62 |
| gameplay | 61 |
| equipment | 60 |
| perks | 59 |
| assault rifle adjustments | 59 |
| field upgrades | 55 |
| scorestreaks | 49 |
| marksman rifle adjustments | 44 |
| audio | 42 |
| lmg adjustments | 42 |
| smg adjustments | 39 |
| new weapons | 35 |
| weapon adjustments | 34 |
| marksman rifles | 31 |
| events | 30 |
| assault rifles | 30 |
| endgame | 30 |
| killstreaks | 29 |
| new attachments | 28 |
| sniper rifle adjustments | 28 |
| shotgun adjustments | 28 |
| graphics | 27 |
| playlist | 27 |
| gunsmith | 26 |
| gobblegums | 25 |
| enemies | 23 |
| ricochet anti-cheat | 23 |
| smgs | 22 |
| contracts | 22 |
| shotguns | 21 |
| movement | 21 |
| sniper rifles | 21 |
| loot & economy | 21 |
| related articles | 20 |
| mxr-17 | 20 |
| ds20 mirage | 20 |

Representative hierarchy paths include `Weapons > Assault Rifle Adjustments > XM4`, `Warzone > Ranked Play > Skill Rating`, and `ZOMBIES > Weapons > Gunsmith`. Full machine-readable inventories are in `data/analysis/heading_inventory.json`, `heading_labels.json`, and `heading_parent_relationships.json`.

## 2. Experience and Surface Discovery

Counts are pages containing the term in a section heading:

| Surface/system | Pages |
|---|---|
| Ranked Play | 30 |
| UI/UX | 27 |
| Anti-Cheat | 22 |
| Warzone | 21 |
| Audio | 19 |
| Economy/Rewards | 19 |
| Performance/Stability | 18 |
| Multiplayer | 17 |
| Zombies | 16 |
| Movement | 15 |
| Progression | 12 |
| Social | 8 |
| Spawning | 6 |
| Settings | 5 |
| Campaign | 4 |
| Customization | 4 |
| Matchmaking | 3 |
| Network | 1 |

The strongest explicit surfaces are Multiplayer, Warzone, Zombies, Campaign, and Ranked Play. Ranked Play is both a competitive surface and a system/mode category, so it should not yet be forced into one class.

## 3. Content / Entity Candidates

`Pages` means pages with a matching heading; `Events` means page-date boundaries under matching headings. Examples and paths preserve source vocabulary. Some candidates are persistent entities while their plural headings are organization categories.

| Candidate | Pages | Events | Examples | Section paths | Title/experience |
|---|---|---|---|---|---|
| Map | 35 | 42 | Available Maps Per Mode, Available Via Map Loot, Cel-Shaded Map Variants, Freerun: Descent (New Freerun Map) | Call of Duty: Black Ops 6 Season 03 Patch Notes > ZOMBIES > Maps; Call of Duty: Black Ops 7 Season 02 Patch Notes > MULTIPLAYER > Maps; Call of Duty: Black Ops 7 Season 03 Patch Notes > ZOMBIES > Maps | Black Ops 6/<NULL>; Black Ops 7/<NULL>; <NULL>/Warzone |
| Weapon | 37 | 72 | Adjustments for Future Weapon Damage Patch Notes, All Weapons, Black Ops 6 Weapons, Classic Weapons | Call of Duty: Warzone Season 01 Patch Notes > WEAPONS; Call of Duty: Warzone Season 02 Patch Notes > WEAPONS; Call of Duty: Black Ops 6 Season 02 Patch Notes > ZOMBIES > Weapons | <NULL>/Warzone; Black Ops 7/<NULL>; Black Ops 6/<NULL> |
| Attachment | 33 | 40 | ATTACHMENT ADJUSTMENTS, Apex Attachment: M4 Hurricane, Attachment Adjustments, Attachment Restrictions | Call of Duty: Black Ops 6 Season 03 Patch Notes > WELCOME TO SEASON 03 RELOADED > New Attachment; Call of Duty: Black Ops 6 Season 03 Patch Notes > WELCOME TO SEASON 03 > New Attachments; Call of Duty: Warzone Season 01 Patch Notes > WEAPONS > New Attachments | <NULL>/Warzone; Black Ops 6/<NULL>; Black Ops 7/<NULL> |
| Mode | 37 | 61 | Astra Malorum: Directed Mode, Available Maps Per Mode, Black Ops Classic (New Mode), Cursed Mode: Ashwood (Launch) | Call of Duty: Warzone Season 01 Patch Notes > PLAYLIST; Call of Duty: Black Ops 7 Season 02 Patch Notes > MULTIPLAYER > Modes; Call of Duty: Warzone Season 01 Patch Notes > MODES | Black Ops 7/<NULL>; Black Ops 6/<NULL>; <NULL>/Warzone |
| Operator | 11 | 12 | New Endgame Feature: Operator Prestige, New Operators, New Operators (Multiplayer & Zombies), OPERATORS | Call of Duty: Black Ops 6 Season 03 Patch Notes > WELCOME TO SEASON 03 > New Operators; Call of Duty: Black Ops 6 Preseason Patch Notes > Monday, November 4, 2024 - 10 am/PT > GLOBAL > Operators; Call of Duty: Black Ops 6 Preseason Patch Notes > Saturday, October 26th, 2024 > GLOBAL > Operators | Black Ops 6/<NULL>; <NULL>/Warzone; Black Ops 7/<NULL> |
| Vehicle | 13 | 15 | VEHICLES, Vehicle Vulnerability, Vehicles, » VEHICLES « | Call of Duty: Warzone Season 03 Reloaded Patch Notes > VEHICLES; Call of Duty: Warzone Season 01 Patch Notes > VEHICLES; Call of Duty: Black Ops 6 Preseason Patch Notes > Friday, November 8, 2024 > ZOMBIES > Vehicles | <NULL>/Warzone; Black Ops 7/<NULL>; Black Ops 6/<NULL> |
| Equipment | 29 | 39 | Available Equipment, EQUIPMENT, EQUIPMENT & KILLSTREAKS, Equipment | Call of Duty: Black Ops 7 Season 01 Patch Notes > MULTIPLAYER > Equipment; Call of Duty: Black Ops 7 Season 02 Patch Notes > MULTIPLAYER > Equipment; Call of Duty: Warzone Season 01 Patch Notes > EQUIPMENT | <NULL>/Warzone; Black Ops 7/<NULL>; Black Ops 6/<NULL> |
| Perk | 30 | 36 | Available Perks, Equipment, Perks, Field Upgrades, and Wildcards, Lootable Perks, New Multiplayer Perk | Call of Duty: Black Ops 6 Season 03 Patch Notes > ZOMBIES > Perks; Call of Duty: Black Ops 7 Season 03 Patch Notes > ZOMBIES > Perk-a-Colas; Call of Duty: Warzone Season 01 Patch Notes > PERKS | Black Ops 6/<NULL>; <NULL>/Warzone; Black Ops 7/<NULL> |
| Scorestreak/Killstreak | 29 | 40 | Available Killstreaks, EQUIPMENT & KILLSTREAKS, KILLSTREAKS, Killstreak Adjustments | Call of Duty: Black Ops 7 Season 02 Patch Notes > MULTIPLAYER > Scorestreaks; Call of Duty: Black Ops 7 Season 01 Patch Notes > MULTIPLAYER > Scorestreaks; Call of Duty: Black Ops 7 Season 03 Patch Notes > MULTIPLAYER > Scorestreaks | Black Ops 6/<NULL>; Black Ops 7/<NULL>; <NULL>/Warzone |
| Field Upgrade | 24 | 28 | Available Field Upgrades, Equipment, Perks, Field Upgrades, and Wildcards, FIELD UPGRADES, Field Upgrade | Call of Duty: Black Ops 7 Season 02 Patch Notes > ZOMBIES > Field Upgrades; Call of Duty: Black Ops 6 Season 03 Patch Notes > ZOMBIES > Field Upgrades; Call of Duty: Black Ops 7 Season 03 Patch Notes > MULTIPLAYER > Field Upgrades | Black Ops 7/<NULL>; Black Ops 6/<NULL>; <NULL>/Warzone |
| Challenge | 22 | 25 | Abomination Challenge (Launch Window), CHALLENGES, Call of Duty Endowment C.O.D.E. Navigator Challenge, Calling Card Challenges | Call of Duty: Black Ops 7 Season 02 Patch Notes > ZOMBIES > Challenges; Call of Duty: Black Ops 7 Preseason Patch Notes > MULTIPLAYER > Challenges; Call of Duty: Black Ops 7 Season 02 Patch Notes > MULTIPLAYER > Challenges | Black Ops 7/<NULL>; Black Ops 6/<NULL>; <NULL>/Warzone |
| Camo | 6 | 6 | CAMOS, Camo Challenges, Camos, Camos & Camo Challenges | Call of Duty: Black Ops 6 Season 03 Patch Notes > MULTIPLAYER > Camos; Call of Duty: Black Ops 6 Season 01 Patch Notes > GLOBAL > Camos; Call of Duty: Black Ops 6 Season 02 Patch Notes > GLOBAL > CHALLENGES > Camos & Camo Challenges | Black Ops 6/<NULL>; <NULL>/Warzone; Black Ops 7/<NULL> |
| Battle Pass | 11 | 11 | BATTLE PASS, Battle Pass, Dresden 9mm - SMG (Battle Pass), EGRT-17 (Assault Rifle, Battle Pass) | Call of Duty: Warzone Season 01 Patch Notes > BATTLE PASS; Call of Duty: Black Ops 6 Season 01 Patch Notes > Friday, November 15, 2024 > GLOBAL > Battle Pass; Call of Duty: Black Ops 6 Season 02 Patch Notes > GLOBAL > BATTLE PASS | <NULL>/Warzone; Black Ops 6/<NULL>; Black Ops 7/<NULL> |
| Event | 33 | 43 | Combat Bow (Event Reward), EVENTS, Events, GPR91 Double-Barrel Conversion (Event Reward) | Call of Duty: Warzone Season 01 Patch Notes > EVENTS; Call of Duty: Warzone Season 02 Patch Notes > EVENTS; Call of Duty: Warzone Season 03 Patch Notes > PUBLIC EVENTS | <NULL>/Warzone; Black Ops 6/<NULL>; Black Ops 7/<NULL> |
| Contract | 15 | 19 | Available Contracts, CONTRACTS, Contract Adjustments, Contract Reveal Timing | Call of Duty: Warzone Season 03 Reloaded Patch Notes > CONTRACTS; Call of Duty: Warzone Season 01 Patch Notes > CONTRACTS; Call of Duty: Warzone Season 02 Patch Notes > CONTRACTS | <NULL>/Warzone |
| Loot | 24 | 33 | Available Via Map Loot, LOOT, LOOT & ECONOMY, Loot | Call of Duty: Warzone Season 03 Patch Notes > LOOT & ECONOMY; Call of Duty: Warzone Season 03 Reloaded Patch Notes > LOOT & ECONOMY; Call of Duty: Warzone Season 05 Patch Notes > LOOT & ECONOMY | <NULL>/Warzone; Black Ops 6/<NULL>; Black Ops 7/<NULL> |

Strong persistent-entity candidates are named maps, weapons, attachments, operators, vehicles, perks, equipment, scorestreaks/killstreaks, field upgrades, and named modes. Maps, Weapons, Events, Challenges, Battle Pass, Camos, Contracts, and Loot can also function as document organization or time-bounded content categories.

## 4. Game-System Candidates

| System candidate | Pages | Events | Examples | Section paths | Title/experience |
|---|---|---|---|---|---|
| Multiplayer | 17 | 24 | MULTIPLAYER, Multiplayer, Multiplayer Map Adjustments, Multiplayer Ranked Play | Call of Duty: Black Ops 7 Season 02 Patch Notes > MULTIPLAYER; Call of Duty: Black Ops 6 Season 03 Patch Notes > MULTIPLAYER; Call of Duty: Black Ops 7 Season 03 Patch Notes > MULTIPLAYER | Black Ops 6/<NULL>; Black Ops 7/<NULL>; Modern Warfare III/<NULL> |
| Warzone | 21 | 26 | CALL OF DUTY: WARZONE, CALL OF DUTY: WARZONE [CONTINUED], Call of Duty: Warzone Season 01 Patch Notes, Call of Duty: Warzone Season 01 Reloaded Patch Notes | Call of Duty: Modern Warfare 4 Beta Patch Notes > WARZONE; Call of Duty: Warzone Season 01 Patch Notes; Call of Duty: Warzone Season 01 Patch Notes > WARZONE | <NULL>/Warzone; Modern Warfare 4/<NULL> |
| Zombies | 16 | 19 | AK-74 Zombies Adjustments, AMES 85 Zombies Adjustments, AS VAL Zombies Adjustments, GPR-91 Zombies Adjustments | Call of Duty: Black Ops 6 Season 03 Patch Notes > ZOMBIES; Call of Duty: Black Ops 7 Season 02 Patch Notes > ZOMBIES; Call of Duty: Black Ops 7 Season 03 Patch Notes > ZOMBIES | Black Ops 6/<NULL>; Black Ops 7/<NULL>; Modern Warfare III/<NULL> |
| Campaign | 4 | 4 | CAMPAIGN, CO-OP CAMPAIGN, CO-OP CAMPAIGN - General Updates, CO-OP CAMPAIGN / ENDGAME | Call of Duty: Black Ops 7 Preseason Patch Notes > CO-OP CAMPAIGN / ENDGAME; Call of Duty: Black Ops 7 Preseason Patch Notes > CO-OP CAMPAIGN; Call of Duty: Black Ops 7 Season 01 Patch Notes > CO-OP CAMPAIGN / ENDGAME | Black Ops 7/<NULL>; Black Ops 6/<NULL> |
| Ranked Play | 30 | 51 | Black Ops 7 Ranked Play, Multiplayer Ranked Play, Multiplayer Ranked Play: Ranking System Update, New Ranked Play Season | Call of Duty: Black Ops 7 Season 02 Patch Notes > RANKED PLAY; Call of Duty: Warzone Season 02 Patch Notes > RANKED PLAY; Call of Duty: Warzone Season 04 Reloaded Patch Notes > RANKED PLAY | <NULL>/Warzone; Black Ops 7/<NULL>; Black Ops 6/<NULL> |
| Movement | 15 | 19 | MOVEMENT, Movement, Movement Adjustments, Movement Updates | Call of Duty: Warzone Season 01 Patch Notes > MOVEMENT; Call of Duty: Black Ops 6 Season 03 Patch Notes > GLOBAL > Movement; Call of Duty: Black Ops 6 Season 03 Patch Notes > GLOBAL > Movement Updates | Black Ops 6/<NULL>; <NULL>/Warzone; Black Ops 7/<NULL> |
| Spawning | 6 | 7 | SPAWNS, Spawns, Weapon XP, Overclock Earn Rates, Spawns, Bug Fixes | Call of Duty: Black Ops 6 Season 02 Patch Notes > MULTIPLAYER > Spawns; Call of Duty: Black Ops 6 Season 03 Patch Notes > Multiplayer > Spawns; Call of Duty: Black Ops 6 Preseason Patch Notes > Monday, November 4, 2024 - 10 am/PT > MULTIPLAYER > Spawns | Black Ops 6/<NULL>; Black Ops 7/<NULL>; Modern Warfare 4/<NULL> |
| Matchmaking | 3 | 3 | Launch Matchmaking, Matchmaking, Matchmaking Update, Matchmaking and Open Moshpit | Call of Duty: Black Ops 6 Preseason Patch Notes > Saturday, October 26th, 2024 > MULTIPLAYER > Matchmaking; Call of Duty: Black Ops 6 Season 01 Patch Notes > RANKED PLAY > Launch Preparations > Launch Matchmaking; Call of Duty: Black Ops 7 Beta Patch Notes > Beta Takeaways > Matchmaking Update | Black Ops 6/<NULL>; Black Ops 7/<NULL> |
| Progression | 12 | 13 | New Endgame Feature: Operator Prestige, New Prestige, PROGRESSION, PROGRESSION & PRESTIGE | Call of Duty: Black Ops 6 Season 03 Patch Notes > MULTIPLAYER > Ranks + Prestige; Call of Duty: Black Ops 6 Preseason Patch Notes > Monday, November 4, 2024 - 10 am/PT > GLOBAL > Progression; Call of Duty: Black Ops 6 Preseason Patch Notes > Friday, November 1, 2024 > MULTIPLAYER > Progression | Black Ops 6/<NULL>; Black Ops 7/<NULL>; Modern Warfare 4/<NULL> |
| Audio | 19 | 26 | AUDIO, Audio | Call of Duty: Modern Warfare 4 Beta Patch Notes > AUDIO; Call of Duty: Black Ops 7 Season 01 Patch Notes > MULTIPLAYER > Audio; Call of Duty: Black Ops 7 Season 04 Patch Notes > ZOMBIES > Audio | Black Ops 7/<NULL>; Black Ops 6/<NULL>; <NULL>/Warzone |
| UI/UX | 27 | 35 | CALL OF DUTY UI & CROSS-LAUNCHING, UI, UI & UX, UI (Multiplayer & Zombies) | Call of Duty: Black Ops 7 Season 02 Patch Notes > ZOMBIES > UI; Call of Duty: Black Ops 6 Season 03 Patch Notes > MULTIPLAYER > UI; Call of Duty: Black Ops 6 Season 04 Patch Notes > MULTIPLAYER > UI | Black Ops 6/<NULL>; Black Ops 7/<NULL>; <NULL>/Warzone |
| Performance/Stability | 18 | 22 | Bugs and Stability, PERFORMANCE, Performance, Stability | Call of Duty: Black Ops 7 Preseason Patch Notes > ZOMBIES > Stability; Call of Duty: Black Ops 6 Season 03 Patch Notes > MULTIPLAYER > Stability; Call of Duty: Black Ops 7 Preseason Patch Notes > MULTIPLAYER > Stability | Black Ops 7/<NULL>; Black Ops 6/<NULL>; <NULL>/Warzone |
| Network | 1 | 1 | Disconnect Protection | Call of Duty: Black Ops 7 Preseason Patch Notes > CO-OP CAMPAIGN / ENDGAME > Disconnect Protection | Black Ops 7/<NULL> |
| Anti-Cheat | 22 | 22 | #TEAMRICOCHET, ANTI-CHEAT, RICOCHET ANTI-CHEAT, RICOCHET ANTICHEAT | Call of Duty: Black Ops 6 Season 03 Patch Notes > GLOBAL > Ricochet Anti-Cheat; Call of Duty: Black Ops 6 Season 03 Patch Notes > GLOBAL > RICOCHET Anti-Cheat; Call of Duty: Warzone Season 01 Patch Notes > RICOCHET ANTI-CHEAT | Black Ops 6/<NULL>; <NULL>/Warzone; Black Ops 7/<NULL> |
| Social | 8 | 8 | Additional Social Features, Join on Friends, New Event: Nuketown Block Party (MP, ZM), Party Games Return | Call of Duty: Black Ops 6 Season 01 Patch Notes > RANKED PLAY > Additional Social Features; Call of Duty: Black Ops 6 Season 02 Patch Notes > JANUARY 31 > GLOBAL > Join on Friends; Call of Duty: Black Ops 6 Season 02 Patch Notes > GLOBAL > SOCIAL & CHANNELS | Black Ops 6/<NULL>; Black Ops 7/<NULL>; <NULL>/Warzone |
| Settings | 5 | 5 | Competitive Settings, Competitive Settings Overview, Console Cross-Play Settings, SETTINGS | Call of Duty: Black Ops 6 Season 03 Patch Notes > GLOBAL > Console Cross-Play Settings; Call of Duty: Black Ops 6 Preseason Patch Notes > Friday, November 1, 2024 > GLOBAL > Settings; Call of Duty: Black Ops 6 Preseason Patch Notes > Saturday, October 26th, 2024 > GLOBAL > Settings | Black Ops 6/<NULL>; <NULL>/Warzone; Modern Warfare III/<NULL> |
| Customization | 4 | 5 | CUSTOMIZATION, Customization | Call of Duty: Warzone Season 6 Patch Notes > CUSTOMIZATION; Call of Duty: Black Ops 7 Season 02 Patch Notes > GLOBAL > Customization; Call of Duty: Warzone Season 03 Patch Notes > CUSTOMIZATION | <NULL>/Warzone; Modern Warfare III/<NULL>; Black Ops 7/<NULL> |
| Economy/Rewards | 19 | 19 | Breakdown: Rewards, Call of Duty: Black Ops 7 Ranked Series Rewards, Career Rewards, Combat Bow (Event Reward) | Call of Duty: Warzone Season 02 Patch Notes > RANKED PLAY > Rewards; Call of Duty: Black Ops 6 Preseason Patch Notes > Saturday, October 26th, 2024 > STORE; Call of Duty: Black Ops 6 Season 01 Patch Notes > Thursday, December 12, 2024 > GLOBAL > Store | Black Ops 6/<NULL>; <NULL>/Warzone; Black Ops 7/<NULL> |

Recurring system vocabulary includes movement, spawning, progression/prestige, audio, UI/UX, stability/performance, network/disconnect protection, matchmaking, Ranked Play, Anti-Cheat/RICOCHET, settings, customization, social, and economy/rewards.

## 5. Change Language

| Observed change family | Visible-text mentions |
|---|---|
| increased/buffed | 4662 |
| modified/adjusted | 4427 |
| fixed/resolved | 3541 |
| improved | 3012 |
| introduced/added | 2229 |
| decreased/nerfed | 2189 |
| removed | 500 |
| balanced | 152 |
| enabled | 98 |
| disabled | 93 |

Underlying source terms include `added`, `new`, `introduced`, `now available`, `adjusted`, `changed`, `modified`, `updated`, `tuned`, `increased`, `boosted`, `buffed`, `decreased`, `reduced`, `nerfed`, `fixed`, `resolved`, `removed`, `disabled`, `enabled`, and `improved`. Possible later families are introduction/availability, modification/balance, magnitude increase, magnitude decrease, defect correction, lifecycle/state, and quality improvement. Raw terms should remain available.

## 6. Hierarchy and Authoring

- Maximum observed heading depth: **5**.
- Entity names commonly appear as headings, especially weapon names, weapon families, maps, and named modes.
- Individual changes commonly occur in bullets and paragraphs below headings; some pages also use tables and structured navigation anchors.
- Dated boundaries are authored inconsistently: date headings, fragment-link anchors, and page-level `p.dateline` elements coexist.
- Unusual patterns include `Season Updates` plus `Reloaded Updates`, overlapping title/Warzone pages, and daily beta dates.

## 7. Cross-Title Consistency

| Segment | Common concepts | Distinctive structure |
|---|---|---|
| Modern Warfare III | Maps, Weapons, Modes, Playlists, UIX, Gameplay, Stability | Compact dated season sections and separate Warzone pages |
| Black Ops 6 | Weapons, Maps, Modes, Challenges, Progression, Stability, Ranked Play | Preseason/season navigation anchors; title and Warzone page families differ |
| Black Ops 7 | Weapons, Maps, Modes, Zombies, Ranked Play, Stability, UI, Challenges | Extensive Season/Reloaded update groups and anchor-led dates |
| Modern Warfare 4 | Beta update dates and beta-specific content | Long run of daily beta dates and distinctive beta terminology |
| Warzone | Maps, Weapons, Playlist, Ranked Play, Contracts, Loot, Vehicles | Explicit experience surface, sometimes without reliable underlying title |

Common concepts include weapons, maps, modes, challenges, stability/performance, UI, progression, Ranked Play, and Zombies where supported. Terminology varies: `UIX`, `UI/UX`, and `UI` overlap; `Killstreaks` and `Scorestreaks` may be analogous; `Playlists` and `Modes` are adjacent but not always equivalent.

## 8. Long Tail

Labels occurring once or twice include many named maps, named weapons, specialized events, and niche systems. Examples include beta-specific sections, `RICOCHET Anti-Cheat`, `Disconnect Protection`, `Directed Mode`, `Rogue Run`, `Dead Ops Arcade 4`, `Contracts`, `Loot`, `Camos`, `Field Upgrades`, and `Deployment Fees`. The complete rare-label inventory is in `data/analysis/heading_labels.json`; frequency alone should not erase these concepts.

## 9. Candidate Ontology Classification

This is a recommendation only, based on corpus evidence.

- **Persistent entities:** maps, weapons, weapon families, attachments, operators, vehicles, perks, equipment, scorestreaks/killstreaks, field upgrades, modes, playlists, contracts, and named challenges.
- **Experiences/surfaces:** Multiplayer, Warzone, Zombies, Campaign, Ranked Play, Endgame, and other consistently player-facing contexts.
- **Game systems:** Movement, spawning, matchmaking, progression/prestige, audio, UI/UX, performance/stability, networking/disconnect protection, Anti-Cheat/RICOCHET, social, settings, customization, rewards, and economy/store systems.
- **Temporal/release entities:** Season, Preseason, Beta, Reloaded, launch, dated update boundaries, events, and Battle Pass phases.
- **Change/event concepts:** added/introduced, modified/adjusted/tuned, increased/buffed, decreased/reduced/nerfed, fixed/resolved, removed, enabled, disabled, improved, and state transitions.
- **Attributes/properties:** damage, range, rate of fire, movement speed, health, cooldown, duration, XP, score, rank, placement, rewards, availability, restrictions, and costs.
- **Raw evidence initially:** exact bullet prose, HTML structure, source headings, section paths, author/date metadata, patch phrasing, rationale, marketing copy, and ambiguous labels.

## 10. Ambiguities Requiring Human Decisions

- Whether Warzone is an experience attached to a title, a separate product surface, or both.
- Whether Ranked Play is an experience, mode, system, or context-dependent combination.
- Whether Killstreaks and Scorestreaks are separate entities or terminology variants.
- Whether Events, Challenges, Battle Pass, Camos, Contracts, and Loot are entities, temporal content, or organization categories.
- How to represent title-specific versus shared weapons/maps.
- Whether page-level datelines are release metadata or update events when navigation has multiple dates.
- Which rare labels merit canonical entities rather than remaining evidence.

## Final Summary

- Pages analyzed: **37**
- Update events represented: **198**
- Unique section labels: **1554**
- Recurring entity/content categories: **Map, Weapon, Attachment, Mode, Operator, Vehicle, Equipment, Perk, Scorestreak/Killstreak, Field Upgrade, Challenge, Camo, Battle Pass, Event, Contract, Loot**
- Recurring game-system categories: **Multiplayer, Warzone, Zombies, Campaign, Ranked Play, Movement, Spawning, Matchmaking, Progression, Audio, UI/UX, Performance/Stability, Anti-Cheat, Social, Settings, Customization, Economy/Rewards**
- Change verbs/concepts: **increased/buffed, modified/adjusted, fixed/resolved, improved, introduced/added, decreased/nerfed, removed, balanced, enabled, disabled**
- Maximum hierarchy depth: **5**
- Title/experience-specific concepts: title pages and Warzone pages share broad categories but use different section paths; Black Ops 7 is especially anchor-led.
- Long-tail concepts: rare named maps, weapons, events, modes, beta systems, Anti-Cheat, disconnect protection, Rogue Run, and Directed Mode.
- Human decisions: entity versus organization category, surface versus system, terminology equivalence, and page-level dateline semantics.

Machine-readable inventories are under `data/analysis/`.
