#!/bin/sh
# MONL-ALIGN (14 Oct 2026): re-derive the untracked ff.140r-141r overviews and line crops from openapi.bnf.fr (>= 3 s apart).
set -e
cd "$(dirname "$0")"; D=images/scratchalign; mkdir -p $D/crops
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
for c in 272 273 274; do curl -sS -A "$UA" -o $D/c$c.jpg "$B/f$c/full/1400,/0/default.jpg"; sleep 3; done
T=../../tools/iiif_lines.py
python3 $T --ark btv1b9060724s --canvas 272 --iiif-host openapi --region 560,1250,2980,5250 --out $D/crops --prefix f140r --deskew-region --mask-neighbours --debug; sleep 3
python3 $T --ark btv1b9060724s --canvas 273 --iiif-host openapi --region 1000,1300,2650,4000 --out $D/crops --prefix f140v --deskew-region --mask-neighbours --debug; sleep 3
python3 $T --ark btv1b9060724s --canvas 274 --iiif-host openapi --region 650,1250,2800,1800 --out $D/crops --prefix f141r --deskew-region --mask-neighbours --debug
