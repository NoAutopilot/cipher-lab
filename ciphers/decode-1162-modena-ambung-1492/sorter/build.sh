#!/bin/sh
# D2-1162, 5 Oct 2026: rebuild the g/q/sigma sign-sorter page for decode-1162 + decode-1168.
# Needs the two full-size DECODE PNGs (one tools/decode_browser_login.js login; sha1s in each folder's images/manifest.json):
#   IMG_R1162_I5837_P1.png (sha1 1a49a5f9...) -> $PAGES/R1162_p1.png
#   IMG_R1168_I5864_P1.png (sha1 c3f2a2ea...) -> $PAGES/R1168_f12r.png
# Usage: sh build.sh PAGES_DIR OUT.html
set -e
D=ciphers/decode-1162-modena-ambung-1492/sorter
python3 tools/sign_sorter.py --signs $D/signs.tsv --labels $D/labels.tsv --pages "$1" \
  --title "Modena 1492 g/q Sorter" --out "$2" --focus $D/focus.tsv \
  --focus-note "R1162 p.1 and R1168 f.12r share one cipher (MOD1162); the labels g and q may hide three or four shapes. Split the piles by shape." \
  --auto-clusters 4 --thumb 120 --page-scale 0.5 --page-quality 70 \
  --lede "31 descender signs (g and q labels) from two 1492 Costabili letters, DECODE R1162 p.1 (10 tiles) and R1168 f.12r (21 tiles). Sort them by shape; make new piles for each distinct shape."
