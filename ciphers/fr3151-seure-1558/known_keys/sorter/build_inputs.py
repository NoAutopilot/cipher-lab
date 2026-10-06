#!/usr/bin/env python3
"""D1-SEURES (6 Oct 2026): sign-sorter inputs for the Morvilliers 1549 cipher block (BnF fr. 3138 fo. 66r, canvas 70).
Usage: python3 build_inputs.py ATLAS_DIR OUT_DIR   (ATLAS_DIR = glyph_atlas.py segment + cluster --k 40 on the region source)
- line ids: nearest eye-set line centre after de-sloping (glyph_atlas's own line 1 merged L01 and L02)
- dropped: L01-L02 (a long ruled stroke runs through both; glyph_atlas finds about 10 of their ~45 signs, also after
  removing the rule and stretching contrast, so they are left to a later recut); clear words (L06 1600-2100 'Neantmoins'; L22 x>1290 'Le S. Ascanio
  colonne est'), and tiles whose centre falls above L01 or below L22 (clear text of the neighbouring lines)
- pages: one flat strip per line cut from the region source, paper flattened (divided by a 51 px median); tiles re-based, boxes padded 4 px
- also dropped: tiles past x=2915 (the leaf's right edge) and specks under 20 px on both sides
- starting piles: the 40 shape clusters, each named by the label-sheet label the two blind passes most often give at the
  tiles' proportional position in the line (a name only; the passes split at err 0.778, so no pile is a reading)
- focus: tiles of the piles whose names sit in the passes' most frequent substitution pairs (per-line edit alignment)
"""
import csv, collections, os, sys
from PIL import Image
A, OUT = sys.argv[1], sys.argv[2]
T = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(T, '..', 'morv')
SRC = os.path.join(T, '..', 'images', 'src_ark_12148_btv1b90601662_f70_4800_700_2950_2850.jpg')
SLOPE = 0.0258
rows = list(csv.DictReader(open(f'{A}/signs.tsv'), delimiter='\t'))
cl = {r['id']: r['cluster'] for r in csv.DictReader(open(f'{A}/clusters.tsv'), delimiter='\t') if r['kind'] == 'sign'}
for r in rows:
    for k in 'xywh': r[k] = int(r[k])
    r['cx'] = r['x'] + r['w'] / 2; r['cy'] = r['y'] + r['h'] / 2; r['dy'] = r['cy'] + SLOPE * r['cx']
# line ids: nearest of D1-SEURE's 22 eye-set line centres (iiif_lines --centres, region y) after de-sloping; offset 20 px
# minimises the mean residual (19 px against a pitch of about 120)
C = [90, 195, 300, 400, 520, 635, 760, 870, 990, 1130, 1260, 1390, 1520, 1650, 1780, 1910, 2040, 2190, 2320, 2450, 2590, 2730]
OFF = 20
def lid(r):
    i = min(range(len(C)), key=lambda i: abs(r['dy'] - C[i] - OFF))
    return f'L{i + 1:02d}'
keep = []
for r in rows:
    r['L'] = lid(r)
    if r['L'] in ('L01', 'L02'): continue  # under the long rule: the segmenter finds only 10 of about 45 signs
    if r['L'] == 'L06' and 1600 < r['cx'] < 2100: continue
    if r['L'] == 'L22' and r['cx'] > 1290: continue
    if max(r['w'], r['h']) < 20: continue  # specks (random check: 1 of 6 tiles was a speck)
    if r['cx'] > 2915: continue  # the leaf's right edge / gutter, not signs
    if r['dy'] < C[0] + OFF - 60 or r['dy'] > C[-1] + OFF + 60: continue
    keep.append(r)
# passes: labels per line, clear words ({...}) dropped
def rd(p):
    out = {}
    for r in csv.DictReader(open(os.path.join(M, p)), delimiter='\t'):
        out[r['line']] = [t for t in r['signs'].split() if not t.startswith('{')]
    return out
