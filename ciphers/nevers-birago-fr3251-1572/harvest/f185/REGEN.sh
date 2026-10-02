#!/bin/sh
# NEVBIR-185, 2 Oct 2026: re-fetch the two native regions of canvas 189 (f.184v foot, f.185r) and re-cut the line crops.
# Run from the repository root. Two Gallica requests, 2 s apart.
set -e
D=ciphers/nevers-birago-fr3251-1572/harvest
B="https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060248g/f189"
curl -sS -A "Mozilla/5.0" "$B/1600,3680,2550,600/full/0/native.jpg" -o $D/f185/src_f189_1600_3680_2550_600.jpg
sleep 2
curl -sS -A "Mozilla/5.0" "$B/4780,980,2850,3420/full/0/native.jpg" -o $D/f185/src_f189_4780_980_2850_3420.jpg
python3 tools/iiif_lines.py --image $D/f185/src_f189_1600_3680_2550_600.jpg --out $D/f184v --prefix f184v --centres 80,205,330,465 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug
python3 tools/iiif_lines.py --image $D/f185/src_f189_4780_980_2850_3420.jpg --out $D/f185r --prefix f185r --centres 105,215,330,435,550,665,775,890 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug
