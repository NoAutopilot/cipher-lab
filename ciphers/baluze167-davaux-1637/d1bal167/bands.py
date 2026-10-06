#!/usr/bin/env python3
"""Cut gloss+cipher bands of Baluze 168 f.166r (c346) from the native region fetched by tools/iiif_lines.py
(images/crops/src_ark_12148_btv1b9001503k_f346_1000_2930_2700_2420.jpg). Band = cipher line centre (region y, read from the
tool's debug overlay x1.6875) minus 190 px to plus 70 px, so the interlinear gloss above the line is inside the band. D1-BAL167, 6 Oct 2026.
  python3 d1bal167/bands.py  -> d1bal167/bands/b168f166_B<nn>_h<1|2>.jpg (two halves, 1400 px wide, 100 px overlap)"""
import os
from PIL import Image
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = f'{D}/images/crops/src_ark_12148_btv1b9001503k_f346_1000_2930_2700_2420.jpg'
CENTRES = [160, 320, 455, 590, 785, 935, 1085, 1280, 1420]
O = f'{D}/d1bal167/bands'; os.makedirs(O, exist_ok=True)
im = Image.open(SRC).convert('L')
for k, c in enumerate(CENTRES, 1):
    for h, (x0, x1) in enumerate([(0, 1400), (1300, 2700)], 1):
        im.crop((x0, max(0, c - 190), x1, min(im.height, c + 70))).save(f'{O}/b168f166_B{k:02d}_h{h}.jpg', quality=88)
print(len(CENTRES), 'bands')