PA, PB = rd('passA.tsv'), rd('passB.tsv')
byL = collections.defaultdict(list)
for r in keep: byL[r['L']].append(r)
vote = collections.defaultdict(collections.Counter)
for L, rs in byL.items():
    rs.sort(key=lambda r: r['cx'])
    for i, r in enumerate(rs):
        p = (i + 0.5) / len(rs)
        for P in (PA, PB):
            s = P.get(L, [])
            if s:
                t = s[min(len(s) - 1, int(p * len(s)))]
                if not t.startswith('?'): vote[cl[r['sid']]][t] += 1
# substitution pairs A vs B (edit alignment per line)
sub = collections.Counter()
for L in PA:
    a, b = PA[L], PB.get(L, [])
    D = [[0] * (len(b) + 1) for _ in a + [0]]
    for i in range(len(a) + 1): D[i][0] = i
    for j in range(len(b) + 1): D[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    i, j = len(a), len(b)
    while i and j:
        if D[i][j] == D[i-1][j-1] + (a[i-1] != b[j-1]):
            if a[i-1] != b[j-1] and not a[i-1].startswith('?') and not b[j-1].startswith('?'):
                sub[tuple(sorted((a[i-1], b[j-1])))] += 1
            i, j = i - 1, j - 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
# pile names: cluster -> top voted label, duplicates suffixed
name, used = {}, collections.Counter()
for c in sorted(vote, key=lambda c: -sum(vote[c].values())):
    t = vote[c].most_common(1)[0][0]; used[t] += 1
    name[c] = t if used[t] == 1 else f'{t}.{used[t]}'
os.makedirs(f'{OUT}/pages', exist_ok=True)
import cv2, numpy as np
g = cv2.imread(SRC, 0).astype(np.float32)  # flatten the paper (stain at right) so the page reads white, ink unchanged in shape
g = np.clip(g / np.maximum(cv2.medianBlur(g.astype(np.uint8), 51).astype(np.float32), 1) * 240, 0, 255)
src = Image.fromarray(g.astype(np.uint8))
sw = csv.writer(open(f'{OUT}/signs.tsv', 'w'), delimiter='\t'); sw.writerow(['sid', 'page', 'x', 'y', 'w', 'h'])
lw = csv.writer(open(f'{OUT}/labels.tsv', 'w'), delimiter='\t'); lw.writerow(['sid', 'sign', 'family'])
cw = open(f'{OUT}/cipher_lines.tsv', 'w'); cw.write('# D1-SEURES: fo. 66r cipher lines (strips = line pages); clear words dropped before the build\n')
for L in sorted(byL):
    rs = byL[L]; y0 = max(0, min(r['y'] for r in rs) - 16); y1 = min(src.height, max(r['y'] + r['h'] for r in rs) + 16)
    src.crop((0, y0, src.width, y1)).save(f'{OUT}/pages/{L}.jpg', quality=80)
    cw.write(f'{L}\n')
    for r in rs:
        sw.writerow([r['sid'], L, max(0, r['x'] - 4), r['y'] - y0 - 4, r['w'] + 8, r['h'] + 8])  # 4 px pad: tight boxes on small solid signs read >60% ink
        lw.writerow([r['sid'], name.get(cl[r['sid']], 'k' + cl[r['sid']]), 'k' + cl[r['sid']]])
piles = set(name.values())
fw = csv.writer(open(f'{OUT}/focus.tsv', 'w'), delimiter='\t')  # no header: sign_sorter reads every row
nf, pairs = 0, []
for (x, y), n in sub.most_common():
    if x in piles and y in piles and len(pairs) < 8: pairs.append((x, y, n))
odd = {r['id']: float(r['dist']) for r in csv.DictReader(open(f'{A}/clusters.tsv'), delimiter='\t')}
inv = collections.defaultdict(list)
for r in keep: inv[name.get(cl[r['sid']])].append(r['sid'])
seen = set()
for x, y, n in pairs:
    for p in (x, y):
        for sid in sorted(inv[p], key=lambda s: -odd.get(s, 0))[:2]:
            if sid in seen: continue
            seen.add(sid); fw.writerow([sid, f'readers {x} / {y} ({n} splits on this pair); which pile?']); nf += 1
print(f'{len(keep)} tiles of {len(rows)} on {len(byL)} lines; {len(piles)} piles; {nf} focus tiles; pairs {pairs}')
