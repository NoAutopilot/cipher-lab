#!/usr/bin/env python3
"""N7-HELBC: cut one 3-row band per cell of R4388 (f.79) for cells.tsv and montage them into reading tiles.
Images are DECODE full-size pages kept in scratch (not committed): --img DIR with IMG_R4388_I26220_P2.jpg / P3.jpg.
Geometry (read by eye from the full-size pages, 4 Oct 2026): printed-number x at row 1 / row 100 per column; rows
y = 316 + (r-1)*47.7. Code 2000+n = entry RIGHT of printed n; 3000+n (n 101-900) = entry LEFT of printed n; 3001-3100 = strip (P3).
"""
import argparse, csv, os
from PIL import Image, ImageDraw, ImageFont
# column k (printed (100k+1)..(100k+100)): (page, x_row1, x_row100)
COL = {0: (2, 230, 280), 1: (2, 820, 856), 2: (2, 1400, 1444), 3: (2, 1990, 2044), 4: (2, 2580, 2624),
       5: (2, 3160, 3200), 6: (3, 570, 610), 7: (3, 1150, 1200), 8: (3, 1740, 1800), 9: (3, 2330, 2380)}
COL5_P3 = (3, 10, 20)  # right-hand entries of 501-600 are on P3's left edge
STRIP = (3, 2960, 3060, 310, 46.4)
W, H = 640, 150

def box(code):
    if 3001 <= code <= 3100:
        p, xa, xb, y1, dy = STRIP; r = code - 3000
        x = xa + (xb - xa) * (r - 1) / 99; y = y1 + (r - 1) * dy
        return p, (int(x - 60), int(y - H / 2), int(x - 60 + W), int(y + H / 2)), r, 'R'
    if code <= 3000: n, side = code - 2000, 'R'
    else: n, side = code - 3000, 'L'
    k = (n - 1) // 100; r = (n - 1) % 100 + 1
    p, xa, xb = COL5_P3 if (k == 5 and side == 'R') else COL[k]
    x = xa + (xb - xa) * (r - 1) / 99; y = 316 + (r - 1) * 47.7
    if side == 'R': bx = (int(x - 60), int(y - H / 2), int(x - 60 + W), int(y + H / 2))
    else: bx = (int(x + 90 - W), int(y - H / 2), int(x + 90), int(y + H / 2))
    return p, bx, n, side

def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('--img', required=True); ap.add_argument('--out', required=True)
    a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
    pages = {p: Image.open(os.path.join(a.img, f'IMG_R4388_I26220_P{p}.jpg')).convert('L') for p in (2, 3)}
    cells = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cells.tsv')), delimiter='\t'))
    font = ImageFont.load_default()
    per = 16; sc = 0.62; cw, ch = int(W * sc), int(H * sc) + 16
    for t in range(0, len(cells), per):
        tile = Image.new('RGB', (2 * cw + 10, 8 * ch), 'white'); d = ImageDraw.Draw(tile)
        for j, c in enumerate(cells[t:t + per]):
            p, bx, n, side = box(int(c['code']))
            im = pages[p].crop(bx).resize((cw, ch - 16)).convert('RGB')
            dd = ImageDraw.Draw(im); my = (ch - 16) // 2
            ax = 0 if side == 'R' else cw - 6
            dd.polygon([(ax, my - 5), (ax + 6, my), (ax, my + 5)], fill=(255, 0, 0))
            ox, oy = (j % 2) * (cw + 10), (j // 2) * ch
            d.text((ox + 2, oy + 2), f"#{c['order']}  row {n}  {'RIGHT' if side == 'R' else 'LEFT'} of the number", fill=(0, 0, 200), font=font)
            tile.paste(im, (ox, oy + 16)); d.rectangle([ox, oy, ox + cw - 1, oy + ch - 1], outline=(150, 150, 150))
        tile.save(os.path.join(a.out, f'tile_{t // per:02d}.png'))
    print('tiles', (len(cells) + per - 1) // per)

if __name__ == '__main__': main()
