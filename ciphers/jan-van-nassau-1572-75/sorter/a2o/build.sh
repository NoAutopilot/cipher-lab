#!/bin/sh
# SORT-A2o: JVN-GLY glyph sorter (5551 p3 L2: the glyph after 103, 140 vs 110, a blind check of the two 104 glyph tokens). No network.
#   sh ciphers/jan-van-nassau-1572-75/sorter/a2o/build.sh <out dir>
set -e
T=ciphers/jan-van-nassau-1572-75/sorter/a2o; OUT=${1:-.}
python3 $T/cut.py
python3 tools/sign_sorter.py --signs $T/signs.tsv --labels $T/labels.tsv --pages $T/pages \
  --title "Jan van Nassau 5551 Glyph Sorter" --out "$OUT/jvn_5551_gly_sorter.html" --data-out "$OUT/jvn_5551_gly_sorter.json" \
  --focus $T/focus.tsv \
  --focus-note "Signs from the one line of a 1574 letter in question: the glyph after the number 103, the digit in the middle of the group after 85/29, and the signs around 104 and 146. Make a pile for each distinct sign you see and move the tiles there; the whole-word crops (X1, X2, X4, X5, X6) are other words from the same page, for comparison." \
  --lede "A cipher letter from Jan van Nassau on page 3 of Huygens WVO 5551, line 2. Tiles are cut from detail crops of the page image. Starting piles are only groups of similar shapes, with no values. Sort by shape: is a tile a long-s, a looped long-s, the small c with a tail-h, a digit 1, a digit 4, or something else? Fix the cut if a box is wrong, or send it to BAD-CUT."
