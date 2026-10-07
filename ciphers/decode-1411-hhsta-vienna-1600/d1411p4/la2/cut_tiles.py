#!/usr/bin/env python3
"""D07-D1411: cut one enlarged tile per p.4 4/5 number (PREREG-LA2.md item 1).
Reads la2/boxes.tsv (line, pos, x0, x1: x-range placed by eye on a 50-px ruler overlay of the native line crop) and
la/tiles.tsv (mask). Each tile = the line crop's full height, x0-25 .. x1+25, enlarged 4x (LANCZOS) -> la2/tiles/<line>_<pos>.png.
  python3 d1411p4/la2/cut_tiles.py [--only line_pos,...]"""
import csv, os, sys
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(H, "..", "..", "images", "d1411p4_crops")
rd = lambda f: list(csv.DictReader(open(f), delimiter="\t"))
only = set(sys.argv[sys.argv.index("--only") + 1].split(",")) if "--only" in sys.argv else None
os.makedirs(os.path.join(H, "tiles"), exist_ok=True); n = 0
for r in rd(os.path.join(H, "boxes.tsv")):
    k = f"{r['line']}_{r['pos']}"
    if only and k not in only:
        continue
    im = Image.open(os.path.join(C, r["line"] + ".jpg")).convert("RGB")
    x0, x1 = max(0, int(r["x0"]) - 25), min(im.width, int(r["x1"]) + 25)
    t = im.crop((x0, 0, x1, im.height))
    t.resize((t.width * 4, t.height * 4), Image.LANCZOS).save(os.path.join(H, "tiles", k + ".png")); n += 1
print(n, "tiles")
