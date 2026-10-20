#!/bin/sh
# MONL-C269A (20 Oct 2026): re-derive the untracked c269 (f.138v) overview, the L01-L10 region and its levelled line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch269; mkdir -p $D/l01; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/ov_c269.jpg "$B/f269/full/1000,/0/default.jpg"; sleep 1.6
curl -sS -A "$UA" -o $D/reg_c269_950_850_2900_1250.jpg "$B/f269/950,850,2900,1250/max/0/default.jpg"
# overlay only (its -2.50 deg deskew and auto bands were not used for the passes; checked against the levelled cut below)
python3 ../../tools/iiif_lines.py --image $D/reg_c269_950_850_2900_1250.jpg --out $D/crops_auto --prefix c269 --deskew-region --debug --max-width 1700 --overlap 150
# crops used: region rotated -2.3 deg, per-segment centres from the row ink profile (s1 x 300-1300, s2 x 1600-2500), +-95 px,
# s1 x 0-1700, s2 x 1400-2510 (cut before the gutter: the facing leaf's clear text starts ~x 2540). L01 = "brev" line.
python3 - "$D" <<'PY'
import sys, os
from PIL import Image
import numpy as np
D = sys.argv[1]
ro = Image.open(f'{D}/reg_c269_950_850_2900_1250.jpg').convert('L').rotate(-2.3, resample=Image.BICUBIC, fillcolor=255)
a = np.asarray(ro).astype(float)
def peaks(x0, x1):
    p = (255 - a[:, x0:x1]).sum(1); p = np.convolve(p, np.ones(15) / 15, 'same')
    return [i for i in range(45, len(p) - 46) if p[i] == p[i - 45:i + 46].max() and p[i] > p.max() * 0.3]
L, R = peaks(300, 1300), peaks(1600, 2500)
assert L[:10] == [73, 200, 315, 425, 533, 645, 757, 866, 983, 1093] and R[:10] == [80, 202, 310, 422, 536, 648, 754, 866, 975, 1089], (L, R)
for n in range(10):
    for s, (x0, x1), c in ((1, (0, 1700), L[n]), (2, (1400, 2510), R[n])):
        ro.crop((x0, max(0, c - 95), x1, c + 95)).save(f'{D}/l01/c269_L{n+1:02d}_s{s}.jpg', quality=92)
PY
