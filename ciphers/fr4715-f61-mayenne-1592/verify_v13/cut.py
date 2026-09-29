#!/usr/bin/env python3
"""VERIFY-F61-V13: cut my own tiles at the centres in v13_positions.tsv. Windows W1 tight (+-70 x, -75..+85 y), W2 wide (+-120, -115..+125),
W3 shifted (centre -25 x, +15 y; +-75, -80..+90), each scaled by the source's sign size (F61 1.0, F108R 0.6, F108V 2.0). All tiles grey,
autocontrast, height 180 px, so the source leaf is not given away by colour. Tiles go to verify_v13/tiles/ (not committed; rerun to regenerate)."""
import csv, os
from PIL import Image, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); I = f"{HERE}/../images"
SRC = {"F61": (f"{I}/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg", 1.0),
       "F108R": (f"{I}/stitch_f108r_f195_1250_450_3600_860.jpg", 0.6), "F108V": (f"{I}/person_pack_108v/f108v_L03.jpg", 2.0)}
BANDS = [(40, 322), (414, 696), (788, 1070), (1162, 1444)]  # f108v_L03.jpg segment image rows (label strips measured by row mean)
WIN = {"W1": (0, 0, 70, 75, 85), "W2": (0, 0, 120, 115, 125), "W3": (-25, 15, 75, 80, 90)}
def rows(): return list(csv.DictReader((l for l in open(f"{HERE}/v13_positions.tsv") if not l.startswith("#")), delimiter="\t"))
_im = {}
def tile(r, w):
    path, s = SRC[r["src"]]; im = _im.setdefault(path, Image.open(path).convert("L"))
    dx, dy, hw, up, dn = [v * s for v in WIN[w]]; x, y = int(r["x"]) + dx, int(r["y"]) + dy
    lo, hi = 0, im.height
    if r["src"] == "F108V": lo, hi = next(b for b in BANDS if b[0] <= int(r["y"]) <= b[1])  # the sheet's image band: no label strip in a tile
    t = im.crop((int(max(0, x - hw)), int(max(lo, y - up)), int(min(im.width, x + hw)), int(min(hi, y + dn))))
    t = ImageOps.autocontrast(t, cutoff=1); return t.resize((int(t.width * 180 / t.height), 180))
if __name__ == "__main__":
    os.makedirs(f"{HERE}/tiles", exist_ok=True)
    for r in rows():
        for w in WIN: tile(r, w).save(f"{HERE}/tiles/{r['id']}_{w}.png")
    print("tiles", len(os.listdir(f"{HERE}/tiles")))
