#!/bin/sh
# Build the f.110 sign-sorter page (no network). Usage from the repo root:
#   sh ciphers/matignon-mayenne-1586/sorter/build.sh <out dir>
set -e
T=ciphers/matignon-mayenne-1586; OUT=${1:-.}
python3 $T/sorter/build_inputs.py
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --title "Matignon f.110 Sign Sorter" --out "$OUT/matignon_f110_sorter.html" --data-out "$OUT/matignon_f110_sorter.json" \
  --focus $T/sorter/focus.tsv \
  --focus-note "Signs the two blind machine readers split on or kept apart from the key's shapes: BOX, z, T, U, w, 4." \
  --lede "BnF fr.15572 f.110, lines 1-6 (Gallica btv1b9061879d, canvas 116). Piles are the existing transcription's shape labels; tiles are approximate cuts from ~52 px line strips. Move a tile to the pile it really belongs to, or to BAD-CUT." \
  --auto-clusters 3
