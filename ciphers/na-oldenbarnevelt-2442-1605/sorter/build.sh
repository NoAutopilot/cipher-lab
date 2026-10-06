#!/bin/sh
# Build the blocks A/C2 sign-sorter page (no network). Usage from the repo root:
#   sh ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh <out dir>
set -e
T=ciphers/na-oldenbarnevelt-2442-1605; OUT=${1:-.}
python3 $T/sorter/recut.py      # R7-OLDFIX re-cut (build_inputs.py was the R7-OLDSORT v1 cut)
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --title "Oldenbarnevelt 2442 Sign Sorter" --out "$OUT/oldenbarnevelt_AC2_sorter.html" --data-out "$OUT/oldenbarnevelt_AC2_sorter.json" \
  --focus $T/sorter/focus.tsv --region $T/sorter/region.json \
  --focus-note "Signs the two blind machine readers wrote differently (vowel-letter/digit notation folded first): the look-alike pairs v/r and the G-shaped ligature (l/c/b) first, then d/8, 5/s, p/g/l, c/t, m/n/r, then the other splits, then tiles that no draft sign lined up with (started by shape)." \
  --lede "Nationaal Archief 1.01.02 inv. 2442, blocks A (folio 54) and C2 (folio 56), cipher text only (the clear opening of A line 1 is not tiled). Tiles are cut from each sign's own ink on deskewed line strips (R7-OLDFIX re-cut, 6 Oct 2026); starting piles are R7-OLDA's reconciled draft labels (a draft: 36 of 165 words uncertain) where a tile lines up with a draft sign, else the pile its shape cluster mostly holds. Move a tile to the pile it really belongs to, fix its box with Fix the cut, or send it to BAD-CUT." \
  --auto-clusters 3
