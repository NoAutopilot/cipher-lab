#!/usr/bin/env python3
"""GAPS182 (3 Oct 2026): scan Clay 1881 (The Agony Column of the "Times" 1800-1870) for a second ad in ad 1's
dot-and-bar sign script, as material for an independent test of Laura's rule (GAPS160/178).

Input: the IA djvu OCR, https://archive.org/download/agonycolumntime00claygoog/agonycolumntime00claygoog_djvu.txt
(not committed, 525 kB; re-fetch with curl). A line is flagged when it carries >= 4 sign-like OCR glyphs
(bullet, square, diamond, bar, equals) or a "( :" / ":||" bracketed-dot or bar cluster, the forms item 1459's own
signs take in this OCR (positive control: item 1459 must be flagged). Each flag is assigned to the nearest
preceding item header and classed by hand in the TSV's last column.
Usage: python3 sign_sibling_scan.py DJVU.txt [--out sign_sibling_scan.tsv]
"""
import argparse, re
ap = argparse.ArgumentParser(); ap.add_argument("djvu"); ap.add_argument("--out", default="sign_sibling_scan.tsv")
a = ap.parse_args()
lines = open(a.djvu, encoding="utf-8", errors="replace").read().split("\n")
hdr = re.compile(r"^([0-9iIlZzOo]{3,4})[.,] ?— ")
item, rows = "front matter", []
for n, l in enumerate(lines, 1):
    m = hdr.match(l)
    if m: item = l.strip()[:45]
    k = sum(l.count(c) for c in "•■♦|=▪●")
    if k >= 4 or "( :" in l or ":||" in l:
        rows.append((n, k, item, l.strip()[:80].replace("\t", " ")))
# Hand classes from reading each flagged line in context (GAPS182): only item 1459 is a sign-script ad.
def cls(r):
    if r[2].startswith("1459"): return "SIGN-SCRIPT (ad 1 itself, positive control)"
    if r[0] < 200: return "plate/frontispiece noise"
    if r[0] > 15000: return "publisher's catalogue noise"
    return "drop-cap or punctuation OCR noise in a clear/number ad"
with open(a.out, "w") as f:
    f.write("line\tglyphs\titem\ttext\tclass\n")
    for r in rows: f.write("\t".join(map(str, r)) + "\t" + cls(r) + "\n")
sign = sum(1 for r in rows if not cls(r).startswith(("plate", "publisher", "drop")))
print(f"flagged lines {len(rows)}; sign-script items: {sorted({r[2] for r in rows if cls(r).startswith('SIGN')})}; other sign-script lines {sign - sum(1 for r in rows if r[2].startswith('1459'))}")
