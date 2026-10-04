#!/usr/bin/env python3
"""N7-HEL86: cut one 3-row band per cell of R4386 (f.75) for cells.tsv and montage them into reading tiles
(adapted from ../key_r4388/crop_cells.py, N7-HELBC). Images are DECODE full-size pages kept in scratch (not committed):
--img DIR with IMG_R4386_I26206_P2.jpg / P3.jpg. Attribution (PREREG-N7HEL86 addendum A, from the full-size heads):
code 1000+n (n 201-1000) = the right-aligned entry LEFT of printed n (heads 120..190 sit over those entries).
Geometry read by eye from the full-size pages, 4 Oct 2026: printed-number x at row 1 / row 100 per column, row y at row 1 / row 100.
--debug CODES writes debug.png with those cells (layout check, before reading).
"""
import argparse, csv, os
from PIL import Image, ImageDraw, ImageFont
# column k (printed (100k+1)..(100k+100)): (page, x_row1, x_row100, y_row1, y_row100)
COL = {2: (2, 1800, 1800, 330, 5075), 3: (2, 2420, 2420, 330, 5075), 4: (2, 3040, 3040, 330, 5075),
       5: (2, 3660, 3660, 330, 5075), 6: (3, 912, 912, 320, 5080), 7: (3, 1532, 1532, 320, 5080),
       8: (3, 2160, 2160, 320, 5080), 9: (3, 2820, 2820, 320, 5080)}
W, H = 640, 150

def box(code):
    n = code - 1000; k = (n - 1) // 100; r = (n - 1) % 100 + 1
    p, xa, xb, ya, yb = COL[k]
    x = xa + (xb - xa) * (r - 1) / 99; y = ya + (yb - ya) * (r - 1) / 99
    return p, (int(x + 60 - W), int(y - H / 2), int(x + 60), int(y + H / 2)), n

def tile(cells, pages, path, label=True):
    font = ImageFont.load_default(); per = len(cells)
    sc = 0.62; cw, ch = int(W * sc), int(H * sc) + 16
    rows = (per + 1) // 2
    t = Image.new('RGB', (2 * cw + 10, rows * ch), 'white'); d = ImageDraw.Draw(t)
    for j, (o, code) in enumerate(cells):
        p, bx, n = box(code)
        im = pages[p].crop(bx).resize((cw, ch - 16)).convert('RGB')
        dd = ImageDraw.Draw(im); my = (ch - 16) // 2; ax = cw - 6
        dd.polygon([(ax, my - 5), (ax + 6, my), (ax, my + 5)], fill=(255, 0, 0))
        ox, oy = (j % 2) * (cw + 10), (j // 2) * ch
        d.text((ox + 2, oy + 2), f"#{o}  row {n}  LEFT of the number", fill=(0, 0, 200), font=font)
        t.paste(im, (ox, oy + 16)); d.rectangle([ox, oy, ox + cw - 1, oy + ch - 1], outline=(150, 150, 150))
    t.save(path)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--img', required=True); ap.add_argument('--out', required=True); ap.add_argument('--debug')
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    pages = {p: Image.open(os.path.join(a.img, f'IMG_R4386_I26206_P{p}.jpg')).convert('L') for p in (2, 3)}
    if a.debug:
        tile([(i, int(c)) for i, c in enumerate(a.debug.split(','))], pages, os.path.join(a.out, 'debug.png')); return
    cells = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cells.tsv')), delimiter='\t'))
    per = 16
    for t in range(0, len(cells), per):
        tile([(int(c['order']), int(c['code'])) for c in cells[t:t + per]], pages, os.path.join(a.out, f'tile_{t // per:02d}.png'))
    print('tiles', (len(cells) + per - 1) // per)

if __name__ == '__main__': main()
