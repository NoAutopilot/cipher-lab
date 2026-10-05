#!/usr/bin/env python3
"""Cut the 15 gloss-fixed letter-sign exemplars of 167 f.157 (PREREG-D2DAVEX.md) from line crops already on disk and paste them on one
labelled sheet. Boxes (x0, x1 in the crop's own pixels, full crop height) were read from each crop's column ink profile (dark-pixel runs in the middle band) and matched to the signs by eye, D2-DAVEX, 5 Oct 2026.
  python3 d2davex/cut_exemplars.py   -> d2davex/exemplars/<line>_<idx>_<letter>.png, d2davex/exemplar_sheet.png"""
import os
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); C = f'{D}/images/crops'; O = f'{D}/d2davex/exemplars'
BOXES = [  # (ciphertext row, token index, letter from gloss, crop file, x0, x1)
 ('L03', 5, 'e', 'b167f157_run1_L03_s2', 545, 653), ('L03', 6, 'u', 'b167f157_run1_L03_s2', 700, 749),
 ('L03', 7, 'o', 'b167f157_run1_L03_s2', 798, 871), ('L03', 8, 'u', 'b167f157_run1_L03_s2', 905, 988),
 ('L03', 10, 'n', 'b167f157_run1_L03_s2', 1229, 1287), ('L03', 15, 'i', 'b167f157_run1_L03_s2', 2060, 2135),
 ('L03', 16, 'x', 'b167f157_run1_L04_s1', 242, 300),
 ('R2', 4, 'n', 'b167f157_run2_L02_s1', 1186, 1269), ('R2', 5, 's', 'b167f157_run2_L02_s1', 1281, 1369),
 ('R2', 7, 'i', 'b167f157_run2_L02_s1', 1590, 1650), ('R2', 9, 'n', 'b167f157_run2_L02_s1', 1855, 1920),
 ('R2', 10, 'n', 'b167f157_run2_L02_s1', 1993, 2092), ('R2', 11, 'a', 'b167f157_run2_L02_s1', 2132, 2225),
 ('R2', 12, 'b', 'b167f157_run2_L02_s1', 2279, 2371), ('R2', 14, 's', 'b167f157_run2_L02_s2', 1295, 1356)]
os.makedirs(O, exist_ok=True); cells = []
for row, i, let, f, x0, x1 in BOXES:
    im = Image.open(f'{C}/{f}.jpg').convert('L'); im = im.crop((x0, 0, x1, im.height))
    im.save(f'{O}/167f157{row}_{i:02d}_{let}.png'); cells.append((f'{row}.{i} {let}', im))
W = 130; H = max(im.height for _, im in cells) + 30
sheet = Image.new('L', (W * len(cells), H), 255); d = ImageDraw.Draw(sheet)
for k, (lab, im) in enumerate(cells):
    sheet.paste(im, (k * W + (W - im.width) // 2, 28)); d.text((k * W + 4, 4), lab, fill=0)
sheet.save(f'{D}/d2davex/exemplar_sheet.png'); print(f'{len(cells)} exemplars, sheet {sheet.size}')
