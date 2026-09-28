#!/usr/bin/env python3
"""F61-FAMILY-6 (28 Sept 2026): the loop half of scripts/f61qo2.relabel (campaign step H51), for decode_period.py and
test_period_key.py --sbs. On f.61r and f.108r every sign H26's blind call put in group G2 (two loops side by side at the stem
head) becomes SBS, every pass-A DBL on f.61r becomes SBS, G1/G3 stay PHI. H27's EBR/ISH relabel (f61joint2) is NOT applied,
so the EBR handling is exactly v3's (EBR_A/EBR_B folded into EBR). Positions: scripts/f61qo2.G, (line, 1-based pos) on the
split_lines sequence, which equals scripts/passA_classes.tsv / passU2_classes.tsv position for position (checked 28 Sept).
"""
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts")))
def relabel(lines):
    from f61qo2 import G
    n = 0
    for line, seq in lines.items():
        for j, c in enumerate(seq):
            if c in ("PHI", "DBL"):
                grp = G.get((line, j + 1))
                if grp == "G2" or (c == "DBL" and not line.startswith("F108")): seq[j] = "SBS"; n += 1
                elif grp in ("G1", "G3"): seq[j] = "PHI"
    return n
