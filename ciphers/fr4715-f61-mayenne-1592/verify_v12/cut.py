#!/usr/bin/env python3
"""VERIFY-F61-V12: cut my own tiles from the f.61 native region (images/src_...f137...jpg) at the centres in v12_positions.tsv.
Windows: W1 tight (+-75 x, -80..+95 y), W2 wide (+-115, -110..+130), W3 shifted (centre +30 x, -20 y; +-80, -85..+95). All tiles resized to
height 190 px, greyscale-free (colour kept). Output verify_v12/tiles/<line>_<pos>_<W>.png (names are for me; sheets use random ids)."""
import csv, os
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = f"{HERE}/../images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg"
WIN = {"W1": (0, 0, 75, 80, 95), "W2": (0, 0, 115, 110, 130), "W3": (30, -20, 80, 85, 95)}
def rows(): return [r for r in csv.DictReader((l for l in open(f"{HERE}/v12_positions.tsv") if not l.startswith("#")), delimiter="\t")]
def tile(im, r, w):
    dx, dy, hw, up, dn = WIN[w]; x, y = int(r["x"]) + dx, int(r["y"]) + dy
    t = im.crop((max(0, x - hw), max(0, y - up), min(im.width, x + hw), min(im.height, y + dn)))
    return t.resize((int(t.width * 190 / t.height), 190))
if __name__ == "__main__":
    im = Image.open(SRC).convert("RGB"); os.makedirs(f"{HERE}/tiles", exist_ok=True)
    for r in rows():
        for w in WIN: tile(im, r, w).save(f"{HERE}/tiles/{r['line']}_{r['pos']}_{w}.png")
    print("tiles", len(os.listdir(f"{HERE}/tiles")))
