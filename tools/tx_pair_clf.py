#!/usr/bin/env python3
"""Pair classifiers from known-answer tiles (TXE2-PAIR, LANE TX-ENGINEER-2 round 1, 9 Oct 2026; PREREG
benchmark-tx/PREREG-txeng2-1.md section X2). Read-free: no model call, no reader, no network.

For each look-alike pair of the Birago 1572 hand (PAIRS, the taxonomy's and TXE-C's list) a small classical classifier is
trained ONLY on the family's S-grade secure tiles (atlas/secure_tokens.tsv) from leaves other than no.87 (f178r, f178v,
f179r), bitmaps from atlas/bitmaps.npz (48x48, ink high). It is applied ONLY at a unit's positions whose line-read sign (L)
is a pair member; everything else keeps L.

Features: the bitmap cropped to its ink bounding box and resized to 32x32; 4x4 zoned ink density (16) + the raw 32x32
(1024) + HOG (scikit-image, 9 orientations, 8x8 cells, 2x2 blocks) when importable. Standardised. Model: logistic
regression (scikit-learn, C=0.1, class_weight balanced) when importable, else a numpy nearest-centroid with a softmax
over negative distances. The `--help` epilogue and train's first output line say which were used.

Usability (fixed before any apply): a pair is trained only when each side has >= 3 tiles and the pair's tiles span >= 2
leaves (leave-one-leaf-out needs a second leaf); otherwise it never moves anything.

Margin and threshold (fixed before any apply): margin m = p(partner) - p(L sign), in [-1, 1]; a position flips to the
partner only when m > t. t is chosen by leave-one-leaf-out over the training leaves only (never no.87): for every training
tile the held-out p is computed with its leaf left out; for each candidate t in {0, 0.1, ..., 0.9} the tiles whose held-out
|2p-1| > t are "decided", and t maximises the accuracy of decided tiles subject to decided >= 25% of the pair's tiles (ties
-> the smaller t). If that best accuracy does not beat the pair's chance rate (majority-class share), the pair is disabled.
An L sign in several usable pairs flips to the partner whose (m - t) is largest and positive.

Box <-> position map: atlas/no87_box_token.tsv, reading ONLY columns sid, fol, line, pos, sign, op (`--map`; enforced by
read_named, which refuses the `truth` column); op 1:1 rows only -- a position with no 1:1 box keeps L.

Subcommands:
  train   [--seed S]            per pair: tiles per side, leaves, LOLO accuracy at t, chance rate, t, enabled -> stdout
                                and, with --report FILE, a TSV. --seed > 0 permutes labels within each pair's training
                                set (the shuffled-label control).
  apply   --unit U [--seed S]   L = benchmark-tx/txeng/units/labels_<U>.tsv; writes --out-dir/passX2_pair_<U>.tsv
                                (line pos sign, every unit position); with --seed > 0 passX2_pair_ctrl<S>_<U>.tsv; and a
                                touched.tsv of the positions considered (line pos sid L pair m t out).
  control --unit U              apply with --seed 1..5.
Never opens a truth file (benchmark-tx/*.truth.tsv, the `truth` column of no87_box_token.tsv).
"""
import argparse, csv, os, sys
from collections import Counter, defaultdict
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAIRS = ['T18/T98', 'T90/T53', 'T76/T66', 'T76/T86', 'T76/T45', 'T64/T95', 'T64/T51', 'T50/T36', 'T92/T95', 'T92/T98',
         'T83/T24', 'T60/T86', 'T13/T64']
NO87 = ('f178r', 'f178v', 'f179r')
D_ATLAS = os.path.join(ROOT, 'ciphers', 'nevers-birago-fr3251-1572', 'atlas')
D_UNITS = os.path.join(ROOT, 'benchmark-tx', 'txeng', 'units')
D_OUT = os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87')
MAP_COLS = ('sid', 'fol', 'line', 'pos', 'sign', 'op')
TS = [round(0.1 * i, 1) for i in range(10)]
MIN_TILES, MIN_LEAVES, MIN_COVER = 3, 2, 0.25

try:
    from skimage.feature import hog
except Exception:
    hog = None
try:
    from sklearn.linear_model import LogisticRegression
except Exception:
    LogisticRegression = None


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def read_named(p, cols):
    """Read only the named columns; refuses to return a column named truth."""
    if 'truth' in cols:
        raise SystemExit('refused: the truth column is never read by this tool')
    with open(p, newline='') as f:
        r = csv.reader(f, delimiter='\t')
        head = next(r)
        ix = [head.index(c) for c in cols]
        return [{c: row[i] for c, i in zip(cols, ix)} for row in r]


