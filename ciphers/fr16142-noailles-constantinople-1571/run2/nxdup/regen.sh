#!/bin/sh
# RUN2-NXDUP: re-fetch Dupuy 521 openings 221-226 (Gallica btv1b100339270) at full/4800, and re-cut the line crops
# exactly as used for the two blind passes (crops are not committed; 6 Gallica requests, 2 s apart).
set -e
S=${1:-/tmp/nxdup}; mkdir -p $S/crops
for c in 221 222 223 224 225 226; do
  [ -f $S/f$c.jpg ] || { curl -sS -A "Mozilla/5.0" -o $S/f$c.jpg "https://gallica.bnf.fr/iiif/ark:/12148/btv1b100339270/f$c/full/4800,/0/native.jpg"; sleep 2; }
done
cut() { python3 tools/iiif_lines.py --image $S/f$1.jpg --region $3 --out $S/crops --prefix d$1$2 --follow-slope 400 --debug; }
cut 221 R 2480,2280,1640,780
for c in 222 223 224 225 226; do cut $c L 620,360,1720,2880; done
for c in 222 223 224 225; do cut $c R 2440,360,1680,2760; done
cut 226 R 2440,360,1680,2360
