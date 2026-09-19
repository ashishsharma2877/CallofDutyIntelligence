#!/usr/bin/env python3
"""Diagnostic structural analysis of the downloaded guide HTML corpus.

This script intentionally ignores visible text and does not extract gameplay
content. It measures DOM shape, structural attributes, and element counts.
"""

import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
GUIDE_DIR = ROOT / "data/raw/guide_pages"
INDEX_PATH = ROOT / "data/processed/guide_index.csv"
OUTPUT_DIR = ROOT / "data/analysis/guides"
REPORT_PATH = ROOT / "docs/analysis/guides/dom-structure-analysis.md"
INVENTORY_PATH = OUTPUT_DIR / "dom-structural-families.json"

THRESHOLDS = (0.95, 0.90, 0.80, 0.70)

# Attributes are retained only as structural tokens. Values that commonly
# contain content identifiers are reduced to stable structural forms.
STRUCTURAL_CLASS_RE = re.compile(r"(?:^|[-_])(?:[a-f0-9]{6,}|\d{2,})(?:$|[-_])", re.I)


def normalize_structural_token(value):
    value = re.sub(r"\s+", " ", value.strip().lower())
    value = re.sub(r"\d+", "#", value)
    value = re.sub(r"[a-f0-9]{8,}", "@hex", value)
    return value[:100]


def class_token(value):
    token = normalize_structural_token(value)
    if STRUCTURAL_CLASS_RE.search(token):
        token = re.sub(r"[a-f0-9]{6,}", "@hex", token, flags=re.I)
    return token


def load_index():
    rows = {}
    with INDEX_PATH.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["source_file"]] = row
    return rows


def add_feature(features, key, amount=1):
    features[key] += amount


def fingerprint_page(path):
    html = path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    root = soup.find("html") or soup

    tag_counts = Counter()
    class_counts = Counter()
    id_counts = Counter()
    pair_counts = Counter()
    depth_counts = Counter()
    heading_counts = Counter()
    ordered_tokens = []
    features = Counter()
    element_count = 0
    max_depth = 0
    main_count = 0
    article_count = 0
    section_count = 0
    container_count = 0

    def visit(node, depth=0):
        nonlocal element_count, max_depth, main_count, article_count
        nonlocal section_count, container_count
        if not getattr(node, "name", None):
            return
        tag = node.name.lower()
        element_count += 1
        max_depth = max(max_depth, depth)
        tag_counts[tag] += 1
        depth_counts[min(depth, 20)] += 1
        ordered_tokens.append(tag)
        add_feature(features, f"tag:{tag}")
        add_feature(features, f"depth_bin:{min(depth // 2, 10)}")

        classes = sorted({class_token(item) for item in (node.get("class") or []) if item})
        for item in classes:
            class_counts[item] += 1
            add_feature(features, f"class:{item}")
        if classes:
            ordered_tokens.append("." + ",".join(classes))

        node_id = node.get("id")
        if node_id:
            normalized_id = class_token(node_id)
            id_counts[normalized_id] += 1
            add_feature(features, f"id:{normalized_id}")
            ordered_tokens.append("#" + normalized_id)

        if tag == "main":
            main_count += 1
        elif tag == "article":
            article_count += 1
        elif tag == "section":
            section_count += 1
        if tag in {"div", "main", "article", "section", "header", "footer", "nav", "aside"}:
            container_count += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            heading_counts[tag] += 1
            add_feature(features, f"heading:{tag}")

        children = [child for child in node.children if getattr(child, "name", None)]
        child_tags = [child.name.lower() for child in children]
        for child_tag in child_tags:
            pair_counts[f"{tag}>{child_tag}"] += 1
            add_feature(features, f"pair:{tag}>{child_tag}")
        for child in children:
            visit(child, depth + 1)

    visit(root)

    # Ordered DOM shape makes exact fingerprints strict while excluding text.
    shape = "|".join(ordered_tokens)
    exact_fingerprint = hashlib.sha256(shape.encode()).hexdigest()

    for tag, count in tag_counts.items():
        add_feature(features, f"tag_count:{tag}:{min(count, 50)}")
    for depth, count in depth_counts.items():
        add_feature(features, f"depth_count:{depth}:{min(count, 100)}")
    for key, count in pair_counts.items():
        add_feature(features, f"pair_count:{key}:{min(count, 50)}")

    return {
        "source_file": path.name,
        "exact_fingerprint": exact_fingerprint,
        "feature_set": sorted(features),
        "tag_counts": dict(tag_counts),
        "class_counts": dict(class_counts),
        "id_counts": dict(id_counts),
        "heading_counts": dict(heading_counts),
        "depth_counts": dict(depth_counts),
        "element_count": element_count,
        "max_depth": max_depth,
        "main_count": main_count,
        "article_count": article_count,
        "section_count": section_count,
        "container_count": container_count,
    }


