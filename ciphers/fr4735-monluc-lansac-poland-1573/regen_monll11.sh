#!/bin/sh
# MONL-L11 (15 Oct 2026): re-derive the untracked c268 (f.138) region covering L06-L15 and the L11-L15 line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch268c; mkdir -p $D; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/src_c268_600_2060_3100_1400.jpg "$B/f268/600,2060,3100,1400/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_2060_3100_1400.jpg --out $D/crops --prefix c268c \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150
# bands c268c_L01..L05 = c268 L06..L10 (same centres as MONL-C268B), c268c_L06..L10 = c268 L11..L15; copied as l11/c268c_L11..L15
mkdir -p $D/l11
for i in 6 7 8 9 10; do n=$((i+5)); for s in 1 2; do cp $D/crops/c268c_L$(printf %02d $i)_s$s.jpg $D/l11/c268c_L${n}_s$s.jpg; done; done