def wr(p, cols, rows):
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
    with open(p, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])


def resize(a, n=32):
    from PIL import Image
    return np.asarray(Image.fromarray(a).resize((n, n), Image.BILINEAR), dtype=np.float32) / 255.0


def feats(bm):
    """bm: 48x48 uint8, ink high -> 1-D feature vector."""
    ys, xs = np.nonzero(bm > 64)
    a = bm[ys.min():ys.max() + 1, xs.min():xs.max() + 1] if len(ys) else bm
    s = resize(a)
    zones = s.reshape(4, 8, 4, 8).mean(axis=(1, 3)).ravel()
    parts = [zones, s.ravel()]
    if hog is not None:
        parts.append(hog(s, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2)).astype(np.float32))
    return np.concatenate(parts)


class Model:
    def fit(self, X, y):
        self.mu, self.sd = X.mean(0), X.std(0) + 1e-6
        Z = (X - self.mu) / self.sd
        if LogisticRegression is not None:
            self.m = LogisticRegression(C=0.1, class_weight='balanced', max_iter=2000).fit(Z, y)
        else:
            self.m = None
            self.c = np.stack([Z[y == k].mean(0) for k in (0, 1)])
        return self

    def p1(self, X):
        Z = (X - self.mu) / self.sd
        if self.m is not None:
            return self.m.predict_proba(Z)[:, list(self.m.classes_).index(1)]
        d = np.sqrt(((Z[:, None, :] - self.c[None]) ** 2).sum(-1)) / np.sqrt(Z.shape[1])
        e = np.exp(-d * 5)
        return e[:, 1] / e.sum(1)


def load_training(atlas):
    sig = rd(os.path.join(atlas, 'signs.tsv'))
    idx = {r['sid']: i for i, r in enumerate(sig)}
    bm = np.load(os.path.join(atlas, 'bitmaps.npz'))['signs']
    tiles = defaultdict(list)                       # code -> [(sid, page)]
    for r in rd(os.path.join(atlas, 'secure_tokens.tsv')):
        if r['grade'] == 'S' and r['page'] not in NO87 and r['sid'] in idx:
            tiles[r['code']].append((r['sid'], r['page']))
    return sig, idx, bm, tiles


def train_pairs(atlas, seed=0, log=None):
    sig, idx, bm, tiles = load_training(atlas)
    rng = np.random.default_rng(seed) if seed else None
    out = {}
    for p in PAIRS:
        a, b = p.split('/')
        ta, tb = tiles.get(a, []), tiles.get(b, [])
        leaves = sorted({pg for _, pg in ta + tb})
        info = dict(pair=p, n_a=len(ta), n_b=len(tb), leaves=len(leaves), lolo_acc='', decided='', chance='', t='',
                    enabled=0, why='')
        if len(ta) < MIN_TILES or len(tb) < MIN_TILES or len(leaves) < MIN_LEAVES:
            info['why'] = 'too few tiles or leaves'
            out[p] = (None, info)
            continue
        sids = [s for s, _ in ta + tb]
        pg = np.array([g for _, g in ta + tb])
        y = np.array([0] * len(ta) + [1] * len(tb))
        if rng is not None:
            y = rng.permutation(y)
        X = np.stack([feats(bm[idx[s]]) for s in sids])
        ph = np.full(len(y), np.nan)
        for g in leaves:
            tr = pg != g
            if len(set(y[tr])) < 2:
                ph[~tr] = 0.5                          # nothing to learn without this leaf: undecided
                continue
            ph[~tr] = Model().fit(X[tr], y[tr]).p1(X[~tr])
        chance = max(y.mean(), 1 - y.mean())
        conf, pred = np.abs(2 * ph - 1), (ph > 0.5).astype(int)
        best = None
        for t in TS:
            d = conf > t
            if d.sum() < MIN_COVER * len(y):
                continue
            acc = (pred[d] == y[d]).mean()
            if best is None or acc > best[0] + 1e-12:
                best = (acc, t, int(d.sum()))
        model = Model().fit(X, y) if len(set(y)) == 2 else None
        if best is None:
            info.update(chance=f'{chance:.3f}', why='no t with 25% coverage')
            out[p] = (None, info)
            continue
        acc, t, nd = best
        en = int(acc > chance and model is not None)
        info.update(lolo_acc=f'{acc:.3f}', decided=nd, chance=f'{chance:.3f}', t=t, enabled=en,
                    why='' if en else 'LOLO accuracy not above chance')
        out[p] = (model if en else None, info)
    return out, sig, idx, bm


