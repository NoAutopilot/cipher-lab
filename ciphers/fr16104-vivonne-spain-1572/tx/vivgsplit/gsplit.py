#!/usr/bin/env python3
"""VIV-GSPLIT (PREREG-VIVGSPLIT.md): does reader label g split by shape into the clerk's r and the clerk's f?

  python3 .../tx/vivgsplit/gsplit.py material      # the label-g tiles of f.102r, f.103r, f.201r with the clerk letter (no classification)
  python3 .../tx/vivgsplit/gsplit.py run           # leave-one-leaf-out with tools/glyph_atlas.py classify --boxes, 200 shuffled-label nulls
  python3 .../tx/vivgsplit/gsplit.py check         # re-run material + run and fail if result.json would change (rule 7)
  VIVGSPLIT2_SCRATCH=DIR gsplit.py material2 | run2 | check2   # VIV-GSPLIT2 (PREREG-VIVGSPLIT2.md): five leaves -> tx/vivgsplit2/
  VIVGSPLIT3_SCRATCH=DIR gsplit.py material3 | run3 | check3   # VIV-GSPLIT3 (PREREG-VIVGSPLIT3.md): every tile hand-cut -> tx/vivgsplit3/

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
    ct = os.path.join(ATLAS, 'clusters.tsv')           # as tx/vivcls/run.py ensure_atlas_stub: no clusters, header only
    if not os.path.exists(ct):
        open(ct, 'w').write('kind\tid\tcluster\n')
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


F191 = os.path.join(FOLD, 'images', 'p63', 'f191')
A191 = os.path.join(W, 'atlas191')


def glyph(args):
    p = subprocess.run([sys.executable, os.path.join(REPO, 'tools', 'glyph_atlas.py')] + args, capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stdout + p.stderr)
    return p.stdout


def f191_units():
    """PREREG Addendum A item 1: pen units of the 72 VIV-F191 crops, overlap deduped at the midpoint (as tx/vivcls/seg.py)."""
    man = json.load(open(os.path.join(F191, 'manifest.json')))['iiif_lines']
    cr = {}
    for e in man:
        c = e['crop']; ln = c.split('_')[3]; sg = int(c.split('_s')[-1].split('.')[0])
        cr[(ln, sg)] = dict(path=os.path.join(F191, c), x0=e['box'][0], x1=e['box'][2], page=f'f191r_{ln}_s{sg}')
    if not os.path.exists(os.path.join(A191, 'signs.tsv')):
        pages = []
        for k, e in sorted(cr.items()):
            pages += ['--page', f"{e['page']}={e['path']}"]
        glyph(['segment', '--out', A191, '--median-h', 'pool'] + pages)
    rows = rd(os.path.join(A191, 'signs.tsv'))
    byline = collections.defaultdict(list)
    for r in rows:
        _, ln, s = r['page'].split('_'); sg = int(s[1:]); e = cr[(ln, sg)]
        byline[ln].append(dict(r, seg=sg, xl=e['x0'] + int(r['x']), xc=e['x0'] + int(r['x']) + int(r['w']) / 2, img=e['path']))
    units = []
    for ln in sorted(byline):
        segs = sorted({s for (l2, s) in cr if l2 == ln})
        for b in byline[ln]:
            sg = b['seg']
            lo = -1e9 if sg == segs[0] else (cr[(ln, sg)]['x0'] + cr[(ln, sg - 1)]['x1']) / 2
            hi = 1e9 if sg == segs[-1] else (cr[(ln, sg + 1)]['x0'] + cr[(ln, sg)]['x1']) / 2
            if lo <= b['xc'] < hi:
                units.append(dict(sid=b['sid'], page='f191r', line=int(ln[1:]), x=int(b['xl']), w=b['w'], img=b['img'],
                                  cx=b['x'], cy=b['y'], cw=b['w'], ch=b['h'], crop_page=b['page']))
    units.sort(key=lambda u: (u['line'], u['x']))
    return units


def cmd_f191(a):
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    import box_token_align as bta
    os.makedirs(W, exist_ok=True)
    units = f191_units()
    usid = {u['sid']: u for u in units}
    lj = os.path.join(W, 'labels_stub.json')
    json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(lj, 'w'))
    bx = os.path.join(W, 'boxes_f191_all.tsv')
    wr(bx, ['box_id', 'image', 'x', 'y', 'w', 'h', 'line', 'pos', 'kind'],
       [dict(box_id=u['sid'], image=u['img'], x=u['cx'], y=u['cy'], w=u['cw'], h=u['ch'], line=u['line'], pos=u['x'], kind='sign') for u in units])
    tk = os.path.join(W, 'topk_f191_fullcode.tsv')
    glyph(['classify', '--out', ATLAS, '--labels', lj, '--boxes', bx, '--boxes-median-h', str(MEDIAN_H), '--only-train-labels',
           '--train-labels', os.path.join(FOLD, 'tx', 'vivcls', 'train', 'labels_r2_both.tsv'), '--knn', '5', '--topk', '3', '--tsv', tk])
    rec = list(csv.DictReader(open(os.path.join(FOLD, 'tx', 'viv63_f191', 'rec.tsv')), delimiter='\t', quoting=csv.QUOTE_NONE))  # a '"' sign
    read = [dict(line='f191r_' + r['line'], pos=r['pos'], sign=r['sign']) for r in rec]
    sg = [dict(sid=u['sid'], page='f191r', line=str(u['line']), x=str(u['x']), w=str(u['w'])) for u in units]
    rows, per = bta.build_map(sg, read, labels=bta.read_labels(topk=tk), lam=bta.LAM, loo=False)
    wr(os.path.join(HERE, 'map_f191r.tsv'), ['sid', 'line', 'pos', 'op', 'labels'], rows)
    by = collections.defaultdict(list)
    for r in rows:
        if r['sid']:
            by[(r['line'], str(r['pos']))].append(r)
    cov = {k: v[0]['sid'] for k, v in by.items() if len(v) == 1 and v[0]['op'] == '1:1'}
    gt = [r for r in rec if r['sign'] == 'g']
    tile = [(r, cov[('f191r_' + r['line'], r['pos'])]) for r in gt if ('f191r_' + r['line'], r['pos']) in cov]
    mat = rd(os.path.join(HERE, 'material.tsv'))
    tr = [m for m in mat if m['leaf'] in ('f102r', 'f103r')]
    tl = os.path.join(W, 'train_f191.tsv')
    wr(tl, ['box', 'code'], [dict(box=m['sid'], code=m['sid']) for m in tr])
    bg = os.path.join(W, 'boxes_f191_g.tsv')
    wr(bg, ['box_id', 'image', 'x', 'y', 'w', 'h', 'line', 'pos', 'kind'],
       [dict(box_id=s, image=usid[s]['img'], x=usid[s]['cx'], y=usid[s]['cy'], w=usid[s]['cw'], h=usid[s]['ch'], line=r['line'], pos=r['pos'],
             kind='sign') for r, s in tile])
    out = os.path.join(W, 'pred_f191_g.tsv')
    glyph(['classify', '--out', ATLAS, '--labels', lj, '--boxes', bg, '--boxes-median-h', str(MEDIAN_H), '--only-train-labels',
           '--train-labels', tl, '--knn', str(KNN), '--topk', '5', '--pool', '40', '--tsv', out])
    pr = {r['box']: r for r in rd(out)}
    cls = {m['sid']: m['cls'] for m in mat}
    res = []
    for r, s in tile:
        p = pr[s]
        res.append(dict(line=r['line'], pos=r['pos'], sid=s, rec_sign=r['sign'], rec_flag=r['flag'], pred_1nn=cls[p['k1']], nn1=p['k1'],
                        d1=p['d1'], crop_page=usid[s]['crop_page'], cx=usid[s]['cx'], cy=usid[s]['cy'], cw=usid[s]['cw'], ch=usid[s]['ch']))
    wr(os.path.join(HERE, 'f191r_g_pred.tsv'), list(res[0].keys()), res)
    summ = dict(units=len(units), g_tokens=len(gt), g_tileable=len(tile), pred_f=sum(r['pred_1nn'] == 'f' for r in res),
                ops=dict(collections.Counter(r['op'] for r in rows)))
    json.dump(summ, open(os.path.join(HERE, 'f191r_summary.json'), 'w'), indent=1)
    print(json.dumps(summ))


def cmd_side(a):
    """PREREG section 4, report-only: the owner's new-sign tiles (hand-cut boxes of tx/sorter_f191/signs.tsv on the VIV-F191 crops) under the
    f.102r+f.103r f/r model; 'neither' when d1 > p95 of the held-out truth tiles' d1 (per_tile.tsv)."""
    os.makedirs(W, exist_ok=True)
    ov = [r for r in csv.DictReader((l for l in open(os.path.join(FOLD, 'tx', 'sorter_f191', 'owner_override_2026-10-15.tsv'))
                                     if not l.startswith('#')), delimiter='\t', quoting=csv.QUOTE_NONE) if r['action'] == 'new-sign']
    sg = {r['sid']: r for r in rd(os.path.join(FOLD, 'tx', 'sorter_f191', 'signs.tsv'))}
    bx = os.path.join(W, 'boxes_side.tsv')
    wr(bx, ['box_id', 'image', 'x', 'y', 'w', 'h', 'line', 'pos', 'kind'],
       [dict(box_id=r['sid'], image=os.path.join(F191, sg[r['sid']]['page'] + '.jpg'), x=sg[r['sid']]['x'], y=sg[r['sid']]['y'],
             w=sg[r['sid']]['w'], h=sg[r['sid']]['h'], line=r['line'], pos=r['pos'], kind='sign') for r in ov])
    lj = os.path.join(W, 'labels_stub.json')
    out = os.path.join(W, 'pred_side.tsv')
    glyph(['classify', '--out', ATLAS, '--labels', lj, '--boxes', bx, '--boxes-median-h', str(MEDIAN_H), '--only-train-labels',
           '--train-labels', os.path.join(W, 'train_f191.tsv'), '--knn', str(KNN), '--topk', '5', '--pool', '40', '--tsv', out])
    pr = {r['box']: r for r in rd(out)}
    cls = {m['sid']: m['cls'] for m in rd(os.path.join(HERE, 'material.tsv'))}
    thr = float(np.percentile([float(r['d1']) for r in rd(os.path.join(HERE, 'per_tile.tsv'))], 95))
    res = []
    for r in ov:
        p = pr[r['sid']]
        near = [cls[p[f'k{k}']] for k in range(1, 6) if p[f'k{k}']]
        df = min((float(p[f'd{k}']) for k in range(1, 6) if p[f'k{k}'] and cls[p[f'k{k}']] == 'f'), default=float('nan'))
        dr = min((float(p[f'd{k}']) for k in range(1, 6) if p[f'k{k}'] and cls[p[f'k{k}']] == 'r'), default=float('nan'))
        res.append(dict(line=r['line'], pos=r['pos'], sid=r['sid'], qid=r['qid'], owner_pile=r['new_sign'], rec_sign=r['rec_sign'],
                        nn1_cls=cls[p['k1']], d1=p['d1'], d_f_top5=('%.3f' % df) if df == df else '', d_r_top5=('%.3f' % dr) if dr == dr else '',
                        top5=''.join(near), call=('neither' if float(p['d1']) > thr else 'nearer ' + cls[p['k1']])))
    wr(os.path.join(HERE, 'side_owner_newsign.tsv'), list(res[0].keys()), res)
    print(f'neither threshold (p95 held-out truth d1) {thr:.3f}')
    for r in res:
        print('\t'.join(str(r[k]) for k in res[0]))


