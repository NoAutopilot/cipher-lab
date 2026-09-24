#!/usr/bin/env python3
"""crop.py IMG OUT [--yfrac y0 y1 | --band N [--bands K] [--xfrac a b] [--scale S]: cut horizontal band N of K (default 12) of a page,
optionally only x fraction a..b, enlarged by S (default 2), contrast-stretched. For reading digit groups."""
import sys, argparse
from PIL import Image, ImageOps
p = argparse.ArgumentParser(); p.add_argument('img'); p.add_argument('out')
p.add_argument('--band', type=int, default=0); p.add_argument('--yfrac', type=float, nargs=2); p.add_argument('--bands', type=int, default=12)
p.add_argument('--xfrac', type=float, nargs=2, default=[0, 1]); p.add_argument('--scale', type=float, default=2)
a = p.parse_args()
im = Image.open(a.img).convert('L'); W, H = im.size; h = H / a.bands
y0 = max(0, int((a.band) * h - h * 0.15)); y1 = min(H, int((a.band + 1) * h + h * 0.15))
if a.yfrac: y0, y1 = int(a.yfrac[0] * H), int(a.yfrac[1] * H)
c = im.crop((int(a.xfrac[0] * W), y0, int(a.xfrac[1] * W), y1)); c = ImageOps.autocontrast(c, cutoff=1)
c = c.resize((int(c.width * a.scale), int(c.height * a.scale)), Image.LANCZOS); c.save(a.out); print(a.out, c.size)
