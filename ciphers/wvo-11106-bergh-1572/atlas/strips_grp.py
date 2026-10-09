#!/usr/bin/env python3
"""BERGH-GRP: de-stacked box-numbered window strips for sign-GROUP reads (the second instrument after BERGH-STRIP).

  python3 atlas/strips_grp.py            # one window per gate box (same 19 windows as atlas/strips.py --gate)
                                         # -> atlas/strips_grp/gate_NN.png + atlas/strips_grp/key.tsv
  python3 atlas/strips_grp.py --line L01 L02 ...   # BERGH-ALL1 (9 Oct 2026): whole-line strips, two halves per line, same
                                         # layout -> atlas/strips_all/Lxx_h1.png, Lxx_h2.png + atlas/strips_all/key.tsv
                                         # halves shown as x 0-1040 / 1010-2050 (atlas/strips.py --line), but each box is
                                         # numbered in one half only (centre < 1025 -> h1), so every box gets exactly one number

Differences from atlas/strips.py (whose stacked leader lines let a reader take a neighbour's number, BERGH-STRIP gate_09):
- the window is drawn twice: a clean copy on top (ink unobscured), the outlined copy below it;
- no leader lines at all: under the outlined copy each box gets a horizontal bar spanning exactly its own x-range, in the
  box's own colour, with its number centred directly under the bar; bars are packed into rows so no two bars/numbers in a
  row overlap, so two boxes sharing an x-range land in different rows;
- when a box's centre is within 20 px (2x scale) of an earlier box's centre, its number is offset sideways by one number
  width, so two stacked boxes never put their numbers on the same vertical;
- six colours, cycled in centre order.
Same window, same boxes (atlas/signs.tsv, centre in window), same number order as atlas/strips.py, so the number -> sid key
is identical to atlas/strips/key.tsv (checked by --check-key). The readers never see the key.
"""
import argparse, csv, os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from strips import GATE, HERE, FOLDER, SCALE, boxes, font  # noqa: E402

COLS = [(220, 20, 20), (20, 60, 220), (0, 140, 40), (170, 0, 170), (230, 120, 0), (0, 150, 160)]
ROWH, PAD = 58, 10
OUT = os.path.join(HERE, 'strips_grp')


def strip(line, x0, x1, allb, name, keyrows, out_dir=OUT, sel_range=None):
    im = Image.open(os.path.join(FOLDER, 'images/crops', f'p2_{line}.jpg')).convert('RGB')
    x0, x1 = max(0, x0), min(im.width, x1)
    crop = im.crop((x0, 0, x1, im.height)).resize(((x1 - x0) * SCALE, im.height * SCALE), Image.LANCZOS)
    s0, s1 = sel_range or (x0, x1)
    sel = sorted([b for b in allb if b['page'] == line and s0 <= b['x'] + b['w'] / 2 < s1], key=lambda b: b['x'] + b['w'] / 2)
    fnt = font(28)
    # place each bar+number in the first row where it does not overlap anything already there
    rows, place, centres = [], [], []
    for i, b in enumerate(sel, 1):
        bx0, bx1 = (b['x'] - x0) * SCALE, (b['x'] + b['w'] - x0) * SCALE
        cx = (bx0 + bx1) // 2
        tw = 18 * len(str(i))
        shift = 0
        if any(abs(cx - c) < 20 for c in centres):
            shift = tw + 6 if (i % 2) else -(tw + 6)
        centres.append(cx)
        tx0 = cx + shift - tw // 2
        lo, hi = min(bx0, tx0) - PAD, max(bx1, tx0 + tw) + PAD
        r = 0
        while r < len(rows) and any(not (hi <= a or lo >= z) for a, z in rows[r]):
            r += 1
        if r == len(rows):
            rows.append([])
        rows[r].append((lo, hi))
        place.append((i, b, bx0, bx1, tx0, r))
    band = ROWH * max(1, len(rows)) + 10
    H = crop.height
    out = Image.new('RGB', (crop.width, 2 * H + 12 + band), 'white')
    out.paste(crop, (0, 0)); out.paste(crop, (0, H + 12))
    d = ImageDraw.Draw(out)
    d.line((0, H + 5, crop.width, H + 5), fill=(160, 160, 160), width=2)
    for i, b, bx0, bx1, tx0, r in place:
        c = COLS[(i - 1) % len(COLS)]
        by = H + 12 + b['y'] * SCALE
        d.rectangle((bx0, by, bx1, by + b['h'] * SCALE), outline=c, width=3)
        ry = 2 * H + 12 + 8 + r * ROWH
        d.rectangle((bx0, ry, bx1, ry + 6), fill=c)
        d.text((tx0, ry + 10), str(i), fill=c, font=fnt)
        keyrows.append((name, i, b['sid']))
    out.save(os.path.join(out_dir, name + '.png'))
    return len(sel), len(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--half', type=int, default=640, help='window width around the gate box centre (px, line-crop scale)')
    ap.add_argument('--check-key', action='store_true', help='exit 1 unless key.tsv equals atlas/strips/key.tsv')
    ap.add_argument('--line', nargs='*', default=[], help='whole-line strips for these lines -> atlas/strips_all/ (no gate strips)')
    a = ap.parse_args()
    allb = boxes(); byid = {b['sid']: b for b in allb}; keyrows = []
    if a.line:
        out_dir = os.path.join(HERE, 'strips_all'); os.makedirs(out_dir, exist_ok=True)
        for line in a.line:
            for h, (x0, x1, s0, s1) in enumerate([(0, 1040, 0, 1025), (1010, 2050, 1025, 99999)], 1):
                k, nr = strip(line, x0, x1, allb, f'{line}_h{h}', keyrows, out_dir, (s0, s1))
                print(f'{line}_h{h} {k} boxes, {nr} label rows')
        open(os.path.join(out_dir, 'key.tsv'), 'w').write('strip\tnum\tsid\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in keyrows))
        n = len({r[2] for r in keyrows}); nl = sum(1 for b in allb if b['page'] in a.line)
        print(f'{len(keyrows)} numbered boxes, {n} distinct, of {nl} atlas boxes on these lines')
        sys.exit(0 if n == len(keyrows) == nl else 1)
    os.makedirs(OUT, exist_ok=True)
    for n, sid in enumerate(GATE, 1):
        b = byid[sid]; c = b['x'] + b['w'] // 2
        k, nr = strip(b['page'], c - a.half // 2, c + a.half // 2, allb, f'gate_{n:02d}', keyrows)
        print(f'gate_{n:02d} {sid} {k} boxes, {nr} label rows')
    body = 'strip\tnum\tsid\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in keyrows)
    open(os.path.join(OUT, 'key.tsv'), 'w').write(body)
    if a.check_key:
        same = body == open(os.path.join(HERE, 'strips', 'key.tsv')).read()
        print('key.tsv', 'identical to atlas/strips/key.tsv' if same else 'DIFFERS from atlas/strips/key.tsv')
        sys.exit(0 if same else 1)


if __name__ == '__main__':
    main()