# ---------------------------------------------------------------- VIV-GSPLIT2 (PREREG-VIVGSPLIT2.md): five truth leaves
OUT2 = os.path.join(FOLD, 'tx', 'vivgsplit2')
SCR = os.environ.get('VIVGSPLIT2_SCRATCH', '')     # where the f.202r crops were cut (VIV-67C cuts them in a scratchpad)
NEW = {'f202r': ('vivonne1573-f202r-dev.truth.tsv', lambda: os.path.join(SCR, 'p67c', 'manifest.json')),
       'f211v': ('vivonne1573-f211v-dev.truth.tsv', lambda: os.path.join(FOLD, 'images', 'p70c', 'manifest.json'))}
LEAVES2 = ('f102r', 'f103r', 'f201r', 'f202r', 'f211v')
RCAP = 20


def leaf_units(leaf, man):
    """PREREG-VIVGSPLIT2 s.1: pen units of one leaf's line crops (segment --median-h pool), overlap deduped at the midpoint,
    as f191_units / tx/vivcls/seg.py."""
    d = os.path.dirname(man)
    ents = json.load(open(man))['iiif_lines']
    cr = {}
    for e in ents:
        c = e['crop']
        if f'_{leaf}_L' not in c:
            continue
        ln = c.split(f'_{leaf}_')[1].split('_')[0]; sg = int(c.split('_s')[-1].split('.')[0])
        cr[(ln, sg)] = dict(path=os.path.join(d, c), x0=e['box'][0], x1=e['box'][2], page=f'{leaf}_{ln}_s{sg}')
    at = os.path.join(W, f'atlas_{leaf}')
    if not os.path.exists(os.path.join(at, 'signs.tsv')):
        pages = []
        for k, e in sorted(cr.items()):
            pages += ['--page', f"{e['page']}={e['path']}"]
        glyph(['segment', '--out', at, '--median-h', 'pool'] + pages)
    byline = collections.defaultdict(list)
    for r in rd(os.path.join(at, 'signs.tsv')):
        _, ln, s_ = r['page'].split('_'); sg = int(s_[1:]); e = cr[(ln, sg)]
        byline[ln].append(dict(r, seg=sg, xl=e['x0'] + int(r['x']), xc=e['x0'] + int(r['x']) + int(r['w']) / 2, img=e['path']))
    units = []
    for ln in sorted(byline):
        segs = sorted({s_ for (l2, s_) in cr if l2 == ln})
        for b in byline[ln]:
            sg = b['seg']
            lo = -1e9 if sg == segs[0] else (cr[(ln, sg)]['x0'] + cr[(ln, sg - 1)]['x1']) / 2
            hi = 1e9 if sg == segs[-1] else (cr[(ln, sg + 1)]['x0'] + cr[(ln, sg)]['x1']) / 2
            if lo <= b['xc'] < hi:
                units.append(dict(sid=b['sid'], line=int(ln[1:]), x=int(b['xl']), w=b['w'], img=b['img'],
                                  cx=b['x'], cy=b['y'], cw=b['w'], ch=b['h']))
    units.sort(key=lambda u: (u['line'], u['x']))
    return units


