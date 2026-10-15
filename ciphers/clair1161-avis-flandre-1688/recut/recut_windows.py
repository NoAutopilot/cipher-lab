#!/usr/bin/env python3
"""C1161-RECUT (15 Oct 2026): re-cut the three K windows (X165, X235, X088) plus three decoy S windows at hand-counted positions
(recut/positions.tsv: strip line, x, band centre, counted by sign sequence on the strip -- X165's line c185R_L23 sits on the
c185R_L22 strip's lower line, its own strip carries only L24 and the top edge of L23). Shuffled under fresh ids (seed 1161),
one montage to OUTDIR (scratchpad; images never go into git); id -> token in recut/recut_key.tsv.   python3 recut/recut_windows.py OUTDIR"""
import csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools')); import lookalike_pass as LP
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
P = list(csv.DictReader(open(os.path.join(H, 'positions.tsv')), delimiter='\t'))
build = LP._line_strips(os.path.join(T, 'la', 'crops', 'manifest.json'), '', '{line}_s*')
rng = random.Random(1161); rng.shuffle(P)
wins = []
with open(os.path.join(H, 'recut_key.tsv'), 'w') as kf:
    kf.write('rid\tline\tpos\tstrip\tx\tc\n')
    for k, r in enumerate(P, 1):
        S = build(r['strip']); x, c = int(r['x']), int(r['c'])
        w = S.crop((max(0, x - 170), max(0, c - 90), min(S.width, x + 170), min(S.height, c + 90))).convert('RGB')
        tx = x - max(0, x - 170); f = 2
        w = w.resize((w.width * f, w.height * f)); d = ImageDraw.Draw(w)
        d.line((tx * f, 0, tx * f, 14), fill='red', width=3); d.line((tx * f, w.height - 14, tx * f, w.height), fill='red', width=3)
        wins.append((f'R{k:02d}', w)); kf.write(f"R{k:02d}\t{r['line']}\t{r['pos']}\t{r['strip']}\t{x}\t{c}\n")
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
cw = max(w.width for _, w in wins); rh = max(w.height for _, w in wins) + 28
M = Image.new('RGB', (2 * (cw + 12), 3 * rh), 'white'); d = ImageDraw.Draw(M)
for j, (rid, w) in enumerate(wins):
    x, y = (j % 2) * (cw + 12), (j // 2) * rh
    d.text((x + 4, y + 2), rid, fill='blue', font=font); M.paste(w, (x, y + 26))
M.save(os.path.join(out, 'recut.jpg'), quality=88); print(len(wins), 'windows')
