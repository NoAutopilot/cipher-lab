#!/usr/bin/env python3
"""Cut the item-2380 crops (Clinton to Haldimand, New York, 22 Oct 1779; BL Add MS 21807 = Brymner B.147) from the
H-1649 full/max frames (GAPS9-pro3055-clinton-1779, 2 Oct 2026):

  Image 772 (p.134, iiif c0d50fv71q4k, 5904x4056)  the period decipherment, lines 1-36  -> images/h1649/p134_lines/
  Image 773 (p.135, iiif c08g8fg27397, 5928x4056)  its last lines + endorsement         -> images/h1649/p135_lines/
  Image 758 (p.120, iiif c06m3328d73r, 6032x4056)  cipher columns 1-2, top/bottom halves -> images/h1649/p120_cols/

The line boxes are tools/iiif_lines.py's own (run --image <frame> --region 2180,620,1900,3380 --ink 45 for p.134 and
--region 2100,620,2000,1560 --ink 45 for p.135; boxes in each folder's manifest.json). To keep the folder under 29 MB
each line crop is then trimmed horizontally to its ink extent (+-40 px; columns with more than 2 pixels darker than 70),
scaled 0.8 (LANCZOS), greyscale, JPEG q50. Column crops: greyscale, the boxes in p120_cols/manifest.json, q45.

Frames are read from CLINTON_H1649_DIR (regen_images.sh sets it; files img772_max.jpg, img773_max.jpg,
img758_max.jpg); output goes to OUT_DIR (default: the folder's images/h1649). Deterministic: the same frame gives the
same bytes.
"""
import json, os
import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
H = os.path.join(ROOT, '..', 'images', 'h1649')
SRC = os.environ.get('CLINTON_H1649_DIR', H)
OUT = os.environ.get('OUT_DIR', H)


def line_crops(frame, sub):
    im = Image.open(os.path.join(SRC, frame)).convert('L')
    os.makedirs(os.path.join(OUT, sub), exist_ok=True)
    for e in json.load(open(os.path.join(H, sub, 'manifest.json')))['iiif_lines']:
        c = im.crop(tuple(e['box']))
        a = np.asarray(c)
        cols = np.where((a < 70).sum(0) > 2)[0]
        x0, x1 = max(0, int(cols.min()) - 40), min(a.shape[1], int(cols.max()) + 40)
        c = c.crop((x0, 0, x1, c.height))
        c = c.resize((round(c.width * 0.8), round(c.height * 0.8)), Image.LANCZOS)
        c.save(os.path.join(OUT, sub, e['crop']), 'JPEG', quality=50)


def col_crops():
    m = json.load(open(os.path.join(H, 'p120_cols', 'manifest.json')))
    im = Image.open(os.path.join(SRC, 'img758_max.jpg')).convert('L')
    os.makedirs(os.path.join(OUT, 'p120_cols'), exist_ok=True)
    for k, b in m['boxes'].items():
        im.crop(tuple(b)).save(os.path.join(OUT, 'p120_cols', k + '.jpg'), 'JPEG', quality=45)


if __name__ == '__main__':
    line_crops('img772_max.jpg', 'p134_lines')
    line_crops('img773_max.jpg', 'p135_lines')
    col_crops()
    print('cut_2380_crops: wrote p134_lines, p135_lines, p120_cols into', OUT)
