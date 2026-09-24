#!/usr/bin/env python3
"""Assign every glyph in Tomokiyo's table (sources/cryptiana/web/francisGramont.png) to a letter column by the pixel
x-centre of the header letters (measured: white letters on the magenta band), not by eye. Writes tomokiyo_columns.tsv.
Rows at y > 140 form a separate band of doubled-letter signs in the table (LL, SS agree with Lasry's LL, SS)."""
import numpy as np
from PIL import Image
from scipy import ndimage
t = Image.open('../../sources/cryptiana/web/francisGramont.png').convert('RGBA')
t = Image.alpha_composite(Image.new('RGBA', t.size, 'white'), t).convert('RGB'); a = np.array(t).astype(int)
H = dict(zip('a b c d e f g h i l m n o p q r s t u x y z'.split(),
             [12, 40, 67, 92, 120, 146, 170, 198, 222, 243, 270, 302, 330, 358, 384, 411, 435, 460, 484, 512, 539, 566]))
ink = a.max(2) < 120
lab, _ = ndimage.label(ndimage.binary_dilation(ink, iterations=2))
with open('tomokiyo_columns.tsv', 'w') as f:
    f.write('column\tband\ty0\ty1\tx0\tx1\tdist_to_header_px\n')
    rows = []
    for s in ndimage.find_objects(lab):
        y0, y1, x0, x1 = s[0].start, s[0].stop, s[1].start, s[1].stop
        if y0 < 30 or y0 > 200 or x0 > 585 or ink[y0:y1, x0:x1].sum() < 15: continue
        cx = (x0 + x1) / 2; k = min(H, key=lambda k: abs(H[k] - cx))
        rows.append((list(H).index(k), y0, k, 'double' if y0 > 140 and k != 'e' or y0 > 170 else 'single', y1, x0, x1, abs(H[k] - cx)))
    for _, y0, k, band, y1, x0, x1, d in sorted(rows):
        f.write(f'{k}\t{band}\t{y0}\t{y1}\t{x0}\t{x1}\t{d:.1f}\n')