def new_leaf_tiles(leaf):
    """Map one new leaf's units to its truth skeleton label-aware (PREREG-VIVGSPLIT Addendum A's map); return f and r tiles."""
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    import box_token_align as bta
    tf, manf = NEW[leaf]
    units = leaf_units(leaf, manf())
    usid = {u['sid']: u for u in units}
    lj = os.path.join(W, 'labels_stub.json')
    json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(lj, 'w'))
    bx = os.path.join(W, f'boxes2_{leaf}_all.tsv')
    wr(bx, ['box_id', 'image', 'x', 'y', 'w', 'h', 'line', 'pos', 'kind'],
       [dict(box_id=u['sid'], image=u['img'], x=u['cx'], y=u['cy'], w=u['cw'], h=u['ch'], line=u['line'], pos=u['x'], kind='sign') for u in units])
    tk = os.path.join(W, f'topk2_{leaf}_fullcode.tsv')
    if not os.path.exists(tk):
        glyph(['classify', '--out', ATLAS, '--labels', lj, '--boxes', bx, '--boxes-median-h', str(MEDIAN_H), '--only-train-labels',
               '--train-labels', os.path.join(FOLD, 'tx', 'vivcls', 'train', 'labels_r2_both.tsv'), '--knn', '5', '--topk', '3', '--tsv', tk])
    truth = rd(os.path.join(BT, tf))
    read = [dict(line=r['line'], pos=r['pos'], sign=r['ref_sign']) for r in truth]
    sg = [dict(sid=u['sid'], page=leaf, line=str(u['line']), x=str(u['x']), w=str(u['w'])) for u in units]
    rows, per = bta.build_map(sg, read, labels=bta.read_labels(topk=tk), lam=bta.LAM, loo=False)
    wr(os.path.join(OUT2, f'map_{leaf}.tsv'), ['sid', 'line', 'pos', 'op', 'labels'], rows)
    by = collections.defaultdict(list)
    for r in rows:
        if r['sid']:
            by[(r['line'], str(r['pos']))].append(r)
    cov = {k: v[0]['sid'] for k, v in by.items() if len(v) == 1 and v[0]['op'] == '1:1'}
    out, cnt = [], collections.Counter()
    for r in truth:
        if r['ref_sign'] != 'g':
            continue
        isf = r['plain'] == 'f'
        isr = r['status'] == 'scored' and not r['flag'] and r['plain'] == 'r'
        if not (isf or isr):
            continue
        c = 'f' if isf else 'r'
        cnt[(c, 'all')] += 1
        s_ = cov.get((r['line'], str(r['pos'])))
        if not s_:
            continue
        cnt[(c, 'tile')] += 1
        u = usid[s_]
        out.append(dict(leaf=leaf, line=r['line'], tpos=r['pos'], sid=s_, cls=c, plain=r['plain'], status=r['status'], src='map',
                        image=os.path.relpath(u['img'], REPO) if u['img'].startswith(REPO) else u['img'], x=u['cx'], y=u['cy'], w=u['cw'], h=u['ch']))
    return out, cnt


