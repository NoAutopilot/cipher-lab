#!/usr/bin/env python3
"""D1A-D1411 placement aid: stack line crops with an x ruler (ticks every 100 px of the crop) into one sheet.
  python3 d1a/ruler.py OUT.jpg CROP [CROP ...]"""
import sys
from PIL import Image, ImageDraw
out, crops = sys.argv[1], sys.argv[2:]
S = 0.55; rows = []
for c in crops:
    im = Image.open(c).convert("RGB"); w, h = im.size
    im = im.resize((int(w*S), int(h*S)))
    can = Image.new("RGB", (im.width, im.height + 34), "white"); can.paste(im, (0, 34)); d = ImageDraw.Draw(can)
    d.text((2, 0), c.split("/")[-1], fill="blue")
    for x in range(0, w, 100):
        d.line([(x*S, 22), (x*S, 34)], fill="red", width=2); d.text((x*S+2, 12), str(x//100), fill="red")
    rows.append(can)
W = max(r.width for r in rows); H = sum(r.height for r in rows)
sh = Image.new("RGB", (W, H), "white"); y = 0
for r in rows: sh.paste(r, (0, y)); y += r.height
sh.save(out, quality=85)
