#!/usr/bin/env python3
"""Discover, download, and index official Call of Duty gameplay guides."""

from __future__ import annotations

import argparse
import csv
import hashlib
import logging
import re
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
GUIDE_HUB = "https://www.callofduty.com/guides"
SITEMAP_URL = "https://www.callofduty.com/sitemap.xml"
SITE_ROOT = "https://www.callofduty.com"
USER_AGENT = "CallofDutyIntelligence/0.2 (+historical research prototype)"
GUIDE_CSV_COLUMNS = [
    "guide_id",
    "url",
    "canonical_url",
    "page_title",
    "title_family",
    "experience_if_explicit",
    "guide_category_if_explicit",
    "publication_or_update_date_if_explicit",
    "discovery_source",
    "source_file",
    "retrieved_at",
]
CANDIDATE_CSV_COLUMNS = [
    "url",
    "page_title",
    "discovery_source",
    "hub_or_title_family",
    "language_or_locale",
    "http_status",
    "canonical_url",
    "content_type_guess",
    "include_candidate",
    "exclusion_reason",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, default=Path("data"))
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    return parser.parse_args()


def get(session: requests.Session, url: str) -> tuple[str, int]:
    try:
        response = session.get(url, timeout=45)
        return response.text, response.status_code
    except Exception:
        return "", 0


def canonical_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    if path.endswith(".html"):
        path = path[:-5]
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def is_guide_path(url: str) -> bool:
    return "/guides/" in urlparse(url).path.lower() and "/patchnotes/" not in urlparse(url).path


def discover_from_sitemap(html: str) -> set[tuple[str, str]]:
    urls = set()
    try:
        root = ET.fromstring(html)
        for element in root.iter():
            if element.tag.rsplit("}", 1)[-1] == "loc" and element.text:
                url = canonical_url(element.text.strip())
                if is_guide_path(url):
                    urls.add((url, "sitemap"))
    except Exception:
        pass
    return urls


def discover_from_hub(html: str, hub_url: str) -> set[tuple[str, str]]:
    urls = set()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.select("a[href]"):
        href = link.get("href", "").split("#", 1)[0]
        if not href:
            continue
        url = urljoin(SITE_ROOT, href)
        canonical = canonical_url(url)
        if is_guide_path(canonical):
            urls.add((canonical, "guide_hub"))
    return urls


def discover_internal_links(html: str, source_url: str) -> set[tuple[str, str]]:
    urls = set()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.select("a[href]"):
        href = link.get("href", "").split("#", 1)[0]
        if not href:
            continue
        url = urljoin(source_url, href)
        canonical = canonical_url(url)
        if is_guide_path(canonical) and canonical != source_url:
            urls.add((canonical, "internal_link"))
    return urls


def extract_metadata(html: str, url: str) -> dict[str, str | None]:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(" ").strip() if soup.title else None
    title = " ".join(title.split()) if title else None

    date_str = None
    for date_elem in soup.select('meta[property*="date"], time[datetime], .date, [class*="date"]'):
        if date_elem.name == "meta":
            content = date_elem.get("content", "")
        elif date_elem.name == "time":
            content = date_elem.get("datetime", "")
        else:
            content = date_elem.get_text(" ").strip()
        if content and re.search(r"\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)", content):
            date_str = " ".join(content.split())[:50]
            break

    title_family = None
    if title:
        for term in ("Modern Warfare III", "Modern Warfare 4", "Black Ops 7", "Black Ops 6", "MW3", "MW4", "BO7", "BO6"):
            if term.lower() in title.lower():
                title_family = term
                break

    experience = None
    if title:
        for exp in ("Multiplayer", "Warzone", "Zombies", "Campaign", "Ranked Play"):
            if exp.lower() in title.lower():
                experience = exp
                break

    category = None
    if title:
        keywords = ("map", "weapon", "loadout", "streak", "perk", "equipment", "operator", "mode", "playlist", "progression", "starter", "guide", "tips", "strategy")
        for kw in keywords:
            if kw in title.lower():
                category = kw.capitalize()
                break

    return {"title": title, "title_family": title_family, "experience": experience, "category": category, "date": date_str}


def source_filename(url: str) -> str:
    slug = urlparse(url).path.rstrip("/").rsplit("/", 1)[-1]
    digest = hashlib.sha256(url.encode()).hexdigest()[:10]
    return f"{slug}-{digest}.html"


