#!/usr/bin/env python3
"""MANT-CENSUS (9 Oct 2026): contact sheets of 12 tiles for the Loc. 694/08 unseen frames (INV08D).
Usage: sheets_d.py FETCH_D.TSV IMGDIR OUTDIR [--seed 6084]
Each sheet = 10 targets + 1 code-bearing control (images/loc694-08-09 on disk: 0510/0511/0579/0580) + 1 clear control (kind control-,
fetched). Tile treatment as sheets_b.py (film header, top 16%, cropped), 4 columns x 3 rows, T=600 px. Order shuffled by seed.
Writes OUTDIR/sheetNN.jpg and OUTDIR/sheet_key_d.tsv; the key is not read until every sheet is classified."""
import csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont
fetch, imgdir, out = sys.argv[1:4]
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 6084
here = os.path.dirname(os.path.abspath(__file__))
disk = os.path.join(here, '..', 'images', 'loc694-08-09')
rows = [r for r in csv.reader(open(fetch), delimiter='\t') if r and r[0] != 'frame']
targets = [r[0] for r in rows if r[1] == 'target']
neg = [r[0] for r in rows if r[1] == 'control-']
pos = ['0510', '0579', '0511', '0580', '0510']
def path(fr):
    p = os.path.join(imgdir, fr + '.jpg')
    return p if os.path.exists(p) else os.path.join(disk, '694-08_%s.jpg' % fr)
rng = random.Random(seed)
n = (len(targets) + 9) // 10
os.makedirs(out, exist_ok=True)
T = 600
font = ImageFont.load_default(size=28)
key = open(os.path.join(out, 'sheet_key_d.tsv'), 'w')
key.write('sheet\tlabel\tframe\tkind\n')
for s in range(1, n + 1):
    g = targets[(s - 1) * 10:s * 10]
    items = [(f, 'target') for f in g] + [(pos[(s - 1) % len(pos)], 'control+'), (neg[0], 'control-')]
    rng.shuffle(items)
    sheet = Image.new('L', (4 * T, 3 * (T + 34)), 255)
    d = ImageDraw.Draw(sheet)
    for k, (fr, kind) in enumerate(items):
        im = Image.open(path(fr)).convert('L')
        w, h = im.size
        im = im.crop((int(w * 0.03), int(h * 0.16), int(w * 0.97), h))
        im.thumbnail((T, T))
        x, y = (k % 4) * T, (k // 4) * (T + 34)
        lab = 'D%d-%d' % (s, k + 1)
        d.text((x + 10, y + 4), lab, fill=0, font=font)
        sheet.paste(im, (x, y + 34))
        key.write('%d\t%s\t%s\t%s\n' % (s, lab, fr, kind))
    sheet.save(os.path.join(out, 'sheet%02d.jpg' % s), quality=82)
key.close()
