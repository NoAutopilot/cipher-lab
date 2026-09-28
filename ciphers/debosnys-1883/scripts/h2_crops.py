#!/usr/bin/env python3
"""H2 (28 Sept 2026): cut per-sign crops for cryptogram 1's disputed positions and tile the inventory sheet.

Reads glyphs/signs.tsv (box x,y,w,h relative to glyphs/pages.json's c1 box), scripts/h2_disputed_positions.tsv,
images/Debosnys-Cryptogram-1.png. Writes scripts/h2_crops/<line>_p<pos>.png (6x Lanczos, 6 px pad),
scripts/h2_crops/ctx_<line>_p<pos>.png (row band, target box outlined in red, 2x) and scripts/h2_crops/inv_NN.png
(glyphs/inventory.png in 10-row tiles at 1.5x). Nothing here reads passA/passB.
"""
import csv, json, os
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
out = os.path.join(here, 'h2_crops'); os.makedirs(out, exist_ok=True)
pages = json.load(open(os.path.join(root, 'glyphs/pages.json')))
bx0, by0 = pages['c1']['box'][0], pages['c1']['box'][1]
page = Image.open(os.path.join(root, 'images', os.path.basename(pages['c1']['image']))).convert('L')
boxes = {(f"c1_L{int(r['line']):02d}", int(r['pos'])): r for r in csv.DictReader(open(os.path.join(root, 'glyphs/signs.tsv')), delimiter='\t') if r['page'] == 'c1'}
disp = [(r['line'], int(r['position'])) for r in csv.DictReader(open(os.path.join(here, 'h2_disputed_positions.tsv')), delimiter='\t')]
manifest = []
for line, pos in disp:
    r = boxes[(line, pos)]; x, y, w, h = (int(r[k]) for k in 'xywh'); x += bx0; y += by0
    pad = 6
    crop = page.crop((x - pad, y - pad, x + w + pad, y + h + pad)).resize(((w + 2 * pad) * 6, (h + 2 * pad) * 6), Image.LANCZOS)
    name = f"{line}_p{pos:02d}"; crop.save(os.path.join(out, name + '.png'))
    band = page.crop((bx0, max(0, y - 18), page.width, y + h + 18)).convert('RGB')
    d = ImageDraw.Draw(band); d.rectangle((x - bx0 - 2, y - max(0, y - 18) - 2, x - bx0 + w + 2, y - max(0, y - 18) + h + 2), outline=(255, 0, 0), width=2)
    band = band.resize((band.width * 2, band.height * 2), Image.LANCZOS); band.save(os.path.join(out, 'ctx_' + name + '.png'))
    manifest.append(dict(crop=name, line=line, position=pos, sid=r['sid'], box=[x, y, w, h]))
json.dump(manifest, open(os.path.join(out, 'manifest.json'), 'w'), indent=1)
inv = Image.open(os.path.join(root, 'glyphs/inventory.png')).convert('L'); rows = 10; rh = 64
tiles = []
for i in range(0, inv.height, rows * rh):
    t = inv.crop((0, i, inv.width, min(inv.height, i + rows * rh))); t = t.resize((int(t.width * 1.5), int(t.height * 1.5)), Image.LANCZOS)
    n = f"inv_{i // (rows * rh):02d}.png"; t.save(os.path.join(out, n)); tiles.append(n)
print(len(manifest), 'crops;', len(tiles), 'inventory tiles', inv.size)
