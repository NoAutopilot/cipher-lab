#!/bin/sh
# MARKS-DEV2: regenerate candidates from the repo root (read-free); then score.py (the only step that opens the dev2 truth).
set -e
T=${TMPDIR:-/tmp}/marks_seg; I=ciphers/fr16104-vivonne-spain-1572/images
args=""; for i in $(seq -w 1 37); do for s in 1 2; do args="$args --page c105_f102r_L${i}_s$s=$I/c105_f102r_L${i}_s$s.jpg"; done; done
python3 tools/glyph_atlas.py segment $args --out $T > /dev/null
python3 benchmark-tx/txeng2/marks/rule.py $T
