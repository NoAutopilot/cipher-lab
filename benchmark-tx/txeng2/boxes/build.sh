#!/bin/sh
# TXE2-BOXES (P1, 9 Oct 2026): regenerate the focus-tile boxes from the repo root (needs opencv-python-headless for the segment step).
#   sh benchmark-tx/txeng2/boxes/build.sh
set -e
B=benchmark-tx/txeng2/boxes; C=benchmark-tx/txeng/confirm/crops; T=${TMPDIR:-/tmp}/txe2_boxes_seg
args=""; for f in $C/p1c_L0*_s*.jpg $C/p2c_L0*_s*.jpg; do args="$args --page $(basename $f .jpg)=$f"; done
python3 tools/glyph_atlas.py segment $args --out $T --median-h 55
python3 $B/spin_join.py $T
python3 $B/build_boxes.py
