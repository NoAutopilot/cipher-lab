#!/usr/bin/env python3
"""H290 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only: the noun + verb pairs that fill 'les W1 W2 trop' (and 'que les W1 W2 trop')
in tools/data/fr16 and fr18 (fr18 is era-mismatched: existence of the construction only), normalised as H268; also 'les W1 W2 W3 trop' for three-word
fillers, since the f.61 run may hold a null beside the two codes (Tomokiyo's third dash before 'trop', H281). Candidate values for a later family test
at LOOPSTEM1/CH; descriptive, no value.  python3 h290_wordcode_candidates.py [--check]"""
import gzip, os, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); DD = os.path.abspath(f"{HERE}/../../../tools/data")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
rows = []
for d in ("fr16", "fr18"):
    toks = []
    for f in sorted(os.listdir(f"{DD}/{d}")):
        if f.endswith(".gz"): toks += re.findall(r"[a-z]+", norm(gzip.open(f"{DD}/{d}/{f}", "rt", encoding="utf-8", errors="ignore").read()).replace("'", " "))
    two, three, q2 = Counter(), Counter(), Counter()
    for i in range(len(toks) - 4):
        if toks[i] == "les":
            if toks[i + 3] == "trop": two[toks[i + 1] + " " + toks[i + 2]] += 1; q2[toks[i + 1] + " " + toks[i + 2]] += (toks[i - 1] == "que")
            if toks[i + 4] == "trop": three[" ".join(toks[i + 1:i + 4])] += 1
    rows.append(f"{d}: 'les W1 W2 trop' {sum(two.values())}: " + ", ".join(f"{k} {v}" for k, v in two.most_common(15)) + f"; of which after 'que' {sum(q2.values())}")
    rows.append(f"{d}: 'les W1 W2 W3 trop' {sum(three.values())}: " + ", ".join(f"{k} {v}" for k, v in three.most_common(10)))
out = "\n".join(rows) + "\n"; p = f"{HERE}/h290_wordcode_candidates_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