def material2():
    """PREREG-VIVGSPLIT2 s.1: the VIV-GSPLIT material + f.202r/f.211v map tiles (r capped at 20 per leaf, seeded) + hand-cut `whole` f boxes."""
    import random
    os.makedirs(OUT2, exist_ok=True); os.makedirs(W, exist_ok=True)
    sg = {r['sid']: r for r in rd(os.path.join(ATLAS, 'signs.tsv'))}
    pj = json.load(open(os.path.join(ATLAS, 'pages.json')))
    mat = []
    for m in rd(os.path.join(HERE, 'material.tsv')):
        a = sg[m['sid']]
        img = pj[a['page']]['image']
        mat.append(dict(m, src='map', image=os.path.relpath(img, REPO), x=a['x'], y=a['y'], w=a['w'], h=a['h']))
    summ = {}
    for leaf in ('f202r', 'f211v'):
        t, cnt = new_leaf_tiles(leaf)
        r = sorted([m for m in t if m['cls'] == 'r'], key=lambda m: (m['line'], float(m['tpos'])))
        if len(r) > RCAP:
            r = random.Random(SEED).sample(r, RCAP)
        mat += [m for m in t if m['cls'] == 'f'] + r
        summ[leaf] = {f'{c}_{k}': cnt[(c, k)] for c in 'fr' for k in ('all', 'tile')}
        summ[leaf]['r_used'] = len(r)
    hc = os.path.join(OUT2, 'boxes_handcut.tsv')
    nh = collections.Counter()
    if os.path.exists(hc):
        for h in rd(hc):
            nh[h['verdict']] += 1
            if h['verdict'] == 'whole':
                mat.append(dict(leaf=h['leaf'], line=h['line'], tpos=h['tpos'], sid='hc_' + h['line'] + '_' + h['tpos'], cls='f', plain='f',
                                status='excluded:letter-off-key', src='handcut', image=h['image'], x=h['x'], y=h['y'], w=h['w'], h=h['h']))
    summ['handcut'] = dict(nh)
    mat.sort(key=lambda m: (LEAVES2.index(m['leaf']), m['line'], float(m['tpos'])))
    wr(os.path.join(OUT2, 'material.tsv'), ['leaf', 'line', 'tpos', 'sid', 'cls', 'plain', 'status', 'src', 'image', 'x', 'y', 'w', 'h'], mat)
    summ['N_f'] = sum(m['cls'] == 'f' for m in mat); summ['N_r'] = sum(m['cls'] == 'r' for m in mat)
    summ['per_leaf'] = {l: [sum(m['leaf'] == l and m['cls'] == c for m in mat) for c in 'fr'] for l in LEAVES2}
    json.dump(summ, open(os.path.join(OUT2, 'material_summary.json'), 'w'), indent=1)
    print(json.dumps(summ))
    return mat


