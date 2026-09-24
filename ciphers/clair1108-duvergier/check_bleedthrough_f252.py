#!/usr/bin/env python3
"""Reproduces the 24 Sept 2026 bleed-through finding on folio249_canvas252.jpg's right
page (249r): the numeral rows visible there are a mirror-flipped ghost of the genuine
cipher on folio 249v (the left page of folio250_canvas253.jpg), not independent cipher
content of 249r. Crops one ghost row from f252, flips it, and saves both crops for a
side-by-side eye check against the corresponding row of f253's left page.

Usage: python3 check_bleedthrough_f252.py [--out DIR]
Exits 0 always (this is an observational check, not a graded reading); prints the
crop paths for a human to compare by eye.
"""
import argparse
import os
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "images", "thumbs"))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    src = os.path.join(HERE, "images", "folio249_canvas252.jpg")
    im = Image.open(src)
    # Right page (249r), the row immediately below "Monseigneur" carrying a ghost of
    # 249v's "198 17 168 ... 200." / "il ma paru beaucoup 249 18 15 24 267 30 278 259" rows.
    crop = im.crop((4552 + 50, 600, 4552 + 3000, 950))
    ghost_path = os.path.join(args.out, "check_f252_ghost_row.jpg")
    crop.save(ghost_path, quality=92)

    flipped = ImageOps.mirror(crop)
    flipped_path = os.path.join(args.out, "check_f252_ghost_row_flipped.jpg")
    flipped.save(flipped_path, quality=92)

    ref_src = os.path.join(HERE, "images", "folio250_canvas253.jpg")
    ref = Image.open(ref_src)
    ref_crop = ref.crop((0, 150, 2600, 500))
    ref_path = os.path.join(args.out, "check_f253L_row_for_comparison.jpg")
    ref_crop.save(ref_path, quality=92)

    print("Wrote:")
    print(" ", ghost_path, "(raw ghost as seen on 249r, right-reading order)")
    print(" ", flipped_path, "(same region, mirrored horizontally)")
    print(" ", ref_path, "(249v direct, from f253's left page, for comparison)")
    print("Eye check (24 Sept 2026): the flipped ghost reads '198 17 168 18 119 50 301 28")
    print("277 290 238 10 301 14 200.' / 'il ma paru beaucoup 249 18 15 24 267 30 278 259',")
    print("an exact digit-for-digit match to the genuine 249v rows in the reference crop.")


if __name__ == "__main__":
    main()
