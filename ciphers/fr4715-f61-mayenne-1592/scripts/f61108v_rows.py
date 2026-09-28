#!/usr/bin/env python3
"""F61-108V-ROWS-FOR-DESK (campaign step H155, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. Per
f.108v row (H59 draft), the covered sign count and the fitted 14-cell map's sequence gain (H127 statistic) ranked among 200
permuted maps (seed 127), to order the ASKS 89 desk pack: rows where the cipher already reads toward French under f.61's cells
and carry the most covered signs are where a person's gloss tests the most letters. No letters are written to the pack.
  -> scripts/f61108v_rows_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_seqgain as G
def main():
    C = G.J.cells(); L = G.J.lines("f108v"); rows = []
    for line in sorted(L):
        g, r, b, med = G.rank({line: L[line]}, C); cov = sum(1 for c in L[line] if c in C); rows.append((r, -cov, line, g, cov))
    rows.sort()
    out = ["order\trow\tcovered_signs\tseqgain\trank_of_201"] + [f"{i}\t{line}\t{cov}\t{g:.3f}\t{r}" for i, (r, _, line, g, cov) in enumerate(rows, 1)]
    txt = "\n".join(out) + "\n"; rp = f"{HERE}/f61108v_rows_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rp) and open(rp).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rp, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
