#!/usr/bin/env python3
"""F61-108V-BOOT (campaign step H152, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H127's f.108v
result (fitted map's sequence gain rank 1 of 201) bootstrapped: 30 resamples of f.108v's seven lines with replacement (seed
152), each with its own 20 shuffles; in each, the fitted 14-cell map's gain ranked among 50 permuted maps (seed 1520+i).
Pre-registered: stands if the fitted map ranks first in >= 27 of 30.   -> scripts/f61seqgain_108v_boot_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
TAG = "f108r_L04_L06_h108" if "--f108r" in ARGS else "f108v"; IX = "--hash4-ix" in ARGS   # H154: f.108r L04-L06, HASH4 dropped or = i/x
def main():
    C = G.J.cells()
    if IX: C = dict(C, HASH4="i/x")
    L = G.J.lines(TAG); keys = sorted(L); labs = sorted(C); rng = random.Random(152); ranks = []
    for i in range(30):
        R = {f"r{k}": L[rng.choice(keys)] for k in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C); pr = random.Random(1520 + i); null = []
        for _ in range(50):
            v = [C[l] for l in labs]; pr.shuffle(v); null.append(G.gain(R, S, dict(zip(labs, v))))
        ranks.append(1 + sum(1 for x in null if x >= g0))
    n1 = sum(r == 1 for r in ranks)
    txt = f"{'f.108v' if TAG == 'f108v' else 'f.108r L04-L06'}{' HASH4=i/x' if IX else ''} bootstrap ranks (of 51): {ranks}\nrank 1 in {n1}/30 -> H152 {'STANDS' if n1 >= 27 else 'DOES NOT STAND'}\n"
    rp = f"{HERE}/f61seqgain_{'108r' if TAG != 'f108v' else '108v'}_boot{'_ix' if IX else ''}_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
