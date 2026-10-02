#!/usr/bin/env python3
"""make_sheet.py -- GAPS14 (2 Oct 2026): value-blind tile sheet of gloss-hand letters for the code-36 c/e letterform test.
Boxes (tiles_boxes.tsv, native px of images/NL-HaNA_1.02.04_63_0001.jpg) were set by eye on ruled zoom strips over the
gloss letter standing above each named group: the 4 code-36 occurrences, the 2 C-graded c tokens (code 14) and 8 C-graded
e tokens (codes 60, 38, 5, 16, 10). Each tile is a fixed 56x48 px window centred on its box, upscaled 3x, numbered 1-14 in
a seeded random order; no line, position, code or value is printed. The number -> id key is written to --keyout, which
stays outside the repository until both blind passes and the reconciliation are in (then copied to tile_key.tsv).
Usage: python3 make_sheet.py --out SHEET.jpg --keyout KEY.tsv [--seed 14]
"""
import argparse, csv, os, random
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(H))
ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); ap.add_argument('--keyout', required=True)
ap.add_argument('--seed', type=int, default=14); a = ap.parse_args()
im = Image.open(os.path.join(T, 'images/NL-HaNA_1.02.04_63_0001.jpg')).convert('RGB')
rows = list(csv.DictReader(open(os.path.join(H, 'tiles_boxes.tsv')), delimiter='\t'))
random.Random(a.seed).shuffle(rows)
W, Hh, S = 56, 48, 3; cols = 5; pad = 30
sheet = Image.new('RGB', (cols * (W * S + 20), ((len(rows) + cols - 1) // cols) * (Hh * S + pad + 10)), 'white')
d = ImageDraw.Draw(sheet)
with open(a.keyout, 'w') as k:
    k.write('tile\tid\n')
    for n, r in enumerate(rows, 1):
        cx = (int(r['x0']) + int(r['x1'])) // 2; cy = (int(r['y0']) + int(r['y1'])) // 2
        t = im.crop((cx - W // 2, cy - Hh // 2, cx + W // 2, cy + Hh // 2)).resize((W * S, Hh * S), Image.LANCZOS)
        X = ((n - 1) % cols) * (W * S + 20); Y = ((n - 1) // cols) * (Hh * S + pad + 10)
        sheet.paste(t, (X, Y + pad)); d.text((X + 4, Y + 8), 'tile %d' % n, fill=(0, 0, 0))
        k.write('%d\t%s\n' % (n, r['id']))
sheet.save(a.out, quality=92); print('tiles', len(rows), '->', a.out)
