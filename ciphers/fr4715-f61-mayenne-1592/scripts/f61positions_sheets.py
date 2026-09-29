#!/usr/bin/env python3
"""H253 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026): ruler copies of f.61's six read_call_A line sheets (images/f61sheet_L01/L03/L05/L07/L08/L11),
for a blind positional read: a red tick and number every 100 sheet px along the bottom of every segment band (segments split by the sheets' black
separator rows), written to <scratch>/h253/. The reader lists every cipher sign per segment left to right with its x (sheet px from the ruler) and marks
each clear handwritten word between signs; scored against read_call_A's order by f61positions_score.py. No letters.  python3 f61positions_sheets.py SCRATCH"""
import os, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); IM = os.path.abspath(f"{HERE}/../images")
def main(scratch):
    os.makedirs(f"{scratch}/h253", exist_ok=True)
    for L in ("L01", "L03", "L05", "L07", "L08", "L11"):
        im = Image.open(f"{IM}/f61sheet_{L}.jpg").convert("RGB"); g = im.convert("L"); W, H = im.size
        rows = [y for y in range(H) if sum(g.getpixel((x, y)) < 40 for x in range(0, W, 20)) > (W // 20) * 0.9]
        bands, y0 = [], 0
        for y in rows + [H]:
            if y - y0 > 40: bands.append((y0, y))
            y0 = y + 1
        c = Image.new("RGB", (W, H + 30 * len(bands)), "white"); d = ImageDraw.Draw(c); oy = 0
        for k, (a, b) in enumerate(bands, 1):
            c.paste(im.crop((0, a, W, b)), (0, oy)); yb = oy + (b - a)
            for x in range(0, W, 100):
                d.line([(x, yb), (x, yb + 12)], fill=(220, 0, 0), width=2); d.text((x + 2, yb + 13), str(x // 100), fill=(220, 0, 0))
            d.text((4, oy + 2), f"segment {k}", fill=(0, 0, 220)); oy = yb + 30
        c.crop((0, 0, W, oy)).resize((W // 2, oy // 2)).save(f"{scratch}/h253/{L}.jpg", quality=85); print(L, len(bands), "segments")
if __name__ == "__main__": main(sys.argv[1])
