#!/usr/bin/env python3
"""C1161-HC (15 Oct 2026): convert the worker's hand-counted S placements (shc/hand_raw.tsv: x in piece pixels, dy = y in the
view_line.py display) to piece coordinates (shc/hand.tsv), and cut RECUT/275-format windows from the single piece (no stitching):
+-2 sign pitches, band +-90 px, upscaled to >= 300 px, red tick top and bottom. Images go to OUTDIR only (scratchpad; never into git).
  python3 shc/cut_hc.py OUTDIR eye   -> hand.tsv, eye montages eye_1/eye_2.jpg of random.Random(2750).sample(rows, 30), key shc/eye_key.tsv
  python3 shc/cut_hc.py OUTDIR eye2  -> same, sample random.Random(2751) over the C1161-HC2 rows only (row 127 on), key shc/eye_key_hc2.tsv
C1161-HC2 (15 Oct 2026): optional hand_raw.tsv column `src` = the line whose piece image carries the sign when the line's own piece clips it
(flag `nb`, the neighbouring line's piece; flag `blk`, the c186Rblk cipher-block crop, since the c186R_L* pieces show the clear text). x, dy
are then in that src line's view_line.py display; the window is cut from images/<src>_<piece>.jpg."""
import csv, glob, os, random, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
out, mode = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
pitch = {}
for r in csv.DictReader(open(os.path.join(T, 's275', 'positions.tsv')), delimiter='\t'):
    pitch[r['line']] = float(r['pitch'])
rows = list(csv.DictReader(open(os.path.join(H, 'hand_raw.tsv')), delimiter='\t'))
for r in rows:
    r['src'] = r.get('src') or r['line']
    ps = sorted(glob.glob(os.path.join(T, 'images', f"{r['src']}_s*.jpg")))
    off = 0
    for p in ps:
        im = Image.open(p)
        if os.path.basename(p)[:-4].endswith(r['piece']):
            break
        off += im.height + 40
    r['y'] = str(int(r['dy']) - off - 40); r['pitch'] = f"{pitch.get(r['line'], 85.0):.1f}"
with open(os.path.join(H, 'hand.tsv'), 'w') as f:
    f.write('line\tpos\tpiece\tx\ty\tpitch\tflag\tsrc\n')
    for r in rows:
        f.write('\t'.join([r['line'], r['pos'], r['piece'], r['x'], r['y'], r['pitch'], r['flag'] or '', r['src']]) + '\n')
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)


def window(r):
    S = Image.open(os.path.join(T, 'images', f"{r['src']}_{r['piece']}.jpg")).convert('RGB')
    x, c, p = int(r['x']), int(r['y']), float(r['pitch'])
    lo, hi = int(max(0, x - 2 * p)), int(min(S.width, x + 2 * p))
    w = S.crop((lo, max(0, c - 90), hi, min(S.height, c + 90)))
    f = max(2, -(-300 // max(1, w.width)))
    w = w.resize((w.width * f, w.height * f)); d = ImageDraw.Draw(w); tx = (x - lo) * f
    d.line((tx, 0, tx, 14), fill='red', width=3); d.line((tx, w.height - 14, tx, w.height), fill='red', width=3)
    return w


def montage(items, path, cols=3):
    ws = [(i, window(r)) for i, r in items]
    cw = max(w.width for _, w in ws); rh = max(w.height for _, w in ws) + 28
    M = Image.new('RGB', (cols * (cw + 12), -(-len(ws) // cols) * rh), 'white'); d = ImageDraw.Draw(M)
    for j, (i, w) in enumerate(ws):
        x, y = (j % cols) * (cw + 12), (j // cols) * rh
        d.text((x + 4, y + 2), i, fill='blue', font=font); M.paste(w, (x, y + 26))
    M.thumbnail((2400, 2400)); M.save(path, quality=88)


if mode == 'eye':
    sel = random.Random(2750).sample(rows, 30)
    items = [(f'E{k:02d}', r) for k, r in enumerate(sel, 1)]
    with open(os.path.join(H, 'eye_key.tsv'), 'w') as f:
        f.write('eid\tline\tpos\tpiece\tflag\n'); [f.write(f"{i}\t{r['line']}\t{r['pos']}\t{r['piece']}\t{r['flag'] or ''}\n") for i, r in items]
    montage(items[:15], os.path.join(out, 'eye_1.jpg')); montage(items[15:], os.path.join(out, 'eye_2.jpg'))
    print('eye montages written')
if mode == 'eye2':
    sel = random.Random(2751).sample(rows[126:], 30)
    items = [(f'E{k:02d}', r) for k, r in enumerate(sel, 1)]
    with open(os.path.join(H, 'eye_key_hc2.tsv'), 'w') as f:
        f.write('eid\tline\tpos\tpiece\tflag\tsrc\n'); [f.write(f"{i}\t{r['line']}\t{r['pos']}\t{r['piece']}\t{r['flag'] or ''}\t{r['src']}\n") for i, r in items]
    montage(items[:15], os.path.join(out, 'eye2_1.jpg')); montage(items[15:], os.path.join(out, 'eye2_2.jpg'))
    print('eye2 montages written')
