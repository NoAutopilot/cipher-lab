#!/usr/bin/env python3
"""FV-N1C-b step 0 (LANE LEDGER-12, 10 Oct 2026): the Wave 3 Step-0 ruling via step0_ordered.py's own functions (words, lcs, body,
blocks, windows, measure; its definitions are executed up to the sweep, so step0_ordered.tsv is not rewritten). Disk only.
Entries: N2-JA JB JC JD JE JF JJ, N2-KD KE. Prints (a) ordered overlap, (b) within-entry shuffle p95, b2 selection-matched p95, hit, (c)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "step0_ordered.py")).read()
g = {"__file__": os.path.join(HERE, "step0_ordered.py")}
exec(src[:src.index("EXTRA = ")], g)
print("entry\tpage\twindow\ta_ordered\tb_p95\tb2_p95\thit\tc_count\tc_key_meanings\tc_plain_absent")
for e in ("N2-JA", "N2-JB", "N2-JC", "N2-JD", "N2-JE", "N2-JF", "N2-JJ", "N2-KD", "N2-KE"):
    p, line = g["ents"][e]
    if p not in g["pagefile"]: print(e, p, "no page JSON on disk"); continue
    allw, codew = g["body"](line)
    r = g["measure"](e, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, e)))
    print(f"{e}\t{p}\t{r['win']}\t{r['a']:.3f} ({r['lcs']}/{r['n']})\t{r['b']:.3f}\t{r['b2']:.3f}\t{'HIT' if r['hit'] else '-'}\t{r['c']}\t{' '.join(r['ck'])}\t{' '.join(r['cp'])}")
