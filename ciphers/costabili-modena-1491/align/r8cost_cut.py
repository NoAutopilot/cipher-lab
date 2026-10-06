#!/usr/bin/env python3
"""R8-COST (6 Oct 2026): cut R1166 P4 cipher spans into ~450 px segment crops (2-3 groups each, gloss above kept),
from page geometry only. Run in a folder holding dec/IMG_R1166_I5856_P4.png; writes crops/ and boxes.tsv."""
import os
from PIL import Image
LINES = [  # (line, y0, y1, [(x0, x1) spans of cipher; clear text and strike-throughs left out])
    ("L1", 1595, 1700, [(540, 2250)]),
    ("L2", 1695, 1800, [(540, 2250)]),
    ("L3", 1790, 1900, [(540, 2250)]),
    ("L4", 1905, 2005, [(540, 2150)]),
    ("L5", 2000, 2080, [(540, 1470)]),
    ("L6", 2055, 2180, [(540, 1180), (1480, 2160)]),
    ("L7", 2150, 2280, [(520, 1420)]),
]
W, STEP = 460, 400
im = Image.open("dec/IMG_R1166_I5856_P4.png").convert("L")
os.makedirs("crops", exist_ok=True)
rows = ["crop\tline\tx0\ty0\tx1\ty1"]
for ln, y0, y1, spans in LINES:
    k = 0
    for a, b in spans:
        x = a
        while x < b - 60:
            x1 = min(x + W, b)
            k += 1
            name = f"p4_{ln}_s{k:02d}"
            im.crop((x, y0, x1, y1)).save(f"crops/{name}.png")
            rows.append(f"{name}\t{ln}\t{x}\t{y0}\t{x1}\t{y1}")
            x += STEP
open("boxes.tsv", "w").write("\n".join(rows) + "\n")
print(len(rows) - 1, "crops")
