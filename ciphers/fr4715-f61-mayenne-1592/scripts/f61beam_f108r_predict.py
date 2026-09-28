#!/usr/bin/env python3
"""F61-108R-BEAM-PREDICT (campaign step H120, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only: the
4-gram beam's resolution (scripts/f61hash4_108r.resolve, fr16, width 400) of f.108r L04-L06 (H108 draft, DBL -> PHI) under the
14 cells + HASH4 = i/x (the H119 map), committed as a pre-registered prediction beside H107/H112 BEFORE the person's gloss
(ASKS 88). One row per draft position: its class, the pair, the beam letter ('.' where the class is outside the map).
H64 scores it letter by letter; H116 predicts about 0.78 right where the true letter is in the pair.
  -> scripts/f61beam_f108r_prediction.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61hash4_108r as H
V = "--f108v" in ARGS; LAT = "--lattice" in ARGS   # H140: the H136 word-lattice beam, files f61lattice_<leaf>_prediction.txt   # H123: f.108v (H59 draft) under the same map, file f61beam_f108v_prediction.txt
def main():
    C = dict(H.J.cells(), HASH4="i/x"); L = H.J.lines("f108v" if V else "f108r_L04_L06_h108")
    out = [("# H123 prediction (28 Sept 2026): f.108v L01-L07, H59 draft positions," if V else "# H120 prediction (28 Sept 2026): f.108r L04-L06, H108 draft positions,") + " beam letter under 14 cells + HASH4=i/x" + (" (H140 word-lattice beam)" if LAT else "") + "; '.' = class outside the map",
           "line\tposition\tclass\tpair\tbeam"]
    summ = []
    for line, seq in L.items():
        idx = [k for k, c in enumerate(seq) if c in C]
        prs = [tuple(H.jp.fold(x) for x in C[seq[k]].split("/")) for k in idx]
        if LAT:
            import f61beam_lattice as BL; s = BL.best_lattice(prs)
        else: s, _, _ = H.resolve(prs)
        m = dict(zip(idx, s))
        for k, c in enumerate(seq): out.append(f"{line}\t{k + 1}\t{c}\t{C.get(c, '')}\t{m.get(k, '.')}")
        summ.append(f"# {line}: " + "".join(m.get(k, ".") for k in range(len(seq))))
    txt = "\n".join(out + summ) + "\n"; rp = f"{HERE}/f61{'lattice' if LAT else 'beam'}_{'f108v' if V else 'f108r'}_prediction.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print("\n".join(summ))
if __name__ == "__main__": main()
