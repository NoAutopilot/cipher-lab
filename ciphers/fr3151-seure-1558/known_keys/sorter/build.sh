#!/bin/sh
# D1-SEURES (6 Oct 2026): Morvilliers 1549 cipher block sign sorter, BnF fr. 3138 fo. 66r (Gallica btv1b90601662 canvas 70).
# Usage from the repo root: sh ciphers/fr3151-seure-1558/known_keys/sorter/build.sh [OUT_DIR]
# Needs the region source (sh ciphers/fr3151-seure-1558/known_keys/regen_images.sh, its canvas-70 line: 1 IIIF request) and
# numpy pillow opencv-python-headless scikit-image scikit-learn. No network.
set -e
T=ciphers/fr3151-seure-1558/known_keys; OUT=${1:-$T/sorter/out}; W=$OUT/work; mkdir -p "$W"
python3 tools/glyph_atlas.py segment --page c70=$T/images/src_ark_12148_btv1b90601662_f70_4800_700_2950_2850.jpg --out "$W/atlas" --debug
python3 tools/glyph_atlas.py cluster --out "$W/atlas" --k 40 --k-marks 8
python3 $T/sorter/build_inputs.py "$W/atlas" "$W/in"
python3 tools/sign_sorter.py --signs "$W/in/signs.tsv" --labels "$W/in/labels.tsv" --pages "$W/in/pages" \
  --cipher-lines "$W/in/cipher_lines.tsv" --focus "$W/in/focus.tsv" \
  --tile-quality 75 --page-quality 55 \
  --title "Morvilliers 1549 Sign Sorter" --out "$OUT/morvilliers_fo66r_sorter.html" --data-out "$OUT/morvilliers_fo66r_sorter.json" \
  --focus-note "Signs from the piles named in the label pairs the two blind machine readers swapped most often (o/phi, d/f, ++/o, ++/=, ...). Pile names are only a starting guess." \
  --lede "BnF fr. 3138 fo. 66r, the cipher block of the Morvilliers 1549 letter (Gallica btv1b90601662, canvas 70), lines 3-22. Two blind machine readers disagreed on 78% of these signs, so nothing here is a reading yet. Tiles are cut by shape and piled into 40 shape groups; each pile is named after the label the readers most often gave at that place, a starting guess only. Clear words on the leaf (Neantmoins, Le S. Ascanio colonne est) are left out; lines 1-2, under a long ruled stroke, are not tiled yet. Some tiles (about a third in a 14-tile spot check) are pieces of long strokes or descenders from the line above: send those to BAD-CUT. Move each tile to the pile of the same sign, merge piles that are one sign, fix a bad box with Fix the cut, or send it to BAD-CUT."