def recut_feats(mat):
    """PREREG-VIVGSPLIT2 s.2: classify --boxes's query side for every tile: glyph_atlas.jitter_tiles unjittered re-cut (rel 0.78, mh 58)
    projected by glyph_atlas.feats(project=True) fitted on the unchanged tx/vivcls/atlas."""
    sys.path.insert(0, os.path.join(REPO, 'tools'))
    import glyph_atlas as ga, cv2
    rows = ga.read(ATLAS, 'signs.tsv')
    bm = np.load(os.path.join(ATLAS, 'bitmaps.npz'))['signs']
    _, proj = ga.feats(bm, rows, project=True)
    inks, tiles = {}, []
    for m in mat:
        src = m['image'] if os.path.isabs(m['image']) else os.path.join(REPO, m['image'])
        if src not in inks:
            g = cv2.imread(src, cv2.IMREAD_GRAYSCALE)
            if g is None:
                sys.exit(f'cannot read {src}')
            k = ga.binarise(g, 0.78)
            inks[src] = cv2.morphologyEx(k, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8)) if min(g.shape) > 2500 else k
        rr = dict(x=int(float(m['x'])), y=int(float(m['y'])), w=max(1, int(float(m['w']))), h=max(1, int(float(m['h']))))
        tiles.append(ga.jitter_tiles(inks[src], rr, MEDIAN_H, 0, 0, 0.0, np.random.default_rng(0))[0])
    return proj(np.array([t[0] for t in tiles]), [t[1] for t in tiles], [t[2] for t in tiles])


