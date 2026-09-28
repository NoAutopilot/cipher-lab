#!/usr/bin/env python3
"""F61-FAMILY-EDGE-BOOT (campaign step H158, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H129's
"in f.61's cells" per family leaf, bootstrapped (scaled for run time, fixed here before the run): per leaf 20 resamples of its
lines (seed 158), each with its own 20 shuffles, the fitted 14-cell map's sequence gain ranked among 20 permuted maps (seed
1580+i). Pre-registered: a leaf is ROBUSTLY in f.61's cells at rank 1 of 21 in >= 18 of 20 resamples, OUT at <= 10 of 20,
else EDGE.   -> scripts/f61family_boot_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
def main():
    C = G.J.cells(); labs = sorted(C); out = []
    for leaf in F.LEAVES:
        L = F.draft(leaf); keys = sorted(L); rng = random.Random(158); n1 = 0
        for i in range(20):
            R = {f"r{k}": L[rng.choice(keys)] for k in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C); pr = random.Random(1580 + i)
            best = True
            for _ in range(20):
                v = [C[l] for l in labs]; pr.shuffle(v)
                if G.gain(R, S, dict(zip(labs, v))) >= g0: best = False; break
            n1 += best
        out.append(f"{leaf}: rank 1 of 21 in {n1}/20 -> " + ("ROBUST" if n1 >= 18 else ("OUT" if n1 <= 10 else "EDGE"))); print(out[-1], flush=True)
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61family_boot_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt)
if __name__ == "__main__": main()
