#!/usr/bin/env python3
"""FV-O9b lead (not a re-audit): the same step-0 figures (ms18/fv_o9b_step0.py) for FV-O9a's four No. 9 entries, for the orchestrator's consistency check. Disk only."""
import importlib.util, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("s0", os.path.join(HERE, "fv_o9b_step0.py"))
src = open(os.path.join(HERE, "fv_o9b_step0.py")).read().split("random.seed(19)")[0]
g = {"__file__": os.path.join(HERE, "fv_o9b_step0.py")}; exec(src, g)
random.seed(20)
print("entry\tpointer\tall_overlap\tcode_overlap\tcode_words")
for e, ps in {"O9-DC": [9673], "O9-DE": [9684], "O9-DH": [9684], "O9-DI": [9684]}.items():
    allw, codew = g["body"](e); t = g["tx"](ps)
    a = g["lcs"](allw, t) / len(allw); c = sum(1 for w in codew if w in set(t)) / max(1, len(codew))
    print(f"{e}\t{ps[0]}\t{a:.3f} ({g['lcs'](allw,t)}/{len(allw)})\t{c:.3f}\t{' '.join(codew)}")
