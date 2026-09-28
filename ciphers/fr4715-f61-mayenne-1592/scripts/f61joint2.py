#!/usr/bin/env python3
"""F61-JOINT2 (campaign step H27, 28 Sept 2026): scripts/f61joint.py with the bracket class split by H22's blind groups.

Pre-registered. Relabels, before the fit: on f.108 (reconciled pass A/B draft), the EBR signs at L02 pos 1, 5, 6, 14, 34,
39 and L03 pos 7, 31 -> EBR_A (the hairline-diagonal E, H22 group A); every other EBR on both leaves -> EBR_B (the
squared C, group B); f.108's OTHER signs at L03 pos 3 and 27 (the capital-I shape, group C) -> ISH. Same folds,
permutations (seed 1) and gate as H20, the gated cells now ten: PHI, C43, 4TRI, INF, VBAR_A, VBAR_B, DBL, EBR_A, EBR_B,
ZHOOK. Gate (H27): both leaf folds above every permutation AND the ten cells identical in every fold (a class absent
from a fold's training set counts as unstable, as in H20).

  python3 scripts/f61joint2.py [--check]   -> scripts/f61joint_h27_result.txt, f61joint_h27_map.tsv
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f61joint
A_POS = {"F108_L02": {1, 5, 6, 14, 34, 39}, "F108_L03": {7, 31}}
I_POS = {"F108_L03": {3, 27}}
def relabel(lines):
    for line, seq in lines.items():
        for j, c in enumerate(seq):
            pos = j + 1
            if c == "EBR": seq[j] = "EBR_A" if pos in A_POS.get(line, ()) else "EBR_B"
            elif c == "OTHER" and pos in I_POS.get(line, ()): seq[j] = "ISH"
if __name__ == "__main__":
    f61joint.main(relabel=relabel, tag="_h27", nine=["PHI", "C43", "4TRI", "INF", "VBAR_A", "VBAR_B", "DBL", "EBR_A", "EBR_B", "ZHOOK"])
