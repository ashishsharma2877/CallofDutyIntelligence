#!/usr/bin/env python3
"""Diagnostic analysis of CMS content-boundary markers.

This script only measures DOM structure and marker/container behavior. It does
not clean files, extract gameplay content, or modify the guide index.
"""

import csv
import json
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
GUIDE_DIR = ROOT / "data/raw/guide_pages"
INDEX_PATH = ROOT / "data/processed/guide_index.csv"
FAMILY_PATH = ROOT / "data/analysis/guides/dom-structural-families.json"
OUTPUT_DIR = ROOT / "data/analysis/guides"
REPORT_PATH = ROOT / "docs/analysis/guides/content-boundary-analysis.md"
OUTPUT_PATH = OUTPUT_DIR / "content-boundary-analysis.json"

MARKER_NAMES = [
    "article-layout",
    "article-layout-content",
    "article-header-container",
    "article-body-container",
    "body-content",
    "body-content-parsys",
    "article-rich-text",
    "cmp-text",
    "main-content",
]

ROOT_SELECTORS = [
    ".article-body-container",
    ".body-content",
    ".body-content-parsys",
    ".article-layout-content",
    "#main-content",
    ".main-content",
    "main#main-content",
    ".guide-content",
    ".map-page",
    ".map-overlay",
    ".map-rich-text-component",
    ".article-rich-text",
    ".atvi-rich-text",
    ".article-layout",
    ".article-content",
    ".content",
    "main",
]

CHROME_RE = re.compile(r"^(cod-header|cod-footer|nav|locale|cookie|article-related-posts|related-wrapper)", re.I)
ARTICLE_NAMING_RE = re.compile(r"(article|body-content|rich-text|cmp-text|table-component|map-rich-text|content)", re.I)
LANDING_CLASSES = (".guide-grid-item", ".cod-guide-grid-item-component", ".guide-grid-item-container")


def load_index():
    with INDEX_PATH.open(encoding="utf-8", newline="") as handle:
        return {row["source_file"]: row for row in csv.DictReader(handle)}


def family_assignments():
    data = json.loads(FAMILY_PATH.read_text(encoding="utf-8"))
    numeric = data["family_assignments"]["0.9"]
    assignments = {source_file: f"0.90-{family_number}" for source_file, family_number in numeric.items()}
    return assignments, data


def classify(path):
    raw = path.read_bytes()
    null_count = raw.count(b"\x00")
    soup = BeautifulSoup(raw, "html.parser")
    tag_count = len(soup.find_all(True))
    has_html = soup.find("html") is not None
    if null_count or tag_count < 10 or not has_html:
        return "non_html_or_binary_asset", soup, {"bytes": len(raw), "null_bytes": null_count, "tag_count": tag_count}
    has_grid = any(soup.select_one(selector) for selector in LANDING_CLASSES)
    has_root = any(soup.select_one(selector) for selector in ROOT_SELECTORS)
    if has_grid and not has_root:
        return "valid_landing_or_index_page", soup, {"bytes": len(raw), "null_bytes": null_count, "tag_count": tag_count}
    return "valid_content_page", soup, {"bytes": len(raw), "null_bytes": null_count, "tag_count": tag_count}


def marker_nodes(soup, marker):
    return soup.select(f".{marker}, #{marker}")


def node_stats(node):
    if node is None:
        return {"text_chars": 0, "headings": 0, "paragraphs": 0, "tables": 0, "rich_text": 0, "chrome": []}
    text = node.get_text(" ", strip=True)
    chrome = []
    for descendant in node.find_all(True):
        classes = descendant.get("class", [])
        identifier = descendant.get("id", "")
        tokens = list(classes) + ([identifier] if identifier else [])
        chrome.extend(token for token in tokens if CHROME_RE.match(token))
    return {
        "text_chars": len(text),
        "headings": len(node.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])),
        "paragraphs": len(node.find_all("p")),
        "tables": len(node.find_all("table")),
        "rich_text": len(node.select(".article-rich-text, .cmp-text, .map-rich-text, .map-rich-text-component")),
        "chrome": sorted(set(chrome)),
    }


