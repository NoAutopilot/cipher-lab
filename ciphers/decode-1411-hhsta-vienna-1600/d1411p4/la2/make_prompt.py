#!/usr/bin/env python3
"""D07-D1411: value-blind prompt for a batch of la2 tiles (PREREG-LA2.md item 2): only the mask pattern is shown.
  python3 d1411p4/la2/make_prompt.py OUT.md line_pos[,line_pos...]"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
M = {f"{r['line']}_{r['pos']}": r["mask"] for r in csv.DictReader(open(os.path.join(H, "..", "la", "tiles.tsv")), delimiter="\t")}
ks = sys.argv[2].split(",")
P = ["# Digit-shape re-read (one enlarged tile per number)", "",
     "Each image is one handwritten cipher number from a German letter of about 1628, cut out of its line and enlarged 4x;",
     "the number is in the horizontal centre of the tile (neighbouring numbers or words may show at the edges; ignore them,",
     "and ignore the small letters written above the number). In this hand two digits look alike: one is written as a",
     "CROSS (like '+', two crossing strokes) and one as an R-FORM (like a small cursive 'r': an upright with a flag or hook to",
     "the upper right). For each tile you are given the digit pattern of the centre number, with '#' for each digit to judge",
     "and the other digits shown. For each '#', say whether that digit is a CROSS (X), an R-FORM (R), or some OTHER digit (O);",
     "if you truly cannot tell, write ?. Open every image with the Read tool. Answer one row per tile, nothing else:",
     "tile<TAB>shapes (one letter per '#', left to right, e.g. XR)<TAB>H|M (H = clear, M = probable)", ""]
for k in ks:
    P.append(f"- {k} : pattern {M[k]} ({len(M[k])} digit{'s' if len(M[k]) > 1 else ''}) : "
             f"/home/user/cipher-lab/ciphers/decode-1411-hhsta-vienna-1600/d1411p4/la2/tiles/{k}.png")
open(sys.argv[1], "w").write("\n".join(P) + "\n"); print(len(ks), "tiles")
