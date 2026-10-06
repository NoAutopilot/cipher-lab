#!/usr/bin/env python3
"""R9-WVOSORT (6 Oct 2026): turn tools/glyph_atlas.py segment output for the ten f.23 cipher rows into sign_sorter.py
inputs. Strips (pages/*.png, shown in the sorter) are each cipher row's band +-30 px (bands.tsv). glyph_atlas segmented
seg_in/*.png: the same strips with everything outside the row's zone (eye centre -45 .. +55 px, zones.tsv) whitened,
so the clear rows written between the cipher rows do not merge into the cipher signs (make_seg_in.py). Kept: signs whose
vertical centre is inside the zone, not edge/gutter slivers, and (row C10) left of the signature (strip x < 900). Piles: k-means (fixed seed) on HOG of the
clipped tiles -- provisional shape piles k01.., NOT readings. Focus: the tiles whose two nearest pile centres are
closest (the grouping's own doubt), worded as a choice between two named piles.
  python3 build_inputs.py   (run from this folder; needs numpy, scikit-image, scikit-learn, pillow)"""
import csv, numpy as np
from PIL import Image
from skimage.feature import hog
from sklearn.cluster import KMeans

K, SEED, NFOCUS = 28, 1564, 24
zones = {r['page']: r for r in csv.DictReader(open('zones.tsv'), delimiter='\t')}
bands = {r['page']: r for r in csv.DictReader(open('bands.tsv'), delimiter='\t')}
signs = list(csv.DictReader(open('seg/signs.tsv'), delimiter='\t'))
marks = list(csv.DictReader(open('seg/marks.tsv'), delimiter='\t'))
kept, dropped = [], []
for s in signs:
    z = zones[s['page']]
    bl = float(z['slope']) * (int(float(s['x'])) + int(float(s['w'])) / 2) + float(z['baseline_at_x0'])
    top, bot = bl - 95, bl + 18
    x, y, w, h = [int(float(s[k])) for k in 'xywh']
    cy = y + h / 2
    if not (top <= cy <= bot):
        dropped.append((s['sid'], 'centre outside zone')); continue
    if s['page'] == 'f23_C10' and x > 900:
        dropped.append((s['sid'], 'signature')); continue
    if w < 10 or h > 6 * w or x > 2640:
        dropped.append((s['sid'], 'sliver/edge')); continue
    y0, y1 = y, y + h
    kept.append(dict(sid=s['sid'], page=s['page'], x=x, y=y0, w=w, h=y1 - y0))
# a clear-row letter that sits just above a sloping cipher row survives the zone mask as a short box riding high:
# drop a box whose bottom is more than 0.4 x the row's median sign height above the median bottom of its neighbours
# (+-300 px) and which is itself under 0.7 x that height
import statistics
k2 = []
for s in kept:
    nb = [t for t in kept if t['page'] == s['page'] and abs(t['x'] - s['x']) <= 300 and t is not s]
    mh = statistics.median(t['h'] for t in kept if t['page'] == s['page'])
    if nb:
        mb = statistics.median(t['y'] + t['h'] for t in nb)
        if s['y'] + s['h'] < mb - 0.4 * mh and s['h'] < 0.7 * mh:
            dropped.append((s['sid'], 'clear-row letter above the cipher row')); continue
    k2.append(s)
kept = k2
ids = {s['sid']: s for s in kept}
mk = []
for m in marks:
    s = ids.get(m['sid'])
    if not s: continue
    x, y, w, h = [int(float(m[k])) for k in 'xywh']
    if y + h >= s['y'] - 8:   # only a mark close above its sign (a clear-row letter further up is not one)
        mk.append(dict(x=x, y=y, w=w, h=h, sid=m['sid']))
imgs = {p: Image.open(f'pages/{p}.png').convert('L') for p in bands}
feats = []
for s in kept:
    t = imgs[s['page']].crop((s['x'], s['y'], s['x'] + s['w'], s['y'] + s['h']))
    side = max(t.size); c = Image.new('L', (side, side), 255); c.paste(t, ((side - t.width) // 2, (side - t.height) // 2))
    a = np.asarray(c.resize((48, 48)), float) / 255.0
    f = hog(1 - a, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
    feats.append(np.concatenate([f, [np.log(s['h'] / 60.0), np.log(s['w'] / 60.0)]]))
X = np.array(feats)
km = KMeans(n_clusters=K, n_init=20, random_state=SEED).fit(X)
d = km.transform(X)
order = np.argsort(d, axis=1)
lab = [f'k{l + 1:02d}' for l in km.labels_]
with open('signs.tsv', 'w') as f:
    f.write('sid\tpage\tx\ty\tw\th\n')
    for s in kept: f.write(f"{s['sid']}\t{s['page']}\t{s['x']}\t{s['y']}\t{s['w']}\t{s['h']}\n")
with open('labels.tsv', 'w') as f:
    f.write('sid\tsign\tfamily\n')
    for s, l in zip(kept, lab): f.write(f"{s['sid']}\t{l}\tshape\n")
with open('marks.tsv', 'w') as f:
    f.write('x\ty\tw\th\tsid\n')
    for m in mk: f.write(f"{m['x']}\t{m['y']}\t{m['w']}\t{m['h']}\t{m['sid']}\n")
ratio = d[np.arange(len(kept)), order[:, 0]] / d[np.arange(len(kept)), order[:, 1]]
with open('focus.tsv', 'w') as f:
    for i in np.argsort(-ratio)[:NFOCUS]:
        a, b = f'k{order[i, 0] + 1:02d}', f'k{order[i, 1] + 1:02d}'
        f.write(f"{kept[i]['sid']}\tShape grouping unsure: the {a} pile or the {b} pile, or a sign of its own? "
                f"(machine readers could not be matched sign by sign here; see README)\n")
with open('dropped.tsv', 'w') as f:
    f.write('sid\twhy\n'); f.writelines(f'{a}\t{b}\n' for a, b in dropped)
with open('cipher_lines.tsv', 'w') as f:
    f.write('# the ten f.23 cipher rows (interlinear clear rows are not tiled)\n' + ''.join((p + ('\t0\t900' if p == 'f23_C10' else '') + '\n') for p in bands))
print(f'kept {len(kept)} signs, dropped {len(dropped)}, marks {len(mk)}, piles {K}')
