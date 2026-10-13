#!/bin/sh
# SFZ-SORT (13 Oct 2026): blind sign sorter for the Duke's two glossed 1447 slips, BnF italien 1584 f.5 + f.8. No network:
# reads the two Gallica native regions already on disk (../sforza-italien1584-1447/duke/images/manifest.json).
#   sh ciphers/sforza-duke-1447-f15/sorter/build.sh <out dir>        (repo root; needs scipy, scikit-learn, Pillow)
# The page, its tiles, pages/, debug/ and region.jpg are NOT committed; this script regenerates them. Preflight runs inside
# tools/sign_sorter.py. Default blind mode: no key, no value, no reader label on the page.
set -e
T=ciphers/sforza-duke-1447-f15/sorter; OUT=${1:-.}; mkdir -p "$OUT"
python3 $T/cut.py
python3 tools/sign_sorter.py --signs $T/signs.tsv --labels $T/labels.tsv --pages $T/pages --cipher-lines $T/cipher_lines.tsv \
  --region $T/region.json --seed-shape \
  --title "Sforza Duke 1447 Sign Sorter" --out "$OUT/sforza_duke_f5_f8_sorter.html" --data-out "$OUT/sforza_duke_f5_f8_data.json" \
  --focus $T/focus.tsv --auto-clusters 4 \
  --focus-note "Forty tiles from the most frequent shapes, two per starting pile. Each started in a pile by its shape alone." \
  --lede "Two cipher slips of January 1447 written for the Duke of Milan (BnF italien 1584, ff. 5 and 8; Gallica canvases 9 and 11): 2,325 tiles from 31 straightened cipher lines, one ink group per tile. The starting piles are shape groups made by machine from the images alone, with no reader, key or value behind them; pile names are not letters. Make one pile per distinct sign: merge piles that are one sign, split piles that mix two, move single tiles, re-cut joined signs, and send dots, specks and bad cuts to BAD-CUT." \
  --thumb 80 --tile-quality 60 --page-scale 0.5 --page-quality 50