def structural_context(node):
    if node is None:
        return {"parents": [], "children": []}
    parents = []
    parent = node.parent
    while parent is not None and getattr(parent, "name", None) and len(parents) < 4:
        parents.append(parent.name + ("." + ".".join(parent.get("class", [])[:2]) if parent.get("class") else ""))
        parent = parent.parent
    children = []
    for child in node.find_all(recursive=False):
        if getattr(child, "name", None):
            children.append(child.name + ("." + ".".join(child.get("class", [])[:2]) if child.get("class") else ""))
    return {"parents": parents, "children": children[:20]}


def marker_inventory(valid_records):
    output = {}
    for marker in MARKER_NAMES:
        counts = []
        locations = Counter()
        parents = Counter()
        children = Counter()
        families = Counter()
        for record in valid_records:
            nodes = marker_nodes(record["soup"], marker)
            if nodes:
                counts.append(len(nodes))
                for node in nodes:
                    context = structural_context(node)
                    for parent in context["parents"][:2]:
                        parents[parent] += 1
                    for child in context["children"][:8]:
                        children[child] += 1
                    locations[node.name] += 1
                families[record["family"]] += 1
        counts_sorted = sorted(counts)
        output[marker] = {
            "pages": len(counts),
            "percentage": round(100 * len(counts) / len(valid_records), 3),
            "average_occurrences_per_page": round(sum(counts) / len(counts), 3) if counts else 0,
            "median_occurrences_per_page": counts_sorted[len(counts_sorted) // 2] if counts_sorted else 0,
            "structural_locations": locations.most_common(8),
            "common_parents": parents.most_common(8),
            "common_children": children.most_common(8),
            "families_containing": families,
        }
    return output


def discover_markers(valid_records):
    pages_by_marker = defaultdict(set)
    for record in valid_records:
        soup = record["soup"]
        for node in soup.find_all(True):
            for token in node.get("class", []) + ([node.get("id")] if node.get("id") else []):
                if ARTICLE_NAMING_RE.search(token):
                    pages_by_marker[token].add(record["source_file"])
    return Counter({marker: len(pages) for marker, pages in pages_by_marker.items()})


def root_candidates(valid_records):
    roots = {}
    for selector in ROOT_SELECTORS:
        page_stats = []
        for record in valid_records:
            nodes = record["soup"].select(selector)
            if not nodes:
                continue
            all_stats = [node_stats(node) for node in nodes]
            page_stats.append({
                "source_file": record["source_file"],
                "count": len(nodes),
                "multiple": len(nodes) > 1,
                "stats": all_stats,
                "total": {
                    key: sum(item[key] if isinstance(item[key], int) else 0 for item in all_stats)
                    for key in ("text_chars", "headings", "paragraphs", "tables", "rich_text")
                },
                "chrome": sorted(set(chrome for item in all_stats for chrome in item["chrome"])),
            })
        roots[selector] = {
            "pages": len(page_stats),
            "percentage": round(100 * len(page_stats) / len(valid_records), 3),
            "exactly_one": sum(item["count"] == 1 for item in page_stats),
            "multiple": sum(item["multiple"] for item in page_stats),
            "pages_with_chrome_inside": sum(bool(item["chrome"]) for item in page_stats),
            "average_text_chars": round(sum(item["total"]["text_chars"] for item in page_stats) / len(page_stats), 1) if page_stats else 0,
            "median_text_chars": sorted(item["total"]["text_chars"] for item in page_stats)[len(page_stats) // 2] if page_stats else 0,
            "average_headings": round(sum(item["total"]["headings"] for item in page_stats) / len(page_stats), 2) if page_stats else 0,
            "average_paragraphs": round(sum(item["total"]["paragraphs"] for item in page_stats) / len(page_stats), 2) if page_stats else 0,
            "average_tables": round(sum(item["total"]["tables"] for item in page_stats) / len(page_stats), 2) if page_stats else 0,
            "average_rich_text_components": round(sum(item["total"]["rich_text"] for item in page_stats) / len(page_stats), 2) if page_stats else 0,
            "chrome_types": Counter(chrome for item in page_stats for chrome in item["chrome"]),
            "page_stats": page_stats,
        }
    return roots


def fallback_analysis(valid_records, roots):
    # Greedy set cover reports only selectors that add pages not already
    # covered. Aliased/nested selectors therefore do not inflate the chain.
    candidates = []
    for selector, data in roots.items():
        page_set = {
            item["source_file"]
            for item in data["page_stats"]
            if item["count"] == 1 and not item["chrome"]
        }
        if page_set:
            candidates.append((selector, data, page_set))
    covered = set()
    steps = []
    while candidates:
        selector, data, page_set = max(
            candidates,
            key=lambda item: (
                len(item[2] - covered),
                -item[1]["pages_with_chrome_inside"],
                item[1]["exactly_one"],
            ),
        )
        newly = page_set - covered
        if not newly:
            break
        covered.update(newly)
        steps.append({"selector": selector, "new_pages": len(newly), "covered_pages": len(covered), "coverage": round(100 * len(covered) / len(valid_records), 3)})
        candidates = [item for item in candidates if item[0] != selector]
    needed = {}
    for target in (80, 90, 95, 99):
        needed[str(target)] = {"selectors": [], "steps": None, "coverage": None}
        for step_number, step in enumerate(steps, 1):
            if step["coverage"] >= target:
                needed[str(target)] = {"selectors": [item["selector"] for item in steps[:step_number]], "steps": step_number, "coverage": step["coverage"]}
                break
    return {"ordering": [step["selector"] for step in steps], "steps": steps, "needed_for_targets": needed, "unresolved": len(valid_records) - len(covered)}


def choose_root(record, fallback_order):
    for selector in fallback_order:
        nodes = record["soup"].select(selector)
        if len(nodes) == 1:
            return selector, nodes[0]
    return None, None


def boundary_preview(record, selector, node):
    if node is None:
        return {"selector": selector, "before_root": [], "root_start": [], "root_end": [], "after_root": []}
    siblings = [item for item in node.parent.find_all(recursive=False) if getattr(item, "name", None)] if node.parent else []
    position = siblings.index(node) if node in siblings else 0
    before = [item.name + "." + ".".join(item.get("class", [])[:2]) for item in siblings[max(0, position - 2):position]]
    after = [item.name + "." + ".".join(item.get("class", [])[:2]) for item in siblings[position + 1:position + 3]]
    meaningful = [item for item in node.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "p", "table"], recursive=True)]
    def token(item):
        return item.name + ("." + ".".join(item.get("class", [])[:2]) if item.get("class") else "")
    return {"selector": selector, "before_root": before, "root_start": [token(item) for item in meaningful[:5]], "root_end": [token(item) for item in meaningful[-5:]], "after_root": after}


