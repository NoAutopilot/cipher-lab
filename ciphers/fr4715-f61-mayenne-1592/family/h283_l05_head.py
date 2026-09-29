#!/usr/bin/env python3
"""H283 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only. L05 opens at the line edge with two keyed signs Tomokiyo leaves as dashes
(L05 1 LOOPSTEM1, pooled q/s; L05 2 CH, pooled e/m; H281) before 'trop avancees'. The clear tail of L04, read by the runner on images/f61sheetB_L04.jpg
(grade M, one look, disclosed in NOTES H283; no pass on disk lists L04's words): '... croys aussi que les'. So the text runs 'que les [LOOPSTEM1] [CH]
trop avancees'. Question for the corpus: what stands between 'les' and 'trop' in period French -- the count of 'les W1 W2 trop' and 'les W1 trop'
patterns in tools/data/fr16 (normalised as H268), with the fillers listed, and whether any two-letter filler (the pooled cells give se, sm, qe, qm)
ever occurs. Descriptive: if the fillers are nouns and verbs, the two signs on f.61 are not letters at this place (a word code or a null run
is what the verifier would weigh); no value is proposed.  python3 h283_l05_head.py [--check]"""
import gzip, os, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.abspath(f"{HERE}/../../../tools/data/fr16")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()
toks = []
for f in sorted(os.listdir(D)):
    if f.endswith(".gz"): toks += re.findall(r"[a-z]+", norm(gzip.open(f"{D}/{f}", "rt", encoding="utf-8", errors="ignore").read()).replace("'", " "))
two = Counter(); one = Counter(); trop_prev = Counter()
for i in range(len(toks) - 3):
    if toks[i] == "les" and toks[i + 3] == "trop": two[toks[i + 1] + " " + toks[i + 2]] += 1
    if toks[i] == "les" and toks[i + 2] == "trop": one[toks[i + 1]] += 1
    if toks[i + 1] == "trop": trop_prev[toks[i]] += 1
fill2 = {"se", "sm", "qe", "qm"}
rows = [f"'les W1 W2 trop': {sum(two.values())} cases: " + ", ".join(f"{k} {v}" for k, v in two.most_common(20)),
        f"'les W1 trop': {sum(one.values())} cases: " + ", ".join(f"{k} {v}" for k, v in one.most_common(12)),
        "word before 'trop' overall: " + ", ".join(f"{k} {v}" for k, v in trop_prev.most_common(12)),
        f"two-letter fillers from the pooled cells (se sm qe qm) as W1 W2 or W1: {sum(v for k, v in two.items() if k.replace(' ', '') in fill2) + sum(v for k, v in one.items() if k in fill2)}"]
out = "\n".join(rows) + "\n"; p = f"{HERE}/h283_l05_head_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
