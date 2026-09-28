#!/usr/bin/env python3
"""F61-ZHOOK-108V (campaign step H157, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. ZHOOK = i/x
(Tomokiyo's markup and his f.108r reprint, H44) against the held f.108v alignment's a/e/u, by the H127 sequence gain on f.108v
(H59 draft, 14-cell map with ZHOOK varied), 30 bootstrap resamples of its lines (seed 157, own shuffles each). Candidates:
i/x (map), a/e, a/u, e/u, and null (ZHOOK dropped). Pre-registered: i/x CONFIRMED against a candidate when it has the higher
gain in >= 29/30 resamples; the candidate PREFERRED at <= 1/30; else OPEN.  -> scripts/f61zhook_108v_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def main():
    C = G.J.cells(); L = G.J.lines("f108v"); keys = sorted(L); n = sum(s.count("ZHOOK") for s in L.values())
    cand = {"a/e": dict(C, ZHOOK="a/e"), "a/u": dict(C, ZHOOK="a/u"), "e/u": dict(C, ZHOOK="e/u"), "null": {k: v for k, v in C.items() if k != "ZHOOK"}}
    rng = random.Random(157); w = {k: 0 for k in cand}
    for _ in range(30):
        R = {f"r{i}": L[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C)
        for k, m in cand.items(): w[k] += g0 > G.gain(R, S, m)
    out = [f"f.108v ZHOOK signs: {n}; map value {C['ZHOOK']}"] + [f"i/x vs {k}: i/x wins {v}/30 -> " + ("i/x CONFIRMED" if v >= 29 else (f"{k} PREFERRED" if v <= 1 else "OPEN")) for k, v in w.items()]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61zhook_108v_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