def main() -> None:
    args = parse_args()
    raw_dir = args.output_root / "raw" / "guide_pages"
    processed_dir = args.output_root / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})

    candidate_map = {}
    logging.info("Discovering guides from sitemap...")
    sitemap_html = get(session, SITEMAP_URL)[0]
    sitemap_urls = discover_from_sitemap(sitemap_html)
    for url, source in sitemap_urls:
        candidate_map.setdefault(url, {})["sources"] = candidate_map.get(url, {}).get("sources", set()) | {source}

    logging.info("Discovering guides from hub...")
    hub_html = get(session, GUIDE_HUB)[0]
    hub_urls = discover_from_hub(hub_html, GUIDE_HUB)
    for url, source in hub_urls:
        candidate_map.setdefault(url, {})["sources"] = candidate_map.get(url, {}).get("sources", set()) | {source}

    logging.info("Discovering internal links...")
    visited = set()
    queue = list(candidate_map.keys())[:50]
    for url in queue:
        if url in visited:
            continue
        visited.add(url)
        time.sleep(args.delay)
        html, status = get(session, url)
        if status != 200:
            continue
        internal = discover_internal_links(html, url)
        for iurl, source in internal:
            candidate_map.setdefault(iurl, {})["sources"] = candidate_map.get(iurl, {}).get("sources", set()) | {source}
        queue.extend([u for u, _ in internal if u not in visited])

    logging.info("Validating and downloading candidates...")
    downloaded = 0
    skipped = 0
    failures = []
    included = []
    excluded = []
    canonicalized = defaultdict(list)

    for url in sorted(candidate_map.keys()):
        sources = candidate_map[url].get("sources", set())
        canonical = canonical_url(url)
        guide_id = hashlib.sha256(canonical.encode()).hexdigest()[:16]
        filename = source_filename(canonical)
        filepath = raw_dir / filename
        
        # Check if file already exists
        if filepath.exists():
            html = filepath.read_text(encoding="utf-8")
            metadata = extract_metadata(html, url) if html else {}
            title = metadata.get("title") or url
            skipped += 1
        else:
            time.sleep(args.delay / 2)
            html, status = get(session, url)
            metadata = extract_metadata(html, url) if html else {}
            title = metadata.get("title") or url

            if status != 200:
                excluded.append({"url": url, "reason": f"HTTP {status}", "canonical": canonical, "title": title, "sources": ";".join(sorted(sources))})
                continue
            
            filepath.write_text(html, encoding="utf-8")
            downloaded += 1

        is_duplicate = canonical != url
        if is_duplicate and any(canonical == row["canonical_url"] for row in included):
            canonicalized[canonical].append(url)
            continue
        retrieved_at = datetime.now(timezone.utc).isoformat()

        included.append({
            "guide_id": guide_id,
            "url": url,
            "canonical_url": canonical,
            "page_title": metadata.get("title"),
            "title_family": metadata.get("title_family"),
            "experience_if_explicit": metadata.get("experience"),
            "guide_category_if_explicit": metadata.get("category"),
            "publication_or_update_date_if_explicit": metadata.get("date"),
            "discovery_source": ";".join(sorted(sources)),
            "source_file": filename,
            "retrieved_at": retrieved_at,
        })

    output_csv = processed_dir / "guide_index.csv"
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=GUIDE_CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(sorted(included, key=lambda r: r["canonical_url"]))

    log_path = processed_dir / "guide_ingestion.log"
    with log_path.open("w", encoding="utf-8") as handle:
        handle.write(f"candidate_urls\t{len(candidate_map)}\n")
        handle.write(f"sitemap_urls\t{len(sitemap_urls)}\n")
        handle.write(f"hub_urls\t{len(hub_urls)}\n")
        handle.write(f"downloaded\t{downloaded}\n")
        handle.write(f"included\t{len(included)}\n")
        handle.write(f"excluded\t{len(excluded)}\n")
        handle.write(f"canonicalized_groups\t{len(canonicalized)}\n")
        for url, sources in canonicalized.items():
            handle.write(f"canonical\t{url}\t{';'.join(sources)}\n")
        for exc in excluded:
            handle.write(f"excluded\t{exc['url']}\t{exc['reason']}\n")

    logging.info("Candidates discovered: %d", len(candidate_map))
    logging.info("Pages skipped (already downloaded): %d", skipped)
    logging.info("Pages newly downloaded: %d", downloaded)
    logging.info("Pages included: %d", len(included))
    logging.info("Pages excluded: %d", len(excluded))
    logging.info("Canonicalized groups: %d", len(canonicalized))
    logging.info("CSV written: %s", output_csv)


if __name__ == "__main__":
    main()
