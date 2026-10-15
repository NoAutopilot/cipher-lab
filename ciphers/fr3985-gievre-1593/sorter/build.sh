#!/bin/sh
# BNF-GIEVRE-SORT (15 Oct 2026): blind sign sorter for the f.89 cipher paragraph, fr3985-gievre-1593. No network, default blind mode.
#   sh ciphers/fr3985-gievre-1593/sorter/build.sh <out dir>
set -e
T=ciphers/fr3985-gievre-1593/sorter; OUT=${1:-.}
python3 $T/cut.py
python3 tools/sign_sorter.py --signs $T/signs.tsv --labels $T/labels.tsv --pages $T/pages \
  --title "Gievre f.89 Cipher Paragraph Sorter" --out "$OUT/gievre_f89_sorter.html" --data-out "$OUT/gievre_f89_sorter.json" \
  --focus $T/focus.tsv --region $T/region.json \
  --focus-note "Tiles at the places where two independent readings of this paragraph split. Make a pile for each distinct sign you see and move the tiles there; fix the cut if a box is wrong, or send it to BAD-CUT." \
  --lede "The short cipher paragraph at the end of a 1593 letter (BnF fr.3985, f.89), three lines of signs with clear words between them. Tiles are cut from the line images. Starting piles are only groups of similar shapes, with no values. Sort by shape alone."
