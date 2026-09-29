#!/usr/bin/env python3
"""H209/H210 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026), script-only, written before the run. f.108v's draft relabelled by H199's bowl
answers (f61bowl_108v_seq.relabel: 4BOWL c/p, 4NOB a/n), the map = the 14 cells + 4BOWL c/p + 4NOB a/n (HASH4 is a skeleton null in the 14 cells).
 H209: HASH4 (14 signs on f.108v) = i/x against d/q and against null, H198's design: 30 bootstrap resamples of f.108v's lines (seed 209), sequence
   gain (H127); i/x CONFIRMED over a candidate at >= 29/30 wins, the candidate PREFERRED at <= 1/30, else OPEN. (H118/H119 found i/x best on
   f.108r's sequence gain; H195's shape test failed its control; VERIFY-F61-V5 held HASH4 d/i/q.)
 H210: the H127 permuted-map rank of the relabelled map on the whole of f.108v (200 permutations of the cell values, seed 127, the same 20
   within-line shuffles), with and without HASH4 = i/x, beside H127's own f.108v rows (pass codes: gain 0.152 / 0.165, rank 1 of 201). Descriptive.
  -> scripts/f61hash4_108v_bowl_result.txt [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G, f61bowl_108v_seq as BS
def main():
    D = BS.draft(); ans = {(r["line"], r["column"]): r["bowl"] for r in BS.rd(f"{HERE}/../family/h199_bowl_positions.tsv")}
    L = BS.relabel(D, ans); M = dict(G.J.cells(), **{"4BOWL": "c/p", "4NOB": "a/n"}); MI = dict(M, HASH4="i/x")
    n = sum(s.count("HASH4") for s in L.values()); out = [f"f.108v (bowl relabel) HASH4 signs: {n}"]
    cand = {"d/q": dict(M, HASH4="d/q"), "null": M}; keys = sorted(L); rng = random.Random(209); w = {k: 0 for k in cand}
    for _ in range(30):
        R = {f"r{i}": L[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, MI)
        for k, m in cand.items(): w[k] += g0 > G.gain(R, S, m)
    out += [f"H209 i/x vs {k}: i/x wins {v}/30 -> " + ("i/x CONFIRMED" if v >= 29 else (f"{k} PREFERRED" if v <= 1 else "OPEN")) for k, v in w.items()]
    for name, m in (("relabelled map", M), ("relabelled map + HASH4 i/x", MI)):
        g, r, b, med = G.rank(L, m)
        out.append(f"H210 {name}: gain {g:.3f}, rank {r} of 201 (best permuted {b:.3f}, median {med:.3f})")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61hash4_108v_bowl_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
