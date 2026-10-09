#!/usr/bin/env python3
"""MANT-INV08B (9 Oct 2026): contact sheets of 6 for the Loc. 694/08 stride-4 offset-2 inventory.
Usage: sheets_b.py FETCH_B.TSV IMGDIR OUTDIR [--seed 6082]
Same tile treatment as sheets.py (film header, top 16%, cropped; 3 columns), but 2 rows: 5 targets + 1 planted control per sheet,
code-bearing controls (images/loc694-08-09 on disk) on odd sheets, clear controls (fetched, kind control-) on even sheets, shuffled.
Writes OUTDIR/sheetNN.jpg and OUTDIR/sheet_key_b.tsv; the key is not read until every sheet is classified."""
import csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont
fetch, imgdir, out = sys.argv[1:4]
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 6082
here = os.path.dirname(os.path.abspath(__file__))
disk = os.path.join(here, '..', 'images', 'loc694-08-09')
rows = [r for r in csv.reader(open(fetch), delimiter='\t') if r]
targets = [r[0] for r in rows if r[1] == 'target']
neg = [r[0] for r in rows if r[1] == 'control-']
pos = ['0510', '0579', '0511', '0580']
def path(fr):
    p = os.path.join(imgdir, fr + '.jpg')
    return p if os.path.exists(p) else os.path.join(disk, '694-08_%s.jpg' % fr)
rng = random.Random(seed)
order = targets[:]; rng.shuffle(order)
n = (len(order) + 4) // 5
os.makedirs(out, exist_ok=True)
T = 760
try:
    font = ImageFont.load_default(size=30)
except TypeError:
    font = ImageFont.load_default()
key = open(os.path.join(out, 'sheet_key_b.tsv'), 'w')
key.write('sheet\tlabel\tframe\tkind\n')
for s in range(1, n + 1):
    g = order[(s - 1) * 5:s * 5]
    c = (pos[(s // 2) % len(pos)], 'control+') if s % 2 else (neg[(s // 2 - 1) % len(neg)], 'control-')
    items = [(f, 'target') for f in g] + [c]
    rng.shuffle(items)
    sheet = Image.new('L', (3 * T, 2 * (T + 34)), 255)
    d = ImageDraw.Draw(sheet)
    for k, (fr, kind) in enumerate(items):
        im = Image.open(path(fr)).convert('L')
        w, h = im.size
        im = im.crop((int(w * 0.03), int(h * 0.16), int(w * 0.97), h))
        im.thumbnail((T, T))
        x, y = (k % 3) * T, (k // 3) * (T + 34)
        lab = 'B%d-%d' % (s, k + 1)
        d.text((x + 10, y + 4), lab, fill=0, font=font)
        sheet.paste(im, (x, y + 34))
        key.write('%d\t%s\t%s\t%s\n' % (s, lab, fr, kind))
    sheet.save(os.path.join(out, 'sheet%02d.jpg' % s), quality=82)
key.close()
