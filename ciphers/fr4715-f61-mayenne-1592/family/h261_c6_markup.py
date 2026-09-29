#!/usr/bin/env python3
"""H261 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026): the pooled key carries C6 = e from three glossed tokens on other leaves (f.101r L42, L45;
f.188r/f.184r L04; key_period_v6.tsv), but Tomokiyo's markup on f.61 pairs every in-span C6 with a dash (H259). Does the C6 = e cell gain or lose any
known-span letter on f.61? Score the five spans (scripts/f61crib.align, the F61-CAL DP) under key v6's f.61 reading with C6 = e as loaded and with C6
removed (no value), and list each in-span C6 with its markup character. Also the same for every f.61 class that never pairs with a letter in the spans
(a census of the classes his markup treats as unread), for the verifier's null band. Descriptive; the HYPOTHESES.md row for the C6 conflict (rule 4,
both witnesses) is appended by the runner from this output.  python3 h261_c6_markup.py [--check]"""
import os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
from build_key_v6 import load_key_v6
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
key = load_key_v6(f61=True); lines = split_lines(load_read()); relabel(lines); spans = load_spans()
def score(k): return sum(align(m, lines[l], k)[0] for _, l, m in spans)
k_no = {c: v for c, v in key.items() if c != "C6"}
rows = [f"C6 cell as loaded (f.61 reading key): {'/'.join(key.get('C6', ()))}", f"five known spans: with C6 = e {score(key)}/55; without C6 {score(k_no)}/55"]
seen = defaultdict(Counter)
for s, l, m in spans:
    for i, j in align(m, lines[l], key)[1]: seen[lines[l][j]][m[i]] += 1
c6 = [(s, l, j + 1, m[i]) for s, l, m in spans for i, j in align(m, lines[l], key)[1] if lines[l][j] == "C6"]
rows.append("in-span C6 and Tomokiyo's character: " + "; ".join(f"{s} {l} pos {p} '{ch}'" for s, l, p, ch in c6))
nul = sorted((c, sum(n.values())) for c, n in seen.items() if set(n) == {"-"})
rows.append("classes pairing only with his dash in the spans (n): " + ", ".join(f"{c} {n}" for c, n in nul))
rows.append("classes pairing with letters: " + ", ".join(f"{c} {''.join(sorted(k for k in n if k != '-'))}" for c, n in sorted(seen.items()) if set(n) != {"-"}))
txt = "\n".join(rows) + "\n"; res = f"{HERE}/h261_c6_markup_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
