#!/usr/bin/env python3
"""VIV-67: cut a decipherment page (widely spaced clerk hand) into horizontal strips at ink minima, each strip in two
halves sharing --share px, as N5-VIVK did for ff.105v-108v (line detection misses lines on this hand).

    python3 tx/viv67_strips.py SRC.jpg --out DIR --prefix c210_f205r --strips 8 [--share 400] [--ink 170] [--win 90]

Writes DIR/<prefix>_S01_h1.jpg, _S01_h2.jpg ... (untracked; regenerate from the native region in images/manifest.json "viv67").
"""
import argparse, os
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('src'); ap.add_argument('--out', required=True); ap.add_argument('--prefix', required=True)
ap.add_argument('--strips', type=int, default=8); ap.add_argument('--share', type=int, default=400)
ap.add_argument('--ink', type=int, default=170); ap.add_argument('--win', type=int, default=90)
a = ap.parse_args()
im = Image.open(a.src).convert('L'); W, H = im.size
arr = np.asarray(im)
prof = (arr < a.ink).sum(axis=1).astype(float)
prof = np.convolve(prof, np.ones(15) / 15, mode='same')
cuts = [0]
for k in range(1, a.strips):
    t = int(H * k / a.strips)
    lo, hi = max(0, t - a.win), min(H, t + a.win)
    cuts.append(lo + int(np.argmin(prof[lo:hi])))
cuts.append(H)
half = (W + a.share) // 2
for i in range(a.strips):
    y0, y1 = cuts[i], cuts[i + 1]
    for h, (x0, x1) in enumerate(((0, half), (W - half, W)), 1):
        im.crop((x0, y0, x1, y1)).save(os.path.join(a.out, f'{a.prefix}_S{i + 1:02d}_h{h}.jpg'), quality=88)
    print(f'S{i + 1:02d} y {y0}-{y1}')
