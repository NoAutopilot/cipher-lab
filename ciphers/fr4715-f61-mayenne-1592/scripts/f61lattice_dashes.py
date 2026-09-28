#!/usr/bin/env python3
"""F61-LATTICE-DASHES (campaign step H139, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. At every
position inside Tomokiyo's five f.61 spans where his markup has a dash (f61crib.align on the known_h51 lines, 14-cell map
+ HASH4 = i/x) and the sign is covered by the map, the word-lattice beam's letter (H136: 44/49 = 0.898 on this leaf's known
letters) and the plain beam's (38/49), with their agreement. A candidate list for the verifier, grade M at best, never a
reading.  -> scripts/f61lattice_dashes.tsv [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_lattice as BL
from f61crib import load_spans, align
M14, jp = BL.M14, BL.jp
def main():
    C = dict(M14.J.cells(), HASH4="i/x"); key = {c: tuple(v.split("/")) for c, v in C.items()}; L = M14.J.lines("known_h51")
    res = {}
    for line, seq in L.items():
        idx = [k for k, c in enumerate(seq) if c in C]; sets = [tuple(jp.fold(x) for x in C[seq[k]].split("/")) for k in idx]
        res[line] = (dict(zip(idx, BL.best_lattice(sets))), dict(zip(idx, M14.BM.best(sets)[0])))
    out = ["# H139: f.61r positions under a Tomokiyo dash, covered by the 14 cells + HASH4 i/x; lattice and plain beam letters (candidates, grade M at best)",
           "span\tline\tpos\tclass\tpair\tlattice\tplain\tagree"]
    for s, line, markup in load_spans():
        for i, j in align(markup, L[line], key)[1]:
            if markup[i] == "-" and j in res[line][0]:
                a, b = res[line][0][j], res[line][1][j]
                out.append(f"{s}\t{line}\t{j + 1}\t{L[line][j]}\t{C[L[line][j]]}\t{a}\t{b}\t{'yes' if a == b else 'no'}")
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61lattice_dashes.tsv"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
