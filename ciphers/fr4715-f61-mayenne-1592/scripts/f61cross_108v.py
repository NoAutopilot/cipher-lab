#!/usr/bin/env python3
"""H197 (runner 7, 29 Sept 2026), script-only, H157's design for CROSS. CROSS leans s on both Desportes leaves (f.176r 0.36, f.176v 0.53; wrong
text 0.09 / 0.05; H192) and is a dash in Tomokiyo's reading of f.61. On f.108v (f.61's hand, H59 draft, 14-cell map + CROSS), by H127 sequence
gain, 30 bootstrap resamples of its lines (seed 197, own shuffles each): CROSS = s against CROSS = e, a, i, t, n and null (CROSS dropped).
Pre-registered: s CONFIRMED against a candidate at >= 29/30 wins, the candidate PREFERRED at <= 1/30, else OPEN. A class with too few signs on
f.108v is reported and not tested.  -> scripts/f61cross_108v_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def main():
    L = G.J.lines("f108v"); keys = sorted(L); n = sum(s.count("CROSS") for s in L.values()); C = dict(G.J.cells(), CROSS="s")
    out = [f"f.108v CROSS signs: {n}"]
    if n < 5: out.append("fewer than 5 CROSS signs: not tested")
    else:
        cand = {x: dict(C, CROSS=x) for x in ("e", "a", "i", "t", "n")}; cand["null"] = {k: v for k, v in C.items() if k != "CROSS"}
        rng = random.Random(197); w = {k: 0 for k in cand}
        for _ in range(30):
            R = {f"r{i}": L[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C)
            for k, m in cand.items(): w[k] += g0 > G.gain(R, S, m)
        out += [f"s vs {k}: s wins {v}/30 -> " + ("s CONFIRMED" if v >= 29 else (f"{k} PREFERRED" if v <= 1 else "OPEN")) for k, v in w.items()]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61cross_108v_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
