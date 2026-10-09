#!/usr/bin/env python3
"""MANT-INV08 (9 Oct 2026): contact sheets for the Loc. 694/08 stride-4 frame inventory.
Usage: sheets.py FETCH.TSV IMGDIR OUTDIR [--seed 608]
FETCH.TSV rows: frame, kind (target|control), url. Controls on disk (images/loc694-08-09/694-08_NNNN.jpg) are added
as positives. Each sheet: 3x3 tiles of 800 px, film header (top 16%) cropped, one known-cipher and one known-clear
control planted, order shuffled; labels S<n>-<k>. Writes OUTDIR/sheetNN.jpg and OUTDIR/sheet_key.tsv (label -> frame, kind).
The key is never shown to the sheet reader."""
import csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont
fetch, imgdir, out = sys.argv[1:4]
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 608
here = os.path.dirname(os.path.abspath(__file__))
disk = os.path.join(here, '..', 'images', 'loc694-08-09')
rows = [r for r in csv.reader(open(fetch), delimiter='\t') if r]
targets = [r[0] for r in rows if r[1] == 'target']
pos = ['0065', '0485', '0005', '0510', '0511', '0579', '0580']   # code-bearing (seen_before.tsv code=y)
neg = ['0125', '0505', '0583']                                   # clear (seen_before.tsv code=n)
def path(fr):
    p = os.path.join(imgdir, fr + '.jpg')
    return p if os.path.exists(p) else os.path.join(disk, '694-08_%s.jpg' % fr)
rng = random.Random(seed)
order = targets[:]; rng.shuffle(order)
n = 14
groups = [order[i::n] for i in range(n)]
os.makedirs(out, exist_ok=True)
T = 800
try:
    font = ImageFont.load_default(size=26)
except TypeError:
    font = ImageFont.load_default()
key = open(os.path.join(out, 'sheet_key.tsv'), 'w')
key.write('sheet\tlabel\tframe\tkind\n')
for s, g in enumerate(groups, 1):
    items = [(f, 'target') for f in g] + [(pos[(s - 1) % len(pos)], 'control+'), (neg[(s - 1) % len(neg)], 'control-')]
    rng.shuffle(items)
    sheet = Image.new('L', (3 * T, 3 * T + 30 * 3), 255)
    d = ImageDraw.Draw(sheet)
    for k, (fr, kind) in enumerate(items):
        im = Image.open(path(fr)).convert('L')
        w, h = im.size
        im = im.crop((int(w * 0.03), int(h * 0.16), int(w * 0.97), h))
        im.thumbnail((T, T))
        x, y = (k % 3) * T, (k // 3) * (T + 30)
        lab = 'S%d-%d' % (s, k + 1)
        d.text((x + 10, y + 8), lab, fill=0, font=font)
        sheet.paste(im, (x, y + 30))
        key.write('%d\t%s\t%s\t%s\n' % (s, lab, fr, kind))
    sheet.save(os.path.join(out, 'sheet%02d.jpg' % s), quality=80)
key.close()
