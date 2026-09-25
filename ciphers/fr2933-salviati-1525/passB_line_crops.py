#!/usr/bin/env python3
"""Pass-B line crops for f56r lines 11-19: crop each line's bounding box (from f56r_boxes.tsv,
padded) from the native glyphs/crops/f56r.png and zoom 3x, so the whole line can be read at once
at higher resolution than the committed strips/ JPGs. Draws the integer pos number above each box
for alignment (geometry only, never the code/cluster_code columns -- pos numbers are not codes).
Writes passB_crops/f56r_L<line>_zoom.png.
"""
import csv, os
from PIL import Image, ImageDraw

ZOOM = 3
PAD = 15

boxes = {}
with open('f56r_boxes.tsv') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        line = int(r['line'])
        boxes.setdefault(line, []).append(
            (float(r['pos']), int(r['x']), int(r['y']), int(r['w']), int(r['h']))
        )
for line in boxes:
    boxes[line].sort(key=lambda t: t[0])

im = Image.open('glyphs/crops/f56r.png').convert('RGB')
W, H = im.size

os.makedirs('passB_crops', exist_ok=True)

for line in range(11, 20):
    bxs = boxes.get(line, [])
    if not bxs:
        continue
    x0 = min(b[1] for b in bxs) - PAD
    y0 = min(b[2] for b in bxs) - PAD
    x1 = max(b[1] + b[3] for b in bxs) + PAD
    y1 = max(b[2] + b[4] for b in bxs) + PAD
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(W, x1), min(H, y1)
    crop = im.crop((x0, y0, x1, y1))
    crop = crop.resize((crop.width * ZOOM, crop.height * ZOOM), Image.LANCZOS)
    draw = ImageDraw.Draw(crop)
    for pos, x, y, w, h in bxs:
        bx0 = (x - x0) * ZOOM
        by0 = (y - y0) * ZOOM
        bx1 = (x + w - x0) * ZOOM
        by1 = (y + h - y0) * ZOOM
        draw.rectangle([bx0, by0, bx1, by1], outline=(255, 0, 0), width=1)
        label = str(pos) if pos != int(pos) else str(int(pos))
        draw.text((bx0, max(0, by0 - 16)), label, fill=(255, 0, 0))
    crop.save(f'passB_crops/f56r_L{line}_zoom.png')
    print(line, crop.size)
