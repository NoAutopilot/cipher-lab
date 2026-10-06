#!/bin/sh
# R9-WVOSORT: rebuild the f.23 sorter inputs from the page image (run from the repo root).
set -e
D=ciphers/wvo-hessen-1564/sorter
(cd $D && python3 make_strips.py)
P=""; for i in 01 02 03 04 05 06 07 08 09 10; do P="$P --page f23_C$i=$D/pages/f23_C$i.png"; done
rm -rf $D/seg_raw $D/seg
python3 tools/glyph_atlas.py segment $P --out $D/seg_raw --merge-vgap 0.15
(cd $D && python3 make_seg_in.py)
P=""; for i in 01 02 03 04 05 06 07 08 09 10; do P="$P --page f23_C$i=$D/seg_in/f23_C$i.png"; done
python3 tools/glyph_atlas.py segment $P --out $D/seg --merge-vgap 0.15
(cd $D && python3 build_inputs.py)
