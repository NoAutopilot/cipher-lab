#!/bin/sh
# MONL-C268B (14 Oct 2026): re-derive the untracked c268 (f.138) L06-L10 native region and line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch268b; mkdir -p $D; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/src_c268_600_2060_3100_660.jpg "$B/f268/600,2060,3100,660/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_2060_3100_660.jpg --out $D/crops --prefix c268b \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150
# bands c268b_L01..L05 = c268 L06..L10 (band L06 is the top of c268 L11, unused)
