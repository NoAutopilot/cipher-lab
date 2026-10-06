#!/bin/sh
# Build the Rayburn sign-sorter page (no network, no vision model). Usage from the repo root:
#   sh ciphers/rayburn-2004/sorter/build.sh [out dir, default the sorter folder]
set -e
T=ciphers/rayburn-2004; OUT=${1:-$T/sorter}
python3 $T/sorter/build_inputs.py --write
python3 tools/sign_sorter.py --signs $T/sorter/signs.tsv --labels $T/sorter/labels.tsv --pages $T/sorter/pages \
  --title "Rayburn Sign Sorter" --out "$OUT/rayburn_sorter.html" \
  --focus $T/sorter/focus.tsv --cipher-lines $T/sorter/cipher_lines.tsv --thumb 120 \
  --focus-note "First, the 40 signs where the two blind machine readings of the sheet differ (R8-RAY2, 47% agreement): each question says what each reader saw. Margin signs may have been written with the sheet turned sideways." \
  --lede "The Rayburn sheet (2004; Schneier's 2006 image, byte-identical to ours), 80 signs: 10 written rows (64) and the two margin columns (8 + 8). Each tile is one sign with its own underline or strike-through and any small sign written just under it (k+r, A+m, R+H, a+v). Starting piles are the reconciled reading, capitals and small letters kept apart. Merge piles that are one sign, split a pile that holds two, move a tile to where it belongs, or send it to BAD-CUT / not a letter. The rectangle round rows 1-2 was drawn later by a family member and is left out; so are the vertical word beside the right margin and the circled mark below the grid."
