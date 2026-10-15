#!/bin/sh
# MONL-L21 (15 Oct 2026): re-derive the untracked c268 (f.138) region covering L20-L25 and the L21-L25 line crops from openapi.bnf.fr.
set -e
cd "$(dirname "$0")"; D=images/scratch268e; mkdir -p $D; echo '*' > $D/.gitignore
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060724s
UA="cipher-lab research script (contact via repository)"
curl -sS -A "$UA" -o $D/src_c268_600_3650_3100_800.jpg "$B/f268/600,3650,3100,800/max/0/default.jpg"
python3 ../../tools/iiif_lines.py --image $D/src_c268_600_3650_3100_800.jpg --out $D/crops --prefix c268e \
  --deskew-region --mask-neighbours --debug --max-width 1700 --overlap 150
# band identity from the debug overlay: see NOTES.md MONL-L21 (bands copied as l21/c268e_L21..L25)
# bands c268e_L01 = c268 L20 (checked against passes/c268d_reconciled.tsv L20: K10 K41 K36 K01 K09 K37 ...), c268e_L02..L06 = c268 L21..L25,
# c268e_L07 = L26 (not used); copied as l21/c268e_L21..L25
mkdir -p $D/l21
for i in 2 3 4 5 6; do n=$((i+19)); for s in 1 2; do cp $D/crops/c268e_L0${i}_s$s.jpg $D/l21/c268e_L${n}_s$s.jpg; done; done
