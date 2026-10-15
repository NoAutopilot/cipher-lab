#!/usr/bin/env python3
"""VIV-GSPLIT (PREREG-VIVGSPLIT.md): does reader label g split by shape into the clerk's r and the clerk's f?

  python3 .../tx/vivgsplit/gsplit.py material      # the label-g tiles of f.102r, f.103r, f.201r with the clerk letter (no classification)
  python3 .../tx/vivgsplit/gsplit.py run           # leave-one-leaf-out with tools/glyph_atlas.py classify --boxes, 200 shuffled-label nulls
  python3 .../tx/vivgsplit/gsplit.py check         # re-run material + run and fail if result.json would change (rule 7)

Material: VIV-CLS round-2 label-aware map tiles at op 1:1 (one tile on the token): tx/vivcls/train/map_r2_f10{2,3}r.tsv against the truth
skeleton; f.201r's map is against passA (tx/vivcls/real/map_r2_f201r.tsv), carried to truth positions by tx/vivhuman/sets.aligned (as
tx/vivhuman/build_inputs.py --packet3b did). Class f = the label-g rows of tx/viv63_fkey/f_tiles.tsv; class r = truth rows with ref_sign g,
status scored, no flag, plain r. Instrument: classify --boxes (hog features, metric none: the setting --boxes supports) with
--only-train-labels; every training tile carries its own sid as its code, so k1..k5 are the five nearest training tiles and any labelling
(real or permuted) is read off the same neighbour list; features do not depend on labels at hog/none, so this is exact.
Untracked inputs: tx/vivcls/atlas (regenerate per images/manifest.json "vivcls").
"""
import argparse, collections, csv, json, os, subprocess, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
REPO = os.path.abspath(os.path.join(FOLD, '..', '..'))
sys.path.insert(0, os.path.join(FOLD, 'tx', 'vivhuman'))
import sets  # noqa: E402
ATLAS = os.path.join(FOLD, 'tx', 'vivcls', 'atlas')
BT = os.path.join(REPO, 'benchmark-tx')
LEAVES = ('f102r', 'f103r', 'f201r')
TRUTH = {'f102r': 'vivonne1573-f102r-dev2.truth.tsv', 'f103r': 'vivonne1573-f103r-confirm2.truth.tsv',
         'f201r': 'vivonne1573-f201r-dev.truth.tsv'}
SEED, NNULL, MEDIAN_H, KNN = 20261015, 200, 58, 1
W = os.path.join(HERE, 'work')


def rd(p):
    return sets.rd(p)


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def material():
    fset = {(r['line'], float(r['pos'])) for r in csv.DictReader(open(os.path.join(FOLD, 'tx', 'viv63_fkey', 'f_tiles.tsv')),
                                                                     delimiter='\t') if r['sign'] == 'g' and r['leaf'] in LEAVES}
    out, cover = [], collections.Counter()
    for leaf in LEAVES:
        truth = rd(os.path.join(BT, TRUTH[leaf]))
        trow = {(r['line'], r['pos']): r for r in truth}
        per = collections.defaultdict(list)
        if leaf == 'f201r':
            tl = collections.defaultdict(list)
            for r in truth:
                tl[r['line']].append(r)
            for ln in tl:
                tl[ln].sort(key=lambda r: float(r['pos']))
            A = sets.aligned(tl, rd(os.path.join(sets.OUTS, 'passA.tsv')))
            a2t = {(ln, ap): tp for (ln, tp), (sg, ap) in A.items()}
            for m in rd(sets.MAP):
                per[(m['line'], a2t.get((m['line'], m['pos'])))].append(m)
        else:
            for m in rd(os.path.join(FOLD, 'tx', 'vivcls', 'train', f'map_r2_{leaf}.tsv')):
                per[(m['line'], m['pos'])].append(m)
        for (ln, tp), ms in per.items():
            if tp is None:
                continue
            r = trow.get((ln, tp))
            if not r or r['ref_sign'] != 'g':
                continue
            isf = (ln, float(tp)) in fset
            isr = (not isf and r['status'] == 'scored' and not r['flag'] and r['plain'] == 'r')
            if not (isf or isr):
                continue
            cover[(leaf, 'f' if isf else 'r', 'all')] += 1
            if len(ms) != 1 or ms[0]['op'] != '1:1':
                continue
            cover[(leaf, 'f' if isf else 'r', 'tile')] += 1
            out.append(dict(leaf=leaf, line=ln, tpos=tp, sid=ms[0]['sid'], cls='f' if isf else 'r', plain=r['plain'], status=r['status']))
    out.sort(key=lambda r: (r['leaf'], r['line'], float(r['tpos'])))
    # the f anchors with no op-1:1 tile, for the record
    for leaf in LEAVES:
        pass
    wr(os.path.join(HERE, 'material.tsv'), ['leaf', 'line', 'tpos', 'sid', 'cls', 'plain', 'status'], out)
    summ = {f'{l}_{c}_{k}': cover[(l, c, k)] for l in LEAVES for c in 'fr' for k in ('all', 'tile')}
    print(json.dumps(summ))
    return out, summ


