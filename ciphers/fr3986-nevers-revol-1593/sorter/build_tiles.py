#!/usr/bin/env python3
"""Sign-sorter inputs for f.198 recto + verso (GAPS5, 2 Oct 2026): boxes, provisional piles, focus list.

1. Boxes: tools/iiif_lines.py --image sorter/lines/<line>.jpg --centres <h/2> --groups 6 (one band per whole-line image;
   gap 6 px chosen from the blank-run histogram, whose short runs 1-5 are inside signs/letters), run into a scratch dir;
   every piece box -> signs.tsv (sid, page, x, y, w, h; page = the line image).
2. Labels: the passes (passes/recto/passA.tsv, passes/v2/passA.tsv + passB.tsv) record line, run and position but no x
   coordinate, and a line's pieces include its clear-French letters (r_L12: 53 pieces for 22 pass signs), so no piece can
   be tied to a pass tag without reading the image. Piles are therefore provisional image clusters (k-means, k=40, seed 1,
   on the 24x24 normalised tile the sorter itself uses), named c01..c40; pieces wider than 1.6x the band height go to
   pile 'wide' (words or joined signs). The pass tags per line are listed in README.md for the owner beside the page.
3. Focus: one tile per line where verso passes A and B split (and every recto line, one reader only): the darkest piece
   of the line (the cipher runs are written heavier than the clear text), with the two readers' tags as the question.
  python3 ciphers/fr3986-nevers-revol-1593/sorter/build_tiles.py SCRATCH_DIR
"""
import csv, json, os, subprocess, sys
from collections import defaultdict
import numpy as np
from PIL import Image
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(T))
S = os.path.join(T, 'sorter'); LINES = os.path.join(S, 'lines'); scratch = sys.argv[1]
rows = []
for f in sorted(os.listdir(LINES)):
    name = f[:-4]; im = Image.open(os.path.join(LINES, f)).convert('L')
    out = os.path.join(scratch, name)
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools/iiif_lines.py'), '--image', os.path.join(LINES, f),
                    '--centres', str(im.height // 2), '--groups', '6', '--out', out, '--prefix', name],
                   check=True, capture_output=True)
    m = json.load(open(os.path.join(out, 'manifest.json')))['iiif_lines']
    for e in m:
        if 'group' not in e: continue
        x0, y0, x1, y1 = e['box']
        rows.append(dict(sid=f"{name}_g{e['group']:02d}", page=name, x=x0, y=y0, w=x1 - x0, h=y1 - y0))
with open(os.path.join(S, 'signs.tsv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, ['sid', 'page', 'x', 'y', 'w', 'h'], delimiter='\t', lineterminator='\n')
    w.writeheader(); w.writerows(rows)
pages = {p: np.asarray(Image.open(os.path.join(LINES, p + '.jpg')).convert('L'), dtype=float)
         for p in {r['page'] for r in rows}}
vec, dark, narrow = [], {}, []
for r in rows:
    g = pages[r['page']][r['y']:r['y'] + r['h'], r['x']:r['x'] + r['w']]
    dark[r['sid']] = float((g < 90).sum()) / g.size
    if r['w'] > 1.6 * r['h']:
        continue
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


def tags(path):
    d = defaultdict(list)
    for r in csv.DictReader(open(os.path.join(T, path)), delimiter='\t'):
        if r['tag'] != 'NONE': d[r['line']].append(r['tag'])
    return d
rA, vA, vB = tags('passes/recto/passA.tsv'), tags('passes/v2/passA.tsv'), tags('passes/v2/passB.tsv')
focus = []
for p in sorted(pages):
    side, L = p.split('_')
    if side == 'v':
        if vA[L] == vB[L]: continue
        q = f"verso {L}: readers split -- A: {' '.join(vA[L]) or '(none)'} | B: {' '.join(vB[L]) or '(none)'}. Which tiles on this line are cipher signs, and which pile is each?"
    else:
        q = f"recto {L} (one reader): {' '.join(rA[L])}. Which tiles on this line are cipher signs, and which pile is each?"
    best = max((r['sid'] for r in rows if r['page'] == p), key=lambda s: dark[s])
    focus.append((best, q.replace('\t', ' ')))
with open(os.path.join(S, 'focus.tsv'), 'w') as fh:
    for sid, q in focus: fh.write(f'{sid}\t{q}\n')
print(f'{len(rows)} tiles, {len(narrow)} clustered into {k}, {len(rows) - len(narrow)} wide, {len(focus)} focus rows')
