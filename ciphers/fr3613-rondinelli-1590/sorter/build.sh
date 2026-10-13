#!/bin/sh
# BNF-RONDI-SORT: blind sign sorter for fr.3613 f.62r (cipher lines L01-L17). No network.
#   sh ciphers/fr3613-rondinelli-1590/sorter/build.sh <out dir>
set -e
T=ciphers/fr3613-rondinelli-1590/sorter; OUT=${1:-.}
python3 $T/cut.py
python3 tools/sign_sorter.py --signs $T/signs.tsv --labels $T/labels.tsv --pages $T/pages --region $T/region.json --cipher-lines $T/cipher_lines.tsv \
  --title "Rondinelli fr.3613 f.62r Sign Sorter" --out "$OUT/rondinelli_f62_sorter.html" --data-out "$OUT/rondinelli_f62_sorter.json" \
  --focus $T/focus.tsv \
  --focus-note "Start with the places where two blind machine readers wrote the page differently: letter-like forms (the same stroke read as g, y, h or a theta) and which sign carries the small figure above it. Make a pile for each distinct sign you see; vowel-like marks stay with their base sign." \
  --lede "fr.3613 f.62r, a cipher letter in a 1590 hand, 17 cipher lines. Tiles are cut from each sign's own ink on straight line strips. Starting piles are only groups of similar shapes, with no values. Sort by shape: move a tile to the pile it really belongs to, fix its box with Fix the cut, or send it to BAD-CUT."