INFO_COLS = ['pair', 'n_a', 'n_b', 'leaves', 'lolo_acc', 'decided', 'chance', 't', 'enabled', 'why']


def backend():
    return (f"features zones+raw32{'+HOG(scikit-image)' if hog else ' (no HOG: scikit-image missing)'}; model "
            f"{'logistic regression (scikit-learn)' if LogisticRegression else 'numpy nearest-centroid (no scikit-learn)'}")


def cmd_train(a):
    res, *_ = train_pairs(a.atlas, a.seed)
    print(backend() + (f'; labels permuted seed {a.seed}' if a.seed else ''))
    rows = [info for _, info in res.values()]
    print('\t'.join(INFO_COLS))
    for r in rows:
        print('\t'.join(str(r[c]) for c in INFO_COLS))
    if a.report:
        wr(a.report, INFO_COLS, rows)
    return 0


def apply_unit(a, seed):
    res, sig, idx, bm = train_pairs(a.atlas, seed)
    L = rd(os.path.join(a.units, f'labels_{a.unit}.tsv'))
    lines = {r['line'] for r in L}
    box = {}
    for r in read_named(a.map, MAP_COLS):
        if r['op'] == '1:1' and r['line'] in lines:
            box[(r['line'], r['pos'])] = r['sid']
    out, touched = [], []
    for r in L:
        s = r['sign']
        sign = s
        cands = []
        for p, (m, info) in res.items():
            pa, pb = p.split('/')
            if m is None or s not in (pa, pb):
                continue
            sid = box.get((r['line'], r['pos']))
            if sid is None or sid not in idx:
                continue
            p1 = float(m.p1(feats(bm[idx[sid]])[None])[0])     # p(class 1 = pb)
            partner = pb if s == pa else pa
            pp = p1 if partner == pb else 1 - p1
            mg = pp - (1 - pp)
            cands.append((mg - info['t'], partner, p, mg, info['t'], sid))
        if cands:
            best = max(cands)
            if best[0] > 0:
                sign = best[1]
            for c in cands:
                touched.append(dict(line=r['line'], pos=r['pos'], sid=c[5], L=s, pair=c[2], m=f'{c[3]:.3f}', t=c[4],
                                    out=sign))
        out.append(dict(line=r['line'], pos=r['pos'], sign=sign))
    tag = f'ctrl{seed}_' if seed else ''
    p = os.path.join(a.out_dir, f'passX2_pair_{tag}{a.unit}.tsv')
    wr(p, ['line', 'pos', 'sign'], out)
    tp = os.path.join(a.touched_dir, f'touched_{tag}{a.unit}.tsv')
    wr(tp, ['line', 'pos', 'sid', 'L', 'pair', 'm', 't', 'out'], touched)
    ch = sum(1 for o, r in zip(out, L) if o['sign'] != r['sign'])
    npos = len({(t['line'], t['pos']) for t in touched})
    print(f'unit {a.unit} seed {seed}: positions {len(out)}; L in a usable pair with a 1:1 box {npos}; changed {ch} -> {p}')
    return 0


def cmd_apply(a):
    return apply_unit(a, a.seed)


def cmd_control(a):
    for s in range(1, 6):
        apply_unit(a, s)
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='backend here: ' + backend())
    sp = ap.add_subparsers(dest='cmd', required=True)
    for name, fn in (('train', cmd_train), ('apply', cmd_apply), ('control', cmd_control)):
        p = sp.add_parser(name)
        p.add_argument('--atlas', default=D_ATLAS)
        p.add_argument('--seed', type=int, default=0)
        if name == 'train':
            p.add_argument('--report')
        else:
            p.add_argument('--unit', required=True)
            p.add_argument('--units', default=D_UNITS)
            p.add_argument('--map', default=os.path.join(D_ATLAS, 'no87_box_token.tsv'))
            p.add_argument('--out-dir', default=D_OUT)
            p.add_argument('--touched-dir', default=os.path.join(ROOT, 'benchmark-tx', 'txeng2', 'pair'))
        p.set_defaults(fn=fn)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == '__main__':
    sys.exit(main())
