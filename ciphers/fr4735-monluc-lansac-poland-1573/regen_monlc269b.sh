#!/bin/sh
# MONL-C269B (20 Oct 2026): re-derive the untracked c269 (f.138v) L11-L22 region and its levelled line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch269; mkdir -p $D/l11; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/reg_c269_950_1900_2900_1750.jpg "$B/f269/950,1900,2900,1750/max/0/default.jpg"
# overlay only (it chose -3.25 deg and 15 bands; checked against the levelled cut below, not used for the passes)
python3 ../../tools/iiif_lines.py --image $D/reg_c269_950_1900_2900_1750.jpg --out $D/crops_auto11 --prefix c269b --deskew-region --debug --max-width 1700 --overlap 150
# crops used: region rotated -2.3 deg (as regen_monlc269.sh), per-segment centres from the row ink profile, +-95 px, s1 x 0-1700,
# s2 x 1400-2510. Top full band = c269 L10 (ends W:my, as c269_reconciled.tsv), so the next band is L11.
python3 - "$D" <<'PY'
import sys
from PIL import Image
import numpy as np
D = sys.argv[1]
ro = Image.open(f'{D}/reg_c269_950_1900_2900_1750.jpg').convert('L').rotate(-2.3, resample=Image.BICUBIC, fillcolor=255)
a = np.asarray(ro).astype(float)
def peaks(x0, x1):
    p = (255 - a[:, x0:x1]).sum(1); p = np.convolve(p, np.ones(15) / 15, 'same')
    return [i for i in range(45, len(p) - 46) if p[i] == p[i - 45:i + 46].max() and p[i] > p.max() * 0.3]
L, R = peaks(300, 1300), peaks(1600, 2500)
assert L[:12] == [159, 264, 384, 498, 615, 732, 863, 986, 1102, 1222, 1348, 1474] and R[:12] == [148, 264, 373, 488, 596, 705, 833, 951, 1075, 1191, 1309, 1427], (L, R)
for n in range(12):
    for s, (x0, x1), c in ((1, (0, 1700), L[n]), (2, (1400, 2510), R[n])):
        ro.crop((x0, max(0, c - 95), x1, c + 95)).save(f'{D}/l11/c269_L{n+11:02d}_s{s}.jpg', quality=92)
PY
