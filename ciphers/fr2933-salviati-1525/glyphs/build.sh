#!/bin/sh
# Rebuild the fr.2933 Salviati glyph atlas from the images on disk (no fetches). Run from the target folder.
# crops/ and debug_*.jpg are regenerated working copies (not committed); clusters.tsv must reproduce the committed
# one exactly (fixed seed), else labels.json no longer refers to the same clusters.
set -e
T=../../tools/glyph_atlas.py
python3 $T segment $(cat glyphs/segment_args.txt) --out glyphs --mark-h 0.8 --debug
python3 $T cluster --out glyphs --k 64 --k-marks 20 --split s52:3 --split s3:2 --split s49:2 --split m10:2 \
  --split m12:2 --split s21:2 --split s45:2
python3 $T atlas --out glyphs --labels glyphs/labels.json --per 10 --prefer f54r
python3 -c "from PIL import Image; im=Image.open('glyphs/atlas.png'); w,h=im.size; half=(h//72//2)*72; im.crop((0,0,w,half)).save('glyphs/atlas_part1.png'); im.crop((0,half,w,h)).save('glyphs/atlas_part2.png')"
