#!/bin/sh
# Rebuild the fr.5761 M36 (1519 election-embassy key) glyph atlas from the images on disk (no fetches).
# Run from the target folder (ciphers/fr5761-election-1519). crops/ and debug_*.jpg are regenerated working
# copies (not committed); clusters.tsv must reproduce the committed one exactly (fixed seed), else labels.json
# no longer refers to the same clusters.
set -e
T=../../tools/glyph_atlas.py
python3 $T segment $(cat glyphs/segment_args.txt) --out glyphs --mark-h 0.8 --debug
python3 $T cluster --out glyphs --k 60 --k-marks 16 \
  --split s19:9 --split s2:6 --split s32:3 --split s47:3 --split s50:4 --split s49:3 --split s35:2 \
  --split s19.5:3 --split s2.4:2 --split s32.2:2 --split s49.2:2 --split s50.0:2
python3 $T atlas --out glyphs --labels glyphs/labels.json --per 8 --prefer f104
python3 -c "from PIL import Image; im=Image.open('glyphs/atlas.png'); w,h=im.size; half=h//2; im.crop((0,0,w,half)).save('glyphs/atlas_part1.png'); im.crop((0,half,w,h)).save('glyphs/atlas_part2.png')"
