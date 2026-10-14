#!/usr/bin/env python3
"""SALV-EYE (14 Oct 2026): in-context exemplar sheets for the SALV-MAP3 types, for a blind eye check against George Lasry's
key sheet. Disk only. The full page images are no longer on disk (folder shrink), so tiles are cut from:
  f54r -- the clean native line strips images/f54r_Lnn_s{1,2}.jpg (iiif_lines crops of the src image at offsets read from
          images_manifest_full.tsv), pasted back into the src frame; box coordinates are glyphs/pages.json's f54r crop frame;
  other leaves -- the numbered classify strips strips/<page>_Lnn[a-h].jpg (1600 px reference scans, box outlines drawn by
          glyph_atlas.py strips), with the strip origin recomputed by that function's own rule and checked against the drawn box.
A token is used only when its glyph-atlas box at the same page/line/pos is classified as the same BASE as transcribed
(double-attested). Up to PER tiles per type, f54r first. Writes lkey/eye/types_g{1,2}.png, his_part{1..3}.png, tiles.tsv."""
import csv, json, os, re, collections
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(D)); R = os.path.dirname(os.path.dirname(T))
GROUPS = {1: ['S^', 'Lx^', 'bh^', 'bh^dot', 'H^', 'ch^', 'a^dot', 'S7^+', 'm^1'],
          2: [']^o', 'sq^', 'sq^o', 'sq^~', 'L^', 'dl^', 'e^+', '#^', 'S4^']}
PER, CELL = 7, 110
PAGES = ['f54r', 'f54v', 'f55r', 'f55v', 'f56r', 'f56v', 'f57r', 'f57v']
bx, byline = {}, collections.defaultdict(list)
for pg in PAGES:
    for r in csv.DictReader(open(os.path.join(T, f'{pg}_boxes.tsv')), delimiter='\t'):
        for k in 'xywh': r[k] = int(float(r[k]))
        bx[(pg, r['line'], r['pos'])] = r; byline[(pg, int(r['line']))].append(r)
marks = collections.defaultdict(list)
for m in csv.DictReader(open(os.path.join(T, 'glyphs/marks.tsv')), delimiter='\t'):
    marks[(m['page'], int(m['line']))].append(int(float(m['y'])))
# f54r src frame from the native strips
src = Image.new('L', (4086, 5513), 255)
for line in open(os.path.join(T, 'images_manifest_full.tsv')):
    m = re.match(r'(images/f54r_L\d+_s\d\.jpg)\t.*box=\[(\d+), (\d+), (\d+), (\d+)\]', line)
    if m:
        x0, y0 = int(m.group(2)) - 4085, int(m.group(3))
        src.paste(Image.open(os.path.join(T, m.group(1))).convert('L'), (x0, y0))
f54r = src.crop(tuple(json.load(open(os.path.join(T, 'glyphs/pages.json')))['f54r']['box']))
def strip_origin(pg, li, b):
    bs = byline[(pg, li)]; ys = [c['y'] for c in bs] + marks[(pg, li)]
    y0 = max(0, min(ys) - 8); x0 = max(0, min(c['x'] for c in bs) - 10)
    names = sorted(f for f in os.listdir(os.path.join(T, 'strips')) if re.match(rf'{pg}_L{li:02d}[a-h]?\.jpg$', f))
    # strips split at box gaps; find the part whose x-range holds b (parts are cut at a box x - 4)
    acc = x0
    for n in names:
        im = Image.open(os.path.join(T, 'strips', n))
        if b['x'] < acc + im.size[0] or n == names[-1]:
            return im, acc, y0
        acc += im.size[0]
def tile(im, x, y, w, h):
    m = int(0.25 * max(w, h)); top = int(0.8 * max(w, h))
    sub = im.crop((max(0, x - m), max(0, y - top), x + w + m, y + h + m)).convert('L')
    sc = min((CELL - 6) / sub.size[0], (CELL - 6) / sub.size[1], 4.0)
    sub = sub.resize((max(1, int(sub.size[0] * sc)), max(1, int(sub.size[1] * sc))), Image.BICUBIC)
    t = Image.new('L', (CELL, CELL), 255); t.paste(sub, ((CELL - sub.size[0]) // 2, (CELL - sub.size[1]) // 2)); return t
toks = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(T, 'lkey/ciphertext_lasry.tsv')), delimiter='\t'):
    pg, l = r['line'].split('_L'); b = bx.get((pg, str(int(l)), r['src_pos']))
    if b is not None and b['code'] == r['sign'].split('^')[0]:
        toks[r['sign']].append((pg, int(l), b))
rows = []
for g, types in GROUPS.items():
    sheet = Image.new('L', (150 + PER * (CELL + 4), len(types) * (CELL + 6)), 255); dr = ImageDraw.Draw(sheet)
    for i, t in enumerate(types):
        cand = toks.get(t, []); by = {p: [c for c in cand if c[0] == p] for p in PAGES}; pick = []
        while len(pick) < PER and any(by.values()):
            for p in PAGES:
                if by[p] and len(pick) < PER: pick.append(by[p].pop(0))
        y = i * (CELL + 6); dr.text((6, y + CELL // 2 - 10), f'{t}', fill=0); dr.text((6, y + CELL // 2 + 6), f'n={len(cand)}', fill=0)
        for j, (pg, li, b) in enumerate(pick):
            if pg == 'f54r':
                tl = tile(f54r, b['x'], b['y'], b['w'], b['h'])
            else:
                im, ox, oy = strip_origin(pg, li, b); tl = tile(im, b['x'] - ox, b['y'] - oy, b['w'], b['h'])
            sheet.paste(tl, (150 + j * (CELL + 4), y)); rows.append([g, t, pg, li, b['pos'], b['box']])
    sheet.save(os.path.join(D, f'types_g{g}.png')); print(g, sheet.size)
with open(os.path.join(D, 'tiles.tsv'), 'w') as f:
    f.write('group\ttype\tpage\tline\tpos\tbox\n'); [f.write('\t'.join(map(str, r)) + '\n') for r in rows]
his = Image.open(os.path.join(R, 'sources/cyphersolver/2026-10-14-lasry/salviati1525/lasry_p031_1.png')).convert('L'); w, h = his.size
for i, (y0, y1) in enumerate([(0, int(h * 0.36)), (int(h * 0.30), int(h * 0.68)), (int(h * 0.62), h)], 1):
    p = his.crop((0, y0, w, y1)); p = p.resize((int(p.size[0] * 1.3), int(p.size[1] * 1.3)), Image.BICUBIC)
    p.save(os.path.join(D, f'his_part{i}.png')); print('his', i, p.size)
