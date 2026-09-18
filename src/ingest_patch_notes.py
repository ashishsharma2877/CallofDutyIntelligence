#!/usr/bin/env python3
"""Build a chronological index of official Call of Duty patch updates."""

from __future__ import annotations

import argparse
import csv
import hashlib
import logging
import re
import time
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ARCHIVE_URL = "https://www.callofduty.com/content/atvi/callofduty/patchnotes/web/en/home.html"
SITEMAP_URL = "https://www.callofduty.com/sitemap.xml"
SITE_ROOT = "https://www.callofduty.com"
USER_AGENT = "CallofDutyIntelligence/0.2 (+historical research prototype)"
CSV_COLUMNS = [
    "update_date",
    "franchise",
    "title",
    "experience",
    "season",
    "update_title",
    "date_source_type",
    "source_page_title",
    "source_url",
    "source_file",
    "retrieved_at",
]
MONTHS = (
    "JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|"
    "NOVEMBER|DECEMBER"
)
DATE_HEADING = re.compile(
    rf"^(?:(?:MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY)\s+)?"
    rf"({MONTHS})\s+(\d{{1,2}})(?:,\s*(\d{{4}}))?$",
    re.IGNORECASE,
)
DATE_TEXT = re.compile(rf"^({MONTHS})\s+(\d{{1,2}})(?:,\s*(\d{{4}}))?$", re.IGNORECASE)
PATCH_PATH = re.compile(r"^/patchnotes/(20\d{2})/(\d{2})/[^/?#]+/?$")
DATE_SOURCE_PRIORITY = {"heading": 0, "dateline": 1, "anchor": 2, "other_structured": 3}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-date", default="2024-09-01", type=date.fromisoformat)
    parser.add_argument("--end-date", default=date.today().isoformat(), type=date.fromisoformat)
    parser.add_argument("--output-root", type=Path, default=Path("data"))
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    return parser.parse_args()


def get(session: requests.Session, url: str) -> str:
    response = session.get(url, timeout=45)
    response.raise_for_status()
    return response.text


def canonical_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    if path.endswith(".html"):
        path = path[:-5]
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def in_range(url: str, start_date: date, end_date: date) -> bool:
    match = PATCH_PATH.match(urlparse(url).path)
    if not match:
        return False
    page_month = date(int(match.group(1)), int(match.group(2)), 1)
    return date(start_date.year, start_date.month, 1) <= page_month <= date(end_date.year, end_date.month, 1)


def discover_sitemap(html: str, start_date: date, end_date: date) -> set[str]:
    urls = set()
    root = ET.fromstring(html)
    for element in root.iter():
        if element.tag.rsplit("}", 1)[-1] != "loc" or not element.text:
            continue
        url = canonical_url(clean_text(element.text))
        if in_range(url, start_date, end_date):
            urls.add(url)
    return urls


