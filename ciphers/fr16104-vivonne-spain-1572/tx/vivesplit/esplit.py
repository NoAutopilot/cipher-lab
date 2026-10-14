#!/usr/bin/env python3
"""VIV-ESPLIT step 1 (PREREG-VIVESPLIT.md): is reader label y (and e) several signs a classifier can tell apart on an unseen leaf?

  python3 .../tx/vivesplit/esplit.py tiles    # f201r map vs its truth skeleton, items for labels e/y + positive control, bitmaps
  python3 .../tx/vivesplit/esplit.py gate     # leave-one-leaf-out: G0 positive control, G1 binomial, G2 permuted labels

Needs tx/vivcls/atlas (tx/vivcls/seg.py; f.201r crops by images/manifest.json "vivcls"). Writes tx/vivesplit/items.tsv,
tiles.npz, f201r_map_r2_truthskel.tsv, gate.json. Map inputs are reader labels only; `plain` is read only as the class.
"""
import csv, json, os, subprocess, sys, collections, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.dirname(HERE)
FOLD = os.path.dirname(TX)
REPO = os.path.abspath(os.path.join(FOLD, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import box_token_align as bta  # noqa: E402
import glyph_atlas as ga  # noqa: E402
VC = os.path.join(TX, 'vivcls')
ATLAS = os.path.join(VC, 'atlas')
BT = os.path.join(REPO, 'benchmark-tx')
TRUTH = {'f102r': os.path.join(BT, 'vivonne1573-f102r-dev2.truth.tsv'),
         'f103r': os.path.join(BT, 'vivonne1573-f103r-confirm2.truth.tsv'),
         'f201r': os.path.join(BT, 'vivonne1573-f201r-dev.truth.tsv')}
LEAVES = ('f102r', 'f103r', 'f201r')
CTRL = ('m', 'o', 'd', 'tz', 'g', 'p')  # p: PREREG Addendum A
SEED = 20261014
MIN_CLASS = 8


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def f201r_map():
    out = os.path.join(HERE, 'f201r_map_r2_truthskel.tsv')
    if os.path.exists(out):
        return rd(out)
    tk = os.path.join(HERE, 'topk_f201r_from_train.tsv')
    lj = os.path.join(ATLAS, 'labels.json')
    if not os.path.exists(lj):
        json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(lj, 'w'))
    ct = os.path.join(ATLAS, 'clusters.tsv')
    if not os.path.exists(ct):
        open(ct, 'w').write('kind\tid\tcluster\n')
    cmd = [sys.executable, os.path.join(REPO, 'tools/glyph_atlas.py'), 'classify', '--out', ATLAS, '--labels', lj, '--page', 'all',
           '--only-train-labels', '--train-labels', os.path.join(VC, 'train/labels_r2_both.tsv'), '--topk', '3', '--tsv', tk,
           '--features', 'hog', '--metric', 'none', '--knn', '5']
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stdout + p.stderr)
    sg = [s for s in rd(os.path.join(VC, 'map_signs.tsv')) if s['page'] == 'f201r']
    read = [dict(line=r['line'], pos=r['pos'], sign=r['ref_sign']) for r in rd(TRUTH['f201r'])]
    rows, _ = bta.build_map(sg, read, labels=bta.read_labels(topk=tk), lam=bta.LAM, loo=True)
    wr(out, ['sid', 'line', 'pos', 'op', 'labels', 'loo_pos'], rows)
    return rows


def maps():
    M = {'f102r': rd(os.path.join(VC, 'train/map_r2_f102r.tsv')), 'f103r': rd(os.path.join(VC, 'train/map_r2_f103r.tsv')),
         'f201r': f201r_map()}
    out = {}
    for leaf, rows in M.items():
        by = collections.defaultdict(list)
        share = collections.defaultdict(list)
        for r in rows:
            if r['sid']:
                by[(r['line'], str(r['pos']))].append(r)
                share[r['sid']].append(int(r['pos']))
        out[leaf] = (by, share)
    return out


def items():
    """label y / e items (class = plain) and positive-control items (class = reader label, ref_sign in truth, scored)."""
    out = []
    for leaf in LEAVES:
        for r in rd(TRUTH[leaf]):
            if r['ref_sign'] in ('y', 'e') and r['plain']:
                out.append(dict(set=r['ref_sign'], leaf=leaf, line=r['line'], pos=r['pos'], cls=r['plain']))
            elif r['status'] == 'scored' and r['ref_sign'] in CTRL and r['ref_sign'] in r['truth'].split('|'):
                out.append(dict(set='ctrl', leaf=leaf, line=r['line'], pos=r['pos'], cls=r['ref_sign']))
    return out


