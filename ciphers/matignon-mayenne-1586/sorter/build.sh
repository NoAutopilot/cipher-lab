#!/bin/sh
# Build the f.110 sign-sorter page (no network). Usage from the repo root:
#   sh ciphers/matignon-mayenne-1586/sorter/build.sh <out dir>
# R8-MATCUT (6 Oct 2026): recut.py (deskewed, one tile = one sign) replaces build_inputs.py (R7-MATSORT v1 flat-band cut,
# kept for the record; its output is signs_v1.tsv / labels_v1.tsv / focus_v1.tsv / fit_v1.tsv).
set -e
T=ciphers/matignon-mayenne-1586; OUT=${1:-.}
python3 $T/sorter/recut.py
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --title "Matignon f.110 Sign Sorter" --out "$OUT/matignon_f110_sorter.html" --data-out "$OUT/matignon_f110_sorter.json" \
  --focus $T/sorter/focus.tsv --region $T/sorter/region.json \
  --focus-note "First, signs the two blind machine readers split on or kept apart from the key's shapes (BOX, z, T, U, w, 4); then tiles that no transcribed sign lined up with (started by shape)." \
  --lede "BnF fr.15572 f.110, written lines 1-5 (Gallica btv1b9061879d, canvas 116). Tiles are cut from each sign's own ink on strips that follow the sloping lines (R8-MATCUT re-cut, 6 Oct 2026). Starting piles are Bourdeau's transcription labels where a tile lines up with a transcribed sign, else the pile its shape mostly holds. At the right edge each line's rising tail carries the end of the line above in the transcription; the right ends of lines 1 and 5 match no transcribed line. Move a tile to the pile it really belongs to, fix its box with Fix the cut, or send it to BAD-CUT." \
  --auto-clusters 3
