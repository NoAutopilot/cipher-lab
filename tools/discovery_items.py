#!/usr/bin/env python3
"""List item-level records of a TNA State Papers piece from the Discovery API, filtered by a search term.

Usage:
    python3 tools/discovery_items.py "SP 91" "SP 91/5" cipher undeciphered duplicate > items.tsv

The first argument is the Discovery record series (e.g. "SP 91"), the second the piece prefix to keep
(e.g. "SP 91/5"), the rest are search terms; each term is queried separately and the union is printed as
TSV sorted by folio, one row per item: reference, covering date, Discovery id, sender/recipient (first
sentence of the description), dateline, and every sentence that mentions cipher, decipher, duplicate or
undeciphered. Prints the full description as the last column. Needs network access to
discovery.nationalarchives.gov.uk; the API answers plain HTTPS GET with a browser User-Agent.

Per-item note mode (2 Oct 2026, A2-YOR):
    python3 tools/discovery_items.py --notes C4539850 > notes.tsv

Keyword search only sees the description; TNA often puts "Partly in cipher." in the separate `note` field
(SP 78/232/44), so a keyword search misses those items. --notes PARENT_ID lists every child of the piece
(/API/records/v1/children) and fetches each item's details record (/API/records/v1/details), 1.6 s apart,
one at a time, printing: reference, covering date, Discovery id, note, cipher flag (cipher word in the note
or description), description. Stops at the first non-200 (good-citizen rule). The piece's Discovery id is
the `parentId` of any of its items' details records.
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://discovery.nationalarchives.gov.uk/API/search/records"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
CIPHER_WORDS = re.compile(r"cipher|cypher|decipher|duplicate|undeciphered", re.I)


def search(series, term):
    q = urllib.parse.urlencode({"sps.searchQuery": term, "sps.recordSeries": series, "sps.resultsPageSize": 200})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r).get("records", [])


REC = "https://discovery.nationalarchives.gov.uk/API/records/v1"


def get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def clean(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", text or "")).strip()


def note_rows(parent_id, fetch=get_json, pause=1.6):
    """Yield (reference, covering date, id, note, flag, description) for every child of parent_id."""
    kids = fetch(f"{REC}/children/{parent_id}?limit=500")
    if kids.get("hasMoreAfterLast"):
        sys.exit("more than 500 children: paging not implemented")
    for asset in kids.get("assets", []):
        time.sleep(pause)
        d = fetch(f"{REC}/details/{asset['id']}")
        note = clean(d.get("note"))
        desc = clean((d.get("scopeContent") or {}).get("description"))
        flag = "cipher" if CIPHER_WORDS.search(note) or CIPHER_WORDS.search(desc) else ""
        yield (d.get("citableReference") or "", d.get("coveringDates") or "", d.get("id") or "", note, flag, desc)


def folio_key(ref):
    return [int(x) for x in re.findall(r"\d+", ref)]


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--notes":
        print("reference\tcovering_date\tdiscovery_id\tnote\tcipher_flag\tdescription")
        for row in note_rows(sys.argv[2]):
            print("\t".join(row), flush=True)
        return
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    series, piece, terms = sys.argv[1], sys.argv[2], sys.argv[3:]
    seen = {}
    for term in terms:
        for rec in search(series, term):
            ref = rec.get("reference") or ""
            if ref.startswith(piece + "/"):
                seen.setdefault(ref, rec)
    print("reference\tcovering_date\tdiscovery_id\tparties\tdateline\tcipher_sentences\tdescription")
    for ref in sorted(seen, key=folio_key):
        rec = seen[ref]
        desc = re.sub(r"\s+", " ", rec.get("description") or "").strip()
        body = desc.split(":", 1)[1].strip() if ":" in desc else desc
        parties = body.split(".", 1)[0].strip()
        m = re.search(r"Dated[^.]*\.", desc)
        dateline = m.group(0) if m else ""
        sentences = [s.strip() for s in re.split(r"(?<=\.)\s+", desc) if CIPHER_WORDS.search(s)]
        print("\t".join([ref, rec.get("coveringDates") or "", rec.get("id") or "", parties, dateline,
                         " / ".join(sentences), desc]))


if __name__ == "__main__":
    main()
