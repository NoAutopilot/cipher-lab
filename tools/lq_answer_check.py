#!/usr/bin/env python3
"""Flag a local-queue-runner answer as a bare image-portal negative or a real
"not digitised" verdict, before the landing worker sets a LOCAL-QUEUE.tsv row `done`
(CLAUDE.md Usage 8a, rules become tools; the L19 incident of 26 Sept 2026).

The incident: LOCAL-QUEUE row L19 (ASKS 30, Bodleian MS. Rawl. A. 24) had the owner's desk
runner search Digital Bodleian, get "no items", and first record that as the answer -- as
if an image portal's search finding nothing meant the volume was not digitised. It wasn't:
the holding catalogue (Bodleian Archives & Manuscripts, records at marco.ox.ac.uk) has the
volume record ("Thurloe Papers, vol. xxiv", ark:/29072/x0x920fw11hz) flagged "Not available
online", with item-level records for individual folios listed underneath it. An image
portal's "no items" answers only "the search found no images"; it never answers "the item
is undigitised or absent" (CLAUDE.md Access playbook, "Getting the material"). The same
shape recurs at every institution in tools/data/catalogue_ladders.tsv whose image portal and
holding catalogue are two different systems.

The rule this script enforces: a runner answer that reports a NEGATIVE ("not found", "no
items", "no results", "not digitised"/"not digitized", "not available", "nothing") must also
show two rungs of the ladder were climbed, not just the image portal:
  (a) a holding-catalogue record URL or ark -- an `ark:/...` identifier, or a URL on a host
      named in tools/data/catalogue_ladders.tsv's `holding_catalogue` column (for the row's
      institution if named with --row, otherwise any institution's), or a bare mention of
      "catalogue"/"catalog" alongside a URL;
  (b) an availability phrase quoted FROM that record -- "not available online", "available
      online", or a viewer/IIIF link mentioned by name.
A negative with both rungs present exits 0 (a genuine "not digitised per the catalogue
record" verdict, the L19 fix's own wording). A negative with either rung missing exits
nonzero, naming which rung is missing, so a bare image-portal "no items" never gets landed
as the answer. A POSITIVE answer (no negative phrase found) always exits 0 -- this script
only gates negatives, since a positive answer already did the work the negative shortcut
skips.

Usage:
  tools/lq_answer_check.py FILE [--row ID]
    FILE is the runner answer file (a `[LQ-<id>]` PR's added file, or a NOTES.md paragraph
    passed by path). --row ID is the LOCAL-QUEUE.tsv row id (e.g. L19); when given and the
    row's target folder can be matched to an institution in catalogue_ladders.tsv, rung (a)
    is checked against that institution's own holding_catalogue host first, falling back to
    any institution's if that specific host is not found in FILE.

Exit 0: FILE has no negative phrase (a positive answer), or it has one and both ladder rungs
  (holding-catalogue URL/ark, quoted availability phrase) are present.
Exit 1: FILE has a negative phrase and is missing one or both ladder rungs -- printed by name
  ("missing rung: holding-catalogue record", "missing rung: availability phrase", or both).
Exit 2: FILE or --row could not be read/resolved.

This checks the shape of the citation (a negative claim backed by a catalogue URL and a
quoted flag), not that the URL is real or the quote is accurate -- that is still the landing
worker's and the verifier's job, the same limit tools/intake_gate_check.py states for its own
citation check.
"""
import argparse
import csv
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LADDER_PATH = os.path.join(ROOT, "tools", "data", "catalogue_ladders.tsv")
LOCAL_QUEUE_PATH = os.path.join(ROOT, "LOCAL-QUEUE.tsv")

# A negative verdict phrase (case-insensitive, word-bounded so "not available online" -- the
# availability phrase itself -- still counts as a negative, which is correct: the shortcut
# this script blocks is answering with the negative and NOTHING else).
NEGATIVE_RE = re.compile(
    r'\bnot\s+found\b|\bno\s+items\b|\bno\s+results\b|\bnot\s+digitis(?:ed|able)\b|'
    r'\bnot\s+digitiz(?:ed|able)\b|\bnot\s+available\b|\bnothing\b',
    re.IGNORECASE,
)

ARK_RE = re.compile(r'\bark:/\d+/\S+', re.IGNORECASE)
CATALOGUE_WORD_URL_RE = re.compile(
    r'\b(?:catalog(?:ue)?)\b[^\n]{0,80}\bhttps?://\S+|https?://\S+[^\n]{0,80}\b(?:catalog(?:ue)?)\b',
    re.IGNORECASE,
)
URL_RE = re.compile(r'https?://[^\s)>\]]+', re.IGNORECASE)

