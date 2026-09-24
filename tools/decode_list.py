#!/usr/bin/env python3
"""Crawl DECODE's (de-crypt.org) RecordsList catalogue, filtered by status and
record type, without logging in.

Discovery, 24 September 2026: the RecordsList grid itself is public (no
DECODE_USER/DECODE_PASS needed, unlike RecordsView/DocumentsList content).
Submitting the site's own "Advanced Search" form (RecordsSearch) for
record_type=Cipher, status=Non-decrypted once, in a real browser, redirects to
a plain repeatable GET:

    RecordsList?x_record_type=1&z_record_type=%3D&x_status=2&z_status=%3D&cmd=search

x_status codes (read from RecordsSearch's own <select name="x_status">, 24 Sept
2026): 1 Decrypted, 2 Non-decrypted, 3 Partially decrypted, 4 N/A.
x_record_type codes: 1 Cipher, 2 Key, 3 Manual. That URL plus &recperpage=50
(the grid's own maximum page size) &page=N works from plain curl/requests with
no cookies at all -- confirmed against the live site.

Usage:
    tools/decode_list.py --status non-decrypted,partially-decrypted --record-type cipher \
        --out sources/decode/records-non-decrypted-2026-09-24.tsv [--raw-dir DIR] \
        [--delay 1.5] [--recperpage 50] [--max-pages N] [--max-requests 300]

Writes a TSV with columns: id, status, record_type, holder_raw, city, shelfmark_code,
date_range, cleartext_lang, plaintext_lang, number_of_pages, source_page. Never
downloads a record's documents or images (this is a listing tool only); never
logs in (no credentials touched). Good-citizen: one request at a time, >=1.5s
apart (default), descriptive User-Agent, and a hard --max-requests cap.
"""
import argparse
import csv
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://de-crypt.org/decrypt-web/RecordsList"
UA = "cipher-lab research script (contact via repository)"

STATUS_CODES = {
    "decrypted": 1,
    "non-decrypted": 2,
    "partially-decrypted": 3,
    "n/a": 4,
}
RECORD_TYPE_CODES = {
    "cipher": 1,
    "key": 2,
    "manual": 3,
}

ROW_RE = re.compile(
    r'data-name="id">\s*<span[^>]*>\s*<span>\s*(\d+)</span>.*?'
    r'data-name="c_holder">\s*<span[^>]*>\s*<span>\s*(.*?)</span>\s*</span>\s*</td>.*?'
    r'data-name="c_cates">\s*<span[^>]*>\s*<span[^>]*>\s*(.*?)</span>.*?'
    r'data-name="c_lang">\s*<span[^>]*>\s*<span[^>]*>\s*(.*?)</span>.*?'
    r'data-name="record_type">\s*<span[^>]*>\s*<span[^>]*>\s*(.*?)</span>.*?'
    r'data-name="status">\s*<span[^>]*>\s*<span[^>]*>\s*(.*?)</span>.*?'
    r'data-name="number_of_pages">\s*<span[^>]*>\s*<span>\s*(.*?)</span>',
    re.S,
)
PAGER_COUNT_RE = re.compile(r'ew-pager-count[^>]*>([\d,]+)<')
TAG_RE = re.compile(r"<[^>]+>")
CITY_RE = re.compile(r"<b>(.*?)</b>")
SMALL_RE = re.compile(r"<small>(.*?)</small>")


def clean(text):
    return re.sub(r"\s+", " ", TAG_RE.sub(" ", text)).strip()


