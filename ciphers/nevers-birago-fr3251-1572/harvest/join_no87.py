#!/usr/bin/env python3
"""Join the reconciled sign sequences of the whole no.87 cipher passage in reading order (GAPS4-nevers-birago, 2 Oct 2026):
f.178r foot (f178r/passC.tsv, passages renamed R01..), f.178v (f178v/passC_L01-23.tsv, L01..L23), f.179r head
(f179r/passC.tsv, renamed V01..) -> passC_no87.tsv for decode_control.py / shuffled_judge.py / align_sheet.py.
  python3 join_no87.py [--out passC_no87.tsv]"""
import argparse, csv
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--out", default=str(HERE / "passC_no87.tsv")); a = ap.parse_args()
parts = [("f178r/passC.tsv", "R"), ("f178v/passC_L01-23.tsv", "L"), ("f179r/passC.tsv", "V")]
n = 0
with open(a.out, "w") as f:
    f.write("passage\tpos\tsign_id\tconf\tnote\n")
    for fn, pre in parts:
        for r in csv.DictReader(open(HERE / fn), delimiter="\t"):
            f.write(f"{pre}{r['passage'].lstrip('L')}\t{r['pos']}\t{r['sign_id']}\t{r['conf']}\t{r.get('note','')}\n"); n += 1
print(f"{n} signs -> {a.out}")
