#!/usr/bin/env python3
"""Item 2380, B.147 pp.121-122 (H-1649 Images 759, 760, full/max): cut each cipher column into top/bottom halves
(120 px overlap), greyscale, autocontrast, q70 (R11-CLIN2380B, 6 Oct 2026). tools/iiif_lines.py --image ... found no
usable rows in a figure column (as on pp.120, 382-384), so the columns are PIL boxes read off a 100 px grid preview.
Usage: cut_2380_p121_122.py IMG_DIR OUT_DIR  (IMG_DIR holds img759.jpg, img760.jpg from
https://image-uab.canadiana.ca/iiif/2/69429%2F{c02z12p3km4p,c0z60bw5z952}/full/max/0/default.jpg). Crops are not committed
(folder at the 30 MB line); the boxes below re-derive them."""
import os, sys
from PIL import Image, ImageOps
BOXES = {
    759: {'y': (660, 3400), 'cols': [(1900, 2105), (2095, 2300), (2290, 2500), (2490, 2690), (2680, 2875), (2865, 3065),
                                     (3060, 3270), (3260, 3520)]},
    760: {'y': (640, 3480), 'cols': [(1990, 2190), (2255, 2455), (2520, 2730), (2790, 2995), (3060, 3260), (3320, 3540)]},
}
def main(src, out):
    os.makedirs(out, exist_ok=True)
    for img, b in BOXES.items():
        im = ImageOps.autocontrast(Image.open(os.path.join(src, f'img{img}.jpg')).convert('L'), cutoff=1)
        y0, y1 = b['y']; mid = (y0 + y1) // 2
        for k, (x0, x1) in enumerate(b['cols'], 1):
            for half, (a, z) in (('top', (y0, mid + 60)), ('bot', (mid - 60, y1))):
                im.crop((x0, a, x1, z)).save(os.path.join(out, f'p{img - 638}_c{k}_{half}.jpg'), quality=70)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