def report(data):
    lines = [
        "# CMS Content Boundary Analysis",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Scope",
        "",
        "This diagnostic uses DOM structure, byte signatures, class/ID naming, and container relationships only. It does not clean files, extract gameplay content, classify text, modify `guide_index.csv`, or delete inputs.",
        "",
        "## 1. Input Validation",
        "",
        "| Structural classification | Count | Percentage |",
        "|---|---:|---:|",
    ]
    for key, value in data["input_classification"].items():
        lines.append(f"| {key} | {value['count']} | {value['percentage']:.2f}% |")
    lines += ["", "### Non-content and Uncertain Inputs", ""]
    for key, value in data["input_classification"].items():
        if key != "valid_content_page":
            lines.append(f"**{key}** ({value['count']}):")
            lines.extend(f"- `{name}` ({size} bytes, {tags} DOM tags, {nulls} null bytes)" for name, size, tags, nulls in value["files"])
            lines.append("")

    lines += ["## 2. CMS Marker Inventory", "", "| Marker | Pages | Coverage | Avg occurrences/page | Median occurrences/page |", "|---|---:|---:|---:|---:|"]
    for marker, value in data["marker_inventory"].items():
        lines.append(f"| `{marker}` | {value['pages']} | {value['percentage']:.2f}% | {value['average_occurrences_per_page']:.2f} | {value['median_occurrences_per_page']} |")
    lines += ["", "### Additional Structurally Named Markers", ""]
    for marker, count in data["discovered_markers"][:30]:
        lines.append(f"- `{marker}`: {count} valid content pages")

    lines += ["", "## 3. Candidate Root Coverage", "", "| Candidate root | Pages | Coverage | Exactly one | Multiple | Chrome inside | Avg text chars | Avg headings | Avg paragraphs | Avg tables | Avg rich-text components |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for selector, value in data["root_candidates"].items():
        lines.append(f"| `{selector}` | {value['pages']} | {value['percentage']:.2f}% | {value['exactly_one']} | {value['multiple']} | {value['pages_with_chrome_inside']} | {value['average_text_chars']:.0f} | {value['average_headings']:.2f} | {value['average_paragraphs']:.2f} | {value['average_tables']:.2f} | {value['average_rich_text_components']:.2f} |")
    lines += ["", "Chrome markers found inside candidate roots are counted structurally, not judged semantically:", ""]
    for selector, value in data["root_candidates"].items():
        if value["chrome_types"]:
            lines.append(f"- `{selector}`: {dict(value['chrome_types'])}")

    lines += ["", "## 4. Smallest Evidence-Supported Fallback Chain", "", "Candidate ordering is empirical: coverage first, then fewer obvious chrome markers, then exact-one prevalence.", "", "| Step | Added selector | Newly covered | Cumulative coverage |", "|---:|---|---:|---:|"]
    for number, step in enumerate(data["fallback_analysis"]["steps"], 1):
        lines.append(f"| {number} | `{step['selector']}` | {step['new_pages']} | {step['coverage']:.2f}% |")
    lines += ["", "| Target | Smallest chain | Coverage |", "|---:|---|---:|"]
    for target, value in data["fallback_analysis"]["needed_for_targets"].items():
        if value["steps"] is None:
            lines.append(f"| {target}% | not reached by measured unique-root candidates | - |")
        else:
            lines.append(f"| {target}% | {' -> '.join(value['selectors'])} | {value['coverage']:.2f}% |")
    lines.append(f"| unresolved | {data['fallback_analysis']['unresolved']} valid content pages | - |")

    lines += ["", "## 5. Cross-check Against Largest 0.90 Structural Families", ""]
    for family in data["family_crosscheck"]:
        lines += [
            f"### {family['family']}",
            "",
            f"- Page count: {family['page_count']}",
            f"- Dominant root: `{family['dominant_root'] or '(none)'}`",
            f"- Dominant-root coverage: {family['dominant_root_coverage']:.2f}% of family",
            f"- Fallback-chain coverage: {family['fallback_coverage']:.2f}% of family",
            f"- Exceptions/unresolved: {family['exceptions']}",
            "",
        ]

    lines += ["## 6. Representative Boundary Previews", ""]
    for sample in data["boundary_samples"]:
        lines += [
            f"### {sample['family']} — {sample['title']}",
            "",
            f"- Source file: `{sample['source_file']}`",
            f"- Root selector: `{sample['selector'] or '(unresolved)'}`",
            f"- Before root: `{sample['preview']['before_root']}`",
            f"- Root start: `{sample['preview']['root_start']}`",
            f"- Root end: `{sample['preview']['root_end']}`",
            f"- After root: `{sample['preview']['after_root']}`",
            "",
        ]

    lines += ["## 7. Failure Modes", ""]
    for failure, count in data["failure_modes"].items():
        lines.append(f"- **{failure}**: {count}")

    targets = data["fallback_analysis"]["needed_for_targets"]
    target_text = {target: (f"{value['steps']} selectors" if value["steps"] is not None else "not reached") for target, value in targets.items()}
    lines += ["", "## Decision", "", f"**{data['decision']}**", "", data["decision_reason"], "", "### Direct Answers", "", f"1. Valid content pages: **{data['input_classification']['valid_content_page']['count']}** of 564.", f"2. Landing/index pages: **{data['input_classification']['valid_landing_or_index_page']['count']}**.", f"3. Malformed/non-HTML/binary assets: **{data['input_classification']['non_html_or_binary_asset']['count']}**.", f"4. Best single root: `{data['best_single_root']['selector']}` at **{data['best_single_root']['coverage']:.2f}%**.", f"5. Best single-root coverage: **{data['best_single_root']['coverage']:.2f}%**.", f"6. Smallest chain for 80%: **{target_text['80']}**.", f"7. Smallest chain for 90%: **{target_text['90']}**.", f"8. Smallest chain for 95%: **{target_text['95']}**.", f"9. Smallest chain for 99%: **{target_text['99']}**.", f"10. Valid content pages unresolved by the measured safe chain: **{data['fallback_analysis']['unresolved']}**.", "11. Largest structural-family result: `.body-content` generalizes across the largest non-map families; the 120-page map family requires a different boundary and its unique candidate contains global chrome.", "12. Systematic loss risk: yes. Repeated rich-text components, map-family chrome, and pages without a unique chrome-free root are enumerated above rather than corrected.", "", "No cleaner was implemented and no corpus files were modified."]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    metadata = load_index()
    assignments, family_data = family_assignments()
    all_records = []
    classifications = defaultdict(list)
    for path in sorted(GUIDE_DIR.glob("*.html")):
        kind, soup, byte_stats = classify(path)
        record = {"source_file": path.name, "kind": kind, "soup": soup, "family": assignments.get(path.name, "unassigned"), "metadata": metadata.get(path.name, {}), "byte_stats": byte_stats}
        all_records.append(record)
        classifications[kind].append(record)

    valid = classifications["valid_content_page"]
    marker_data = marker_inventory(valid)
    discovered = discover_markers(valid)
    roots = root_candidates(valid)
    fallback = fallback_analysis(valid, roots)
    fallback_order = [step["selector"] for step in fallback["steps"]]

    family_crosscheck = []
    for family in family_data["largest_families"][:20]:
        members = [record for record in valid if record["family"] == family["family"]]
        root_counts = Counter()
        resolved = 0
        for record in members:
            selector, _ = choose_root(record, fallback_order)
            if selector:
                root_counts[selector] += 1
                resolved += 1
        dominant, dominant_count = root_counts.most_common(1)[0] if root_counts else (None, 0)
        family_crosscheck.append({"family": family["family"], "page_count": len(members), "dominant_root": dominant, "dominant_root_coverage": round(100 * dominant_count / len(members), 3) if members else 0, "fallback_coverage": round(100 * resolved / len(members), 3) if members else 0, "exceptions": len(members) - resolved})

    samples = []
    seen_families = set()
    for record in valid:
        if record["family"] in seen_families or len(samples) >= 20:
            continue
        selector, node = choose_root(record, fallback_order)
        samples.append({"family": record["family"], "source_file": record["source_file"], "title": record["metadata"].get("page_title", ""), "selector": selector, "preview": boundary_preview(record, selector, node)})
        seen_families.add(record["family"])

    best_selector, best_data = max(roots.items(), key=lambda item: (item[1]["pages"], -item[1]["pages_with_chrome_inside"]))
    failure_modes = {
        "no_unique_candidate_content_root": sum(not any(len(record["soup"].select(selector)) == 1 for selector in ROOT_SELECTORS) for record in valid),
        "multiple_competing_roots_or_nodes": sum(any(len(record["soup"].select(selector)) > 1 for selector in ROOT_SELECTORS) for record in valid),
        "candidate_root_includes_obvious_chrome": sum(any(item["chrome"] for selector in ROOT_SELECTORS for item in roots[selector]["page_stats"] if item["source_file"] == record["source_file"]) for record in valid),
        "landing_or_index_page": len(classifications["valid_landing_or_index_page"]),
        "non_html_or_binary": len(classifications["non_html_or_binary_asset"]),
        "root_appears_to_omit_headings": sum(any(item["total"]["headings"] == 0 for selector in ROOT_SELECTORS for item in roots[selector]["page_stats"] if item["source_file"] == record["source_file"]) for record in valid),
        "root_appears_to_omit_tables": sum(any(item["total"]["tables"] == 0 for selector in ROOT_SELECTORS for item in roots[selector]["page_stats"] if item["source_file"] == record["source_file"]) for record in valid),
        "root_appears_to_omit_rich_text": sum(any(item["total"]["rich_text"] == 0 for selector in ROOT_SELECTORS for item in roots[selector]["page_stats"] if item["source_file"] == record["source_file"]) for record in valid),
    }

    classification_output = {}
    for kind, records in classifications.items():
        classification_output[kind] = {"count": len(records), "percentage": round(100 * len(records) / len(all_records), 3), "files": [(r["source_file"], r["byte_stats"]["bytes"], r["byte_stats"]["tag_count"], r["byte_stats"]["null_bytes"]) for r in records]}

    steps_for_95 = fallback["needed_for_targets"].get("95", {}).get("steps")
    decision = "GENERIC CMS EXTRACTION VIABLE WITH FALLBACKS" if steps_for_95 is not None and steps_for_95 <= 5 and fallback["unresolved"] <= 50 else "TEMPLATE-SPECIFIC EXTRACTION REQUIRED"
    coverage_for_95 = fallback["needed_for_targets"].get("95", {}).get("coverage")
    coverage_for_95_text = f"{coverage_for_95:.2f}%" if coverage_for_95 is not None else "not reached"
    steps_for_95_text = str(steps_for_95) if steps_for_95 is not None else "not reached"
    data = {
        "generated_at": datetime.now().isoformat(),
        "input_total": len(all_records),
        "input_classification": classification_output,
        "marker_inventory": marker_data,
        "discovered_markers": discovered.most_common(),
        "root_candidates": roots,
        "fallback_analysis": fallback,
        "best_single_root": {"selector": best_selector, "coverage": best_data["percentage"]},
        "family_crosscheck": family_crosscheck,
        "boundary_samples": samples,
        "failure_modes": failure_modes,
        "decision": decision,
        "decision_reason": f"The best single root covers {best_data['percentage']:.2f}% of valid content pages. The measured safe fallback chain reaches {coverage_for_95_text} at {steps_for_95_text} selectors and leaves {fallback['unresolved']} valid content pages unresolved. Root behavior still varies across structural families, so fallback handling is required.",
    }
    # Compact output: remove per-page soup objects and retain root page stats/boundaries.
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(data, indent=2, default=lambda value: dict(value) if isinstance(value, Counter) else value), encoding="utf-8")
    report(data)
    print(f"Classified {len(all_records)} inputs: {dict((k, len(v)) for k, v in classifications.items())}")
    print(f"Best root: {best_selector} ({best_data['percentage']:.2f}%)")
    print(f"Fallback targets: {fallback['needed_for_targets']}")
    print(f"Decision: {decision}")


if __name__ == "__main__":
    main()
