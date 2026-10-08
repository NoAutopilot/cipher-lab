#!/usr/bin/env python3
"""BERGH-STRIP: cut box-numbered window strips from the committed line crops (images/crops/p2_Lxx.jpg).

  python3 atlas/strips.py --gate            # one window per PREREG-BERGH-STRIP.md gate box -> atlas/strips/gate_NN.png + key
  python3 atlas/strips.py --line L06 ...    # whole-line strips (two halves per line) for the all-box pass

Every atlas box (atlas/signs.tsv) whose centre falls in the window is outlined and numbered with a window-local number; the
number -> sid key goes to atlas/strips/key.tsv, which readers never see. Numbers sit in a band under the strip, staggered in
three rows, with a leader line to the box. Width after the 2x upscale stays <= 2500 px.
"""
import argparse, csv, os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.dirname(HERE)
GATE = ['L15_01_013', 'L11_01_020', 'L12_01_044', 'L20_01_006', 'L02_01_038', 'L06_01_020', 'L06_01_004', 'L20_01_036',
        'L06_01_026', 'L07_01_009', 'L18_01_018', 'L22_01_007', 'L10_01_037', 'L14_01_018', 'L18_01_007', 'L15_01_031',
        'L21_01_015', 'L11_01_019', 'L08_01_026']
COLS = [(220, 20, 20), (20, 60, 220), (0, 150, 40), (170, 0, 170)]
SCALE, BAND = 2, 150


def boxes():
    with open(os.path.join(HERE, 'signs.tsv')) as f:
        return [dict(r, x=int(r['x']), y=int(r['y']), w=int(r['w']), h=int(r['h'])) for r in csv.DictReader(f, delimiter='\t')]


def font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf']:
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()


def strip(line, x0, x1, allb, name, keyrows):
    im = Image.open(os.path.join(FOLDER, 'images/crops', f'p2_{line}.jpg')).convert('RGB')
    x0, x1 = max(0, x0), min(im.width, x1)
    crop = im.crop((x0, 0, x1, im.height)).resize(((x1 - x0) * SCALE, im.height * SCALE), Image.LANCZOS)
    out = Image.new('RGB', (crop.width, crop.height + BAND), 'white'); out.paste(crop, (0, 0))
    d = ImageDraw.Draw(out); fnt = font(30)
    sel = sorted([b for b in allb if b['page'] == line and x0 <= b['x'] + b['w'] / 2 < x1], key=lambda b: b['x'] + b['w'] / 2)
    for i, b in enumerate(sel, 1):
        c = COLS[i % 4]
        bx, by = (b['x'] - x0) * SCALE, b['y'] * SCALE
        d.rectangle((bx, by, bx + b['w'] * SCALE, by + b['h'] * SCALE), outline=c, width=3)
        cx = bx + b['w'] * SCALE // 2; ty = crop.height + 6 + (i % 3) * 46
        d.line((cx, by + b['h'] * SCALE, cx, ty), fill=c, width=1)
        d.text((cx - 14, ty), str(i), fill=c, font=fnt)
        keyrows.append((name, i, b['sid']))
    out.save(os.path.join(HERE, 'strips', name + '.png'))
    return len(sel)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--gate', action='store_true'); ap.add_argument('--line', nargs='*', default=[])
    ap.add_argument('--half', type=int, default=640, help='window half-width for gate strips is half of this (px, line-crop scale)')
    a = ap.parse_args()
    allb = boxes(); byid = {b['sid']: b for b in allb}; keyrows = []
    os.makedirs(os.path.join(HERE, 'strips'), exist_ok=True)
    if a.gate:
        for n, sid in enumerate(GATE, 1):
            b = byid[sid]; c = b['x'] + b['w'] // 2
            k = strip(b['page'], c - a.half // 2, c + a.half // 2, allb, f'gate_{n:02d}', keyrows)
            print(f'gate_{n:02d} {sid} {k} boxes')
    for line in a.line:
        for h, (x0, x1) in enumerate([(0, 1040), (1010, 2050)], 1):
            k = strip(line, x0, x1, allb, f'{line}_h{h}', keyrows)
            print(f'{line}_h{h} {k} boxes')
    kp = os.path.join(HERE, 'strips', 'key.tsv')
    new = not os.path.exists(kp)
    with open(kp, 'a') as f:
        if new: f.write('strip\tnum\tsid\n')
        for r in keyrows: f.write('\t'.join(map(str, r)) + '\n')


if __name__ == '__main__':
    main()
