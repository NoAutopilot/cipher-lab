#!/usr/bin/env python3
"""FV-N1C-a step 0 (LANE LEDGER-12; Wave-3 Step-0 ruling of the ledger10 jobs file), disk only.
Runs ms18/step0_ordered.py's own functions (source executed up to its EXTRA= line, so its sweep and tsv are not re-run)
on E382 E388 E390 E391 (reading.md) and N2-IE IF II IJ (reading-no2.md); prints (a), (b), b2, hit, (c)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "step0_ordered.py")).read()
g = {"__file__": os.path.join(HERE, "step0_ordered.py")}
exec(src[:src.index("EXTRA = {")], g)
print("entry\tpointer\twindow\ta_ordered\tb_p95\tb2_p95\thit\tc_count\tc_key_meanings\tc_plain_absent")
for e in ("E382", "E388", "E390", "E391", "N2-IE", "N2-IF", "N2-II", "N2-IJ"):
    p, line = g["ents"][e]
    if p not in g["pagefile"]: print(f"{e}\t{p}\tno page JSON on disk (not fetched)"); continue
    allw, codew = g["body"](line)
    r = g["measure"](e, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, e)))
    print(f"{e}\t{p}\t{r['win']}\t{r['a']:.3f} ({r['lcs']}/{r['n']})\t{r['b']:.3f}\t{r['b2']:.3f}\t{'HIT' if r['hit'] else '-'}\t{r['c']}\t{' '.join(r['ck'])}\t{' '.join(r['cp'])}")
# E391's two Wallace messages sit in the reading's {tail}, which body() drops: measure them apart (same functions, window = blocks 1 and 2).
import re
tail = re.search(r"\{tail: (.*?)\}", g["ents"]["E391"][1]).group(1)
w1, w2 = tail.split("end WB Gilmore")
bl = g["blocks"]([9772])
for tag, txt, k in (("E391-W1 (Wallace 12 m, printed p.32)", w1.split("keep hand in", 1)[1], 1), ("E391-W2 (Wallace, Balto 4th)", w2, 2)):
    allw, codew = g["body"](txt.replace("{", "").replace("}", ""))
    r = g["measure"](tag, allw, codew, [(str(k), bl[k])], sum(map(ord, tag)))
    print(f"{tag}\t9772\t{r['win']}\t{r['a']:.3f} ({r['lcs']}/{r['n']})\t{r['b']:.3f}\t-\t{'HIT' if r['hit'] else '-'}\t{r['c']}\t{' '.join(r['ck'])}\t{' '.join(r['cp'])}")
