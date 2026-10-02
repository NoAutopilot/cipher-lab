#!/usr/bin/env python3
"""Join no.86's (27 Aug 1572) reconciled blind sequences into one per-letter sequence (NEVBIR-174V-B, 2 Oct 2026).
  python3 join_no86.py [--halfA f174vA/passC.tsv] [--out no86/passC_halfB.tsv]
Pieces, in page order, each relabelled with its folio so passages stay distinct:
  f.174r foot  f174r/passC.tsv           (NEVBIR-170)                    -> f174r_L01..
  f.174v 1-11  --halfA (NEVBIR-174V-A)   only when given                 -> f174v_L01..L11
  f.174v 12-22 f174vB/passC.tsv L01..L11 (page lines 12-22; V* rows from the first, off-line f175v crops are dropped)
                                                                          -> f174v_L12..L22
  f.175r head  f174vB/passC.tsv R01      -> f175r_R01
  f.175v run   f175v/passC.tsv V01..V03  -> f175v_V01..V03
Without --halfA it writes half B alone (no f.174r): --with-f174r adds the f.174r foot.
"""
import argparse, csv
from pathlib import Path
H = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument("--halfA"); ap.add_argument("--with-f174r", action="store_true")
ap.add_argument("--out", required=True); a = ap.parse_args()
def rows(p):
    return list(csv.DictReader(open(H / p), delimiter="\t"))
out = []
if a.with_f174r or a.halfA:
    out += [dict(r, passage="f174r_" + r["passage"]) for r in rows("f174r/passC.tsv")]
if a.halfA:
    out += [dict(r, passage="f174v_" + r["passage"]) for r in rows(a.halfA)]
for r in rows("f174vB/passC.tsv"):
    p = r["passage"]
    if p.startswith("L"):
        out.append(dict(r, passage=f"f174v_L{int(p[1:]) + 11:02d}"))
    elif p.startswith("R"):
        out.append(dict(r, passage="f175r_" + p))
out += [dict(r, passage="f175v_" + r["passage"]) for r in rows("f175v/passC.tsv")]
(H / a.out).parent.mkdir(parents=True, exist_ok=True)
with open(H / a.out, "w") as f:
    f.write("passage\tpos\tsign_id\tconf\tnote\n")
    for r in out:
        f.write(f"{r['passage']}\t{r['pos']}\t{r['sign_id']}\t{r.get('conf','')}\t{r.get('note','') or ''}\n")
print(f"{len(out)} signs -> {a.out}")
