#!/usr/bin/env python3
"""F61-ZHOOK-POOL (campaign step H161, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H157's ZHOOK
test on the family pool (f.97r, f.101r, f.188r, f.124r drafts; map = 14 cells + KEY.md equivalences LOOPS h/u, H24 i/x,
ZBAR f/s): ZHOOK i/x vs a/e, a/u, e/u and null by sequence gain, 30 bootstrap resamples of the pool's lines (seed 161).
Pre-registered as H157: i/x CONFIRMED against a candidate at >= 29/30, candidate PREFERRED at <= 1/30, else OPEN.
  -> scripts/f61zhook_pool_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61seqgain_family as F
G = F.G
def main():
    C = dict(G.J.cells(), LOOPS="h/u", H24="i/x", ZBAR="f/s")
    pool = {f"{lf}_{k}": v for lf in ("f97r", "f101r", "f188r", "f124r") for k, v in F.draft(lf).items()}
    n = sum(s.count("ZHOOK") for s in pool.values()); keys = sorted(pool)
    cand = {"a/e": dict(C, ZHOOK="a/e"), "a/u": dict(C, ZHOOK="a/u"), "e/u": dict(C, ZHOOK="e/u"), "null": {k: v for k, v in C.items() if k != "ZHOOK"}}
    rng = random.Random(161); w = {k: 0 for k in cand}
    for _ in range(30):
        R = {f"r{i}": pool[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C)
        for k, m in cand.items(): w[k] += g0 > G.gain(R, S, m)
    out = [f"family pool ZHOOK signs: {n}"] + [f"i/x vs {k}: i/x wins {v}/30 -> " + ("i/x CONFIRMED" if v >= 29 else (f"{k} PREFERRED" if v <= 1 else "OPEN")) for k, v in w.items()]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61zhook_pool_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
