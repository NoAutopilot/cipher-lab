#!/usr/bin/env python3
"""D2-C1161LA (5 Oct 2026): per-sign A/B/C alignment for the th/z/S/4 look-alike pass.
C = ciphertext.tsv (merged); A, B = tx/<leaf>_passA/B.tsv (the two blind readers), aligned per line to C by edit distance
(tools/lookalike_pass._align). Writes la/align_abc.tsv (passage,pos,merged,idA,idB,status), la/passC.tsv
(passage,pos,sign_id), la/confusion.tsv (tools/lookalike_pass.py confusion on align_abc.tsv).
  python3 la/build_align.py
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from lookalike_pass import _align, confusion
# reader-label synonyms settled in NOTES.md (c187L/c185R reconciliations): ss and pass A's NEW:5hook = small s 's',
# NEW:v-bar = vdash, epsilon = e
SYN = {"ss": "s", "NEW:5hook": "s", "NEW:v-bar": "vdash", "\u03b5": "e"}
LEAF = {"c185R": "c185R", "c186L": "c186L", "c186R": "c186R_blk", "c187L": "c187L", "c187R": "c187R", "c188L": "c188L"}

def rows(p):
    d = {}
    for r in csv.DictReader(open(p), delimiter="\t"):
        d[r["row"]] = [SYN.get(x.rstrip("?"), x.rstrip("?")) for x in r["codes"].split()]
    return d

C = {}
for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t"):
    C.setdefault(r["line"], []).append(r["sign"])
P = {lf: (rows(os.path.join(T, "tx", f"{pf}_passA.tsv")), rows(os.path.join(T, "tx", f"{pf}_passB.tsv"))) for lf, pf in LEAF.items()}
out, pc = [], []
for ln, seq in C.items():
    lf, row = ln.split("_", 1)
    A, B = P[lf]
    a = _align(seq, A.get(row, [])); b = _align(seq, B.get(row, []))
    for i, (s, x, y) in enumerate(zip(seq, a, b), 1):
        x, y = x or "", y or ""
        st = "agree" if x == y == s else ("split" if x and y and x != y else ("split_gap" if not (x and y) else "agree_AB_notC"))
        out.append(dict(passage=ln, pos=i, merged=s, idA=x, idB=y, status=st, posA=i))
        pc.append(dict(passage=ln, pos=i, sign_id=s))
w = lambda p, rs: (lambda f: (lambda dw: (dw.writeheader(), dw.writerows(rs)))(csv.DictWriter(f, fieldnames=list(rs[0]), delimiter="\t", lineterminator="\n")))(open(p, "w"))
w(os.path.join(HERE, "align_abc.tsv"), out); w(os.path.join(HERE, "passC.tsv"), pc)
print(confusion([os.path.join(HERE, "align_abc.tsv")], os.path.join(HERE, "confusion.tsv")))
from collections import Counter
print(Counter(r["status"] for r in out))
TG = {"th", "z", "S", "4"}
print("C label in TG:", Counter(r["merged"] for r in out if r["merged"] in TG))
print("split with TG on any side:", Counter(r["merged"] for r in out if r["status"].startswith("split") and TG & {r["merged"], r["idA"], r["idB"]}))
