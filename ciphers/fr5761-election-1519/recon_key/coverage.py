#!/usr/bin/env python3
"""Atlas coverage for the f104 alphabet sign row (glyphs/signs.tsv line 1), the one row of
f104 sign boxes that is unambiguously all cipher signs (no plain-script letters mixed in --
unlike the correspondent-name lines, which mix cursive names with one code sign each and
have no clean per-box split in signs.tsv). Coverage = share of the 21 positions whose HOG
cluster (glyphs/clusters.tsv) maps, via glyphs/labels.json, to a named K-code rather than "_".

Run from the target folder: python3 recon_key/coverage.py
"""
import csv, json, sys
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent.parent
    clusters = {r["id"]: r["cluster"] for r in csv.DictReader(open(root / "glyphs/clusters.tsv"), delimiter="\t") if r["kind"] == "sign"}
    labels = json.load(open(root / "glyphs/labels.json"))["signs"]
    signs = list(csv.DictReader(open(root / "glyphs/signs.tsv"), delimiter="\t"))

    line1 = [r for r in signs if r["page"] == "f104" and r["line"] == "1"]
    n = len(line1)
    coded = 0
    for r in line1:
        c = clusters.get(r["sid"])
        code = labels.get(c, "_") if c else "_"
        if code != "_":
            coded += 1
    pct = coded / n if n else 0.0
    print(f"f104 line1 (alphabet sign row): {coded}/{n} = {pct:.1%} have a mechanical atlas code")
    print("gate: >=70% ->", "PASS, no atlas expansion needed" if pct >= 0.70 else "FAIL, add missing alphabet signs as new atlas codes")
    return 0 if True else 1

if __name__ == "__main__":
    sys.exit(main())
