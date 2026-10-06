#!/bin/sh
# Build the blocks A/C2 sign-sorter page (no network). Usage from the repo root:
#   sh ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh <out dir>
set -e
T=ciphers/na-oldenbarnevelt-2442-1605; OUT=${1:-.}
python3 $T/sorter/build_inputs.py
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --title "Oldenbarnevelt 2442 Sign Sorter" --out "$OUT/oldenbarnevelt_AC2_sorter.html" --data-out "$OUT/oldenbarnevelt_AC2_sorter.json" \
  --focus $T/sorter/focus.tsv \
  --focus-note "Signs the two blind machine readers wrote differently (vowel-letter/digit notation folded first): the look-alike pairs v/r and the G-shaped ligature (l/c/b) first, then d/8, 5/s, p/g/l, c/t, m/n/r, then the rest." \
  --lede "Nationaal Archief 1.01.02 inv. 2442, blocks A (folio 54) and C2 (folio 56), from R7-OLDA's deskewed line crops. Piles are R7-OLDA's reconciled draft labels (a draft: 36 of 165 words uncertain); tiles are approximate cuts laid out along each line by sign count, so a tile can be a sign off. Move a tile to the pile it really belongs to, or to BAD-CUT." \
  --auto-clusters 3
