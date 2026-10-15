#!/bin/sh
# MAT-NOM, 15 Oct 2026: re-derive the f.91r / f.91v / f.92r line crops (BnF fr.15572, btv1b9061879d canvases 97-98).
# Images are never committed (lane rule); run from the repository root. 2 requests to openapi.bnf.fr, >= 3 s apart.
# Usage: sh ciphers/matignon-mayenne-1586/f91/regen_f91.sh OUTDIR
set -e
O=${1:?OUTDIR}; mkdir -p "$O/crops"
UA='cipher-lab research script (contact via repository)'
B=https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9061879d
curl -sS -A "$UA" -o "$O/c97_r700-820-7360x4630.jpg" "$B/f97/700,820,7360,4630/max/0/default.jpg"; sleep 3.2
curl -sS -A "$UA" -o "$O/c98_max.jpg" "$B/f98/full/max/0/default.jpg"
I97="$O/c97_r700-820-7360x4630.jpg"; I98="$O/c98_max.jpg"
# regions are x,y,w,h in the fetched file (c97 file = native + (700,820) offset; c98 file = native)
while read img reg pre; do
  python3 tools/iiif_lines.py --image "$(eval echo $img)" --out "$O/crops" --region "$reg" --prefix "$pre" --debug
done <<LIST
\$I97 3800,860,620,230 f91r_glA
\$I97 4480,740,2880,360 f91r_ciA
\$I97 3800,3880,680,750 f91r_glB
\$I97 4480,3780,2880,800 f91r_ciB
\$I98 930,980,800,1600 f91v_glC
\$I98 1650,1020,2900,1440 f91v_ciC
\$I98 930,2800,800,780 f91v_glD
\$I98 1650,2740,2900,780 f91v_ciD
\$I98 5130,1180,760,900 f92r_glE
\$I98 5780,1260,2260,620 f92r_ciE
\$I98 5130,2680,800,1600 f92r_glF
\$I98 5780,2660,2260,1340 f92r_ciF
LIST
