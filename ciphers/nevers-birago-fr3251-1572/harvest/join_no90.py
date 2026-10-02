#!/usr/bin/env python3
"""Join no.90's (2 Oct 1572) reconciled blind sequences into one per-letter sequence (NEVBIR-185, 2 Oct 2026).
  python3 join_no90.py --out no90/passC_all.tsv
Pieces, in page order, relabelled with the folio so passages stay distinct:
  f.184r runs      f184r/passC.tsv        (NEVBIR-184)  L01..L12 -> f184r_L01..
  f.184v foot      f185r/passC_rest90.tsv (NEVBIR-185)  f184v_L01..L04 (already folio-labelled)
  f.185r L01-L08   f185r/passC_rest90.tsv (NEVBIR-185)  f185r_L01..L08 (manuscript line numbers)
f.185r lines 11-14 and 17-28 and the f.185v run are not read yet (NOTES.md, Remaining gaps)."""
import argparse, csv
from pathlib import Path
H = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
def rows(p):
    return list(csv.DictReader(open(H / p), delimiter="\t"))
out = [dict(r, passage="f184r_" + r["passage"]) for r in rows("f184r/passC.tsv")] + rows("f185r/passC_rest90.tsv")
(H / a.out).parent.mkdir(exist_ok=True)
with open(H / a.out, "w") as f:
    f.write("passage\tpos\tsign_id\tconf\tnote\n")
    for r in out:
        f.write(f"{r['passage']}\t{r['pos']}\t{r['sign_id']}\t{r['conf']}\t{r.get('note') or ''}\n")
print(len(out), "signs ->", a.out)
