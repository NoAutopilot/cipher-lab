#!/usr/bin/env python3
"""MANT-Y49 crop sheets: pack the known-subset strips (shuffled, seed 49) at native scale onto sheets <= 1340x1500,
labelled S01..; one probe sheet (0063 slots, fix19 slots at 2x) labelled P01... Writes y49/sheets/*.jpg and
y49/sheets/strips.tsv (label, sheet, source crop, leaf)."""
import csv, os, random
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'sheets'); os.makedirs(OUT, exist_ok=True)
DIRS = {'0089': 'f0089_08', '0136': 'f0136_08', '0309': 'f0309_08', '0312': 'f0312_08', '0314': 'f0314_08',
        '0317': 'f0317_08', '0474': 'f0474_08', '0490': 'f0490_08', '0490L': 'f0490_08', '0494': 'f0494_08'}
rows = list(csv.DictReader(open(os.path.join(HERE, 'known.tsv')), delimiter='\t'))
strips = sorted({(r['leaf'], r['crop']) for r in rows})
random.Random(49).shuffle(strips)
items = [('S%02d' % (i + 1), os.path.join(DIRS[l], 'crops', c + '.jpg'), l) for i, (l, c) in enumerate(strips)]
probes = [('P%02d' % (i + 1), p, l) for i, (p, l) in enumerate(
    [('f0063_09/crops/slot0%d.jpg' % k, '0063') for k in (1, 2, 3, 4)] +
    [('mant0608/fix19/%s' % f, f[1:5]) for f in ('x0398s02p17_L01.jpg', 'x0410s02p3_L01.jpg', 'x0410s02p8_L01.jpg')])]
W, H, LAB, GAP = 1300, 1500, 34, 14
def pack(its, scale, name0):
    sheets, cur, y, x, rowh = [], [], 0, 0, 0
    for lab, p, l in its:
        im = Image.open(os.path.join(ROOT, p)).convert('RGB')
        if scale != 1: im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
        w, h = im.width + 70, im.height + LAB
        if x + w > W: y += rowh + GAP; x, rowh = 0, 0
        if y + h > H: sheets.append(cur); cur, y, x, rowh = [], 0, 0, 0
        cur.append((lab, p, l, im, x, y)); x += w + GAP; rowh = max(rowh, h)
    if cur: sheets.append(cur)
    out = []
    for k, sh in enumerate(sheets):
        hh = max(y + im.height + LAB for _, _, _, im, _, y in sh) + 10
        ww = max(x + im.width + 70 for _, _, _, im, x, _ in sh) + 10
        S = Image.new('RGB', (ww, hh), 'white'); d = ImageDraw.Draw(S)
        for lab, p, l, im, x, y in sh:
            d.text((x + 2, y + 4), lab, fill='black', font_size=26); d.rectangle([x, y, x + im.width + 69, y + im.height + LAB - 1], outline='gray')
            S.paste(im, (x + 66, y + LAB - 4))
        fn = '%s%d.jpg' % (name0, k + 1); S.save(os.path.join(OUT, fn), quality=92); out.append((fn, sh))
    return out
res = pack(items, 1, 'sheet') + pack(probes, 2, 'probe')
with open(os.path.join(OUT, 'strips.tsv'), 'w') as f:
    f.write('label\tsheet\tsource\tleaf\n')
    for fn, sh in res:
        for lab, p, l, im, x, y in sh: f.write('%s\t%s\t%s\t%s\n' % (lab, fn, p, l))
for fn, sh in res: print(fn, len(sh), Image.open(os.path.join(OUT, fn)).size)
