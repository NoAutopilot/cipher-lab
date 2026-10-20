#!/bin/sh
# MONL-C269C (20 Oct 2026): re-derive the untracked c269 (f.138v) L23-L33 region and its levelled line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch269; mkdir -p $D/l23; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/reg_c269_950_3250_2900_1600.jpg "$B/f269/950,3250,2900,1600/max/0/default.jpg"
# overlay only (it chose its own deskew and 12 bands; checked against the levelled cut below, not used for the passes)
python3 ../../tools/iiif_lines.py --image $D/reg_c269_950_3250_2900_1600.jpg --out $D/crops_auto23 --prefix c269c --deskew-region --debug --max-width 1700 --overlap 150
# crops used: region rotated -2.3 deg (as regen_monlc269b.sh), per-segment centres from the row ink profile, +-95 px, s1 x 0-1700,
# s2 x 1400-2510. The first full band (left peak 125, absolute y 3375) is the band MONL-C269B cut as L22 (left peak 1474 + 1900 = 3374),
# so L23-L33 are the next 11 bands. L33 is a short line: its s2 centre is the left peak - 17 (right peak 1368 is the closing flourish).
python3 - "$D" <<'PY'
import sys
from PIL import Image
import numpy as np
D = sys.argv[1]
ro = Image.open(f'{D}/reg_c269_950_3250_2900_1600.jpg').convert('L').rotate(-2.3, resample=Image.BICUBIC, fillcolor=255)
a = np.asarray(ro).astype(float)
def peaks(x0, x1):
    p = (255 - a[:, x0:x1]).sum(1); p = np.convolve(p, np.ones(15) / 15, 'same')
    return [i for i in range(45, len(p) - 46) if p[i] == p[i - 45:i + 46].max() and p[i] > p.max() * 0.3]
L, R = peaks(300, 1300), peaks(1600, 2500)
assert L[:12] == [125, 241, 356, 469, 578, 691, 804, 918, 1023, 1126, 1236, 1344] and R[:11] == [80, 195, 313, 433, 545, 654, 775, 887, 1006, 1105, 1219], (L, R)
R = R[1:11] + [L[11] - 17]
for n in range(11):
    for s, (x0, x1), c in ((1, (0, 1700), L[n + 1]), (2, (1400, 2510), R[n])):
        ro.crop((x0, max(0, c - 95), x1, c + 95)).save(f'{D}/l23/c269_L{n+23:02d}_s{s}.jpg', quality=92)
PY