def cosine(left, right):
    left_set = set(left["feature_set"])
    right_set = set(right["feature_set"])
    if not left_set or not right_set:
        return 0.0
    intersection = len(left_set & right_set)
    return intersection / math.sqrt(len(left_set) * len(right_set))


def connected_families(records, threshold):
    parent = list(range(len(records)))

    def find(item):
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left, right):
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    for left in range(len(records)):
        for right in range(left + 1, len(records)):
            if cosine(records[left], records[right]) >= threshold:
                union(left, right)

    groups = defaultdict(list)
    for index in range(len(records)):
        groups[find(index)].append(index)
    return sorted(groups.values(), key=lambda group: (-len(group), group[0]))


def exact_groups(records):
    groups = defaultdict(list)
    for index, record in enumerate(records):
        groups[record["exact_fingerprint"]].append(index)
    return sorted(groups.values(), key=lambda group: (-len(group), group[0]))


def metadata_summary(group, records, metadata):
    title_families = Counter()
    categories = Counter()
    experiences = Counter()
    periods = Counter()
    for index in group:
        row = metadata.get(records[index]["source_file"], {})
        for counter, field in ((title_families, "title_family"), (categories, "guide_category_if_explicit"), (experiences, "experience_if_explicit")):
            value = row.get(field) or "(blank)"
            counter[value] += 1
        date = row.get("publication_or_update_date_if_explicit") or ""
        periods[date[:4] if date[:4].isdigit() else "(unknown)"] += 1
    return {
        "title_families": dict(title_families),
        "categories": dict(categories),
        "experiences": dict(experiences),
        "publication_years": dict(periods),
    }


def family_entry(group, records, metadata, label):
    representative = records[group[0]]
    representative_metadata = metadata.get(representative["source_file"], {})
    return {
        "family": label,
        "page_count": len(group),
        "percentage": round(100 * len(group) / len(records), 3),
        "representative_source_file": representative["source_file"],
        "representative_guide": {
            "title": representative_metadata.get("page_title", ""),
            "url": representative_metadata.get("url", ""),
            "guide_id": representative_metadata.get("guide_id", ""),
        },
        "metadata": metadata_summary(group, records, metadata),
        "major_dom_characteristics": {
            "element_count": representative["element_count"],
            "max_depth": representative["max_depth"],
            "main_count": representative["main_count"],
            "article_count": representative["article_count"],
            "section_count": representative["section_count"],
            "container_count": representative["container_count"],
            "top_tags": Counter(representative["tag_counts"]).most_common(12),
            "top_classes": Counter(representative["class_counts"]).most_common(12),
            "heading_counts": representative["heading_counts"],
        },
    }


def coverage_counts(families, total):
    cumulative = 0
    result = {}
    for target in (80, 90, 95, 99):
        cumulative = 0
        for number, group in enumerate(families, 1):
            cumulative += len(group)
            if 100 * cumulative / total >= target:
                result[str(target)] = number
                break
    return result


def concentration(families, total):
    return {str(number): round(100 * sum(map(len, families[:number])) / total, 3) for number in (1, 3, 5, 10, 20)}


