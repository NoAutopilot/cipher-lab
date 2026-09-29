#!/usr/bin/env python3
"""H211 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, written before the run. H209's design (30 bootstrap resamples of a
leaf's lines, H127 sequence gain; a candidate CONFIRMED over another at >= 29/30 wins, the other PREFERRED at <= 1/30, else OPEN), two leaves side by
side: (a) f.108v relabelled by bowl (H201 map), HASH4 d/q vs null (seed 211); (b) f.108r L04-L06 (H112's reconciled draft, J.lines
'f108r_L04_L06_h108'; its 4-family read as the passes coded it, since H202 found f.108r's codes follow the bowl), the 14 cells, HASH4 i/x vs d/q and
each vs null (seed 211). Descriptive, for the verifier.  -> scripts/f61hash4_two_leaves_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G, f61bowl_108v_seq as BS
def duel(L, m1, m2, seed):
    keys = sorted(L); rng = random.Random(seed); w = 0
    for _ in range(30):
        R = {f"r{i}": L[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); w += G.gain(R, S, m1) > G.gain(R, S, m2)
    return w
def verdict(a, b, w): return f"{a} vs {b}: {a} wins {w}/30 -> " + (f"{a} CONFIRMED" if w >= 29 else (f"{b} PREFERRED" if w <= 1 else "OPEN"))
def main():
    D = BS.draft(); ans = {(r["line"], r["column"]): r["bowl"] for r in BS.rd(f"{HERE}/../family/h199_bowl_positions.tsv")}
    Lv = BS.relabel(D, ans); Mv = dict(G.J.cells(), **{"4BOWL": "c/p", "4NOB": "a/n"}); C = G.J.cells(); Lr = G.J.lines("f108r_L04_L06_h108")
    out = [f"f.108v (bowl relabel) HASH4 {sum(s.count('HASH4') for s in Lv.values())}; f.108r L04-L06 HASH4 {sum(s.count('HASH4') for s in Lr.values())}",
           "(a) f.108v " + verdict("d/q", "null", duel(Lv, dict(Mv, HASH4="d/q"), Mv, 211))]
    for a, b in (("i/x", "d/q"), ("i/x", "null"), ("d/q", "null")):
        ma = dict(C, HASH4=a); mb = C if b == "null" else dict(C, HASH4=b)
        out.append("(b) f.108r " + verdict(a, b, duel(Lr, ma, mb, 211)))
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61hash4_two_leaves_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
