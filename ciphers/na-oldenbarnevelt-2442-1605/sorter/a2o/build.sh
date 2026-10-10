#!/bin/sh
# SORT-A2o: Oldenbarnevelt 2442 leaves 4 and 7 (OLD-O2 masked line crops) sign sorter. No network.
#   sh ciphers/na-oldenbarnevelt-2442-1605/sorter/a2o/build.sh <out dir>
set -e
T=ciphers/na-oldenbarnevelt-2442-1605/sorter/a2o; OUT=${1:-.}
python3 $T/cut.py
python3 tools/sign_sorter.py --signs $T/signs.tsv --labels $T/labels.tsv --pages $T/pages \
  --title "Oldenbarnevelt 2442 Leaves 4 and 7 Sign Sorter" --out "$OUT/oldenbarnevelt_L47_sorter.html" --data-out "$OUT/oldenbarnevelt_L47_sorter.json" \
  --focus $T/focus.tsv --region $T/region.json --tile-quality 70 \
  --focus-note "Signs near the places where two independent blind machine readings of these two leaves wrote different signs. Sort these first; the rest is optional. Look-alikes to watch: 3/4/7/8, v and r, l and the loop shapes." \
  --lede "Nationaal Archief 1.01.02 inv. 2442, leaves 4 and 7 (cipher text only), cut from levelled copies of the page with the neighbouring lines masked out. Tiles are the ink groups of each line. Starting piles are only groups of similar shapes, with no values and no machine reading. Move a tile to the pile it really belongs to, make a new pile for a sign you see that has none, fix its box with Fix the cut, or send it to BAD-CUT."
