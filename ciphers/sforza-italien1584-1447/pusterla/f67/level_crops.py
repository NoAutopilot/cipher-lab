#!/usr/bin/env python3
"""Level line crops of f.67 (SFZ-NEXT, 8 Oct 2026). Line centres from tools/iiif_lines.py --dry-run ink profiles of the
source region in two column strips (0:600 -> x=300, 2200:2800 -> x=2500); each line is fitted y = a + b*x through the two
centres and sheared level (PIL affine), 96 px high, cut in two halves (0-1500, 1400-2850) with 100 px overlap."""
import os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
L = [66,143,223,304,372,453,547,634,707,788,874,957,1040,1130,1211,1302,1380,1457,1545,1625,1702,1795,1873,1952,2026,2099,2198,2419]
R = [28,107,189,269,374,448,526,610,697,785,860,940,1017,1108,1185,1269,1361,1462,1535,1615,1689,1772,1850,1935,1998,2072,2138,2383]
src = Image.open(os.path.join(HERE, 'src_ark_12148_btv1b100373864_f64_4250_480_2850_2500.jpg')).convert('L')
H = 96
for n, (yl, yr) in enumerate(zip(L, R), 1):
    b = (yr - yl) / 2200.0; a = yl - 300 * b
    # output (u, v) <- source (u, a - H/2 + v + b*u)
    lev = src.transform((src.width, H), Image.AFFINE, (1, 0, 0, b, 1, a - H / 2), resample=Image.BICUBIC, fillcolor=255)
    for k, (x0, x1) in enumerate(((0, 1500), (1400, 2850)), 1):
        lev.crop((x0, 0, x1, H)).save(os.path.join(HERE, f'f67_L{n:02d}_h{k}.jpg'), quality=88)
print(len(L), 'lines')