def cmd_tiles(_):
    S = {r['sid']: r for r in rd(os.path.join(ATLAS, 'signs.tsv'))}
    med = {k: v['median_h'] for k, v in json.load(open(os.path.join(ATLAS, 'pages.json'))).items()}
    M = maps()
    grey = {}
    rows, bms = [], []
    for it in items():
        by, share = M[it['leaf']]
        bx = by.get((it['line'], str(it['pos'])), [])
        if not bx:
            it.update(tier='none')
            rows.append(it)
            continue
        ops = {b['op'] for b in bx}
        boxes = [S[b['sid']] for b in bx]
        if len(bx) == 1 and ops == {'1:1'}:
            tier = 'T1'
        elif '1:2' in ops:
            tier = 'T3'
        else:
            tier = 'T2'
        pg = collections.Counter(b['page'] for b in boxes).most_common(1)[0][0]
        boxes = [b for b in boxes if b['page'] == pg]
        x0 = min(int(b['x']) for b in boxes); x1 = max(int(b['x']) + int(b['w']) for b in boxes)
        y0 = min(int(b['y']) for b in boxes); y1 = max(int(b['y']) + int(b['h']) for b in boxes)
        if tier == 'T3':
            sid = [b['sid'] for b in bx if b['op'] == '1:2'][0]
            ps = sorted(set(share[sid]))
            if len(ps) >= 2:
                k = ps.index(int(it['pos']))
                w = (x1 - x0) / len(ps)
                x0, x1 = int(x0 + k * w), int(x0 + (k + 1) * w)
        if pg not in grey:
            from PIL import Image
            g = np.asarray(Image.open(os.path.join(ATLAS, 'crops', pg + '.png')).convert('L'))
            grey[pg] = ga.binarise(g)
        ink = grey[pg][y0:y1, x0:x1]
        if ink.size == 0 or ink.sum() == 0:
            it.update(tier='empty')
            rows.append(it)
            continue
        ys, xs = np.nonzero(ink)
        ink = ink[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        mh = float(med[pg])
        it.update(tier=tier, page=pg, x0=x0, x1=x1, y0=y0, y1=y1, rh=round(ink.shape[0] / mh, 3), rw=round(ink.shape[1] / mh, 3),
                  idx=len(bms))
        bms.append(ga.bitmap(ink))
        rows.append(it)
    wr(os.path.join(HERE, 'items.tsv'), ['set', 'leaf', 'line', 'pos', 'cls', 'tier', 'page', 'x0', 'x1', 'y0', 'y1', 'rh', 'rw', 'idx'], rows)
    np.savez_compressed(os.path.join(HERE, 'tiles.npz'), bm=np.array(bms, np.uint8))
    c = collections.Counter((r['set'], r['leaf'], r['tier']) for r in rows)
    print(json.dumps({'|'.join(k): v for k, v in sorted(c.items())}, indent=0))


_CACHE = {}


def featurise(bm, rows, tr):
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    key = (id(bm), len(rows))
    if key not in _CACHE:  # fold-independent raw features, computed once per item set (speed only)
        _CACHE[key] = (ga._hog(bm), np.array([ga.zone_topo_feats(b, (float(r['rh']), float(r['rw']), 0.0)) for b, r in zip(bm, rows)]))
    H, Zt = _CACHE[key]
    s1 = StandardScaler().fit(H[tr]); pca = PCA(n_components=min(20, len(tr) - 1), random_state=SEED).fit(s1.transform(H[tr]))
    Z = pca.transform(s1.transform(H))
    s2 = StandardScaler().fit(Zt[tr])
    return np.hstack([Z, s2.transform(Zt)])


def lolo(bm, rows, y, perm_rng=None):
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
    pred = [None] * len(rows)
    base = [None] * len(rows)
    for te_leaf in LEAVES:
        tr = [i for i, r in enumerate(rows) if r['leaf'] != te_leaf]
        te = [i for i, r in enumerate(rows) if r['leaf'] == te_leaf]
        if not te:
            continue
        ytr = [y[i] for i in tr]
        if perm_rng is not None:
            ytr = ytr[:]
            # permute within each training leaf
            for lf in LEAVES:
                ids = [k for k, i in enumerate(tr) if rows[i]['leaf'] == lf]
                vals = [ytr[k] for k in ids]
                perm_rng.shuffle(vals)
                for k, v in zip(ids, vals):
                    ytr[k] = v
        X = featurise(bm, rows, tr)
        m = LDA(solver='lsqr', shrinkage='auto').fit(X[tr], ytr)
        p = m.predict(X[te])
        maj = collections.Counter(ytr).most_common(1)[0][0]
        for i, v in zip(te, p):
            pred[i] = v
            base[i] = maj
    return pred, base


def binom_sf(k, n, p):
    from math import comb
    return sum(comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def evaluate(bm_all, rows, name, nperm=200):
    bm = bm_all[[int(r['idx']) for r in rows]]
    y = [r['cls'] for r in rows]
    pred, base = lolo(bm, rows, y)
    n = len(y); k = sum(a == b for a, b in zip(pred, y)); kb = sum(a == b for a, b in zip(base, y))
    acc, p0 = k / n, kb / n
    # c_prop pooled
    cp = 0.0
    for te_leaf in LEAVES:
        te = [r['cls'] for r in rows if r['leaf'] == te_leaf]
        trc = collections.Counter(r['cls'] for r in rows if r['leaf'] != te_leaf)
        tot = sum(trc.values())
        cp += sum(trc[c] / tot for c in te)
    cp /= n
    pv = binom_sf(k, n, p0)
    perm = []
    for i in range(nperm):
        pp, _ = lolo(bm, rows, y, perm_rng=random.Random(SEED + i))
        perm.append(sum(a == b for a, b in zip(pp, y)) / n)
    perm = sorted(perm)
    p95 = perm[int(0.95 * nperm) - 1]
    pm = float(np.mean(perm))
    conf = collections.Counter((a, b) for a, b in zip(y, pred))
    per_leaf = {lf: round(sum(pred[i] == y[i] for i, r in enumerate(rows) if r['leaf'] == lf) / max(1, sum(r['leaf'] == lf for r in rows)), 4)
                for lf in LEAVES}
    res = dict(set=name, n=n, k=k, acc=round(acc, 4), p0=round(p0, 4), c_prop=round(cp, 4), binom_p=round(pv, 6),
               G1=pv < 0.05, perm_mean=round(pm, 4), perm_p95=round(p95, 4), perm_near_chance=pm <= max(p0, cp) + 0.10,
               G2=(acc > p95) and (pm <= max(p0, cp) + 0.10), per_leaf_acc=per_leaf,
               class_counts=dict(collections.Counter(y)), tiers=dict(collections.Counter(r['tier'] for r in rows)),
               confusion={f'{a}->{b}': v for (a, b), v in sorted(conf.items())})
    return res, pred


def cmd_gate(_):
    bm_all = np.load(os.path.join(HERE, 'tiles.npz'))['bm']
    allr = [r for r in rd(os.path.join(HERE, 'items.tsv')) if r['tier'] in ('T1', 'T2', 'T3')]
    out = {}
    for lab in ('y', 'e'):
        rr = [r for r in allr if r['set'] == lab]
        pooled = collections.Counter(r['cls'] for r in rr)
        leaves = collections.defaultdict(set)
        for r in rr:
            leaves[r['cls']].add(r['leaf'])
        classes = [c for c, v in pooled.most_common() if v >= MIN_CLASS and len(leaves[c]) >= 2]
        out[f'{lab}_classes'] = classes
        out[f'{lab}_pooled_after_tiling'] = dict(pooled)
        if len(classes) < 2:
            out[lab] = 'untestable: fewer than 2 classes reach the class rule (>= 8 pooled, >= 2 leaves)'
            continue
        rows = [r for r in rr if r['cls'] in classes]
        res, pred = evaluate(bm_all, rows, lab)
        out[lab] = res
        wr(os.path.join(HERE, f'pred_{lab}.tsv'), ['leaf', 'line', 'pos', 'cls', 'pred', 'tier'],
           [dict(r, pred=p) for r, p in zip(rows, pred)])
        # positive control matched to this label's per-leaf per-class counts
        cnt = collections.Counter((r['leaf'], r['cls']) for r in rows)
        rank = {c: CTRL[i] for i, c in enumerate(classes) if i < len(CTRL)}
        rng = random.Random(SEED)
        ctrl = []
        cr = [r for r in allr if r['set'] == 'ctrl']
        for (leaf, c), v in sorted(cnt.items()):
            pool = [r for r in cr if r['leaf'] == leaf and r['cls'] == rank[c]]
            rng.shuffle(pool)
            ctrl += pool[:v]
        cres, _ = evaluate(bm_all, ctrl, f'ctrl_for_{lab}')
        cres['G0'] = cres['G1']
        out[f'ctrl_for_{lab}'] = cres
        out[f'{lab}_PASS'] = bool(cres['G0'] and res['G1'] and res['G2'])
        print(json.dumps({k: v for k, v in res.items() if k != 'confusion'}), flush=True)
        print(json.dumps({k: v for k, v in cres.items() if k != 'confusion'}), flush=True)
    json.dump(out, open(os.path.join(HERE, 'gate.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k.endswith('PASS') or k.endswith('classes') or k == 'e'}, indent=1))


if __name__ == '__main__':
    {'tiles': cmd_tiles, 'gate': cmd_gate}[sys.argv[1]](sys.argv[2:])
