#!/usr/bin/env python3
"""VERIFY-F61-V12 helper: cut a native strip of the f.61 region with an x/y grid, for placing tile boxes by eye (placement only)."""
import sys
from PIL import Image, ImageDraw
SRC = "images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg"
def strip(y0, y1, x0, x1, out, scale=0.6):
    im = Image.open(SRC).convert("RGB").crop((x0, y0, x1, y1)); d = ImageDraw.Draw(im)
    for x in range((x0 // 50 + 1) * 50, x1, 50):
        d.line([(x - x0, 0), (x - x0, 12 if x % 100 else 25)], fill=(255, 0, 0), width=2)
        if x % 100 == 0: d.text((x - x0 + 2, 12), str(x), fill=(255, 0, 0))
    for y in range((y0 // 50 + 1) * 50, y1, 50):
        d.line([(0, y - y0), (15, y - y0)], fill=(0, 0, 255), width=2); d.text((17, y - y0 - 5), str(y), fill=(0, 0, 255))
    im.resize((int(im.width * scale), int(im.height * scale))).save(out)
if __name__ == "__main__":
    a = list(map(int, sys.argv[1:5])); strip(*a, sys.argv[5], float(sys.argv[6]) if len(sys.argv) > 6 else 0.6)
