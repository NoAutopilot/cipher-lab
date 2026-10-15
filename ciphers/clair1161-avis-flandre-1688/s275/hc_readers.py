#!/usr/bin/env python3
"""C1161-S275 (15 Oct 2026): reader montages for the s275 PREREG (addendum B) from the hand-placed S windows in shc/hand.tsv, window format
exactly as shc/cut_hc.py (single piece, +-2 pitches, band +-90 px, >= 300 px, red tick). Images go to OUTDIR only (scratchpad; never git).
  python3 s275/hc_readers.py OUTDIR R1 2751   -> R1_b1a.jpg, R1_b1b.jpg ... (7 batches of <= 40, two montages of <= 20 each); key s275/key_R1.tsv
  python3 s275/hc_readers.py OUTDIR R3 2753 s275/recon_tokens.tsv   -> same for the reconciliation subset (line, pos rows)"""
import csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
out, R, seed = sys.argv[1], sys.argv[2], int(sys.argv[3]); os.makedirs(out, exist_ok=True)
rows = list(csv.DictReader(open(os.path.join(T, 'shc', 'hand.tsv')), delimiter='\t'))
if len(sys.argv) > 4:
    want = {(r['line'], r['pos']) for r in csv.DictReader(open(sys.argv[4]), delimiter='\t')}
    rows = [r for r in rows if (r['line'], r['pos']) in want]
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


def montage(items, path, cols=4):
    ws = [(i, window(r)) for i, r in items]
    cw = max(w.width for _, w in ws); rh = max(w.height for _, w in ws) + 28
    M = Image.new('RGB', (cols * (cw + 12), -(-len(ws) // cols) * rh), 'white'); d = ImageDraw.Draw(M)
    for j, (i, w) in enumerate(ws):
        x, y = (j % cols) * (cw + 12), (j // cols) * rh
        d.text((x + 4, y + 2), i, fill='blue', font=font); M.paste(w, (x, y + 26))
    M.thumbnail((2400, 2400)); M.save(path, quality=88)


Q = rows[:]; random.Random(seed).shuffle(Q)
items = [(f'{R}-{k:03d}', r) for k, r in enumerate(Q, 1)]
with open(os.path.join(H, f'key_{R}.tsv'), 'w') as f:
    f.write('wid\tline\tpos\n'); [f.write(f"{i}\t{r['line']}\t{r['pos']}\n") for i, r in items]
nb = 0
for g in range(0, len(items), 40):
    nb += 1; b = items[g:g + 40]
    montage(b[:20], os.path.join(out, f'{R}_b{nb}a.jpg'))
    if b[20:]:
        montage(b[20:], os.path.join(out, f'{R}_b{nb}b.jpg'))
print(len(items), 'windows', nb, 'batches')
