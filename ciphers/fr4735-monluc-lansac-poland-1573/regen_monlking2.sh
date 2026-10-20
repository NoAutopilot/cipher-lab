#!/bin/sh
# MONL-KING2 (20 Oct 2026): re-derive the untracked c258 (f.133) native page and the L01-L10 crops read in king2/ (2 requests).
set -e
cd "$(dirname "$0")"; D=images/scratchking2; mkdir -p $D/crops; echo '*' > $D/.gitignore
[ -f $D/src_image_v3_ark_12148_btv1b9060724s_f258_full.jpg ] || curl -sS -A "cipher-lab research script (contact via repository)" -o $D/src_image_v3_ark_12148_btv1b9060724s_f258_full.jpg "https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s/f258/full/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_image_v3_ark_12148_btv1b9060724s_f258_full.jpg --region 1150,720,2550,1330 --out $D --prefix c258k --deskew --debug
python3 - $D <<'PY'
import sys
from PIL import Image
D = sys.argv[1]
for i in range(1, 11):
    a = Image.open(f'{D}/c258k_L{i:02d}_s1.jpg'); b = Image.open(f'{D}/c258k_L{i:02d}_s2.jpg')
    a.crop((0, 0, 1700, a.height)).save(f'{D}/crops/c258_L{i:02d}_s1.jpg', quality=92)   # native x 1150-2850
    b.crop((1250, 0, 2400, b.height)).save(f'{D}/crops/c258_L{i:02d}_s2.jpg', quality=92)  # native x 2550-3700
PY
