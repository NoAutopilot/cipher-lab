#!/bin/sh
# SUP-MONLUC (20 Oct 2026): re-derive the untracked c268 (f.138) region covering L25-L31 and the L26-L30 line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch268f; mkdir -p $D; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/src_c268_600_4180_3100_800.jpg "$B/f268/600,4180,3100,800/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_4180_3100_800.jpg --out $D/crops --prefix c268f \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150
# SUP-MONLUC: automatic centres were off (~40 px, a spurious band); re-cut with eye centres from the debug overlay
rm -rf $D/crops
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_4180_3100_800.jpg --out $D/crops --prefix c268f \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150 --centres 122,240,352,465,572,680
# band c268f_L01 = c268 L25 (opens K04 K05 K10 K41 K34 K26, passes/c268e_reconciled.tsv L25), c268f_L02..L06 = c268 L26..L30
mkdir -p $D/l26
for i in 2 3 4 5 6; do n=$((i+24)); for s in 1 2; do cp $D/crops/c268f_L0${i}_s$s.jpg $D/l26/c268f_L${n}_s$s.jpg; done; done