def classify_fold(mat, held):
    os.makedirs(W, exist_ok=True)
    sg = {r['sid']: r for r in rd(os.path.join(ATLAS, 'signs.tsv'))}
    tr = [m for m in mat if m['leaf'] != held]
    te = [m for m in mat if m['leaf'] == held]
    tl = os.path.join(W, f'train_{held}.tsv')
    wr(tl, ['box', 'code'], [dict(box=m['sid'], code=m['sid']) for m in tr])
    bx = os.path.join(W, f'boxes_{held}.tsv')
    wr(bx, ['box_id', 'page', 'x', 'y', 'w', 'h', 'line', 'pos', 'kind'],
       [dict(box_id=m['sid'], page=sg[m['sid']]['page'], x=sg[m['sid']]['x'], y=sg[m['sid']]['y'], w=sg[m['sid']]['w'],
             h=sg[m['sid']]['h'], line=m['line'], pos=m['tpos'], kind='sign') for m in te])
    lj = os.path.join(W, 'labels_stub.json')
    json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(lj, 'w'))
    out = os.path.join(W, f'pred_{held}.tsv')
    cmd = [sys.executable, os.path.join(REPO, 'tools', 'glyph_atlas.py'), 'classify', '--out', ATLAS, '--labels', lj,
           '--boxes', bx, '--boxes-median-h', str(MEDIAN_H), '--only-train-labels', '--train-labels', tl,
           '--knn', str(KNN), '--topk', '5', '--pool', '40', '--tsv', out]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stdout + p.stderr)
    return {r['box']: r for r in rd(out)}, tr, te, ' '.join(os.path.relpath(c, REPO) if os.path.isabs(c) else c for c in cmd[1:])


def prf(pairs):
    tp = sum(1 for t, p in pairs if t == 'f' and p == 'f')
    fp = sum(1 for t, p in pairs if t == 'r' and p == 'f')
    fn = sum(1 for t, p in pairs if t == 'f' and p == 'r')
    tn = sum(1 for t, p in pairs if t == 'r' and p == 'r')
    rec = tp / (tp + fn) if tp + fn else 0.0
    pre = tp / (tp + fp) if tp + fp else 0.0
    f1 = 2 * pre * rec / (pre + rec) if pre + rec else 0.0
    rrec = tn / (tn + fp) if tn + fp else 0.0
    rpre = tn / (tn + fn) if tn + fn else 0.0
    return dict(tp=tp, fp=fp, fn=fn, tn=tn, f_recall=round(rec, 4), f_precision=round(pre, 4), f1=round(f1, 4),
                r_recall=round(rrec, 4), r_precision=round(rpre, 4), n_f=tp + fn, n_r=tn + fp)


def predict(pred, te, lab):
    """1-NN: the label of the nearest training tile (k1). Report-only beside it: distance-weighted 5-NN over k1..k5."""
    p1, p5 = [], []
    for m in te:
        r = pred[m['sid']]
        p1.append((m['cls'], lab[r['k1']]))
        v = collections.Counter()
        for k in range(1, 6):
            if r[f'k{k}']:
                v[lab[r[f'k{k}']]] += 1 / (float(r[f'd{k}']) + 1e-6)
        p5.append((m['cls'], max(v, key=v.get)))
    return p1, p5


