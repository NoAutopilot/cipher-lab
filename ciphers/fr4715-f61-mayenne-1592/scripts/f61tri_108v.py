#!/usr/bin/env python3
"""H198 (runner 7, 29 Sept 2026), script-only, H157's design for 4TRI. The 4-family bowl sign reads c/p on fr.3984 f.176v/f.176r (H193, period
decipherment) and at Tomokiyo's f.61 positions (H194); H188 showed his known positions cannot discriminate 4TRI c/p from c/p/t. On f.108v (f.61's
hand, H59 draft, unread text), by H127 sequence gain with the 14-cell map and 4TRI = c/p, 30 bootstrap resamples of its lines (seed 198, own
shuffles each): 4TRI = c/p against c/p/t, a/n and null (4TRI dropped). Pre-registered: c/p CONFIRMED against a candidate at >= 29/30 wins, the
candidate PREFERRED at <= 1/30, else OPEN. Fewer than 5 4TRI signs on f.108v: not tested.  -> scripts/f61tri_108v_result.txt [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def main():
    L = G.J.lines("f108v"); keys = sorted(L); n = sum(s.count("4TRI") for s in L.values()); base = G.J.cells()
    C = dict(base, **{"4TRI": "c/p"})
    out = [f"f.108v 4TRI signs: {n}; map 4TRI was {base.get('4TRI', '-')}"]
    if n < 5: out.append("fewer than 5 4TRI signs: not tested")
    else:
        cand = {"c/p/t": dict(C, **{"4TRI": "c/p/t"}), "a/n": dict(C, **{"4TRI": "a/n"}), "null": {k: v for k, v in C.items() if k != "4TRI"}}
        rng = random.Random(198); w = {k: 0 for k in cand}
        for _ in range(30):
            R = {f"r{i}": L[rng.choice(keys)] for i in range(len(keys))}; S = G.shuffles(R); g0 = G.gain(R, S, C)
            for k, m in cand.items(): w[k] += g0 > G.gain(R, S, m)
        out += [f"c/p vs {k}: c/p wins {v}/30 -> " + ("c/p CONFIRMED" if v >= 29 else (f"{k} PREFERRED" if v <= 1 else "OPEN")) for k, v in w.items()]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61tri_108v_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
