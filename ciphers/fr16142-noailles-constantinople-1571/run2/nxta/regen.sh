#!/bin/sh
# RUN2-NXTA: re-cut the c510 line crops (kept out of the repo; ~30 MB of strips). Run from the repository root.
# Usage: sh ciphers/fr16142-noailles-constantinople-1571/run2/nxta/regen.sh OUTDIR
set -e
OUT=${1:-/tmp/nxta}; mkdir -p "$OUT"
D=ciphers/fr16142-noailles-constantinople-1571/run2/nxta
[ -f "$OUT/c510_full.jpg" ] || curl -sS -A "Mozilla/5.0" -o "$OUT/c510_full.jpg" \
  "https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060927q/f510/full/full/0/default.jpg"   # native 4986x7169
python3 tools/iiif_lines.py --image "$OUT/c510_full.jpg" --region 1100,1040,3650,4680 \
  --centres 82,213,342,493,619,743,867,991,1114,1243,1373,1496,1620,1754,1889,2018,2142,2267,2393,2524,2651,2769,2903,3031,3153,3278,3407,3536,3672,3796,3930,4054,4190,4315,4451,4582 \
  --follow-slope 300 --slope-margin 15 --max-width 1900 --overlap 100 --prefix c510 --out "$OUT/crops510" --debug
# L00 = cipher tail of manuscript line 4 (after the clear "...la reception dicelle que"), cut by hand
python3 -c "from PIL import Image; Image.open('$OUT/c510_full.jpg').crop((3420,905,4720,1090)).save('$OUT/crops510/c510_L00_s1.jpg')"
python3 "$D/mark_overlap.py" "$OUT/crops510"
