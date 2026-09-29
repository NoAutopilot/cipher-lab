#!/usr/bin/env python3
"""H295 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only: f.61 L05 reads 'les choses sont a [LOOPSTEM1] [CH] trop avancees' (NOTES
Correction). In tools/data/fr16 (normalised as H268): 'sont trop' bare, 'sont W trop', 'sont W1 W2 trop', 'sont a W trop' with the fillers, and the
same for 'estoient'. If 'sont trop' is ordinary, French needs nothing between them and the null reading of the edge a + two signs is unforced by
the grammar (Tomokiyo's dashes); if fillers dominate, a one- or two-word filler (an adverb) would be the alternative. Descriptive.  [--check]"""
import gzip, os, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
toks = []
for f in sorted(os.listdir(D)):
    if f.endswith(".gz"): toks += re.findall(r"[a-z]+", norm(gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read()).replace("'", " "))
rows = []
for v in ("sont", "estoient", "est"):
    bare = one = two = 0; f1 = Counter(); f2 = Counter(); a1 = Counter()
    for i in range(len(toks) - 3):
        if toks[i] != v: continue
        if toks[i + 1] == "trop": bare += 1
        elif toks[i + 2] == "trop": one += 1; f1[toks[i + 1]] += 1
        elif toks[i + 3] == "trop": two += 1; f2[toks[i + 1] + " " + toks[i + 2]] += 1; a1[toks[i + 2]] += (toks[i + 1] == "a")
    rows.append(f"'{v} trop' bare {bare}; '{v} W trop' {one}: " + ", ".join(f"{k} {n}" for k, n in f1.most_common(8)) + f"; '{v} W1 W2 trop' {two}: " + ", ".join(f"{k} {n}" for k, n in f2.most_common(6)) + f"; of which '{v} a W trop' {sum(a1.values())}")
out = "\n".join(rows) + "\n"; p = f"{HERE}/h295_sont_trop_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
