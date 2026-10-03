#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-13 (3 Oct 2026): overlapping gloss bands of no.28 f.51r from the native region
images/src_ark_12148_btv1b52509819x_f117_360_1480_3200_2240.jpg (tools/iiif_lines.py --dry-run: 39 ink rows (lines + gloss rows), pitch 43,
centres pasted in NOTES.md). Same shape as cut_f62r_gloss_bands.py: bands 170 px tall every 110 px, 3 overlapping
segments, 1.5x, so each gloss is whole with the line under it in at least one band. Regenerable, not committed.
usage: cut_f51r_gloss_bands.py OUTDIR"""
import sys, os
from PIL import Image
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEG = [(0, 1220), (990, 2210), (1980, 3200)]
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
im = Image.open(os.path.join(HERE, 'images/src_ark_12148_btv1b52509819x_f117_360_1480_3200_2240.jpg'))
n = 0
for i, up in enumerate(range(100, im.height - 120, 110)):
    dn = min(up + 170, im.height)
    for s, (x0, x1) in enumerate(SEG, 1):
        c = im.crop((x0, up, x1, dn))
        c = c.resize((int(c.width * 1.5), int(c.height * 1.5)), Image.LANCZOS)
        c.save(os.path.join(out, f'f51r_g{i+1:02d}_s{s}.jpg'), quality=88); n += 1
print('wrote', n, 'crops to', out)
