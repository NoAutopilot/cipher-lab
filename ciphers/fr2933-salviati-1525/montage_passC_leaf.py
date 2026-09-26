#!/usr/bin/env python3
"""(bSALC: any leaf, usage montage_passC_leaf.py <leaf>) Stack passC_crops/*.png into one labelled montage per line, so pass C can read a whole line's
disagreements in one image. Writes passC_crops/montage_L<line>.png."""
import csv, sys
LEAF = sys.argv[1]
from collections import defaultdict
from PIL import Image, ImageDraw, ImageFont

rows = list(csv.DictReader(open(f'passC_crops/{LEAF}/manifest.tsv'), delimiter='\t'))
by_line = defaultdict(list)
for r in rows:
    if r['file'] == 'NO_BOX_FOUND':
        continue
    by_line[int(r['line'])].append(r)

MAXH = 2200
LABEL_H = 36
PAD = 8
try:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 24)
except Exception:
    font = ImageFont.load_default()

def write(line, ci, items, n):
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
    out = f'passC_crops/{LEAF}/montage_L{line:02d}' + (f'_{ci+1}' if n > 1 else '') + '.png'
    canvas.save(out)
    print(out, canvas.size)

for line, items in sorted(by_line.items()):
    items.sort(key=lambda r: float(r['pos']))
    # bSALC: chunk a line into parts of at most MAXH px so no montage is too tall to read
    chunks, cur, h = [], [], 0
    for r in items:
        ih = Image.open(r['file']).height + LABEL_H + PAD
        if cur and h + ih > MAXH:
            chunks.append(cur); cur, h = [], 0
        cur.append(r); h += ih
    chunks.append(cur)
    for ci, items in enumerate(chunks):
        write(line, ci, items, len(chunks))

