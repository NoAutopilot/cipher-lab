#!/usr/bin/env python3
"""SIG-AVS: score the blind pile sorts (piles.json) against the label maps under prereg_sigavs.md. --check: exit 1 if result.tsv stale."""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(f"{D}/piles.json"))
def lab(read, keyf):
    m = json.load(open(f"{D}/{keyf}")); return [[m[i].split("_")[0] for i in p] for p in P[read]]
def pile_of(piles, x): return next(i for i, p in enumerate(piles) if x in p)
out = ["test\tread\tgate\tresult\tdetail"]
for r, kf in ((1, "key_qf_read1.json"), (2, "key_qf_read2.json")):
    pl = lab(f"qf_read{r}", kf); pf = {pile_of(pl, x) for x in ("P1", "P2", "FP1", "FP2")}
    k = len(pf) == 1 and not any(pile_of(pl, x) in pf for x in ("D1", "D2", "FD", "G", "N"))
    c = pile_of(pl, "FQ") not in pf
    t = pile_of(pl, "T") in pf
    out += [f"A\t{r}\tK\t{'PASS' if k else 'FAIL'}\t{pl}", f"A\t{r}\tC\t{'PASS' if c else 'FAIL'}\tFQ in Pf pile: {not c}",
            f"A\t{r}\tT_with_Pf\t{t}\t"]
for r, kf in ((1, "key_read74_1.json"), (2, "key_read74_2.json")):
    pl = lab(f"t74_read{r}", kf)
    pt, p7 = {pile_of(pl, "T1"), pile_of(pl, "T2")}, {pile_of(pl, "S1"), pile_of(pl, "S2")}
    k = len(pt) == 1 and len(p7) == 1 and pt != p7 and pile_of(pl, "J") not in pt | p7
    x = "7" if pile_of(pl, "X") in p7 else "T" if pile_of(pl, "X") in pt else "other"
    out += [f"B\t{r}\tK74\t{'PASS' if k else 'FAIL'}\t{pl}", f"B\t{r}\tX_with\t{x}\t"]
txt = "\n".join(out) + "\n"
if "--check" in sys.argv:
    sys.exit(0 if open(f"{D}/result.tsv").read() == txt else 1)
open(f"{D}/result.tsv", "w").write(txt); print(txt)