def write_report(records, metadata, exact, threshold_groups, inventory):
    total = len(records)
    lines = [
        "# DOM Structure Analysis of the Call of Duty Guide Corpus",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Scope and Method",
        "",
        "This is a diagnostic of HTML/DOM structure only. It does not clean pages, extract gameplay content, classify semantic content, or modify `guide_index.csv`.",
        "",
        f"- HTML pages analyzed: **{total}**",
        f"- Exact structural fingerprints: **{len(exact)}**",
        "- Fingerprints use ordered DOM tag shape, normalized class/ID tokens, element counts, heading levels, container presence, depth, and parent-child tag pairs.",
        "- Text nodes, page titles, URLs, dates, and content names were excluded from fingerprints.",
        "- Near-family counts use connected components over pairwise structural cosine similarity.",
        "",
        "## Similarity Diagnostics",
        "",
        "| Similarity threshold | Structural families | Largest family | Pages in largest family |",
        "|---:|---:|---:|---:|",
    ]
    for threshold, groups in threshold_groups.items():
        largest = len(groups[0])
        lines.append(f"| {threshold:.2f} | {len(groups)} | 1 | {largest} ({100 * largest / total:.2f}%) |")
    lines += [
        "",
        "### Exact Fingerprint Distribution",
        "",
        f"- Pages represented in exact duplicate groups (size >= 2): {sum(len(group) for group in exact if len(group) >= 2)}",
        f"- Exact groups of size >= 2: {sum(1 for group in exact if len(group) >= 2)}",
        f"- Singleton exact fingerprints: {sum(1 for group in exact if len(group) == 1)}",
        "",
        "### Coverage of Largest Near-Families",
        "",
        "| Largest families included | Corpus covered |",
        "|---:|---:|",
    ]
    for number, value in inventory["concentration"].items():
        lines.append(f"| {number} | {value:.2f}% |")

    lines += ["", "### Families Needed for Coverage", "", "| Target coverage | Families needed |", "|---:|---:|"]
    for target, count in inventory["families_needed_for_coverage"].items():
        lines.append(f"| {target}% | {count} |")

    lines += ["", "## Structural Family Size Distribution", ""]
    for threshold, groups in threshold_groups.items():
        sizes = [len(group) for group in groups]
        lines += [
            f"### Threshold {threshold:.2f}",
            "",
            f"- Families: {len(sizes)}",
            f"- Largest: {max(sizes)} pages",
            f"- Median: {sorted(sizes)[len(sizes) // 2]} pages",
            f"- Singleton families: {sum(size == 1 for size in sizes)}",
            f"- Top 10 sizes: {sizes[:10]}",
            "",
        ]

    lines += ["## Largest Structural Families", ""]
    for item in inventory["largest_families"]:
        lines += [
            f"### {item['family']}",
            "",
            f"- Pages: **{item['page_count']}** ({item['percentage']:.2f}% of corpus)",
            f"- Representative guide: **{item['representative_guide']['title'] or '(title unavailable)'}**",
            f"- Representative URL: `{item['representative_guide']['url'] or '(URL unavailable)'}`",
            f"- Representative source file: `{item['representative_source_file']}`",
            f"- Title families: {item['metadata']['title_families']}",
            f"- Guide categories: {item['metadata']['categories']}",
            f"- Experiences: {item['metadata']['experiences']}",
            f"- Publication years: {item['metadata']['publication_years']}",
            f"- DOM characteristics: {item['major_dom_characteristics']}",
            "",
        ]

    lines += [
        "## Metadata Association and Interpretation",
        "",
        "Metadata was used only after structural grouping to test association; it was not included in fingerprints.",
        "",
        f"- Exact/near families should be compared with title and guide-category distributions in the machine-readable inventory.",
        f"- Largest-family metadata purity at threshold 0.90: {inventory['largest_family_metadata']['threshold_0.90']}",
        f"- Largest-family metadata purity at threshold 0.80: {inventory['largest_family_metadata']['threshold_0.80']}",
        "",
        "### Difference Diagnosis",
        "",
        "- **Shared page shell vs. meaningful layout**: duplicate and high-similarity groups indicate a shared shell where pages differ mainly in content-bearing nodes excluded from the fingerprint.",
        "- **Historical redesigns**: multiple persistent families with distinct container/class structures and year/title mixtures are evidence of more than one shell; publication-year concentrations should be treated as supporting, not definitive, evidence.",
        "- **Title-specific templates**: a family dominated by one title family but structurally distinct from other title families supports title-specific layout variation.",
        "- **Guide-type-specific templates**: category-pure families support map/mode/weapon-specific layouts; mixed families indicate shared shell reuse.",
        "- **Random/inconsistent markup**: singleton-heavy distributions and low-threshold fragmentation indicate residual markup variation or page-specific modules.",
        "",
        "## Assessment",
        "",
        f"**{inventory['assessment']}**",
        "",
        inventory["assessment_reason"],
        "",
        "The number of structural families needed for 80%, 90%, 95%, and 99% coverage is reported above. These are diagnostic structural families, not extraction templates.",
        "",
        "## Machine-Readable Output",
        "",
        f"- `{INVENTORY_PATH.relative_to(ROOT)}` contains per-page fingerprints, family assignments at all thresholds, representative families, metadata summaries, and coverage statistics.",
        "",
        "No cleaning or gameplay extraction was performed.",
    ]
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    metadata = load_index()
    paths = sorted(GUIDE_DIR.glob("*.html"))
    records = [fingerprint_page(path) for path in paths]
    exact = exact_groups(records)
    threshold_groups = {threshold: connected_families(records, threshold) for threshold in THRESHOLDS}

    family_assignments = {}
    for threshold, groups in threshold_groups.items():
        assignments = {}
        for family_number, group in enumerate(groups, 1):
            for index in group:
                assignments[records[index]["source_file"]] = family_number
        family_assignments[str(threshold)] = assignments

    representative_families = []
    for family_number, group in enumerate(threshold_groups[0.90][:20], 1):
        representative_families.append(family_entry(group, records, metadata, f"0.90-{family_number}"))

    largest_metadata = {}
    for threshold in (0.90, 0.80):
        group = threshold_groups[threshold][0]
        summary = metadata_summary(group, records, metadata)
        largest_metadata[f"threshold_{threshold:.2f}"] = {
            "page_count": len(group),
            "title_family_purity": round(max(summary["title_families"].values()) / len(group), 3),
            "category_purity": round(max(summary["categories"].values()) / len(group), 3),
            "experience_purity": round(max(summary["experiences"].values()) / len(group), 3),
            "summary": summary,
        }

    concentration_values = concentration(threshold_groups[0.90], len(records))
    coverage = coverage_counts(threshold_groups[0.90], len(records))
    # A moderate assessment is warranted when a small number of families cover
    # most pages but singleton and metadata-pure families remain.
    largest_90 = len(threshold_groups[0.90][0]) / len(records)
    family_count_90 = len(threshold_groups[0.90])
    if largest_90 >= 0.80 and family_count_90 <= 20:
        assessment = "STRONGLY TEMPLATIZABLE"
    elif concentration_values["10"] >= 80:
        assessment = "MODERATELY TEMPLATIZABLE"
    elif concentration_values["20"] >= 80:
        assessment = "WEAKLY TEMPLATIZABLE"
    else:
        assessment = "NOT TEMPLATIZABLE"

    inventory = {
        "generated_at": datetime.now().isoformat(),
        "pages_analyzed": len(records),
        "exact_fingerprint_count": len(exact),
        "exact_fingerprint_size_distribution": Counter(len(group) for group in exact),
        "thresholds": list(THRESHOLDS),
        "family_counts": {str(threshold): len(groups) for threshold, groups in threshold_groups.items()},
        "family_size_distributions": {str(threshold): Counter(len(group) for group in groups) for threshold, groups in threshold_groups.items()},
        "concentration": concentration_values,
        "families_needed_for_coverage": coverage,
        "largest_families": representative_families,
        "largest_family_metadata": largest_metadata,
        "assessment": assessment,
        "assessment_reason": (
            f"At the 0.90 diagnostic threshold, {family_count_90} structural families were observed and the largest covered "
            f"{largest_90:.1%} of pages. The concentration of the largest ten families was {concentration_values['10']:.1f}%, "
            "while exact fingerprints and lower-similarity fragmentation expose meaningful residual variation."
        ),
        "pages": records,
        "family_assignments": family_assignments,
    }
    # Counter keys must be strings for portable JSON.
    inventory["exact_fingerprint_size_distribution"] = {str(k): v for k, v in inventory["exact_fingerprint_size_distribution"].items()}
    inventory["family_size_distributions"] = {
        threshold: {str(k): v for k, v in distribution.items()}
        for threshold, distribution in inventory["family_size_distributions"].items()
    }
    INVENTORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    INVENTORY_PATH.write_text(json.dumps(inventory, indent=2), encoding="utf-8")
    write_report(records, metadata, exact, threshold_groups, inventory)
    print(f"Analyzed {len(records)} pages")
    print(f"Exact fingerprints: {len(exact)}")
    for threshold, groups in threshold_groups.items():
        print(f"Threshold {threshold:.2f}: {len(groups)} families; largest={len(groups[0])}")
    print(f"Assessment: {assessment}")
    print(f"Report: {REPORT_PATH}")
    print(f"Inventory: {INVENTORY_PATH}")


if __name__ == "__main__":
    main()
