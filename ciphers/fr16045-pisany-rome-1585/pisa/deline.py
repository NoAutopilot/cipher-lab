#!/usr/bin/env python3
"""D4-PISA: remove the drawn band lines from images/f275vGH_lines_debug.jpg (the only on-disk image holding the whole
head gloss of f.275v, 0.646 x native; Gallica answered 500/503 on 8 Oct 2026) -> grayscale, each 1-px coloured row
(and its JPEG fringe, rows y-1..y+1, coloured pixels only) replaced by the mean of rows y-2 and y+2.
Usage: python3 pisa/deline.py OUT.png"""
import sys
import numpy as np
from PIL import Image
a = np.array(Image.open('images/f275vGH_lines_debug.jpg').convert('RGB')).astype(int)
sat = a.max(-1) - a.min(-1)
g = a.mean(-1)
out = g.copy()
lines = [y for y in range(a.shape[0]) if (sat[y] > 60).sum() > 400]
for y in lines:
    lo, hi = max(y - 2, 0), min(y + 2, a.shape[0] - 1)
    fill = (g[lo] + g[hi]) / 2
    for yy in range(max(y - 1, 0), min(y + 2, a.shape[0])):
        m = sat[yy] > 25
        out[yy][m] = fill[m]
Image.fromarray(out.clip(0, 255).astype('uint8')).save(sys.argv[1])
print('lines removed at rows', lines)
