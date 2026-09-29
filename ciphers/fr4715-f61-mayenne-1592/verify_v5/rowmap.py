#!/usr/bin/env python3
"""VERIFY-F61-V5 (29 Sept 2026): which clear line of fol. 177r-v the runner's DP puts opposite each f.176r cipher row
(build_f176_key.py's own consensus, clear text and alignment, L01-L47), so the verifier's blind clear read covers its sample rows."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
sys.path.insert(0, F); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
import build_f176_key as b, h170_gate as g
from f61crib import align
from collections import Counter
A, B = b.pass_rows("A"), b.pass_rows("B"); rows = [f"L{k:02d}" for k in range(1, 48)]
seq, rowof = [], []
for l in rows:
    c = b.consensus(A[l], B[l]); seq += c; rowof += [l] * len(c)
# clear text with a line tag per letter
import glob
lines = {}
for f in sorted(glob.glob(f"{b.P}/f177r_clearA_*.tsv")):
    for r in g.rd(f): lines.setdefault(r["line"], r["text"])
for f in sorted(glob.glob(f"{b.P}/f177v_clearA_*.tsv")):
    for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
order = sorted([l for l in lines if l.startswith("L")], key=lambda l: int(l[1:])) + sorted([l for l in lines if l.startswith("V")], key=lambda l: int(l[1:]))
text, lineof = "", []
for l in order:
    x = lines[l]
    if l == "L01": x = x.split("/", 1)[1] if "/" in x else x
    fx = g.fold(x); text += fx; lineof += [l] * len(fx)
N = min(len(text), int(0.8 * len(seq))); key = g.load_key()
_, pairs = align(text[:N], seq, key)
m = {}
for i, j in pairs: m.setdefault(rowof[j], Counter())[lineof[i]] += 1
for l in rows:
    c = m.get(l, Counter()); print(l, len([r for r in rowof if r == l]), " ".join(f"{k}:{v}" for k, v in sorted(c.items(), key=lambda t: order.index(t[0]))))
