#!/usr/bin/env python3
"""Deterministically inventory the preserved Call of Duty patch-note corpus."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/patch_pages"
CSV = ROOT / "data/processed/cod_change_history.csv"
OUT = ROOT / "data/analysis"
REPORT = ROOT / "docs/ontology/corpus-analysis.md"
MONTHS = "January|February|March|April|May|June|July|August|September|October|November|December"
DATE = re.compile(rf"^(?:(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\s+)?(?:{MONTHS})\s+\d{{1,2}}(?:,\s*\d{{4}})?$", re.I)
DATE_TEXT = re.compile(rf"^(?:{MONTHS})\s+\d{{1,2}}(?:,\s*\d{{4}})?$", re.I)

CONTENT = {
    "Map": r"\bmaps?\b", "Weapon": r"\bweapons?\b", "Attachment": r"\battachments?\b",
    "Mode": r"\bmodes?\b|\bplaylists?\b", "Operator": r"\boperators?\b", "Vehicle": r"\bvehicles?\b",
    "Equipment": r"\bequipment\b", "Perk": r"\bperks?\b", "Scorestreak/Killstreak": r"\b(?:score|kill)streaks?\b",
    "Field Upgrade": r"\bfield upgrades?\b", "Challenge": r"\bchallenges?\b", "Camo": r"\bcamos?\b",
    "Battle Pass": r"\bbattle pass\b", "Event": r"\bevents?\b", "Contract": r"\bcontracts?\b", "Loot": r"\bloot\b",
}
SYSTEMS = {
    "Multiplayer": r"\bmultiplayer\b", "Warzone": r"\bwarzone\b", "Zombies": r"\bzombies?\b", "Campaign": r"\bcampaign\b",
    "Ranked Play": r"\branked play\b", "Movement": r"\bmovement\b", "Spawning": r"\bspawns?|spawning\b",
    "Matchmaking": r"\bmatchmaking\b", "Progression": r"\bprogression\b|\bprestige\b", "Audio": r"\baudio\b",
    "UI/UX": r"\bui(?:/ux|/ui)?\b|user interface", "Performance/Stability": r"\bperformance\b|\bstability\b|optimization",
    "Network": r"\bnetwork\b|latency|connection|disconnect", "Anti-Cheat": r"anti-?cheat|ricochet",
    "Social": r"\bsocial\b|friends|party", "Settings": r"\bsettings?\b", "Customization": r"\bcustomization\b|customisation",
    "Economy/Rewards": r"\bstore\b|currency|purchase|buying|rewards?",
}
CHANGES = {
    "introduced/added": r"\b(?:added|add|new|introduced|introducing|now available|available)\b",
    "modified/adjusted": r"\b(?:adjusted|adjustments?|changed|change|modified|modifications?|updated|tuned)\b",
    "increased/buffed": r"\b(?:increased|increase|higher|more|boosted|buffed)\b",
    "decreased/nerfed": r"\b(?:decreased|decrease|lower|less|reduced|nerfed|nerf)\b",
    "fixed/resolved": r"\b(?:fixed|fixes?|resolved|corrected|addressed)\b",
    "removed": r"\b(?:removed|remove|no longer|retired)\b", "disabled": r"\bdisabled\b", "enabled": r"\benabled\b",
    "balanced": r"\bbalance(?:d| changes?)?\b", "improved": r"\b(?:improved|improvement|improvements)\b",
}

def norm(s): return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip().casefold()
def text(s): return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()
def boundary_date(label, page_events):
    label_norm = norm(label)
    for event in page_events:
        if norm(event["update_title"]) == label_norm:
            return event["update_date"]
    match = re.search(rf"({MONTHS})\s+(\d{{1,2}})", label, re.I)
    if not match:
        return None
    month = match.group(1).casefold()
    day = int(match.group(2))
    for event in page_events:
        event_date = __import__("datetime").date.fromisoformat(event["update_date"])
        if event_date.strftime("%B").casefold() == month and event_date.day == day:
            return event["update_date"]
    return None
def md_table(headers, rows):
    return "| " + " | ".join(headers) + " |\n|" + "|".join("---" for _ in headers) + "|\n" + "\n".join("| " + " | ".join(str(x).replace("|", "\\|") for x in row) + " |" for row in rows)
def write_json(name, value):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=True, default=str) + "\n", encoding="utf-8")

def main():
    events = list(csv.DictReader(CSV.open(newline="", encoding="utf-8")))
    files = sorted({x["source_file"].split(" | ")[0] for x in events})
    contexts = []
    all_headings = []
    for filename in files:
        path = RAW / filename
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
        for node in soup(["script", "style", "noscript", "svg"]): node.decompose()
        page_events = [x for x in events if filename in x["source_file"].split(" | ")]
        stack, headings = [], []
        tags = soup.find_all(True)
        positions = {id(node): index for index, node in enumerate(tags)}
        for node in soup.find_all(["h1","h2","h3","h4","h5","h6"]):
            label = text(node.get_text(" "))
            if not label or norm(label) == "choose your region": continue
            level = int(node.name[1])
            while stack and stack[-1][0] >= level: stack.pop()
            path_labels = [x[1] for x in stack] + [label]
            parent = stack[-1][1] if stack else None
            stack.append((level, label))
            item = {"page": filename, "label": label, "normalized_label": norm(label), "level": level, "depth": len(path_labels), "parent": parent, "path": path_labels, "event_date": None, "_position": positions[id(node)]}
            headings.append(item); all_headings.append(item)
        boundaries = []
        for node in tags:
            if node.name == "p" and "dateline" not in (node.get("class") or []):
                continue
            if node.name == "a" and not str(node.get("href", "")).startswith("#"):
                continue
            if node.name not in {"h1", "h2", "h3", "h4", "h5", "h6", "p", "a"}:
                continue
            label = text(node.get_text(" "))
            if label and (DATE.fullmatch(label) or DATE_TEXT.fullmatch(label) or node.name == "p"):
                event_date = boundary_date(label, page_events)
                if event_date:
                    boundaries.append((positions[id(node)], event_date))
        for heading in headings:
            prior = [event_date for position, event_date in boundaries if position <= heading["_position"]]
            heading["event_date"] = prior[-1] if prior else None
            heading.pop("_position", None)
        contexts.append({"file": filename, "soup": soup, "events": page_events, "headings": headings, "text": text(soup.get_text(" "))})

    labels = Counter(x["normalized_label"] for x in all_headings)
    parents = Counter((x["normalized_label"], norm(x["parent"]) if x["parent"] else "<ROOT>") for x in all_headings)
    max_depth = max(x["depth"] for x in all_headings)
    surfaces = Counter()
    for c in contexts:
        for label, pattern in SYSTEMS.items():
            if any(re.search(pattern, heading["label"], re.I) for heading in c["headings"]): surfaces[label] += 1

    def candidate_stats(patterns):
        output = {}
        for category, pattern in patterns.items():
            matched = [x for x in all_headings if re.search(pattern, x["label"], re.I)]
            pages = {x["page"] for x in matched}
            dates = {(x["page"], x["event_date"]) for x in matched if x["event_date"]}
            paths = Counter(" > ".join(x["path"]) for x in matched)
            examples = sorted({x["label"] for x in matched})[:8]
            title_exp = Counter()
            for x in matched:
                if x["event_date"]:
                    for event in next(c["events"] for c in contexts if c["file"] == x["page"]):
                        if event["update_date"] == x["event_date"]: title_exp[(event.get("title") or "<NULL>", event.get("experience") or "<NULL>")] += 1
            output[category] = {"pages": len(pages), "events": len(dates), "examples": examples, "section_paths": paths.most_common(8), "title_experience": title_exp.most_common(8)}
        return output

    content = candidate_stats(CONTENT); systems = candidate_stats(SYSTEMS)
    change_counts = Counter()
    for c in contexts:
        for phrase, pattern in CHANGES.items(): change_counts[phrase] += len(re.findall(pattern, c["text"], re.I))
    title_pages = Counter()
    for c in contexts:
        for event in c["events"]: title_pages[event.get("title") or "<NULL>"] += 1

    write_json("heading_inventory.json", all_headings)
    write_json("heading_labels.json", dict(labels.most_common()))
    write_json("heading_parent_relationships.json", [{"label": a, "parent": b, "count": n} for (a,b),n in parents.most_common()])
    write_json("content_candidates.json", content); write_json("system_candidates.json", systems); write_json("change_language.json", dict(change_counts.most_common()))

    content_rows = [[k,v["pages"],v["events"],", ".join(v["examples"][:4]),"; ".join(p for p,_ in v["section_paths"][:3]),"; ".join(f"{a}/{b}" for (a,b),_ in v["title_experience"][:3])] for k,v in content.items() if v["pages"]]
    system_rows = [[k,v["pages"],v["events"],", ".join(v["examples"][:4]),"; ".join(p for p,_ in v["section_paths"][:3]),"; ".join(f"{a}/{b}" for (a,b),_ in v["title_experience"][:3])] for k,v in systems.items() if v["pages"]]
    recurring = [(k,n) for k,n in labels.items() if n > 1]; rare = [(k,n) for k,n in labels.items() if n <= 2]
    report = f'''# Call of Duty Patch-Note Corpus Analysis

## Scope and Method

This deterministic analysis covers all **{len(contexts)}** HTML pages in `data/raw/patch_pages/` and the **{len(events)}** logical update events represented by the existing ledger. It does not modify `data/processed/cod_change_history.csv`, extract individual bullet-level changes, use an LLM, or implement an ontology.

Headings retain original labels and are analyzed with normalized whitespace/case. Hierarchies use HTML heading levels and the nearest preceding lower-level heading. Sections are associated with the most recent dated event when the heading label matches the event index.

## Corpus Summary

- Pages analyzed: **{len(contexts)}**
- Update events represented: **{len(events)}**
- Unique normalized section labels: **{len(labels)}**
- Total heading occurrences: **{len(all_headings)}**
- Maximum observed heading depth: **{max_depth}**
- Recurring labels: **{len(recurring)}**

## 1. Document Structure Inventory

The corpus commonly follows `page title > dated update > surface/system > content category > named entity`. Other recurring patterns include `Weapons > weapon family > named weapon`, `Warzone > Maps/Weapons/Playlist/Ranked Play`, and `ZOMBIES > Weapons/Maps/Modes/Stability`.

Top labels:

{md_table(["Normalized label", "Occurrences"], [[k,n] for k,n in labels.most_common(50)])}

Representative hierarchy paths include `Weapons > Assault Rifle Adjustments > XM4`, `Warzone > Ranked Play > Skill Rating`, and `ZOMBIES > Weapons > Gunsmith`. Full machine-readable inventories are in `data/analysis/heading_inventory.json`, `heading_labels.json`, and `heading_parent_relationships.json`.

## 2. Experience and Surface Discovery

Counts are pages containing the term in a section heading:

{md_table(["Surface/system", "Pages"], [[k,n] for k,n in surfaces.most_common()])}

The strongest explicit surfaces are Multiplayer, Warzone, Zombies, Campaign, and Ranked Play. Ranked Play is both a competitive surface and a system/mode category, so it should not yet be forced into one class.

## 3. Content / Entity Candidates

`Pages` means pages with a matching heading; `Events` means page-date boundaries under matching headings. Examples and paths preserve source vocabulary. Some candidates are persistent entities while their plural headings are organization categories.

{md_table(["Candidate", "Pages", "Events", "Examples", "Section paths", "Title/experience"], content_rows)}

Strong persistent-entity candidates are named maps, weapons, attachments, operators, vehicles, perks, equipment, scorestreaks/killstreaks, field upgrades, and named modes. Maps, Weapons, Events, Challenges, Battle Pass, Camos, Contracts, and Loot can also function as document organization or time-bounded content categories.

## 4. Game-System Candidates

{md_table(["System candidate", "Pages", "Events", "Examples", "Section paths", "Title/experience"], system_rows)}

Recurring system vocabulary includes movement, spawning, progression/prestige, audio, UI/UX, stability/performance, network/disconnect protection, matchmaking, Ranked Play, Anti-Cheat/RICOCHET, settings, customization, social, and economy/rewards.

## 5. Change Language

{md_table(["Observed change family", "Visible-text mentions"], [[k,n] for k,n in change_counts.most_common()])}

Underlying source terms include `added`, `new`, `introduced`, `now available`, `adjusted`, `changed`, `modified`, `updated`, `tuned`, `increased`, `boosted`, `buffed`, `decreased`, `reduced`, `nerfed`, `fixed`, `resolved`, `removed`, `disabled`, `enabled`, and `improved`. Possible later families are introduction/availability, modification/balance, magnitude increase, magnitude decrease, defect correction, lifecycle/state, and quality improvement. Raw terms should remain available.

## 6. Hierarchy and Authoring

- Maximum observed heading depth: **{max_depth}**.
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

- Pages analyzed: **{len(contexts)}**
- Update events represented: **{len(events)}**
- Unique section labels: **{len(labels)}**
- Recurring entity/content categories: **{", ".join(k for k,v in content.items() if v["pages"] > 1)}**
- Recurring game-system categories: **{", ".join(k for k,v in systems.items() if v["pages"] > 1)}**
- Change verbs/concepts: **{", ".join(k for k,_ in change_counts.most_common())}**
- Maximum hierarchy depth: **{max_depth}**
- Title/experience-specific concepts: title pages and Warzone pages share broad categories but use different section paths; Black Ops 7 is especially anchor-led.
- Long-tail concepts: rare named maps, weapons, events, modes, beta systems, Anti-Cheat, disconnect protection, Rogue Run, and Directed Mode.
- Human decisions: entity versus organization category, surface versus system, terminology equivalence, and page-level dateline semantics.

Machine-readable inventories are under `data/analysis/`.
'''
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(report, encoding="utf-8")

if __name__ == "__main__": main()
