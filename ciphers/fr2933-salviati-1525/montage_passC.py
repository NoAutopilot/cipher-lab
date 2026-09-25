#!/usr/bin/env python3
"""Stack passC_crops/*.png into one labelled montage per line, so pass C can read a whole line's
disagreements in one image. Writes passC_crops/montage_L<line>.png."""
import csv
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont

rows = list(csv.DictReader(open('passC_crops/manifest.tsv'), delimiter='\t'))
by_line = defaultdict(list)
for r in rows:
    if r['file'] == 'NO_BOX_FOUND':
        continue
    by_line[int(r['line'])].append(r)

LABEL_H = 36
PAD = 8
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
except Exception:
    font = ImageFont.load_default()

for line, items in sorted(by_line.items()):
    items.sort(key=lambda r: float(r['pos']))
    imgs = [Image.open(r['file']) for r in items]
    maxw = max(im.width for im in imgs)
    total_h = sum(im.height + LABEL_H + PAD for im in imgs) + PAD
    canvas = Image.new('RGB', (maxw + 2 * PAD, total_h), 'white')
    draw = ImageDraw.Draw(canvas)
    y = PAD
    for r, im in zip(items, imgs):
        draw.text((PAD, y), f'line {r["line"]} pos {r["pos"]}', fill='red', font=font)
        y += LABEL_H
        canvas.paste(im, (PAD, y))
        y += im.height + PAD
    out = f'passC_crops/montage_L{line}.png'
    canvas.save(out)
    print(out, canvas.size)