AVAILABILITY_PHRASES = (
    "not available online",
    "available online",
    "viewer link",
    "iiif",
)
VIEWER_WORD_RE = re.compile(r'\bviewer\b', re.IGNORECASE)


def _host_of(url):
    m = re.match(r'https?://([^/]+)', url, re.IGNORECASE)
    return m.group(1).lower() if m else ""


def load_ladder(path=LADDER_PATH):
    """Return list of dict rows from tools/data/catalogue_ladders.tsv, or [] if unreadable."""
    if not os.path.isfile(path):
        return []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def ladder_hosts_for_institution(rows, institution):
    """Hostnames mentioned in the holding_catalogue cell of the named institution's row(s)."""
    hosts = set()
    for row in rows:
        if institution and row.get("institution", "").strip().lower() != institution.strip().lower():
            continue
        cell = row.get("holding_catalogue", "")
        for url in URL_RE.findall(cell):
            hosts.add(_host_of(url))
        for token in re.findall(r'[a-z0-9.-]+\.[a-z]{2,}(?:/\S*)?', cell, re.IGNORECASE):
            hosts.add(token.split("/")[0].lower())
    return {h for h in hosts if h}


def all_ladder_holding_hosts(rows):
    hosts = set()
    for row in rows:
        hosts |= ladder_hosts_for_institution(rows, row.get("institution", ""))
    return hosts


def institution_for_row(row_id, ladder_rows):
    """Best-effort: match a LOCAL-QUEUE.tsv row's target folder or instruction text against
    ladder institution names/hosts. Returns institution name or None. Never invents a match --
    returns None (not a guess) when nothing in the row's text names a known institution."""
    if not row_id or not os.path.isfile(LOCAL_QUEUE_PATH):
        return None
    with open(LOCAL_QUEUE_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            rid = row.get("id", "").strip()
            if rid == row_id or rid.split(":")[-1] == row_id:
                text = " ".join(row.values())
                for lrow in ladder_rows:
                    inst = lrow.get("institution", "")
                    if not inst:
                        continue
                    if inst.lower() in text.lower():
                        return inst
                    for host in ladder_hosts_for_institution(ladder_rows, inst):
                        if host and host in text.lower():
                            return inst
                return None
    return None


def find_negative(text):
    m = NEGATIVE_RE.search(text)
    return m.group(0) if m else None


def has_holding_catalogue_rung(text, ladder_rows, institution=None):
    if ARK_RE.search(text):
        return True
    if CATALOGUE_WORD_URL_RE.search(text):
        return True
    hosts = ladder_hosts_for_institution(ladder_rows, institution) if institution else set()
    if not hosts:
        hosts = all_ladder_holding_hosts(ladder_rows)
    for url in URL_RE.findall(text):
        if _host_of(url) in hosts:
            return True
    return False


def has_availability_rung(text):
    low = text.lower()
    if any(phrase in low for phrase in AVAILABILITY_PHRASES):
        return True
    return bool(VIEWER_WORD_RE.search(text))


def check(text, ladder_rows, institution=None):
    """Pure check used by the offline test. Returns (exit_code, message)."""
    neg = find_negative(text)
    if neg is None:
        return 0, "positive answer (no negative phrase found) -- nothing to gate"
    missing = []
    if not has_holding_catalogue_rung(text, ladder_rows, institution):
        missing.append("holding-catalogue record (an ark:/ id, a catalogue URL, or a URL on a "
                        "host from tools/data/catalogue_ladders.tsv's holding_catalogue column)")
    if not has_availability_rung(text):
        missing.append("availability phrase quoted from the record ('not available online', "
                        "'available online', a viewer or IIIF link)")
    if missing:
        lines = "\n".join(f"  missing rung: {m}" for m in missing)
        return 1, (
            f"negative answer ({neg!r}) with a missing ladder rung -- an image portal's negative "
            f"is a search result, not a digitisation verdict (L19, 26 Sept 2026):\n{lines}"
        )
    return 0, f"negative answer ({neg!r}) with both ladder rungs present -- a genuine not-digitised verdict"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="the runner answer file to check")
    ap.add_argument("--row", default=None, help="LOCAL-QUEUE.tsv row id (e.g. L19), for institution matching")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.file):
        print(f"no such file: {args.file}")
        return 2
    with open(args.file, encoding="utf-8") as f:
        text = f.read()

    ladder_rows = load_ladder()
    institution = institution_for_row(args.row, ladder_rows) if args.row else None

    code, message = check(text, ladder_rows, institution)
    row_label = f" (row {args.row})" if args.row else ""
    print(f"{args.file}{row_label}: {message}")
    return code


if __name__ == "__main__":
    sys.exit(main())