def loo2(mat, X, leaves, lab):
    """1-NN (and distance-weighted 5-NN, report-only) leave-one-leaf-out; lab: {index: class} for the training side."""
    P1, P5, per, near = [], [], {}, {}
    for held in leaves:
        tr = [i for i, m in enumerate(mat) if m['leaf'] != held]
        te = [i for i, m in enumerate(mat) if m['leaf'] == held]
        p1, p5 = [], []
        for i in te:
            d = np.linalg.norm(X[tr] - X[i], axis=1)
            o = np.argsort(d, kind='stable')
            j = tr[o[0]]
            p1.append((mat[i]['cls'], lab[j])); near[i] = (j, float(d[o[0]]))
            v = collections.Counter()
            for q in o[:5]:
                v[lab[tr[q]]] += 1 / (float(d[q]) + 1e-6)
            p5.append((mat[i]['cls'], max(v, key=v.get)))
        P1 += p1; P5 += p5; per[held] = (p1, p5)
    return P1, P5, per, near


def gate_run(mat, X, leaves, tag):
    real = {i: m['cls'] for i, m in enumerate(mat)}
    P1, P5, per, near = loo2(mat, X, leaves, real)
    rng = np.random.default_rng(SEED)
    nf1, nf5 = [], []
    for _ in range(NNULL):
        lab = {}
        for leaf in leaves:
            ids = [i for i, m in enumerate(mat) if m['leaf'] == leaf]
            cl = [real[i] for i in ids]
            rng.shuffle(cl)
            lab.update(dict(zip(ids, cl)))
        a, b, _, _ = loo2(mat, X, leaves, lab)
        nf1.append(prf(a)['f1']); nf5.append(prf(b)['f1'])
    nf1.sort(); nf5.sort()
    res = dict(tag=tag, pooled_1nn=prf(P1), pooled_5nn_report_only=prf(P5), folds={})
    for h in leaves:
        res['folds'][h] = dict(nn1=prf(per[h][0]), nn5_report_only=prf(per[h][1]))
        res['folds'][h]['testable'] = res['folds'][h]['nn1']['n_f'] >= 4
    res['null_f1_1nn'] = dict(mean=round(float(np.mean(nf1)), 4), p95=round(float(np.percentile(nf1, 95)), 4),
                              p99=round(float(np.percentile(nf1, 99)), 4), max=nf1[-1])
    res['null_f1_5nn_report_only'] = dict(mean=round(float(np.mean(nf5)), 4), p99=round(float(np.percentile(nf5, 99)), 4))
    g = res['pooled_1nn']
    res['gate'] = dict(recall=g['f_recall'] >= 0.60, precision=g['f_precision'] >= 0.60, f1_over_null_p99=g['f1'] > res['null_f1_1nn']['p99'])
    res['verdict'] = 'PASS' if all(res['gate'].values()) else 'FAIL'
    rows = []
    for h in leaves:
        te = [i for i, m in enumerate(mat) if m['leaf'] == h]
        for i, (t1, q1), (t5, q5) in zip(te, per[h][0], per[h][1]):
            j, d = near[i]
            rows.append(dict(leaf=h, line=mat[i]['line'], tpos=mat[i]['tpos'], sid=mat[i]['sid'], src=mat[i]['src'], cls=t1, pred_1nn=q1,
                             pred_5nn=q5, nn1=mat[j]['sid'], nn1_cls=mat[j]['cls'], d1='%.3f' % d))
    return res, rows