def fetch(url, delay, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    time.sleep(delay)
    return html


def parse_lang(raw):
    m = re.search(r"Cleartext:</b>(.*?)<br", raw, re.S)
    cleartext = clean(m.group(1)) if m else ""
    m = re.search(r"Plaintext:</b>(.*)$", raw, re.S)
    plaintext = clean(m.group(1)) if m else ""
    return cleartext, plaintext


def parse_holder(raw):
    city_m = CITY_RE.search(raw)
    city = clean(city_m.group(1)) if city_m else ""
    small_m = SMALL_RE.search(raw)
    shelfmark_code = clean(small_m.group(1)) if small_m else ""
    holder_plain = clean(SMALL_RE.sub("", raw))
    return holder_plain, city, shelfmark_code


def parse_rows(html, source_page):
    rows = []
    for m in ROW_RE.finditer(html):
        rid, holder_raw, cates, lang_raw, rtype, status, npages = m.groups()
        holder_plain, city, shelfmark_code = parse_holder(holder_raw)
        cleartext_lang, plaintext_lang = parse_lang(lang_raw)
        rows.append(
            {
                "id": rid,
                "status": clean(status),
                "record_type": clean(rtype),
                "holder_raw": holder_plain,
                "city": city,
                "shelfmark_code": shelfmark_code,
                "date_range": clean(cates),
                "cleartext_lang": cleartext_lang,
                "plaintext_lang": plaintext_lang,
                "number_of_pages": clean(npages),
                "source_page": source_page,
            }
        )
    return rows


def pager_total(html):
    m = PAGER_COUNT_RE.search(html)
    if not m:
        return None
    return int(m.group(1).replace(",", ""))


def crawl_status(status_name, record_type_name, recperpage, delay, max_pages, budget, raw_dir):
    status_code = STATUS_CODES[status_name]
    rtype_code = RECORD_TYPE_CODES[record_type_name]
    params = {
        "x_record_type": rtype_code,
        "z_record_type": "=",
        "x_status": status_code,
        "z_status": "=",
        "cmd": "search",
        "recperpage": recperpage,
        "page": 1,
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    if budget[0] <= 0:
        return [], 0
    html = fetch(url, delay)
    budget[0] -= 1
    total = pager_total(html) or 0
    pages = (total + recperpage - 1) // recperpage if total else (1 if html else 0)
    if max_pages:
        pages = min(pages, max_pages)
    rows = parse_rows(html, 1)
    if raw_dir:
        (raw_dir / f"{status_name}_p1.html").write_text(html, encoding="utf-8")
    for page in range(2, pages + 1):
        if budget[0] <= 0:
            print(f"  budget exhausted at page {page} of {pages} for {status_name}", file=sys.stderr)
            break
        params["page"] = page
        url = BASE + "?" + urllib.parse.urlencode(params)
        html = fetch(url, delay)
        budget[0] -= 1
        rows.extend(parse_rows(html, page))
        if raw_dir:
            (raw_dir / f"{status_name}_p{page}.html").write_text(html, encoding="utf-8")
    return rows, total


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--status", required=True, help="comma-separated: non-decrypted,partially-decrypted,decrypted,n/a")
    ap.add_argument("--record-type", default="cipher", help="cipher (default), key, or manual")
    ap.add_argument("--out", required=True, help="output TSV path")
    ap.add_argument("--raw-dir", default=None, help="optional directory to save raw fetched HTML pages")
    ap.add_argument("--delay", type=float, default=1.5, help="seconds between requests (default 1.5, good-citizen minimum)")
    ap.add_argument("--recperpage", type=int, default=50, help="rows per page, max 50 (site limit)")
    ap.add_argument("--max-pages", type=int, default=0, help="cap pages per status (0 = no cap)")
    ap.add_argument("--max-requests", type=int, default=300, help="hard cap on total HTTP requests this run")
    args = ap.parse_args()

    statuses = [s.strip().lower() for s in args.status.split(",") if s.strip()]
    for s in statuses:
        if s not in STATUS_CODES:
            ap.error(f"unknown status {s!r}; choose from {sorted(STATUS_CODES)}")
    rtype = args.record_type.strip().lower()
    if rtype not in RECORD_TYPE_CODES:
        ap.error(f"unknown record-type {rtype!r}; choose from {sorted(RECORD_TYPE_CODES)}")

    raw_dir = Path(args.raw_dir) if args.raw_dir else None
    if raw_dir:
        raw_dir.mkdir(parents=True, exist_ok=True)

    budget = [args.max_requests]
    all_rows = []
    for status in statuses:
        rows, total = crawl_status(status, rtype, args.recperpage, args.delay, args.max_pages, budget, raw_dir)
        print(f"{status}: {total} total, {len(rows)} fetched", file=sys.stderr)
        all_rows.extend(rows)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id", "status", "record_type", "holder_raw", "city", "shelfmark_code",
        "date_range", "cleartext_lang", "plaintext_lang", "number_of_pages", "source_page",
    ]
    with out_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
        w.writeheader()
        for row in all_rows:
            w.writerow(row)
    print(f"wrote {len(all_rows)} rows to {out_path}; requests used: {args.max_requests - budget[0]}", file=sys.stderr)


if __name__ == "__main__":
    main()
