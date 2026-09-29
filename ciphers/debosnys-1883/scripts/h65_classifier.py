#!/usr/bin/env python3
"""H65 (29 Sept 2026): per-glyph classifier over the six pixel-limited class groups, per h65/PREREG.md (pushed fc0198f4
before any score). kNN (k 3, distance-weighted) on 48x48 bitmaps (glyphs/bitmaps.npz), linear SVM as a side arm;
leave-one-out control first; then reader-read arbitration on R2-2's known-answer page (gating) and H63's (reported).
Writes h65/result.json."""
import os, sys, csv, json, collections
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
G = [('EIGHT', 'VENUS', 'THREE'), ('C-BAR-X', 'ARCH-DASH'), ('CIRC-O', 'BLOB'), ('O-SLASH', 'PHI'), ('II-DASH', 'CC-DASH'), ('S-CURL', 'DOUBLE-LOOP')]
GROUP = {m: i for i, g in enumerate(G) for m in g}
BASE = {'PCT-SLASH': 'PCT', 'X-DOT': 'X', 'X-CURL': 'X'}; MARKS = {'BLOB', 'BAR-SOLID', 'HOOK-L', 'DASH-V', '_', 'MARK'}
def f_r22(s): s = BASE.get(s, s); return '_' if s in MARKS else s
rows = list(csv.DictReader(open(os.path.join(root, 'glyphs/signs.tsv')), delimiter='\t')); IDX = {r['sid']: i for i, r in enumerate(rows)}
BM = np.load(os.path.join(root, 'glyphs/bitmaps.npz'))['signs'].reshape(len(rows), -1).astype(float) / 255.0
def sid(line, pos): pg, l = line.split('_L'); return f"{pg}_{int(l):02d}_{int(pos):03d}"
pages = {'R2-2': dict(truth=os.path.join(root, 'swarm/R2/R2-2/control/truth.tsv'), r1=os.path.join(root, 'swarm/R2/R2-2/control/reads_R1_sonnet.tsv'), r2=os.path.join(root, 'swarm/R2/R2-2/control/reads_R2_opus.tsv')),
         'H63': dict(truth=os.path.join(root, 'h63/truth.tsv'), r1=os.path.join(root, 'h63/reads_R1_opus.tsv'), r2=os.path.join(root, 'h63/reads_R2_opus.tsv'))}
EXCL = set()
for p in pages.values(): EXCL |= {r['source_box'] for r in csv.DictReader(open(p['truth']), delimiter='\t')}
train = collections.defaultdict(list)
for f in ('ciphertext_c1_draft.tsv', 'ciphertext_c2_draft.tsv', 'ciphertext_c34_draft.tsv'):
    for r in csv.DictReader(open(os.path.join(root, f)), delimiter='\t'):
        if not (r['why'] == 'agree-AB' or (r['why'] == 'settled-majority' and r['confidence'] == 'H')): continue
        s = r['sign'].rstrip('?'); k = sid(r['line'], r['position'])
        if s in GROUP and k in IDX and k not in EXCL: train[GROUP[s]].append((IDX[k], s))
out = dict(train_sizes={'/'.join(G[g]): collections.Counter(s for _, s in v) for g, v in train.items()}, loo={})
models = {}
tot = cor = maj = 0
for g, v in train.items():
    X = BM[[i for i, _ in v]]; y = np.array([s for _, s in v]); c = 0
    for i in range(len(v)):
        m = np.ones(len(v), bool); m[i] = False
        if len(set(y[m])) < 2: c += y[m][0] == y[i]; continue
        k = KNeighborsClassifier(n_neighbors=min(3, m.sum()), weights='distance').fit(X[m], y[m]); c += k.predict(X[i:i + 1])[0] == y[i]
    mj = collections.Counter(y).most_common(1)[0][1]
    out['loo']['/'.join(G[g])] = dict(n=len(v), knn_correct=int(c), majority=int(mj)); tot += len(v); cor += c; maj += mj
    models[g] = (KNeighborsClassifier(n_neighbors=3, weights='distance').fit(X, y), LinearSVC(C=1.0, max_iter=20000).fit(X, y) if len(set(y)) > 1 else None)
out['loo_pooled'] = dict(n=tot, knn_acc=round(cor / tot, 3), majority_acc=round(maj / tot, 3)); out['control_pass'] = cor > maj
print('LOO', out['loo_pooled'], out['control_pass'])
def score(p, arm):
    T = {r['crop']: (r['true'], r['source_box']) for r in csv.DictReader(open(p['truth']), delimiter='\t')}
    def reads(f): return {r[0].strip(): r[1].strip() for r in csv.reader(open(f), delimiter='\t') if len(r) >= 2 and not r[0].startswith('crop')}
    a, b = reads(p['r1']), reads(p['r2']); res = {}
    for mode in ('readers', 'arbitrated'):
        uns = wrong = 0; det = []
        for c, (t, sb) in T.items():
            x, y = f_r22(a.get(c, '?')), f_r22(b.get(c, '?'))
            if mode == 'arbitrated':
                for v in ('x', 'y'):
                    s = x if v == 'x' else y
                    if s in GROUP and sb in IDX:
                        m = models.get(GROUP[s])
                        if m: pr = (m[0] if arm == 'knn' else (m[1] or m[0])).predict(BM[IDX[sb]:IDX[sb] + 1])[0]; s = pr
                    if v == 'x': x = s
                    else: y = s
            tt = f_r22(t)
            if x != y: uns += 1; det.append((c, t, x, y))
            elif x != tt: wrong += 1; det.append((c, t, x, y))
        res[mode] = dict(unsettled=uns, agreed_wrong=wrong, err_pct=round(100 * (uns + wrong) / len(T), 1), residual=det)
    return res
if out['control_pass']:
    for arm in ('knn', 'svm'):
        for name, p in pages.items():
            r = score(p, arm); out[f'{name}:{arm}'] = r
            print(name, arm, {k: {kk: vv for kk, vv in v.items() if kk != 'residual'} for k, v in r.items()})
    out['kill'] = out['R2-2:knn']['arbitrated']['err_pct'] >= 15.6
    print('kill', out['kill'])
json.dump(out, open(os.path.join(root, 'h65', 'result.json'), 'w'), indent=1, default=str)