def cmd_run2(a):
    mat = rd(os.path.join(OUT2, 'material.tsv'))
    X = recut_feats(mat)
    out = {}
    old = [i for i, m in enumerate(mat) if m['leaf'] in LEAVES and m['src'] == 'map' and m['sid'] in
           {r['sid'] for r in rd(os.path.join(HERE, 'material.tsv'))}]
    b, _ = gate_run([mat[i] for i in old], X[old], LEAVES, 'bridge_viv_gsplit_material_recut')
    out['bridge_report_only'] = b
    leaves = [l for l in LEAVES2 if any(m['leaf'] == l for m in mat)]
    r, rows = gate_run(mat, X, leaves, 'registered')
    out['registered'] = r
    mo = [i for i, m in enumerate(mat) if m['src'] == 'map']
    lm = [l for l in leaves if any(mat[i]['leaf'] == l for i in mo)]
    out['map_only_report_only'], _ = gate_run([mat[i] for i in mo], X[mo], lm, 'map_only')
    out['N_f'] = sum(m['cls'] == 'f' for m in mat); out['N_r'] = sum(m['cls'] == 'r' for m in mat)
    out['f191_step_runs'] = out['N_f'] >= 12 and r['verdict'] == 'PASS'
    wr(os.path.join(OUT2, 'per_tile.tsv'), list(rows[0].keys()), rows)
    json.dump(out, open(os.path.join(OUT2, 'result.json'), 'w'), indent=1)
    for k in ('bridge_report_only', 'registered', 'map_only_report_only'):
        x = out[k]
        print(k, 'pooled', x['pooled_1nn'], 'null', x['null_f1_1nn'], x['verdict'])
        for h, f in x['folds'].items():
            print('   ', h, f['nn1']['n_f'], f['nn1']['n_r'], 'rec', f['nn1']['f_recall'], 'pre', f['nn1']['f_precision'], 'f1', f['nn1']['f1'])
    print('N_f', out['N_f'], 'N_r', out['N_r'], 'f191 step runs', out['f191_step_runs'])


OUT3 = os.path.join(FOLD, 'tx', 'vivgsplit3')
LEAVES3 = ('f102r', 'f103r', 'f201r', 'f201v', 'f211r', 'f202r', 'f211v')


