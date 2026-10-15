#!/usr/bin/env python3
"""LVN-4610H line sheets. usage: sheets.py PNGDIR OUTDIR. PNGDIR holds p1-1.png, p2-2.png, p3-3.png (pdftoppm -r 300 of WVO 04610.pdf).
Line box = images/manifest.json 150-dpi box x2, padded 20 px; each line cut in two overlapping halves (0-1340, 1140-2482) at 1.15x, four
lines to a sheet, the line's numerals printed under each half with targets (lvn4610h/targets.tsv) bracketed and H rows ending in 2 marked
'<..>' (the control). Images go to OUTDIR (scratch), never into git."""
import sys, os, json, csv
from PIL import Image, ImageDraw, ImageFont
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
src, out = sys.argv[1:3]; os.makedirs(out, exist_ok=True)
def walk(o):
    if isinstance(o, dict):
        if 'crop' in o and 'box' in o: yield o
        for v in o.values(): yield from walk(v)
    elif isinstance(o, list):
        for v in o: yield from walk(v)
E = {e['crop']: e['box'] for e in walk(json.load(open(os.path.join(T, 'images', 'manifest.json'))))}
tg = {(r['line'], r['position']) for r in csv.DictReader(open(os.path.join(H, 'targets.tsv')), delimiter='\t')}
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext_4610.tsv')), delimiter='\t'))
lines = sorted({ln for ln, _ in tg})
pages = {p: Image.open(os.path.join(src, f'p{p}-{p}.png')).convert('L') for p in '123'}
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 22)
except OSError: F = ImageFont.load_default()
def label(ln):
    s = []
    for r in rows:
        if r['line'] != ln: continue
        v = r['sign']
        if (ln, r['position']) in tg: v = f"[{r['position']}:{v}]"
        elif r['confidence'] == 'H' and v.isdigit() and v.endswith('2'): v = f"<{r['position']}:{v}>"
        elif v.startswith('='): v = v[1:]
        s.append(v)
    return ' '.join(s)
strips = []
for ln in lines:
    x0, y0, x1, y1 = [2 * v for v in E[f'04610_{ln}.jpg']]
    im = pages[ln[1]]; y0 = max(0, y0 - 20); y1 = min(im.height, y1 + 20)
    for a, b in ((0, 1340), (1140, im.width)):
        c = im.crop((a, y0, b, y1)); c = c.resize((int(c.width * 1.15), int(c.height * 1.15)), Image.LANCZOS).convert('RGB')
        strips.append((ln, a, c))
for k in range(0, len(lines), 4):
    grp = [s for s in strips if s[0] in lines[k:k + 4]]
    W = max(c.width for *_, c in grp); Ht = sum(c.height + 64 for *_, c in grp)
    o = Image.new('RGB', (W, Ht), 'white'); d = ImageDraw.Draw(o); y = 0
    for ln, a, c in grp:
        d.text((4, y), f'{ln} {"left" if a == 0 else "right"}: {label(ln)}', fill=(0, 0, 0), font=F)
        o.paste(c, (0, y + 30)); y += c.height + 64
    o.save(os.path.join(out, f'sheet_{k // 4 + 1:02d}.jpg'), quality=88)
print(len(lines), 'lines,', (len(lines) + 3) // 4, 'sheets')
