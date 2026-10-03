#!/usr/bin/env python3
"""Sign-sorter inputs for f.120r (FT4b, 3 Oct 2026): line images, boxes, provisional piles, focus list.

Worked example followed: ciphers/fr3986-nevers-revol-1593/sorter/build_tiles.py (GAPS5).
1. Lines: each band of images/manifest.json (the FT4 crop run, segment 1 rows) is re-cut at full page width from the
   committed source image images/src_ark_12148_btv1b52503046q_f452_full.jpg into SCRATCH/lines/f120r_Lnn.jpg (not
   committed: regenerated here, so the folder stays small). The s1/s2 half crops overlap by 659 px and would double
   every sign in the overlap, so they are not used as tile pages.
2. Boxes: tools/iiif_lines.py --image <line> --centres <h/2> --groups 4. Gap 4 from L04's blank-run histogram
   (widths 1..: 112 39 25 17 10 ...): runs 1-3 are inside signs; 4 cuts fewer signs in two than 6 does (76 vs 70
   pieces on L04, against 43-44 pass tokens there, some of them whole clear words). Every piece -> signs.tsv.
3. Labels: passes/f120r_pass{A,B}.tsv record line and position but no x coordinate, and lines mix clear Spanish with
   signs and code groups, so no piece is tied to a pass tag without reading the image. Piles are provisional image
   clusters (k-means, k=40, seed 1, on the 24x24 normalised tile the sorter itself uses), c01..c40; pieces wider than
   1.6x their own height go to pile 'wide' (clear words, code groups, joined signs).
4. Focus: the (A, B) tag pairs the two passes split on (passes/disagreements.tsv, clear-word vs clear-word splits
   dropped), commonest first, at most 40 pairs; for each, its first occurrence's tile is placed by proportion (column
   / line columns along the line's ink extent), so the tile is near, not necessarily on, the split sign: the question
   says so.
  python3 ciphers/esp318-sicilia-1503/sorter/build_tiles.py SCRATCH_DIR
"""
import csv, json, os, subprocess, sys
from collections import Counter, defaultdict
import numpy as np
from PIL import Image
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(T))
S = os.path.join(T, 'sorter'); scratch = sys.argv[1]; LINES = os.path.join(scratch, 'lines')
os.makedirs(LINES, exist_ok=True)
src = Image.open(os.path.join(T, 'images', 'src_ark_12148_btv1b52503046q_f452_full.jpg'))
for e in json.load(open(os.path.join(T, 'images', 'manifest.json')))['iiif_lines']:
    if e.get('segment') == 1:
        _, y0, _, y1 = e['box']
        src.crop((0, y0, src.width, y1)).save(os.path.join(LINES, 'f120r_L%02d.jpg' % e['band']), quality=88)
rows = []
for f in sorted(os.listdir(LINES)):
    name = f[:-4]; im = Image.open(os.path.join(LINES, f))
    out = os.path.join(scratch, 'groups', name)
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools/iiif_lines.py'), '--image', os.path.join(LINES, f),
                    '--centres', str(im.height // 2), '--groups', '4', '--out', out, '--prefix', name],
                   check=True, capture_output=True)
    for e in json.load(open(os.path.join(out, 'manifest.json')))['iiif_lines']:
        if 'group' not in e: continue
        x0, y0, x1, y1 = e['box']
        rows.append(dict(sid=f"{name}_g{e['group']:02d}", page=name, x=x0, y=y0, w=x1 - x0, h=y1 - y0))
with open(os.path.join(S, 'signs.tsv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, ['sid', 'page', 'x', 'y', 'w', 'h'], delimiter='\t', lineterminator='\n')
    w.writeheader(); w.writerows(rows)
pages = {p: np.asarray(Image.open(os.path.join(LINES, p + '.jpg')).convert('L'), dtype=float)
         for p in {r['page'] for r in rows}}
vec, narrow = [], []
for r in rows:
    if r['w'] > 1.6 * r['h']: continue
    g = pages[r['page']][r['y']:r['y'] + r['h'], r['x']:r['x'] + r['w']]
    v = np.asarray(Image.fromarray(g.astype(np.uint8)).resize((24, 24)), dtype=float).ravel()
    narrow.append(r['sid']); vec.append((v - v.mean()) / (v.std() or 1))
X = np.array(vec); rng = np.random.default_rng(1); k = 40
C = X[rng.choice(len(X), k, replace=False)]
for _ in range(50):
    lab = ((X[:, None, :] - C[None]) ** 2).sum(-1).argmin(1)
    C = np.array([X[lab == j].mean(0) if (lab == j).any() else C[j] for j in range(k)])
pile = {sid: f'c{j + 1:02d}' for sid, j in zip(narrow, lab)}
with open(os.path.join(S, 'labels.tsv'), 'w') as fh:
    fh.write('sid\tsign\tfamily\n')
    for r in rows:
        p = pile.get(r['sid'], 'wide')
        fh.write(f"{r['sid']}\t{p}\t{'wide' if p == 'wide' else 'cluster'}\n")
cols = {r['line']: int(r['columns']) for r in csv.DictReader(open(os.path.join(T, 'passes/agreement.tsv')), delimiter='\t')}
byline = defaultdict(list)
for r in rows: byline[r['page'].split('_')[1]].append(r)
pairs, first = Counter(), {}
for r in csv.DictReader(open(os.path.join(T, 'passes/disagreements.tsv')), delimiter='\t'):
    a, b = r['A'] or '(none)', r['B'] or '(none)'
    if a.startswith('w:') and b.startswith('w:'): continue
    key = (a, b); pairs[key] += 1; first.setdefault(key, (r['line'], int(r['col'])))
focus, used = [], set()
for (a, b), n in pairs.most_common():
    if len(focus) >= 40: break
    L, col = first[(a, b)]; ps = byline.get(L)
    if not ps or L not in cols: continue
    lo = min(p['x'] for p in ps); hi = max(p['x'] + p['w'] for p in ps)
    tx = lo + (col - 0.5) / cols[L] * (hi - lo)
    best = min(ps, key=lambda p: abs(p['x'] + p['w'] / 2 - tx))['sid']
    if best in used: continue
    used.add(best)
    q = (f"{L} column {col}/{cols[L]}: reader A '{a}' vs reader B '{b}' ({n}x on the page). Tile placed by position, "
         f"so the split sign is this one or a neighbour: what is it, and which pile does it belong to?")
    focus.append((best, q.replace('\t', ' ')))
with open(os.path.join(S, 'focus.tsv'), 'w') as fh:
    for sid, q in focus: fh.write(f'{sid}\t{q}\n')
print(f'{len(rows)} tiles, {len(narrow)} clustered into {k}, {len(rows) - len(narrow)} wide, {len(focus)} focus rows')
