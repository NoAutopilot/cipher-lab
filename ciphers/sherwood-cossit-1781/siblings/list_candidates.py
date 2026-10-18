#!/usr/bin/env python3
"""List Brymner 1888 calendar entries in B.175-B.178 that name Cossit/Sumner, a cypher, or Claremont.

Reads archive.org reportoncanadian1888publuoft_djvu.txt (re-downloadable; not committed), splits the
B.175-B.178 block (djvu lines 36930-45125) into calendar entries at blank lines, takes each entry's trailing
page number and the volume from the last running head above it, and writes candidates.tsv.
Usage: list_candidates.py DJVU_TXT [--out candidates.tsv]
"""
import argparse, re, csv

ap = argparse.ArgumentParser()
ap.add_argument("djvu")
ap.add_argument("--out", default="candidates.tsv")
a = ap.parse_args()
lines = open(a.djvu, encoding="utf-8", errors="replace").read().split("\n")
LO, HI = 36930, 45125
TERMS = re.compile(r"cos+[bi]t|summer|sumner|sammer|cyph|ciph|claremont", re.I)
vol = "B.175"
entries, cur, start = [], [], None
for i in range(LO - 1, HI):
    s = re.sub(r"\s+", " ", lines[i]).strip()
    m = re.search(r"\bB\. ?(17[5-8])(?:[-‑](\d))?", s)
    if m and len(s) < 60:
        vol = "B.%s%s" % (m.group(1), "-" + m.group(2) if m.group(2) else "")
        continue
    if not s:
        if cur:
            entries.append((start, vol, " ".join(cur)))
        cur = []
        continue
    if not cur:
        start = i + 1
    cur.append(s)
rows = []
for ln, v, t in entries:
    if not TERMS.search(t) or len(t) < 25:
        continue
    if re.search(r"\bsummer\b", t, re.I) and not re.search(r"cos+[bi]t|\bsummers?\b (to|and)|(to|and|Mr\.|Capt\.|Captain|Squire|B\.|Benjamin|Berjamin) summers?|by summer|from summer|with summer|Summer\.|Summer,", t, re.I):
        continue  # the season, not the man
    pm = re.search(r"(?:Page\s*)?(\d{1,3}(?:\s*(?:to|,|-)\s*\d{1,3})?)\s*\.?\s*$", t)
    page = pm.group(1) if pm else ""
    cy = "yes" if re.search(r"cyph|ciph", t, re.I) else "no"
    rows.append((v, page, ln, t[:400], cy))
with open(a.out, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["volume", "page_as_ocr", "djvu_line", "brymner_words", "cypher_flag"])
    w.writerows(rows)
print(len(rows), "candidate entries;", sum(r[4] == "yes" for r in rows), "cypher-flagged")
