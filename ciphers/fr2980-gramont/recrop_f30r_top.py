#!/usr/bin/env python3
"""Evidence crops for the f.30r top-lines re-read (24 Sept 2026), from disk only.

The committed line-half crops (images/crops_f30/, native resolution) are pasted back at their page
coordinates (crops/crops.json; b halves start at splits.json - 8) into one mosaic of f.30r L01-L13, so a
sign that straddles the a/b seam can be seen whole. Each evidence crop in CROPS is cut from that mosaic in
page pixels of the f32 region (4004x5566), contrast-stretched, magnified and given a page-x ruler.
Writes crops/f30r_top/<name>.jpg. No network.  Usage: python3 recrop_f30r_top.py
"""
import json, os
from PIL import Image, ImageOps, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'crops', 'f30r_top')
X0, Y0, X1, Y1 = 500, 450, 3600, 2050
# name: (x0, y0, x1, y1, magnification), page pixels
CROPS = {
    'L01_z3':      (1280, 540, 1600, 690, 3),
    'L02_INF':     (560, 680, 800, 830, 4),
    'L02_seam_B8': (1720, 670, 2020, 800, 4),
    'L03_CROSS':   (3250, 740, 3420, 880, 4),
    'L04_br10':    (1340, 900, 1560, 1010, 5),
    'L04_br33':    (2990, 850, 3140, 960, 5),
    'L07_CROSS':   (820, 1250, 940, 1360, 5),
    'L07_A2_tail': (2270, 1170, 2480, 1310, 4),
    'L07_q':       (3020, 1190, 3140, 1340, 5),
    'L07_lam':     (2040, 1180, 2220, 1320, 4),
    'L08_blot':    (1760, 1330, 2400, 1510, 2),
    'L08_seam':    (1780, 1340, 1990, 1490, 4),
    'L08_b':       (2360, 1280, 3200, 1420, 2),
    'L11_CROSS':   (780, 1680, 900, 1830, 4),
    'L11_zb':      (2720, 1640, 2880, 1760, 5),
    'L12_lz':      (560, 1820, 900, 1960, 3),
    'L12_seam_mx': (1760, 1760, 1960, 1900, 4),
}

def mosaic():
    c = json.load(open(os.path.join(HERE, 'crops', 'crops.json')))
    sp = json.load(open(os.path.join(HERE, 'crops', 'splits.json')))
    M = Image.new('L', (X1 - X0, Y1 - Y0), 235)
    for i in range(1, 14):
        L = f'f30r_L{i:02d}'
        for h, x in (('a', c[L]['a'][0]), ('b', sp[L] - 8)):
            im = Image.open(os.path.join(HERE, 'images', 'crops_f30', f'{L}{h}.jpg')).convert('L')
            M.paste(im, (x - X0, c[L][h][1] - Y0))
    return M

def main():
    os.makedirs(OUT, exist_ok=True)
    M = mosaic()
    for n, (x0, y0, x1, y1, k) in CROPS.items():
        p = ImageOps.autocontrast(M.crop((x0 - X0, y0 - Y0, x1 - X0, y1 - Y0)), cutoff=1)
        p = p.resize(((x1 - x0) * k, (y1 - y0) * k), Image.LANCZOS)
        cv = Image.new('L', (p.width, p.height + 22), 255); cv.paste(p, (0, 22)); d = ImageDraw.Draw(cv)
        step = 25 if k >= 3 else 50
        for x in range((x0 // step + 1) * step, x1, step):
            X = (x - x0) * k; d.line((X, 12, X, 22), fill=0); d.text((X + 2, 1), str(x), fill=0)
        cv.save(os.path.join(OUT, n + '.jpg'), quality=80)
    print(len(CROPS), 'crops in', OUT)

if __name__ == '__main__':
    main()
