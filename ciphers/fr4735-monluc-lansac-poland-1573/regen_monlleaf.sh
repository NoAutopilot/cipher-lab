#!/bin/sh
# MONL-LEAF (20 Oct 2026): re-derive the untracked overview and first-two-line crops of c269 (f.138v), c264, c258 from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratchleaf; mkdir -p $D/crops; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
for c in 258 262 264 269; do curl -sS -A "$UA" -o $D/ov_c$c.jpg "$B/f$c/full/1000,/0/default.jpg"; sleep 1.6; done
curl -sS -A "$UA" -o $D/reg_c269w.jpg "$B/f269/1000,820,2900,420/max/0/default.jpg"; sleep 1.6
curl -sS -A "$UA" -o $D/reg_c264.jpg "$B/f264/750,450,2750,420/max/0/default.jpg"; sleep 1.6
curl -sS -A "$UA" -o $D/reg_c258.jpg "$B/f258/1100,680,2600,420/max/0/default.jpg"
python3 - "$D" <<'PY'
import sys
from PIL import Image
D = sys.argv[1]
cuts = {'c269': ('reg_c269w.jpg', 2420, {(1, 1): (95, 225), (1, 2): (50, 185), (2, 1): (180, 305), (2, 2): (150, 280)}),
        'c264': ('reg_c264.jpg', 2750, {(1, 1): (80, 215), (1, 2): (80, 215), (2, 1): (200, 335), (2, 2): (200, 335)}),
        'c258': ('reg_c258.jpg', 2600, {(1, 1): (75, 210), (1, 2): (75, 210), (2, 1): (190, 320), (2, 2): (190, 320)})}
for c, (f, W, ys) in cuts.items():
    im = Image.open(f'{D}/{f}')
    for (n, s), (y0, y1) in ys.items():
        x0, x1 = (0, 1700) if s == 1 else (1400, W)
        im.crop((x0, y0, x1, y1)).save(f'{D}/crops/{c}_L{n:02d}_s{s}.jpg', quality=92)
PY
