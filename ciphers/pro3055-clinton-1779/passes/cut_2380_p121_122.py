#!/usr/bin/env python3
"""Item 2380, B.147 pp.121-122 (H-1649 Images 759, 760, full/max): cut each cipher column into top/bottom halves
(120 px overlap), greyscale, autocontrast, q70 (R11-CLIN2380B, 6 Oct 2026). tools/iiif_lines.py --image ... found no
usable rows in a figure column (as on pp.120, 382-384), so the columns are PIL boxes read off a 100 px grid preview.
Usage: cut_2380_p121_122.py IMG_DIR OUT_DIR [IMAGE ...]  (IMG_DIR holds img759.jpg, img760.jpg from
https://image-uab.canadiana.ca/iiif/2/69429%2F{c02z12p3km4p,c0z60bw5z952}/full/max/0/default.jpg). Crops are not committed
(folder at the 30 MB line); the boxes below re-derive them."""
import os, sys
from PIL import Image, ImageOps
BOXES = {
    759: {'y': (660, 3400), 'cols': [(1900, 2105), (2095, 2300), (2290, 2500), (2490, 2690), (2680, 2875), (2865, 3065),
                                     (3060, 3270), (3260, 3520)]},
    760: {'y': (640, 3480), 'cols': [(1990, 2190), (2255, 2455), (2520, 2730), (2790, 2995), (3060, 3260), (3320, 3540)]},
    # 3853 cipher, B.147 p.406 (R15-CLIN3853, 6 Oct 2026; img1056.jpg from .../69429%2Fc0q52f84tj1f/full/max/0/default.jpg)
    1056: {'y': (900, 3250), 'cols': [(1525, 1825), (1825, 2105), (2100, 2315), (2310, 2530), (2525, 2775), (2750, 3010)]},
    # 3853 cipher continued, B.147 p.407 (R15-CLIN407, 6 Oct 2026; img1058.jpg from .../69429%2Fc0fn10p9j08z/full/max/0/default.jpg)
    1058: {'y': (520, 3100), 'cols': [(1510, 1770), (1760, 1990), (1990, 2215), (2220, 2450), (2450, 2730), (2720, 3000)]},
    # 25 Sept 1782 cipher copy, B.148 p.123 (D4-CLIN, 8 Oct 2026; img1205.jpg from .../69429%2Fc0ft8dg56944/full/max/0/default.jpg;
    # white ink on grey as filmed, read as is; run with SHEAR=0.012 PAD=0)
    1205: {'y': (720, 3800), 'cols': [(2330, 2660), (2640, 2930), (2900, 3200), (3130, 3460), (3420, 3760), (3700, 4120)]},
    # its continuation, B.148 p.124 (UNA-CLIN, 9 Oct 2026; img1206.jpg from .../69429%2Fc0b27pp7jj22/full/max/0/default.jpg; dark ink
    # as filmed). The columns fan out down the page (c1 ~0 px, c5 ~+150 px), which no single shear undoes, so this frame takes no
    # shear and its own boxes for the bottom half ('cols_bot'); column 6 holds only the clear words at its head.
    1206: {'y': (740, 3790), 'shear': 0.0,
           'cols': [(2400, 2650), (2640, 2900), (2860, 3170), (3140, 3420), (3420, 3720), (3700, 4000)],
           'cols_bot': [(2400, 2700), (2650, 2960), (2950, 3215), (3200, 3500), (3490, 3780), (3700, 4000)]},
}
LABEL = {1056: 406, 1058: 407, 1205: 123, 1206: 124}  # page label where it is not image - 638
STRETCH = {1205}  # low-contrast frames (white ink on grey as filmed): autocontrast each crop on its own
SHEAR = float(os.environ.get('SHEAR', '0.025'))  # 0 = the first cut (R11-CLIN2380B blind pass A read SHEAR=0 crops)
PAD = int(os.environ.get('PAD', '30'))  # widen each box by PAD px both sides (0 for pass A's crops)


def main(src, out, only=None):
    os.makedirs(out, exist_ok=True)
    for img, b in BOXES.items():
        if only and img not in only:
            continue
        im = ImageOps.autocontrast(Image.open(os.path.join(src, f'img{img}.jpg')).convert('L'), cutoff=1)
        y0, y1 = b['y']; mid = (y0 + y1) // 2
        shear = b.get('shear', SHEAR)
        if shear:  # the columns drift right down the page (about 50-90 px over the height); undo it before boxing
            im = im.transform(im.size, Image.AFFINE, (1, shear, -shear * y0, 0, 1, 0), resample=Image.BICUBIC, fillcolor=255)
        for k, (x0, x1) in enumerate(b['cols'], 1):
            for half, (a, z) in (('top', (y0, mid + 60)), ('bot', (mid - 60, y1))):
                if half == 'bot' and 'cols_bot' in b:
                    x0, x1 = b['cols_bot'][k - 1]
                c = im.crop((x0 - PAD, a, x1 + PAD, z))
                if img in STRETCH:
                    c = ImageOps.autocontrast(c, cutoff=2)
                c.save(os.path.join(out, f'p{LABEL.get(img, img - 638)}_c{k}_{half}.jpg'), quality=70)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], [int(a) for a in sys.argv[3:]])  # optional image numbers, e.g. 1056
