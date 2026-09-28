#!/usr/bin/env python3
"""VERIFY-F61-V4 step 5a: f.61r under key v4 in two-way form, line by line (verify_v4/f61r_v4_twoway.txt), from the
committed family/f61_decode_period_v4_frac0.1_sbs.tsv. Firm letters plain, sets in [..], unread <CLASS>. Under each span line,
Tomokiyo's markup placed on the signs by test_period_key's DP (key v4). Runs of >= 3 consecutive firm letters are listed
(the only places a word could be forced with no choice inside a set).   python3 verify_v4/twoway.py [--check]"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{H}/../family"); sys.path.insert(0, F)
chk = "--check" in sys.argv
sys.argv = ["x", "--key", f"{F}/key_period_v4.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1"]
import test_period_key as T
from sbs_relabel import relabel
from collections import defaultdict
dec = defaultdict(list)
for r in csv.DictReader(open(f"{F}/f61_decode_period_v4_frac0.1_sbs.tsv"), delimiter="\t"): dec[r["line"]].append(r)
key = T.load_key(); L = T.split_lines(T.load_read()); L.update(T.f108_lines()); relabel(L)
spans = {line: (s, m) for s, line, m in T.load_spans()}
def tok(r): return r["period_letters"] if r["grade"] in ("C", "C+") else (f"[{r['period_letters']}]" if r["grade"] == "M" else f"<{r['class']}>")
out = ["# f.61r under key_period_v4.tsv, two-way form (VERIFY-F61-V4, 28 Sept 2026). firm letter plain | [a/b] period set, no choice made | <CLASS> no period pair.",
       "# 'T:' rows: Tomokiyo's markup (published, his tentative reading, sources/cryptiana) set under the signs by test_period_key's DP; '-' his dash, '.' a sign outside his span or skipped.", ""]
runs = []
for line in sorted(dec):
    rs = dec[line]; toks = [tok(r) for r in rs]; w = [max(len(t), 3) for t in toks]
    out.append(f"{line}  " + " ".join(t.ljust(x) for t, x in zip(toks, w)))
    out.append(f"  pos " + " ".join(str(i + 1).ljust(x) for i, x in enumerate(w)))
    if line in spans:
        s, m = spans[line]; _, pairs = T.align(m, L[line], key); byj = {j: m[i] for i, j in pairs}
        out.append(f"T:{s:4}" + " ".join(byj.get(j, ".").ljust(x) for j, x in enumerate(w)) + f"   (his markup '{m}')")
        our = "".join((dec[line][j]["period_letters"] if dec[line][j]["grade"] in ("C", "C+") else "?") for j in sorted(byj))
    out.append("")
    run = []
    for r in rs + [None]:
        if r is not None and r["grade"] in ("C", "C+"): run.append(r)
        else:
            if len(run) >= 3: runs.append(f"{line}/{run[0]['pos']}-{run[-1]['pos']} " + "".join(x["period_letters"] for x in run))
            run = []
out.append("runs of >= 3 consecutive firm letters: " + ("; ".join(runs) if runs else "none"))
txt = "\n".join(out) + "\n"; p = f"{H}/f61r_v4_twoway.txt"
if chk: ok = open(p).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(txt, end="")
