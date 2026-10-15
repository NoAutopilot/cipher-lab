#!/usr/bin/env python3
"""C1161-HC (15 Oct 2026): render one line's pieces (images/<line>_s*.jpg), unstitched, stacked, each with an x ruler every 50 px
(labels every 100), for counting S positions by eye. No class, value or prior S result is drawn. Output goes to OUTDIR (scratchpad only).
  python3 shc/view_line.py OUTDIR LINE [LINE ...]   -> OUTDIR/<line>.jpg; prints the line's ciphertext.tsv sequence with S positions"""
import csv, glob, os, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 16)
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
CT = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
for line in sys.argv[2:]:
    ps = sorted(glob.glob(os.path.join(T, 'images', f'{line}_s*.jpg')))
    ims = [Image.open(p).convert('RGB') for p in ps]
    W = max(i.width for i in ims); Hh = sum(i.height + 40 for i in ims)
    M = Image.new('RGB', (W, Hh), 'white'); d = ImageDraw.Draw(M); y = 0
    for p, im in zip(ps, ims):
        d.text((4, y + 2), os.path.basename(p)[:-4][-2:], fill='blue', font=font)
        for x in range(0, im.width, 50):
            d.line((x, y + 22, x, y + 38), fill='green' if x % 100 else 'blue', width=1)
            if x % 100 == 0 and x: d.text((x + 2, y + 20), str(x), fill='blue', font=font)
        M.paste(im, (0, y + 40)); y += im.height + 40
    M.save(os.path.join(out, f'{line}.jpg'), quality=90)
    seq = [(r['pos'], r['sign']) for r in CT if r['line'] == line]
    print(line, ' '.join(f'{p}:{s}' for p, s in seq), '| S at', [p for p, s in seq if s == 'S'])
