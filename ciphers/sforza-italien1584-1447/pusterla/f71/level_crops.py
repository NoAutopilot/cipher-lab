#!/usr/bin/env python3
"""Level line crops of f.71 (SFZ-NEXT, 8 Oct 2026). Line centres from tools/iiif_lines.py --dry-run ink profiles of the
source region in two column strips (0:600 -> x=300, 2200:2800 -> x=2500); each line is fitted y = a + b*x through the two
centres and sheared level (PIL affine), 96 px high, cut in two halves (0-1500, 1400-2850) with 100 px overlap."""
import os, sys
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
L = [128,218,297,364,432,507,594,676,755,832,898,966,1053,1140,1232,1304,1391,1475,1561,1645,1726,1832,1917,1999,2090,
     2175,2249,2323,2402,2468,2546,2626,2714,2807,2886,2971,3055,3124,3211,3286,3363,3438,3515,3614,3697,3779]
R = [173,258,321,405,477,560,623,709,790,865,951,1031,1105,1191,1259,1341,1419,1496,1586,1663,1750,1830,1918,2011,2093,
     2178,2260,2342,2422,2497,2574,2667,2759,2839,2936,3013,3091,3174,3262,3339,3423,3493,3572,3639,3720,3813]
src = Image.open(os.path.join(HERE, 'src_ark_12148_btv1b100373864_f68_4250_1330_2850_3900.jpg')).convert('L')
H = 96
for n, (yl, yr) in enumerate(zip(L, R), 1):
    b = (yr - yl) / 2200.0; a = yl - 300 * b
    # output (u, v) <- source (u, a - H/2 + v + b*u)
    lev = src.transform((src.width, H), Image.AFFINE, (1, 0, 0, b, 1, a - H / 2), resample=Image.BICUBIC, fillcolor=255)
    for k, (x0, x1) in enumerate(((0, 1500), (1400, 2850)), 1):
        lev.crop((x0, 0, x1, H)).save(os.path.join(HERE, f'f71_L{n:02d}_h{k}.jpg'), quality=88)
print(len(L), 'lines')
# Committed crops were re-saved at JPEG quality 72 after the passes (SFZ-NEXT, folder size); this script writes quality 88.
