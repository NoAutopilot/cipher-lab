#!/usr/bin/env python3
"""RUN6-BIR3637 (5 Oct 2026): list the 193 split positions of the kept F36-READ rows (all but r36_L09-L15) for one
reconciliation call, F36R-REREAD's adjudicate_in.tsv format. Split = both readers gave a sign id and they differ."""
import csv
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; OLD = HERE.parent / "f36"
DROP = {f"r36_L{i:02d}" for i in range(9, 16)}
SEGS = defaultdict(int)
for p in (OLD / "crops").glob("*_s*.png"):
    SEGS[p.name.rsplit("_s", 1)[0]] += 1
rows = defaultdict(list)
for r in csv.DictReader(open(OLD / "recon.tsv"), delimiter="\t"):
    if r["line"] not in DROP: rows[r["line"]].append(r)
out = ["line\tpos\tcand_1\tcand_2\tleft_context\tright_context\tsegment_hint"]
for line, rs in rows.items():
    n = len(rs)
    for i, r in enumerate(rs):
        a, b = r["A"].strip(), r["B"].strip()
        if a in ("", "?") or b in ("", "?") or a == b: continue
        L = " ".join(x["sign"] for x in rs[max(0, i - 3):i]); R = " ".join(x["sign"] for x in rs[i + 1:i + 4])
        seg = min(SEGS[line], int(i / n * SEGS[line]) + 1)
        out.append(f"{line}\t{r['pos']}\t{a}\t{b}\t{L}\t{R}\tabout _s{seg} of {SEGS[line]} (pos {r['pos']} of {n})")
(HERE / "adjudicate_in.tsv").write_text("\n".join(out) + "\n"); print(len(out) - 1)
