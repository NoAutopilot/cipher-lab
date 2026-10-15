#!/bin/sh
# MONL-L16 (15 Oct 2026): re-derive the untracked c268 (f.138) region covering L14-L22 and the L16-L20 line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch268d; mkdir -p $D; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/src_c268_600_2950_3100_1000.jpg "$B/f268/600,2950,3100,1000/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_2950_3100_1000.jpg --out $D/crops --prefix c268d \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150
# bands c268d_L01 = c268 L14 (ink blot), c268d_L02 = L15 (the '//'), c268d_L03..L07 = c268 L16..L20; copied as l16/c268d_L16..L20
mkdir -p $D/l16
for i in 3 4 5 6 7; do n=$((i+13)); for s in 1 2; do cp $D/crops/c268d_L0${i}_s$s.jpg $D/l16/c268d_L${n}_s$s.jpg; done; done