def cmd_run(a):
    mat = [m for m in rd(os.path.join(HERE, 'material.tsv'))]
    real = {m['sid']: m['cls'] for m in mat}
    folds, res = {}, {'folds': {}}
    for held in LEAVES:
        pred, tr, te, cmd = classify_fold(mat, held)
        folds[held] = (pred, tr, te)
        res['folds'][held] = dict(cmd=cmd, n_train_f=sum(m['cls'] == 'f' for m in tr), n_train_r=sum(m['cls'] == 'r' for m in tr))
    rng = np.random.default_rng(SEED)
    perms = []
    for _ in range(NNULL):
        lab = {}
        for leaf in LEAVES:
            ids = [m['sid'] for m in mat if m['leaf'] == leaf]
            cl = [real[s] for s in ids]
            rng.shuffle(cl)
            lab.update(dict(zip(ids, cl)))
        perms.append(lab)

    def pooled(lab):
        P1, P5, per = [], [], {}
        for held in LEAVES:
            pred, tr, te = folds[held]
            p1, p5 = predict(pred, te, lab)
            P1 += p1; P5 += p5
            per[held] = (p1, p5)
        return P1, P5, per
    P1, P5, per = pooled(real)
    res['pooled_1nn'] = prf(P1)
    res['pooled_5nn_report_only'] = prf(P5)
    for held in LEAVES:
        res['folds'][held].update(nn1=prf(per[held][0]), nn5_report_only=prf(per[held][1]))
        res['folds'][held]['testable'] = res['folds'][held]['nn1']['n_f'] >= 4
    nf1 = sorted(prf(pooled(l)[0])['f1'] for l in perms)
    nf5 = sorted(prf(pooled(l)[1])['f1'] for l in perms)
    res['null_f1_1nn'] = dict(mean=round(float(np.mean(nf1)), 4), p95=round(float(np.percentile(nf1, 95)), 4),
                              p99=round(float(np.percentile(nf1, 99)), 4), max=nf1[-1])
    res['null_f1_5nn_report_only'] = dict(mean=round(float(np.mean(nf5)), 4), p99=round(float(np.percentile(nf5, 99)), 4))
    g = res['pooled_1nn']
    res['gate'] = dict(recall=g['f_recall'] >= 0.60, precision=g['f_precision'] >= 0.60, f1_over_null_p99=g['f1'] > res['null_f1_1nn']['p99'])
    res['verdict'] = 'PASS' if all(res['gate'].values()) else 'FAIL'
    rows = []
    for held in LEAVES:
        pred, tr, te = folds[held]
        for m, (t1, q1), (t5, q5) in zip(te, per[held][0], per[held][1]):
            r = pred[m['sid']]
            rows.append(dict(leaf=held, line=m['line'], tpos=m['tpos'], sid=m['sid'], cls=m['cls'], pred_1nn=q1, pred_5nn=q5,
                             nn1=r['k1'], nn1_cls=real[r['k1']], d1=r['d1']))
    wr(os.path.join(HERE, 'per_tile.tsv'), ['leaf', 'line', 'tpos', 'sid', 'cls', 'pred_1nn', 'pred_5nn', 'nn1', 'nn1_cls', 'd1'], rows)
    json.dump(res, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'folds'}, indent=1))
    for held in LEAVES:
        f = res['folds'][held]
        print(held, 'train f/r', f['n_train_f'], f['n_train_r'], '1nn', f['nn1'], 'testable', f['testable'])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    sp.add_parser('material')
    sp.add_parser('run')
    sp.add_parser('check')
    a = ap.parse_args()
    if a.cmd == 'material':
        material()
    elif a.cmd == 'run':
        cmd_run(a)
    else:
        old = open(os.path.join(HERE, 'result.json')).read()
        material(); cmd_run(a)
        sys.exit(0 if open(os.path.join(HERE, 'result.json')).read() == old else 'result.json is stale')


if __name__ == '__main__':
    main()
