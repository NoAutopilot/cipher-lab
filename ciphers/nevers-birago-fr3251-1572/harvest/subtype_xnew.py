#!/usr/bin/env python3
"""Relabel the recurring off-sheet "ae/oe ligature" sign as X_AE in a reconciled sequence (NEVBIR-185B, 2 Oct 2026).
passC rows carry only X_NEW; the readers' shape notes live in their own pass files. A passC X_NEW row becomes X_AE when
either reader's note at the aligned position (via <out>_agreement.tsv: posA/posB) describes the ligature (ae, oe,
"x with e", ligature, æ, œ). Value-blind: reads shapes only.  The r value is then tested as a fitted extra
(decode_control.py --extra X_AE=r), shuffled with the rest of the map in the control.
  python3 subtype_xnew.py PASSC AGREEMENT PASSA PASSB OUT"""
import csv, re, sys
pc, ag, pa, pb, out = sys.argv[1:6]
PAT = re.compile(r"\bae\b|\boe\b|ae/oe|x with e|ligature|æ|œ|x-e|xe\b", re.I)
def notes(fn):
    return {(r["passage"], r["pos"]): r.get("note") or "" for r in csv.DictReader(open(fn), delimiter="\t")}
NA, NB = notes(pa), notes(pb)
# merged position k (1-based, per passage) <- k-th non-dropped agreement row
lig, cnt = set(), {}
for r in csv.DictReader(open(ag), delimiter="\t"):
    if r["merged"] in ("", "NONE"):
        continue
    p = r["passage"]; cnt[p] = cnt.get(p, 0) + 1
    if PAT.search(NA.get((p, r["posA"]), "")) or PAT.search(NB.get((p, r["posB"]), "")):
        lig.add((p, str(cnt[p])))
rows = list(csv.DictReader(open(pc), delimiter="\t")); n = 0
for r in rows:
    if r["sign_id"] == "X_NEW" and (r["passage"], r["pos"]) in lig:
        r["sign_id"] = "X_AE"; n += 1
w = csv.DictWriter(open(out, "w"), fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
w.writeheader(); w.writerows(rows)
print(n, "X_NEW -> X_AE of", sum(r["sign_id"] in ("X_NEW", "X_AE") for r in rows), "->", out)
