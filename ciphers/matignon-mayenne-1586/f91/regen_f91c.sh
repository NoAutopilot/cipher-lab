#!/bin/sh
# MAT-F91C, 15 Oct 2026: re-derive the blocks C and F line crops of f.91v/92r (BnF fr.15572, btv1b9061879d canvas 98).
# Images are never committed (lane rule); run from the repository root. 1 request to openapi.bnf.fr (skipped if OUTDIR/c98_max.jpg exists;
# sha1 dfec5334995404682b478e338d522405ec8e32a2, 8722x6347). Usage: sh ciphers/matignon-mayenne-1586/f91/regen_f91c.sh OUTDIR
set -e
O=${1:?OUTDIR}; mkdir -p "$O"
I="$O/c98_max.jpg"
[ -s "$I" ] || curl -sS -A 'cipher-lab research script (contact via repository)' -o "$I" \
  "https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9061879d/f98/full/max/0/default.jpg"
F='--deskew-region --band-extent --mask-neighbours --max-width 1600 --overlap 80 --debug'
python3 tools/iiif_lines.py --image "$I" --out "$O/crops" --region 1480,1050,3100,1400 --prefix ciC $F
python3 tools/iiif_lines.py --image "$I" --out "$O/crops" --region 5230,2640,2900,1420 --prefix ciF $F
