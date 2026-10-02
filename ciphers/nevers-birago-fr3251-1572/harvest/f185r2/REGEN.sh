#!/bin/sh
# NEVBIR-185B, 2 Oct 2026: re-fetch canvas 189's f.185r region and canvas 190, re-cut the line crops (crops gitignored:
# folder over its 30 MB line). Run from the repository root. Two Gallica requests, 2 s apart.
set -e
D=ciphers/nevers-birago-fr3251-1572/harvest
B="https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060248g"
[ -f $D/f185/src_f189_4780_980_2850_3420.jpg ] || curl -sS -A "Mozilla/5.0" "$B/f189/4780,980,2850,3420/full/0/native.jpg" -o $D/f185/src_f189_4780_980_2850_3420.jpg
sleep 2
curl -sS -A "Mozilla/5.0" "$B/f190/1850,1300,1700,260/full/0/native.jpg" -o $D/f185/src_f190_1850_1300_1700_260.jpg
python3 tools/iiif_lines.py --image $D/f185/src_f189_4780_980_2850_3420.jpg --out $D/f185r2 --prefix f185r --centres 1206,1308,1410,1785,1892,2045,2165,2289,2397,2544,2685,2810,2948,3080 --follow-slope 300 --slope-margin 15 --max-width 1250 --overlap 50 --debug
python3 tools/iiif_lines.py --image $D/f185/src_f190_1850_1300_1700_260.jpg --out $D/f185v --prefix f185v --centres 120 --max-width 1250 --overlap 50 --debug
# 2x reader crops: python3 -c "from PIL import Image ..." as in NOTES.md NEVBIR-185B (LANCZOS 2x into lines2x/)
