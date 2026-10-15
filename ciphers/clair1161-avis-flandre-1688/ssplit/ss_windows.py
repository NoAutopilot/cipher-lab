#!/usr/bin/env python3
"""C1161-SSPLIT (15 Oct 2026): one window per S token (all, ciphertext.tsv order), shuffled under opaque ids (seed 1688),
grid montages written to OUTDIR (scratchpad; images never go into git), id -> token key to ssplit/windows_key.tsv.
Helpers from tools/lookalike_pass.py as s7/s7_windows.py (CL1161-S7).   python3 ssplit/ss_windows.py OUTDIR"""
import csv, collections, os, random, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import lookalike_pass as LP
sys.path.insert(0, HERE); import ss_locate as L
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
seq = collections.defaultdict(list)
for r in rows:
    seq[r['line']].append(r['sign'])
toks = [(ln, i + 1) for ln, s in seq.items() for i, x in enumerate(s) if x == 'S']
rng = random.Random(1688); rng.shuffle(toks)
build = LP._line_strips(os.path.join(T, 'la', 'crops', 'manifest.json'), '', '{line}_s*')
strips, wins = {}, []
with open(os.path.join(HERE, 'windows_key.tsv'), 'w') as kf:
    kf.write('wid\tline\tpos\n')
    for k, (ln, pos) in enumerate(toks, 1):
        if ln not in strips:
            S = build(ln); strips[ln] = (S,) + LP._ink_extent(S, 110, 2)
        S = strips[ln][0]; x, p, c = L.locate(S, len(seq[ln]), pos)
        lo, hi = int(max(0, x - 1.6 * p)), int(min(S.width, x + 1.6 * p))
        w = S.crop((lo, max(0, c - 90), hi, c + 90)).convert('RGB'); f = max(1, 300 // max(1, w.width) + 1) if w.width < 300 else 1
        w = w.resize((w.width * f, w.height * f)); dr = ImageDraw.Draw(w); tx = (x - lo) * f
        dr.line((tx, 0, tx, 12), fill='red', width=3); dr.line((tx, w.height - 12, tx, w.height), fill='red', width=3)
        wins.append((f'X{k:03d}', w))
        kf.write(f'X{k:03d}\t{ln}\t{pos}\n')
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 20)
C, R = 4, 5
for g in range(0, len(wins), C * R):
    grp = wins[g:g + C * R]
    cw = max(w.width for _, w in grp); rh = max(w.height for _, w in grp) + 26
    M = Image.new('RGB', (C * (cw + 10), R * rh), 'white'); d = ImageDraw.Draw(M)
    for j, (wid, w) in enumerate(grp):
        x, y = (j % C) * (cw + 10), (j // C) * rh
        d.text((x + 4, y + 2), wid, fill='blue', font=font); M.paste(w, (x, y + 24))
    M.save(os.path.join(out, f'ss_{g // (C * R) + 1:02d}.jpg'), quality=85)
print(len(wins), 'windows,', (len(wins) + C * R - 1) // (C * R), 'montages')
