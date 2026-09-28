#!/usr/bin/env python3
"""F61-MAP-REFINED-KNOWN (campaign step H147, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, one run.
The 14-cell map refined by H119 (HASH4 = i/x) and H146 (VBAR_B = s alone; VBAR_A g/t kept), scored on the known-answer
positions of H116 (f.61 spans) and H121 (f.108r overlay) with the plain beam and the H136 word-lattice, beside the unrefined
map. Known positions are placed with the unrefined map's pairs (as H126/H136) so both maps are scored on the same letters.
GATE H147: refined lattice >= 113/125 and neither text worse than unrefined.   -> scripts/f61refined_known_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_lattice as BL
from f61crib import load_spans
M14 = BL.M14
def main():
    C = M14.J.cells(); CR = dict(C, HASH4="i/x", VBAR_B="s/s")
    L61, sp61 = M14.J.lines("known_h51"), load_spans(); L108, sp108 = M14.K.load108()
    P61, P108 = M14.known_positions(L61, sp61, C), M14.known_positions(L108, sp108, C)
    out = []; tot = {}
    for name, m in (("unrefined", C), ("refined", CR)):
        a = BL.score(L61, m, P61); b = BL.score(L108, m, P108); tot[name] = (a, b)
        out.append(f"{name}: f.61 spans lattice {a[0]}/{a[2]} plain {a[1]}/{a[2]}; f.108r overlay lattice {b[0]}/{b[2]} plain {b[1]}/{b[2]}; pooled lattice {a[0] + b[0]}/{a[2] + b[2]} plain {a[1] + b[1]}/{a[2] + b[2]}")
    (ua, ub), (ra, rb) = tot["unrefined"], tot["refined"]
    ok = ra[0] + rb[0] >= 113 and ra[0] >= ua[0] and rb[0] >= ub[0]
    out.append(f"GATE H147 (refined lattice >= 113/125, no text worse): {'PASS' if ok else 'FAIL'}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61refined_known_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
