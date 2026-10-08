#!/usr/bin/env python3
"""D1A-D1411 placement aid: segment the number band (y0-y1) of a line crop into ink groups and draw them indexed.
  python3 d1a/bandseg.py OUT.jpg CROP:y0:y1 [...]   -> prints groups; writes the indexed sheet"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw
def groups(path, y0, y1, mingap=11):
    g = np.asarray(Image.open(path).convert("L"), dtype=float)[y0:y1]
    t = np.median(g) - 55
    col = (g < t).sum(0) >= 2
    out = []; x = 0; n = len(col)
    while x < n:
        if col[x]:
            s = x
            while x < n and col[x:x + mingap].any(): x += 1
            out.append((s, x))
        x += 1
    return [o for o in out if o[1] - o[0] >= 8]
if __name__ == "__main__":
    out = sys.argv[1]; rows = []; S = 0.6
    for a in sys.argv[2:]:
        c, y0, y1 = a.split(":"); y0, y1 = int(y0), int(y1)
        gs = groups(c, y0, y1); print(os.path.basename(c), [(i, a_, b) for i, (a_, b) in enumerate(gs)])
        im = Image.open(c).convert("RGB"); d0 = ImageDraw.Draw(im)
        for i, (p, q) in enumerate(gs):
            d0.rectangle([p, y0, q, y1], outline=(255, 0, 0) if i % 2 else (0, 0, 255), width=2)
        im = im.crop((0, max(0, y0 - 10), im.width, min(im.height, y1 + 10)))
        im = im.resize((int(im.width * S), int(im.height * S)))
        can = Image.new("RGB", (im.width, im.height + 26), "white"); can.paste(im, (0, 26)); d = ImageDraw.Draw(can)
        d.text((2, 0), os.path.basename(c), fill="black")
        for i, (p, q) in enumerate(gs): d.text((p * S, 12), str(i), fill=(255, 0, 0) if i % 2 else (0, 0, 255))
        rows.append(can)
    W = max(r.width for r in rows); sh = Image.new("RGB", (W, sum(r.height for r in rows)), "white"); y = 0
    for r in rows: sh.paste(r, (0, y)); y += r.height
    sh.save(out, quality=85)
