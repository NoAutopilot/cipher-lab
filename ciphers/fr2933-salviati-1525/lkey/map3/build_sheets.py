#!/usr/bin/env python3
"""SALV-MAP3 (14 Oct 2026): cut our atlas rows (glyphs/atlas.png, 72 px per code, row order = glyphs/atlas.tsv) for the codes of the
22 types under test into one sheet per atlas part (lkey/map3/sheet_part{1,2}.png). No other change to the pixels."""
import csv, os
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(D))
PARTS = {1: ["a", "e", "m", "nt", "bh", "ch", "S", "Z", "S7"], 2: ["S4", "Lx", "L", "H", "#", "eps", "dl", "]", "sq"]}
codes = [r["code"] for r in csv.DictReader(open(os.path.join(T, "glyphs/atlas.tsv"), encoding="utf-8"), delimiter="\t")]
im = Image.open(os.path.join(T, "glyphs/atlas.png")); w = im.size[0]
for p, cs in PARTS.items():
    out = Image.new(im.mode, (w, 72 * len(cs)), "white")
    for i, c in enumerate(cs):
        j = codes.index(c); out.paste(im.crop((0, 72 * j, w, 72 * (j + 1))), (0, 72 * i))
    out.save(os.path.join(D, f"sheet_part{p}.png")); print(p, out.size, cs)
