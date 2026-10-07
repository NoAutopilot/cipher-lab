#!/usr/bin/env python3
"""D4-MERC, 7 Oct 2026: shared-scale glyph sheet, f.151 strips beside Lasry's fr.15564 key image.
Disk only. Key image scaled x2.2, f.151 MERC151 crops (images/f151_L0*_s*.jpg) scaled x0.9, so a key glyph
(~19 px full height at 1x, row ink profile) and an f.151 sign body (~45 px, row ink profile) land at about the
same height (~40 px). The settled draft carries span/position but no pixel boxes, so per-label exemplar cuts are
not possible by script; the sheet shows each crop half with a 100-px ruler and the key's letter+nomenclator+unknown
rows on top of every tile. Writes sheet/tile_{1..4}.jpg (each <=1568 px long side, read unscaled) and sheet/sheet_full.jpg."""
from PIL import Image, ImageDraw
import glob, os
KS, FS = 2.2, 0.9
here = os.path.dirname(os.path.abspath(__file__))
key = Image.open(os.path.join(here, '../../sources/cryptiana/web/GL/GL_BnFfr15564.png')).convert('RGB')
key = key.resize((int(key.width*KS), int(key.height*KS)), Image.LANCZOS)
strips = []
for f in sorted(glob.glob(os.path.join(here, 'images/f151_L0*_s*.jpg'))):
    im = Image.open(f).convert('RGB'); w = im.width//2
    for h, box in (('a', (0, 0, w+60, im.height)), ('b', (w-60, 0, im.width, im.height))):
        s = im.crop(box); s = s.resize((int(s.width*FS), int(s.height*FS)), Image.LANCZOS)
        d = ImageDraw.Draw(s)
        for x in range(0, s.width, 100): d.line([(x, 0), (x, 8)], fill=(255, 0, 0), width=2); d.text((x+2, 8), str(x), fill=(255, 0, 0))
        d.text((s.width-160, s.height-14), os.path.basename(f)[5:12]+h, fill=(0, 0, 255))
        strips.append(s)
W = max(key.width, max(s.width for s in strips))
def stack(parts):
    out = Image.new('RGB', (W, sum(p.height for p in parts)+4*len(parts)), 'white'); y = 0
    for p in parts: out.paste(p, (0, y)); y += p.height+4
    return out
os.makedirs(os.path.join(here, 'sheet'), exist_ok=True)
for i in range(4):
    stack([key]+strips[i*3:(i+1)*3]).save(os.path.join(here, f'sheet/tile_{i+1}.jpg'), quality=85)
stack([key]+strips).save(os.path.join(here, 'sheet/sheet_full.jpg'), quality=85)
