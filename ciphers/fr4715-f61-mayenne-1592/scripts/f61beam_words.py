#!/usr/bin/env python3
"""F61-BEAM-WORDS (campaign step H134, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H131: the beam
fails where nulls cut a span into short runs. Variant fixed before any run: the same beam (fr16 4-gram, width 400, states
recombined on the last three letters) keeps all final states; each final string is rescored as (sum of 4-gram log10) +
0.5 x (letters covered by NgramModel.cover's greedy word segmentation); the best rescored string is the resolution. No other
weight is tried. Scored on the 125 known positions of H126 (f.61 spans + f.108r overlay; 14-cell map), against the plain
beam's 107/125. GATE H134: >= 115/125.   -> scripts/f61beam_words_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_margin14 as M14
from f61crib import load_spans
H = M14.BM.H; lp, jp, NM = H.lp, H.jp, H.M
def best_words(sets):
    beam = [("", 0.0)]
    for st in sets:
        nb = {}
        for s, v in beam:
            for ch in st:
                t = s + ch; w = v + (lp(t[-4:]) if len(t) >= 4 else 0.0)
                if t[-3:] not in nb or nb[t[-3:]][1] < w: nb[t[-3:]] = (t, w)
        beam = sorted(nb.values(), key=lambda x: -x[1])[:400]
    return max(beam, key=lambda x: x[1] + 0.5 * NM.cover(x[0]) * len(x[0]))[0]
def score(L, C, P):
    r = n = rp = 0
    for line, seq in L.items():
        idx = [k for k, c in enumerate(seq) if c in C]; sets = [tuple(jp.fold(x) for x in C[seq[k]].split("/")) for k in idx]
        s = best_words(sets); s0 = M14.BM.best(sets)[0]
        for i, k in enumerate(idx):
            if (line, k) in P and P[(line, k)][1] in sets[i]:
                n += 1; r += s[i] == P[(line, k)][1]; rp += s0[i] == P[(line, k)][1]
    return r, rp, n
def main():
    C = M14.J.cells(); L61, sp61 = M14.J.lines("known_h51"), load_spans(); L108, sp108 = M14.K.load108()
    a = score(L61, C, M14.known_positions(L61, sp61, C)); b = score(L108, C, M14.known_positions(L108, sp108, C))
    r, rp, n = a[0] + b[0], a[1] + b[1], a[2] + b[2]
    out = [f"f.61 spans: word beam {a[0]}/{a[2]}, plain beam {a[1]}/{a[2]}", f"f.108r overlay: word beam {b[0]}/{b[2]}, plain beam {b[1]}/{b[2]}",
           f"pooled: word beam {r}/{n}, plain beam {rp}/{n}; GATE H134 (>= 115/125): {'PASS' if r >= 115 else 'FAIL'}"]
    txt = "\n".join(out) + "\n"; rpth = f"{HERE}/f61beam_words_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rpth) and open(rpth).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rpth, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