def material3():
    """PREREG-VIVGSPLIT3 s.1-2: only hand-cut boxes (tx/vivgsplit3/boxes_handcut.tsv), verdict whole, registered yes; no map tile."""
    scr = os.environ.get('VIVGSPLIT3_SCRATCH', '')
    mat = []
    for h in rd(os.path.join(OUT3, 'boxes_handcut.tsv')):
        if h['verdict'] != 'whole' or h['registered'] != 'yes':
            continue
        img = h['image'].replace('$VIVGSPLIT3_SCRATCH', scr)
        mat.append(dict(leaf=h['leaf'], line=h['line'], tpos=h['tpos'], sid=h['tid'], cls=h['cls'], plain=h['cls'], src='handcut',
                        image=img if os.path.isabs(img) else img, x=h['x'], y=h['y'], w=h['w'], h=h['h']))
    mat.sort(key=lambda m: (LEAVES3.index(m['leaf']), m['line'], float(m['tpos'])))
    summ = dict(N_f=sum(m['cls'] == 'f' for m in mat), N_r=sum(m['cls'] == 'r' for m in mat),
                per_leaf={l: [sum(m['leaf'] == l and m['cls'] == c for m in mat) for c in 'fr'] for l in LEAVES3})
    return mat, summ


def cmd_run3(a):
    mat, summ = material3()
    X = recut_feats(mat)
    leaves = [l for l in LEAVES3 if any(m['leaf'] == l for m in mat)]
    r, rows = gate_run(mat, X, leaves, 'registered_handcut')
    # VIV-GSPLIT3C (Addendum B): the r sample is complete when every registered r target is logged whole/unsure/none
    logged = {h['tid'] for h in rd(os.path.join(OUT3, 'boxes_handcut.tsv')) if h['verdict'] in ('whole', 'unsure', 'none')}
    complete = all(t['tid'] in logged for t in rd(os.path.join(OUT3, 'targets.tsv')) if t['cls'] == 'r')
    out = dict(material=summ, registered=r, r_sample_complete=complete,
               f191_step_runs=summ['N_f'] >= 12 and r['verdict'] == 'PASS' and complete)
    wr(os.path.join(OUT3, 'per_tile.tsv'), list(rows[0].keys()), rows)
    json.dump(out, open(os.path.join(OUT3, 'result.json'), 'w'), indent=1)
    print('material', json.dumps(summ))
    print('registered pooled', r['pooled_1nn'], 'null', r['null_f1_1nn'], r['verdict'], r['gate'])
    print('5nn report-only', r['pooled_5nn_report_only'], r['null_f1_5nn_report_only'])
    for h, f in r['folds'].items():
        print('   ', h, f['nn1']['n_f'], f['nn1']['n_r'], 'rec', f['nn1']['f_recall'], 'pre', f['nn1']['f_precision'], 'f1', f['nn1']['f1'])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    sp.add_parser('material')
    sp.add_parser('run')
    sp.add_parser('check')
    sp.add_parser('f191')
    sp.add_parser('side')
    sp.add_parser('material2')
    sp.add_parser('run2')
    sp.add_parser('check2')
    sp.add_parser('material3')
    sp.add_parser('run3')
    sp.add_parser('check3')
    a = ap.parse_args()
    if a.cmd == 'material':
        material()
    elif a.cmd == 'run':
        cmd_run(a)
    elif a.cmd == 'f191':
        cmd_f191(a)
    elif a.cmd == 'side':
        cmd_side(a)
    elif a.cmd == 'material2':
        material2()
    elif a.cmd == 'run2':
        cmd_run2(a)
    elif a.cmd == 'material3':
        print(json.dumps(material3()[1]))
    elif a.cmd == 'run3':
        cmd_run3(a)
    elif a.cmd == 'check3':
        old = open(os.path.join(OUT3, 'result.json')).read()
        cmd_run3(a)
        sys.exit(0 if open(os.path.join(OUT3, 'result.json')).read() == old else 'tx/vivgsplit3/result.json is stale')
    elif a.cmd == 'check2':
        old = open(os.path.join(OUT2, 'result.json')).read()
        cmd_run2(a)
        sys.exit(0 if open(os.path.join(OUT2, 'result.json')).read() == old else 'tx/vivgsplit2/result.json is stale')
    else:
        old = open(os.path.join(HERE, 'result.json')).read()
        material(); cmd_run(a)
        sys.exit(0 if open(os.path.join(HERE, 'result.json')).read() == old else 'result.json is stale')


if __name__ == '__main__':
    main()
