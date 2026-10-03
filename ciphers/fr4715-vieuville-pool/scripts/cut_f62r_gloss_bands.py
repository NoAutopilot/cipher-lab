#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-11 (3 Oct 2026): overlapping gloss bands of no.39 f.62r from the native region
images/src_ark_12148_btv1b52509819x_f139_450_1580_3200_1580.jpg (tools/iiif_lines.py --dry-run: 24 lines, pitch 54,
centres pasted in NOTES.md). As for f.44r (cut_f44r_gloss_bands.py), the row centres do not follow the leaf's slant
and a midpoint band splits a gloss from its code, so the crops are bands 170 px tall every 110 px (about three lines,
each gloss whole with the line under it in at least one band), 3 overlapping segments, 1.5x. Regenerable, not committed.
usage: cut_f62r_gloss_bands.py OUTDIR"""
import sys, os
from PIL import Image
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEG = [(0, 1200), (1000, 2200), (2000, 3200)]
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
im = Image.open(os.path.join(HERE, 'images/src_ark_12148_btv1b52509819x_f139_450_1580_3200_1580.jpg'))
n = 0
for i, up in enumerate(range(100, 1480, 110)):
    dn = min(up + 170, im.height)
    for s, (x0, x1) in enumerate(SEG, 1):
        c = im.crop((x0, up, x1, dn))
        c = c.resize((int(c.width * 1.5), int(c.height * 1.5)), Image.LANCZOS)
        c.save(os.path.join(out, f'f62r_g{i+1:02d}_s{s}.jpg'), quality=88); n += 1
print('wrote', n, 'crops to', out)
