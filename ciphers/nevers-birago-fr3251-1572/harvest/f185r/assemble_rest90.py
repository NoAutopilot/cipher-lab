#!/usr/bin/env python3
"""NEVBIR-185 (2 Oct 2026): assemble one reader's pass of no.90's f.184v foot + f.185r L01-08.
The first f.185r cut (manifest.json) put band L03 on manuscript line 2 again (both readers flagged it) and missed line 5;
line 5 was cut separately (l5/, --centres 610) and read as passage f185r_L05x. This drops the duplicate band, renumbers
the old bands L04/L05 to manuscript lines 3/4, and puts L05x in as line 5, so passage ids are manuscript line numbers.
  python3 assemble_rest90.py A   -> passA_rest90_ms.tsv     (and B)"""
import csv, sys
from pathlib import Path
H = Path(__file__).resolve().parent
r = sys.argv[1]
ren = {"f185r_L04": "f185r_L03", "f185r_L05": "f185r_L04", "f185r_L05x": "f185r_L05"}
rows = list(csv.DictReader(open(H / f"pass{r}_rest90.tsv"), delimiter="\t"))
l5 = list(csv.DictReader(open(H / f"pass{r}_l5.tsv"), delimiter="\t"))
fields = list(rows[0].keys())
out = []
for row in rows:
    p = row["passage"]
    if p == "f185r_L03":
        continue
    if p == "f185r_L06" and not any(o["passage"] == "f185r_L05" for o in out):
        out += [dict(x, passage=ren[x["passage"]]) for x in l5]
    if row["sign_id"] == "K":  # reader A wrote the brief's Latin-capital-K code as bare K once (f184v_L01 pos 6)
        row["sign_id"] = "X_K"
    out.append(dict(row, passage=ren.get(p, p)))
w = csv.DictWriter(open(H / f"pass{r}_rest90_ms.tsv", "w"), fieldnames=fields, delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(out)
print(r, len(out), "signs")
