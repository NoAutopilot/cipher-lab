#!/usr/bin/env python3
"""R12D-GRAZB2: lay r12zb2/tiles/*.png out as numbered sorter sheets (ids only, no labels), r12zb2/sort_sheet_<k>.jpg.
python3 r12zb2/sheets.py"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent
ids = sorted(int(p.stem) for p in (H / "tiles").glob("*.png"))
PER, COLS, CW, CH = 24, 6, 170, 250
for k in range(0, len(ids), PER):
    grp = ids[k:k + PER]; rows = (len(grp) + COLS - 1) // COLS
    S = Image.new("RGB", (COLS * CW, rows * CH), "white"); d = ImageDraw.Draw(S)
    for n, i in enumerate(grp):
        t = Image.open(H / "tiles" / f"{i:03d}.png").convert("RGB")
        if t.width > CW - 10: t = t.resize((CW - 10, int(t.height * (CW - 10) / t.width)))
        x, y = (n % COLS) * CW, (n // COLS) * CH
        S.paste(t, (x + (CW - t.width) // 2, y + 26)); d.rectangle([x, y, x + CW - 1, y + CH - 1], outline=(160, 160, 160))
        d.text((x + 6, y + 6), f"#{i}", fill=(200, 0, 0))
    S.save(H / f"sort_sheet_{k // PER + 1}.jpg", quality=88)
print((len(ids) + PER - 1) // PER, "sheets")