def discover_archive(html: str, start_date: date, end_date: date) -> set[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls = set()
    for link in soup.select("a[href]"):
        href = link["href"].split("#", 1)[0]
        if not PATCH_PATH.match(urlparse(href).path):
            continue
        url = canonical_url(urljoin(SITE_ROOT, href))
        if in_range(url, start_date, end_date):
            urls.add(url)
    return urls


def clean_text(value: str) -> str:
    return " ".join(value.split())


def page_metadata(source_title: str, source_url: str) -> tuple[str | None, str | None, str | None, str | None]:
    franchise = "Call of Duty" if re.search(r"Call of Duty", source_title, re.IGNORECASE) else None
    title = None
    for pattern, value in (
        (r"Modern Warfare III", "Modern Warfare III"),
        (r"Modern Warfare 4", "Modern Warfare 4"),
        (r"Black Ops 7", "Black Ops 7"),
        (r"Black Ops 6", "Black Ops 6"),
    ):
        if re.search(pattern, source_title, re.IGNORECASE):
            title = value
            break
    experience = "Warzone" if re.search(r"Warzone", source_title, re.IGNORECASE) or "warzone" in source_url.lower() else None
    season_match = re.search(r"\b(Preseason|Beta|Season\s+\d{1,2}(?:\s+Reloaded)?)\b", source_title, re.IGNORECASE)
    season = season_match.group(1) if season_match else None
    return franchise, title, experience, season


def date_for_text(text: str, source_url: str, explicit_year: str | None) -> date | None:
    match = DATE_TEXT.fullmatch(text)
    if not match:
        return None
    page_match = re.search(r"/(20\d{2})/(\d{2})/", urlparse(source_url).path)
    if explicit_year:
        year = int(explicit_year)
    elif page_match:
        page_year, page_month = int(page_match.group(1)), int(page_match.group(2))
        month = datetime.strptime(match.group(1).title(), "%B").month
        year = page_year + (1 if page_month >= 10 and month <= 2 else 0)
    else:
        return None
    try:
        return date(year, datetime.strptime(match.group(1).title(), "%B").month, int(match.group(2)))
    except ValueError:
        return None


def make_event(parsed_date: date, update_title: str, source_type: str, metadata: dict[str, str | None]) -> dict[str, str | None]:
    return {
        "update_date": parsed_date.isoformat(),
        "franchise": metadata["franchise"],
        "title": metadata["title"],
        "experience": metadata["experience"],
        "season": metadata["season"],
        "update_title": update_title,
        "date_source_type": source_type,
        "source_page_title": metadata["source_page_title"],
        "source_url": metadata["source_url"],
        "source_file": metadata["source_file"],
        "retrieved_at": metadata["retrieved_at"],
    }


def source_priority(source_types: str) -> int:
    return min(DATE_SOURCE_PRIORITY[value] for value in source_types.split(";"))


def extract_updates(html: str, source_url: str, retrieved_at: str, source_file: str) -> list[dict[str, str | None]]:
    soup = BeautifulSoup(html, "html.parser")
    source_title = clean_text(soup.title.get_text(" ")) if soup.title else None
    franchise, title, experience, season = page_metadata(source_title or "", source_url)
    metadata = {
        "franchise": franchise,
        "title": title,
        "experience": experience,
        "season": season,
        "source_page_title": source_title,
        "source_url": source_url,
        "source_file": source_file,
        "retrieved_at": retrieved_at,
    }
    events = []
    for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        text = clean_text(heading.get_text(" "))
        match = DATE_HEADING.fullmatch(text)
        if match:
            parsed_date = date_for_text(f"{match.group(1)} {match.group(2)}", source_url, match.group(3))
            if parsed_date:
                events.append(make_event(parsed_date, text, "heading", metadata))
    for dateline in soup.select("p.dateline"):
        text = clean_text(dateline.get_text(" "))
        match = DATE_TEXT.fullmatch(text)
        if match:
            parsed_date = date_for_text(text, source_url, match.group(3))
            if parsed_date:
                events.append(make_event(parsed_date, text, "dateline", metadata))
    for anchor in soup.select('a[href^="#"]'):
        text = clean_text(anchor.get_text(" "))
        if DATE_TEXT.fullmatch(text):
            parsed_date = date_for_text(text, source_url, None)
            if parsed_date:
                events.append(make_event(parsed_date, text, "anchor", metadata))
    unique = {}
    for event in events:
        key = event["update_date"]
        existing = unique.get(key)
        if existing is None:
            unique[key] = event
            continue
        existing_priority = source_priority(existing["date_source_type"])
        source_types = set(existing["date_source_type"].split(";"))
        source_types.add(event["date_source_type"])
        existing["date_source_type"] = ";".join(sorted(source_types, key=DATE_SOURCE_PRIORITY.get))
        if DATE_SOURCE_PRIORITY[event["date_source_type"]] < existing_priority:
            existing["update_title"] = event["update_title"]
    return list(unique.values())


def source_filename(url: str) -> str:
    slug = urlparse(url).path.rstrip("/").rsplit("/", 1)[-1]
    digest = hashlib.sha256(url.encode()).hexdigest()[:10]
    return f"{slug}-{digest}.html"


def reconcile_events(events: list[dict[str, str | None]]) -> tuple[list[dict[str, str | None]], int]:
    grouped = defaultdict(list)
    for event in events:
        key = (
            event["update_date"],
            event["franchise"],
            event["title"],
            event["experience"],
            event["update_title"].lower(),
        )
        grouped[key].append(event)
    reconciled = []
    duplicate_events = 0
    for group in grouped.values():
        if len(group) > 1:
            duplicate_events += len(group) - 1
        primary = sorted(group, key=lambda event: source_priority(event["date_source_type"]))[0].copy()
        for field in ("season", "source_page_title", "source_url", "source_file", "retrieved_at"):
            values = list(dict.fromkeys(event[field] for event in group if event[field]))
            primary[field] = " | ".join(values) if values else None
        source_types = set()
        for event in group:
            source_types.update(event["date_source_type"].split(";"))
        primary["date_source_type"] = ";".join(sorted(source_types, key=DATE_SOURCE_PRIORITY.get))
        reconciled.append(primary)
    return reconciled, duplicate_events


def main() -> None:
    args = parse_args()
    raw_dir = args.output_root / "raw" / "patch_pages"
    processed_dir = args.output_root / "processed"
    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})

    sitemap_urls = discover_sitemap(get(session, SITEMAP_URL), args.start_date, args.end_date)
    archive_urls = discover_archive(get(session, ARCHIVE_URL), args.start_date, args.end_date)
    pages = sorted(sitemap_urls | archive_urls)
    logging.info("URLs found through sitemap: %d", len(sitemap_urls))
    logging.info("URLs found through archive: %d", len(archive_urls))
    logging.info("URLs found by both: %d", len(sitemap_urls & archive_urls))
    logging.info("URLs unique to sitemap: %d", len(sitemap_urls - archive_urls))
    logging.info("URLs unique to archive: %d", len(archive_urls - sitemap_urls))
    logging.info("Pages discovered: %d", len(pages))

    events = []
    failures = []
    downloaded = 0
    for index, url in enumerate(pages):
        if index:
            time.sleep(args.delay)
        filename = source_filename(url)
        try:
            html = get(session, url)
            (raw_dir / filename).write_text(html, encoding="utf-8")
            downloaded += 1
            retrieved_at = datetime.now(timezone.utc).isoformat()
            page_events = extract_updates(html, url, retrieved_at, filename)
            page_events = [
                event for event in page_events if args.start_date <= date.fromisoformat(event["update_date"]) <= args.end_date
            ]
            events.extend(page_events)
            logging.info("Downloaded %s; dated updates extracted: %d", url, len(page_events))
            if not page_events:
                failures.append((url, "no structured dated updates extracted"))
        except (requests.RequestException, OSError, UnicodeError) as exc:
            failures.append((url, str(exc)))
            logging.error("Download/parsing failed for %s: %s", url, exc)

    reconciled, duplicate_events = reconcile_events(events)
    output_csv = processed_dir / "cod_change_history.csv"
    with output_csv.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        writer.writerows(sorted(reconciled, key=lambda row: (row["update_date"] or "", row["source_url"] or "")))
    log_path = processed_dir / "ingestion.log"
    with log_path.open("w", encoding="utf-8") as handle:
        handle.write(f"sitemap_urls\t{len(sitemap_urls)}\n")
        handle.write(f"archive_urls\t{len(archive_urls)}\n")
        handle.write(f"both\t{len(sitemap_urls & archive_urls)}\n")
        handle.write(f"sitemap_only\t{len(sitemap_urls - archive_urls)}\n")
        handle.write(f"archive_only\t{len(archive_urls - sitemap_urls)}\n")
        handle.write(f"pages_discovered\t{len(pages)}\n")
        handle.write(f"pages_downloaded\t{downloaded}\n")
        handle.write(f"raw_events\t{len(events)}\n")
        handle.write(f"logical_events\t{len(reconciled)}\n")
        handle.write(f"duplicate_events_reconciled\t{duplicate_events}\n")
        for url, reason in failures:
            handle.write(f"failure\t{url}\t{reason}\n")
    logging.info("Pages downloaded: %d", downloaded)
    logging.info("Raw dated updates extracted: %d", len(events))
    logging.info("Logical update events: %d", len(reconciled))
    logging.info("Duplicate events reconciled: %d", duplicate_events)
    logging.info("Pages with failures or no dated updates: %d", len(failures))
    logging.info("CSV written: %s", output_csv)


if __name__ == "__main__":
    main()
