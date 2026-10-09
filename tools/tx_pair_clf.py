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
Never opens a truth file (benchmark-tx/*.truth.tsv, the `truth` column of no87_box_token.tsv) in the default secure
training domain.

X2b extension (TXE2-PAIR2, LANE TX-ENGINEER-2 round 3, 9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-3.md section X2b):
`--train-domain dev_tune` trains on no.87's OWN dev_tune boxes instead of the secure tiles of other leaves. Rules fixed here
before any apply:
  - Truth: read ONLY by read_truth_lines(), which takes the list of training lines and returns rows for those lines only
    (status 'scored', flag empty; columns line, pos, truth); the apply step never calls it. The truth file is
    benchmark-tx/birago1572-no87.truth.tsv (truth = the letter's homophone set). The box<->position map is read with
    read_named (no truth column).
  - Training tiles of pair a/b: training-line positions with a 1:1 box whose L sign (labels_dev_tune.tsv) is a or b; label
    a when a is in the truth set and b is not, b when b is and a is not; else (neither, both: a homophone pair) excluded.
  - Usability: >= 3 tiles per side, spread over >= 2 training lines.
  - Threshold: leave-one-line-out INSIDE the training lines gives each training tile a held-out p; at each tile m =
    p(partner of L) - p(L); for t in {0, 0.1, ..., 0.9} net(t) = #(m > t and label = partner) - #(m > t and label = L);
    t = argmax net (ties -> the larger t); the pair is disabled when max net <= 0. Model then refit on all training lines.
  - `--loo-lines` (apply/control on the training unit itself): each line h is predicted by a model whose training lines are
    the unit's other lines (h's truth never read for h's own fold). Without it, training is all dev_tune lines and --unit
    must be another unit (e.g. eval_heldout), whose truth is never read.
  - Control (`--seed S`): labels permuted within each pair's training tiles (rng seed S*1000 + fold), then the same rules.
  - Outputs: passX2b_pair2[_ctrlS]_<unit>.tsv; touched / train report under --touched-dir (benchmark-tx/txeng2/pair2).
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


# ---------------------------------------------------------------- X2b: train on no.87 dev_tune own ink (TXE2-PAIR2)
D_TRUTH = os.path.join(ROOT, 'benchmark-tx', 'birago1572-no87.truth.tsv')
DEV_UNIT = 'dev_tune'


def read_truth_lines(path, lines):
    """Training step only: truth rows (line, pos -> set of signs) for the named training lines; scored, unflagged."""
    lines = set(lines)
    out = {}
    with open(path) as f:
        rows = [l.rstrip('\n').split('\t') for l in f if not l.startswith('#')]
    head = rows[0]
    il, ip, it, ist, ifl = (head.index(c) for c in ('line', 'pos', 'truth', 'status', 'flag'))
    for r in rows[1:]:
        if r[il] in lines and r[ist] == 'scored' and not (r[ifl] if len(r) > ifl else ''):
            out[(r[il], r[ip])] = set(r[it].split('|'))
    return out


def box_map(path, lines):
    return {(r['line'], r['pos']): r['sid'] for r in read_named(path, MAP_COLS) if r['op'] == '1:1' and r['line'] in lines}


def fit_pairs_dev(a, train_lines, seed=0, fold=0, report=None):
    """Train every pair on the given dev_tune lines (truth read for those lines only). Returns {pair: (model, info)}."""
    sig = rd(os.path.join(a.atlas, 'signs.tsv'))
    idx = {r['sid']: i for i, r in enumerate(sig)}
    bm = np.load(os.path.join(a.atlas, 'bitmaps.npz'))['signs']
    Ld = [r for r in rd(os.path.join(a.units, f'labels_{DEV_UNIT}.tsv')) if r['line'] in set(train_lines)]
    truth = read_truth_lines(a.truth, train_lines)
    box = box_map(a.map, set(train_lines))
    rng = np.random.default_rng(seed * 1000 + fold) if seed else None
    out = {}
    for p in PAIRS:
        pa, pb = p.split('/')
        X, y, g, lsg = [], [], [], []
        for r in Ld:
            if r['sign'] not in (pa, pb):
                continue
            k = (r['line'], r['pos'])
            sid, ts = box.get(k), truth.get(k)
            if sid is None or sid not in idx or ts is None:
                continue
            ina, inb = pa in ts, pb in ts
            if ina == inb:
                continue
            X.append(feats(bm[idx[sid]]))
            y.append(int(inb))
            g.append(r['line'])
            lsg.append(int(r['sign'] == pb))
        y, g, lsg = np.array(y, int), np.array(g), np.array(lsg, int)
        if rng is not None and len(y):
            y = rng.permutation(y)
        info = dict(fold=fold, pair=p, n_a=int((y == 0).sum()), n_b=int((y == 1).sum()), lines=len(set(g)), t='',
                    net='', enabled=0, why='')
        if info['n_a'] < MIN_TILES or info['n_b'] < MIN_TILES or info['lines'] < MIN_LEAVES:
            info['why'] = 'too few tiles or lines'
            out[p] = (None, info)
            continue
        X = np.stack(X)
        ph = np.full(len(y), 0.5)
        for h in sorted(set(g)):
            tr = g != h
            if len(set(y[tr])) == 2:
                ph[~tr] = Model().fit(X[tr], y[tr]).p1(X[~tr])
        # m = p(partner of L) - p(L); class-1 prob ph
        p_partner = np.where(lsg == 1, 1 - ph, ph)
        m = 2 * p_partner - 1
        partner_lab = 1 - lsg
        best = None
        for t in TS:
            fl = m > t
            net = int((fl & (y == partner_lab)).sum() - (fl & (y == lsg)).sum())
            if best is None or net >= best[0]:
                best = (net, t)
        net, t = best
        en = int(net > 0)
        info.update(t=t, net=net, enabled=en, why='' if en else 'inner leave-one-line-out net <= 0')
        out[p] = (Model().fit(X, y) if en else None, info)
    return out, idx, bm


INFO2_COLS = ['fold', 'pair', 'n_a', 'n_b', 'lines', 't', 'net', 'enabled', 'why']


def apply_dev(a, seed):
    """Apply step: reads L, the map (no truth) and the models; never calls read_truth_lines for an applied line."""
    Lu = rd(os.path.join(a.units, f'labels_{a.unit}.tsv'))
    ulines = sorted({r['line'] for r in Lu})
    dev_lines = sorted({r['line'] for r in rd(os.path.join(a.units, f'labels_{DEV_UNIT}.tsv'))})
    if a.loo_lines:
        if a.unit != DEV_UNIT:
            raise SystemExit('--loo-lines applies to the training unit itself (dev_tune)')
        folds = [(i + 1, [h], [l for l in dev_lines if l != h]) for i, h in enumerate(ulines)]
    else:
        if set(ulines) & set(dev_lines):
            raise SystemExit('without --loo-lines the applied unit must not share lines with dev_tune')
        folds = [(0, ulines, dev_lines)]
    box = box_map(a.map, set(ulines))
    reports, out, touched = [], [], []
    for fold, alines, tlines in folds:
        assert not set(alines) & set(tlines)
        res, idx, bm = fit_pairs_dev(a, tlines, seed, fold)
        reports += [info for _, info in res.values()]
        for r in Lu:
            if r['line'] not in alines:
                continue
            s = sign = r['sign']
            cands = []
            for p, (m, info) in res.items():
                pa, pb = p.split('/')
                if m is None or s not in (pa, pb):
                    continue
                sid = box.get((r['line'], r['pos']))
                if sid is None or sid not in idx:
                    continue
                p1 = float(m.p1(feats(bm[idx[sid]])[None])[0])
                partner = pb if s == pa else pa
                pp = p1 if partner == pb else 1 - p1
                mg = 2 * pp - 1
                cands.append((mg - info['t'], partner, p, mg, info['t'], sid))
            if cands:
                best = max(cands)
                if best[0] > 0:
                    sign = best[1]
                for c in cands:
                    touched.append(dict(line=r['line'], pos=r['pos'], sid=c[5], L=s, pair=c[2], m=f'{c[3]:.3f}', t=c[4],
                                        out=sign))
            out.append(dict(line=r['line'], pos=r['pos'], sign=sign))
    order = {(r['line'], r['pos']): i for i, r in enumerate(Lu)}
    out.sort(key=lambda r: order[(r['line'], r['pos'])])
    tag = f'ctrl{seed}_' if seed else ''
    p = os.path.join(a.out_dir, f'passX2b_pair2_{tag}{a.unit}.tsv')
    wr(p, ['line', 'pos', 'sign'], out)
    wr(os.path.join(a.touched_dir, f'touched_{tag}{a.unit}.tsv'), ['line', 'pos', 'sid', 'L', 'pair', 'm', 't', 'out'],
       touched)
    wr(os.path.join(a.touched_dir, f'train_{tag}{a.unit}.tsv'), INFO2_COLS, reports)
    Lmap = {(r['line'], r['pos']): r['sign'] for r in Lu}
    ch = sum(1 for o in out if o['sign'] != Lmap[(o['line'], o['pos'])])
    en = sum(int(r['enabled']) for r in reports)
    print(f'X2b unit {a.unit} seed {seed} folds {len(folds)}: pair-folds enabled {en}/{len(reports)}; '
          f'positions considered {len({(t["line"], t["pos"]) for t in touched})}; changed {ch} -> {p}')
    return 0


def cmd_apply(a):
    return (apply_dev if a.train_domain == DEV_UNIT else apply_unit)(a, a.seed)


def cmd_control(a):
    for s in range(1, 6):
        (apply_dev if a.train_domain == DEV_UNIT else apply_unit)(a, s)
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
            p.add_argument('--touched-dir', default=None, help='default benchmark-tx/txeng2/pair (secure) or pair2 (dev_tune)')
            p.add_argument('--train-domain', choices=('secure', DEV_UNIT), default='secure',
                           help='secure: S-grade tiles of other leaves (X2); dev_tune: no.87 dev_tune own boxes (X2b)')
            p.add_argument('--loo-lines', action='store_true', help='X2b: leave-one-line-out over the dev_tune unit')
            p.add_argument('--truth', default=D_TRUTH, help='X2b training step only (training lines only)')
        p.set_defaults(fn=fn)
    a = ap.parse_args(argv)
    if getattr(a, 'touched_dir', 1) is None:
        a.touched_dir = os.path.join(ROOT, 'benchmark-tx', 'txeng2', 'pair2' if a.train_domain == DEV_UNIT else 'pair')
    return a.fn(a)


if __name__ == '__main__':
    sys.exit(main())
