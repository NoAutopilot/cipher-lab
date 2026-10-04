#!/bin/sh
# BIR87-SORTER (4 Oct 2026): build the no.87 mini sign sorter (README.md). Run from anywhere:
#   sh ciphers/nevers-birago-fr3251-1572/sorter/no87/build.sh OUT.html
# The account-3 orchestrator builds and publishes (capabilities {"db": {}}); workers do not publish.
set -eu
HERE=$(cd "$(dirname "$0")" && pwd); ROOT=$(cd "$HERE/../../../.." && pwd); OUT=${1:?usage: build.sh OUT.html}
python3 "$HERE/build_inputs.py"
python3 "$ROOT/tools/sign_sorter.py" --signs "$HERE/signs.tsv" --labels "$HERE/labels.tsv" \
  --pages "$ROOT/ciphers/nevers-birago-fr3251-1572/atlas/pages.json" --refs "$HERE/refs.tsv" --focus "$HERE/focus.tsv" \
  --tile-quality 80 --page-scale 0.5 --page-quality 70 \
  --title "Birago no.87 Sign Sorter" \
  --lede "Nevers-Birago no.87 (f.178r, f.178v, f.179r). The piles are YOUR piles from the 4 Oct sort; tiles with a green check are the ones you sorted then, shown as examples, and stay put. Every other tile is from no.87, placed by a computer in the pile whose examples it looks closest to. Take out what does not belong and place it. Start with the box at the top: tiles nearly as close to two of your piles." \
  --focus-note "Each of these no.87 tiles is about as close to two of your piles; the computer's pick is a guess." \
  --out "$OUT"
