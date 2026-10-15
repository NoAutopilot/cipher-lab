#!/bin/bash
# OBRED-556 (15 Oct 2026): re-derive NA 1.01.02 inv. 6019 scans 555-557 at 5000 px (4 requests incl. METS), the line crops the two blind
# passes read, and the taller gloss crops. Images stay outside git. Run from this folder. Usage: bash screen_tools/regen_556.sh OUTDIR
set -e; O=${1:-scratch_556}; M=1ebb4182-2b80-4e37-a226-8b8c7e578c8b
python3 screen_tools/na_fetch.py $M $O 5000 555 556 557
python3 ../../tools/iiif_lines.py --image $O/s0555_5000.jpg --out $O/c555 --region 2480,1180,2280,1560 --prefix s555 --debug
python3 ../../tools/iiif_lines.py --image $O/s0556_5000.jpg --out $O/c556 --region 440,660,2160,720 --prefix s556 --debug
python3 - "$O" <<'PY'
import sys, os
from PIL import Image
o = sys.argv[1]; os.makedirs(o + '/g', exist_ok=True)
a = Image.open(o + '/s0555_5000.jpg'); b = Image.open(o + '/s0556_5000.jpg')
c555 = {'L01':34,'L02':137,'L03':241,'L04':338,'L05':442,'L06':546,'L08':756,'L09':858,'L12':1179,'L13':1257,'L14':1350,'L15':1455}
c556 = {'L01':155,'L02':254,'L03':358,'L04':466,'L05':573,'L06':678}
for k, c in c555.items():
    y = 1180 + c; a.crop((2900, max(0, y - 105), 4760, y + 45)).save(f'{o}/g/t555_{k}.jpg')
for k, c in c556.items():
    y = 660 + c; b.crop((440, y - 105, 2620, y + 45)).save(f'{o}/g/t556_{k}.jpg')
a.crop((2400,1300,3150,2700)).save(f'{o}/m555.jpg'); b.crop((150,700,1300,1150)).save(f'{o}/m556.jpg')
PY
sha1sum $O/s055[567]_5000.jpg
