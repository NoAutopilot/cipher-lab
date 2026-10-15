#!/usr/bin/env python3
"""C1161-275 (15 Oct 2026): cut one window per S token at the counted position (s275/positions.tsv), +-2 sign pitches, band +-90 px,
upscaled to >= 300 px wide, red tick top and bottom (RECUT's format). Images go to OUTDIR only (scratchpad; never into git).
  python3 s275/cut_windows.py OUTDIR eye             -> eye-check montage of 30 random windows (seed 2750), labelled E01..E30, key s275/eye_key.tsv
  python3 s275/cut_windows.py OUTDIR reader R SEED   -> montages R_01.jpg... (4x5, 20 windows each) under ids R001...; key s275/key_R.tsv"""
import csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools')); import lookalike_pass as LP
build = LP._line_strips(os.path.join(T, 'la', 'crops', 'manifest.json'), '', '{line}_s*')
P = list(csv.DictReader(open(os.path.join(H, 'positions.tsv')), delimiter='\t'))
out = sys.argv[1]; mode = sys.argv[2]; os.makedirs(out, exist_ok=True)
_s = {}


def window(r):
    if r['strip'] not in _s:
        _s[r['strip']] = build(r['strip'])
    S = _s[r['strip']]; x, c, p = int(r['x']), int(r['c']), float(r['pitch'])
    lo, hi = int(max(0, x - 2 * p)), int(min(S.width, x + 2 * p))
    w = S.crop((lo, max(0, c - 90), hi, min(S.height, c + 90))).convert('RGB')
    f = max(2, -(-300 // max(1, w.width)))
    w = w.resize((w.width * f, w.height * f)); d = ImageDraw.Draw(w); tx = (x - lo) * f
    d.line((tx, 0, tx, 14), fill='red', width=3); d.line((tx, w.height - 14, tx, w.height), fill='red', width=3)
    return w


font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)


def montage(items, path, cols=4):
    ws = [(i, window(r)) for i, r in items]
    cw = max(w.width for _, w in ws); rh = max(w.height for _, w in ws) + 28
    rows = -(-len(ws) // cols)
    M = Image.new('RGB', (cols * (cw + 12), rows * rh), 'white'); d = ImageDraw.Draw(M)
    for j, (i, w) in enumerate(ws):
        x, y = (j % cols) * (cw + 12), (j // cols) * rh
        d.text((x + 4, y + 2), i, fill='blue', font=font); M.paste(w, (x, y + 26))
    M.thumbnail((2400, 2400)); M.save(path, quality=88)


if mode == 'eye':
    sel = random.Random(2750).sample(P, 30)
    items = [(f'E{k:02d}', r) for k, r in enumerate(sel, 1)]
    with open(os.path.join(H, 'eye_key.tsv'), 'w') as f:
        f.write('eid\tline\tpos\n'); [f.write(f"{i}\t{r['line']}\t{r['pos']}\n") for i, r in items]
    montage(items[:15], os.path.join(out, 'eye_1.jpg'), 3); montage(items[15:], os.path.join(out, 'eye_2.jpg'), 3)
else:
    R, seed = sys.argv[3], int(sys.argv[4])
    Q = P[:]; random.Random(seed).shuffle(Q)
    items = [(f'{R}{k:03d}', r) for k, r in enumerate(Q, 1)]
    with open(os.path.join(H, f'key_{R}.tsv'), 'w') as f:
        f.write('wid\tline\tpos\n'); [f.write(f"{i}\t{r['line']}\t{r['pos']}\n") for i, r in items]
    for g in range(0, len(items), 20):
        montage(items[g:g + 20], os.path.join(out, f'{R}_{g // 20 + 1:02d}.jpg'))
    print(len(items), 'windows', -(-len(items) // 20), 'montages')
