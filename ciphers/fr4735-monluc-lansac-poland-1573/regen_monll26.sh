#!/bin/sh
# SUP-MONLUC (20 Oct 2026): re-derive the untracked c268 (f.138) region covering L25-L31 and the L26-L30 line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch268f; mkdir -p $D; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/src_c268_600_4180_3100_800.jpg "$B/f268/600,4180,3100,800/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_4180_3100_800.jpg --out $D/crops --prefix c268f \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150
# SUP-MONLUC: tools/iiif_lines.py's auto bands were off (spurious band); with --centres its s2 segments still sat ~50 px off the
# line (the deskew it reported, -2.70 deg, is too shallow for the right half; first two passes on those crops are void,
# passes/void_c268f/). Crops used for the passes: the region rotated -4.3 deg (left/right ink-profile peaks agree within 3 px),
# centre +-95 px, s1 x 0-1700, s2 x 1400-3100, no mask. Band 1 = c268 L25 (opens K04 K05 K10 K41 K34 K26), bands 2-6 = L26-L30.
python3 - "$D" <<'PY'
import sys, os
from PIL import Image
D = sys.argv[1]; im = Image.open(f'{D}/src_c268_600_4180_3100_800.jpg').convert('L')
ro = im.rotate(-4.3, resample=Image.BICUBIC, fillcolor=255); os.makedirs(f'{D}/l26', exist_ok=True)
for n, c in zip(range(26, 31), (202, 308, 422, 536, 649)):
    for s, (x0, x1) in ((1, (0, 1700)), (2, (1400, 3100))):
        ro.crop((x0, c - 95, x1, min(800, c + 95))).save(f'{D}/l26/c268f_L{n}_s{s}.jpg', quality=92)
PY
