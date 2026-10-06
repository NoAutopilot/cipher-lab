#!/usr/bin/env python3
"""D1-BAL167 (6 Oct 2026): cut the 168 f.166r gloss-fixed letter-sign exemplars listed in d1bal167/exemplars.tsv, paste every exemplar
(f.157's 15 from d2davex/exemplars + f.166's) on one sheet grouped by shape, and report the per-shape oracle leave-one-out ceiling
(D2-DAVEX's ceiling.py, by shape instead of by letter) and the coverage of the f.247 label set.
Per-shape oracle: an exemplar scores if the OTHER exemplars of its shape have a unique majority letter equal to its own letter
(a labeller that knows the shape exactly and votes by the gloss). Letter-level oracle as in d2davex/ceiling.py, for comparison.
f.247 coverage: F247_SHAPE maps each label of passes/reconciled_b168f247v.tsv to the exemplar shape it resembles, by eye from the c510-511
crops (D1-BAL167); None = no exemplar shape resembles it. Exit 0 always (no gate is decided here; the labeller is not run).
  python3 d1bal167/cut_and_ceiling.py  -> d1bal167/exemplars/*.png, d1bal167/exemplar_sheet.png, d1bal167/ceiling.txt"""
import os, csv, collections, re
from PIL import Image, ImageDraw
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = f'{D}/images/crops/src_ark_12148_btv1b9001503k_f346_1000_2930_2700_2420.jpg'
CENTRES = [160, 320, 455, 590, 785, 935, 1085, 1280, 1420]   # same as d1bal167/bands.py
F247_SHAPE = {'s:p': 'p', 's:f': 'S', 's:y': 'y+', 's:t': 'u4', 's:d': 'loop',
              's:b': None, 's:L': None, 's:u': None, 's:K': None, 's:q': None, 's:n': None, 's:a': None}
O = f'{D}/d1bal167/exemplars'; os.makedirs(O, exist_ok=True)
rows = [r for r in csv.DictReader((l for l in open(f'{D}/d1bal167/exemplars.tsv') if not l.startswith('#')), delimiter='\t')]
src = Image.open(SRC).convert('L'); cells = []
for r in rows:
    if r['leaf'] == '168f166':
        c = CENTRES[int(r['line']) - 1]
        im = src.crop((int(r['x0']), c - 70, int(r['x1']), c + 45))
        im.save(f"{O}/168f166_L{int(r['line'])}_{int(r['pos'])}_{r['letter']}.png")
    else:
        im = Image.open(f"{D}/d2davex/exemplars/167f157{r['line']}_{int(r['pos']):02d}_{r['letter']}.png")
    cells.append((r, im))
cells.sort(key=lambda t: (t[0]['shape'], t[0]['letter']))
W = 120; H = 150
sheet = Image.new('L', (W * 16, (H + 24) * ((len(cells) + 15) // 16)), 255); d = ImageDraw.Draw(sheet)
for k, (r, im) in enumerate(cells):
    im = im.copy(); im.thumbnail((W - 6, H))
    x, y = (k % 16) * W, (k // 16) * (H + 24)
    sheet.paste(im, (x + 3, y + 22)); d.text((x + 3, y + 3), f"{r['shape']}={r['letter']} {r['leaf'][3:]}", fill=0)
sheet.save(f'{D}/d1bal167/exemplar_sheet.png')
out = []
def oracle(key):
    ok = 0
    for i, r in enumerate(rows):
        others = collections.Counter(s['letter'] for j, s in enumerate(rows) if j != i and key(s) == key(r))
        if not others: continue
        top = others.most_common(); 
        if top[0][0] == r['letter'] and (len(top) == 1 or top[1][1] < top[0][1]): ok += 1
    return ok
for name, sub in (('f157 only (D2-DAVEX set)', [r for r in rows if r['leaf'] == '167f157']), ('f157 + f166', rows)):
    save = rows[:]; rows[:] = sub
    bys = collections.defaultdict(collections.Counter)
    for r in rows: bys[r['shape']][r['letter']] += 1
    ge2 = sorted(s for s, c in bys.items() if sum(c.values()) >= 2)
    out.append(f'== {name}: {len(rows)} exemplars, {len(bys)} shapes, {len(ge2)} shapes with >= 2 exemplars: ' + ', '.join(ge2))
    out.append('   per shape: ' + '; '.join(f"{s} {dict(c)}" for s, c in sorted(bys.items())))
    lo = oracle(lambda s: s['letter']) if False else sum(1 for r in rows if sum(1 for s in rows if s['letter'] == r['letter']) >= 2)
    so = oracle(lambda s: s['shape'])
    out.append(f'   letter-level oracle LOO ceiling {lo}/{len(rows)} = {lo/len(rows):.3f} (D2-DAVEX measure)')
    out.append(f'   per-shape oracle LOO ceiling {so}/{len(rows)} = {so/len(rows):.3f} (D2-DAVEX target >= 0.9)')
    tok = collections.Counter()
    for l in open(f'{D}/passes/reconciled_b168f247v.tsv'):
        if l.startswith('#') or l.startswith('row'): continue
        tok.update(t for t in re.sub(r'\{[^}]*\}', ' ', l.split('\t', 1)[1]).split() if t.startswith('s:'))
    cov = []; covtok = 0
    for lab, n in tok.most_common():
        sh = F247_SHAPE.get(lab); k = sum(bys[sh].values()) if sh else 0
        cov.append(f'{lab}({n})->{sh or "-"}:{k}'); covtok += n if k >= 2 else 0
    nlab = sum(1 for lab in tok if F247_SHAPE.get(lab) and sum(bys[F247_SHAPE[lab]].values()) >= 2)
    out.append(f'   f.247 labels with a resembling shape at >= 2 exemplars: {nlab}/{len(tok)} labels, {covtok}/{sum(tok.values())} tokens; ' + ' '.join(cov))
    rows[:] = save
open(f'{D}/d1bal167/ceiling.txt', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
