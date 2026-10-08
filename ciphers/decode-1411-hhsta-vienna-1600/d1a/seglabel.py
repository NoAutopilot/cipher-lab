#!/usr/bin/env python3
"""D1A-D1411 placement aid: draw segment.py groups with index labels on line crops, stacked.
  python3 d1a/seglabel.py OUT.jpg MINGAP CROP [CROP ...]"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from segment import groups
from PIL import Image, ImageDraw
out, mg, crops = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
S = 0.55; rows = []
for c in crops:
    im = Image.open(c).convert("RGB"); w, h = im.size; gs = groups(c, mg)
    d0 = ImageDraw.Draw(im)
    for i, (a, b) in enumerate(gs):
        d0.rectangle([a, int(h*.15), b, int(h*.85)], outline=(255, 0, 0) if i % 2 else (0, 0, 255), width=3)
    im = im.resize((int(w*S), int(h*S)))
    can = Image.new("RGB", (im.width, im.height + 22), "white"); can.paste(im, (0, 22)); d = ImageDraw.Draw(can)
    d.text((2, 0), os.path.basename(c), fill="black")
    for i, (a, b) in enumerate(gs):
        d.text((a*S+8*0, 10), str(i), fill=(255, 0, 0) if i % 2 else (0, 0, 255))
    rows.append(can)
W = max(r.width for r in rows); H = sum(r.height for r in rows)
sh = Image.new("RGB", (W, H), "white"); y = 0
for r in rows: sh.paste(r, (0, y)); y += r.height
sh.save(out, quality=85)
