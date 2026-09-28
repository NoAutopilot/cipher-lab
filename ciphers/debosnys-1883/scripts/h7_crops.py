#!/usr/bin/env python3
"""H7: per-box crops of the c4a0 band (the verse's first line) for the blind eye pass; same recipe as h2_crops.py."""
import csv, os, sys
from PIL import Image, ImageDraw
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
src = sys.argv[1]  # scratch signs.tsv holding the c4a0 rows
out = os.path.join(here, 'h7_crops'); os.makedirs(out, exist_ok=True)
bx0, by0 = 280, 372
page = Image.open(os.path.join(root, 'images/Debosnys-Cryptogram-4a.png')).convert('L')
rows = [r for r in csv.DictReader(open(src), delimiter='\t') if r['page'] == 'c4a0']
for r in rows:
    x, y, w, h = (int(r[k]) for k in 'xywh'); x += bx0; y += by0; pad = 6; name = f"c4a0_p{int(r['pos']):02d}"
    page.crop((x - pad, y - pad, x + w + pad, y + h + pad)).resize(((w + 2 * pad) * 6, (h + 2 * pad) * 6), Image.LANCZOS).save(os.path.join(out, name + '.png'))
    band = page.crop((bx0, by0 - 10, bx0 + 460, by0 + 74)).convert('RGB'); d = ImageDraw.Draw(band)
    d.rectangle((x - bx0 - 2, y - by0 + 10 - 2, x - bx0 + w + 2, y - by0 + 10 + h + 2), outline=(255, 0, 0), width=2)
    band.resize((band.width * 2, band.height * 2), Image.LANCZOS).save(os.path.join(out, 'ctx_' + name + '.png'))
print(len(rows), 'crops')
