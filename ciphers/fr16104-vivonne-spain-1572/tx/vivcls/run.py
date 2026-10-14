#!/usr/bin/env python3
"""VIV-CLS steps 2-5 (PREREG-VIVCLS.md): map pen-unit tiles to tokens, label the training leaves from their truth, fit a
supervised kNN (tools/glyph_atlas.py classify --only-train-labels), cross-validate across f.102r / f.103r, one look at f.201r.

  python3 .../tx/vivcls/run.py train          # round-1 map, round-1 labels, round-2 map, round-2 labels, CV grid (no f.201r truth)
  python3 .../tx/vivcls/run.py predict --features F --metric M --knn K [--permute SEED] --tag TAG
                                               # fit on both training leaves, f.201r round-2 map against passA, hybrid + top-3
                                               # output, sha256 written; still no f.201r truth read
  python3 .../tx/vivcls/run.py score --tag TAG   # the ONE look: opens the f.201r truth, per-position table, writes score_TAG.json

Truth of f.102r / f.103r is read in `train` for labels and CV. The f.201r truth is read only in `score`.
"""
import argparse, csv, hashlib, json, os, subprocess, sys, collections, math
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
REPO = os.path.abspath(os.path.join(FOLD, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import box_token_align as bta  # noqa: E402
import tx_bench  # noqa: E402

ATLAS = os.path.join(HERE, 'atlas')
BT = os.path.join(REPO, 'benchmark-tx')
TRUTH = {'f102r': os.path.join(BT, 'vivonne1573-f102r-dev2.truth.tsv'),
         'f103r': os.path.join(BT, 'vivonne1573-f103r-confirm2.truth.tsv'),
         'f201r': os.path.join(BT, 'vivonne1573-f201r-dev.truth.tsv')}
PASSA = os.path.join(BT, 'outputs/vivonne1573-f201r-dev/passA.tsv')
TRAIN = ('f102r', 'f103r')
GRID = [(f, m, k) for f in ('hog', 'hog+zone+topo') for m in ('none', 'lda') for k in (5, 15)]


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def signs():
    return rd(os.path.join(HERE, 'map_signs.tsv'))


def leaf_of(line):
    return line.split('_')[0]


def ref_read(leaf):
    """the truth file's own token skeleton (line, pos, ref_sign): where the truth positions live. Train leaves only."""
    assert leaf in TRAIN
    return [dict(line=r['line'], pos=r['pos'], sign=r['ref_sign']) for r in rd(TRUTH[leaf])]


def build(leaf, read, topk=None, lam=0.0):
    sg = [s for s in signs() if s['page'] == leaf]
    labels = bta.read_labels(topk=topk) if topk else None
    rows, per = bta.build_map(sg, read, labels=labels, lam=lam, loo=bool(lam))
    return rows, per


def covered(rows):
    """{(line, pos): sid} for tokens with exactly one box at op 1:1 (and no other box on the token)."""
    by = collections.defaultdict(list)
    for r in rows:
        if r['sid']:
            by[(r['line'], str(r['pos']))].append(r)
    return {k: v[0]['sid'] for k, v in by.items() if len(v) == 1 and v[0]['op'] == '1:1'}


def labels_from(leaf, cov):
    out = []
    for r in rd(TRUTH[leaf]):
        if r['status'] != 'scored':
            continue
        sid = cov.get((r['line'], str(r['pos'])))
        if not sid:
            continue
        ts = [t for t in r['truth'].split('|') if t]
        if r['ref_sign'] in ts:
            code = r['ref_sign']
        elif len(ts) == 1:
            code = ts[0]
        else:
            continue
        out.append(dict(box=sid, code=code, line=r['line'], pos=r['pos']))
    return out


def scored_count(leaf):
    return sum(r['status'] == 'scored' for r in rd(TRUTH[leaf]))


def ensure_atlas_stub():
    lj = os.path.join(ATLAS, 'labels.json')
    if not os.path.exists(lj):
        json.dump({'signs': {}, 'marks': {}, 'override': {}}, open(lj, 'w'))
    ct = os.path.join(ATLAS, 'clusters.tsv')
    if not os.path.exists(ct):
        open(ct, 'w').write('kind\tid\tcluster\n')
    return lj


def classify(train_tsv, out_tsv, features='hog', metric='none', knn=5):
    lj = ensure_atlas_stub()
    cmd = [sys.executable, os.path.join(REPO, 'tools/glyph_atlas.py'), 'classify', '--out', ATLAS, '--labels', lj,
           '--page', 'all', '--only-train-labels', '--train-labels', train_tsv, '--topk', '3', '--tsv', out_tsv,
           '--features', features, '--metric', metric, '--knn', str(knn),
           '--topo-cache', os.path.join(ATLAS, 'topo_cache.npy')]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode:
        sys.exit(p.stdout + p.stderr)
    return {r['box']: r for r in rd(out_tsv)}


def write_labels(path, rows):
    wr(path, ['box', 'code', 'line', 'pos'], rows)


def cv_err(pred, lab_rows):
    n = len(lab_rows)
    e1 = sum(pred[r['box']]['k1'] != r['code'] for r in lab_rows)
    e3 = sum(r['code'] not in (pred[r['box']]['k1'], pred[r['box']]['k2'], pred[r['box']]['k3']) for r in lab_rows)
    return e1 / n, e3 / n, n


def cmd_train(a):
    os.makedirs(os.path.join(HERE, 'train'), exist_ok=True)
    T = os.path.join(HERE, 'train')
    rep = {}
    # round 1: width-only map against each training leaf's ref skeleton
    lab1 = {}
    for leaf in TRAIN:
        rows, per = build(leaf, ref_read(leaf), lam=0.0)
        cov = covered(rows)
        lab1[leaf] = labels_from(leaf, cov)
        write_labels(os.path.join(T, f'labels_r1_{leaf}.tsv'), lab1[leaf])
        rep[f'r1_{leaf}'] = dict(scored=scored_count(leaf), covered_scored=sum(1 for r in rd(TRUTH[leaf]) if r['status'] == 'scored' and (r['line'], str(r['pos'])) in cov),
                                 labels=len(lab1[leaf]))
    # round-1 classifiers (default setting hog/none/knn5), cross-leaf, for the round-2 top-k
    tk = {}
    for leaf, other in (('f102r', 'f103r'), ('f103r', 'f102r')):
        tk[leaf] = os.path.join(T, f'topk_r1_for_{leaf}.tsv')
        classify(os.path.join(T, f'labels_r1_{other}.tsv'), tk[leaf])
    both1 = os.path.join(T, 'labels_r1_both.tsv')
    write_labels(both1, lab1['f102r'] + lab1['f103r'])
    # round 2: label-aware map, labels again
    lab2 = {}
    for leaf in TRAIN:
        rows, per = build(leaf, ref_read(leaf), topk=tk[leaf], lam=bta.LAM)
        wr(os.path.join(T, f'map_r2_{leaf}.tsv'), ['sid', 'line', 'pos', 'op', 'labels', 'loo_pos'], rows)
        cov = covered(rows)
        lab2[leaf] = labels_from(leaf, cov)
        write_labels(os.path.join(T, f'labels_r2_{leaf}.tsv'), lab2[leaf])
        ops = collections.Counter(r['op'] for r in rows)
        sc = scored_count(leaf)
        cs = sum(1 for r in rd(TRUTH[leaf]) if r['status'] == 'scored' and (r['line'], str(r['pos'])) in cov)
        rep[f'r2_{leaf}'] = dict(scored=sc, covered_scored=cs, coverage=round(cs / sc, 3), labels=len(lab2[leaf]),
                                 ops=dict(ops), codes=len({r['code'] for r in lab2[leaf]}))
    write_labels(os.path.join(T, 'labels_r2_both.tsv'), lab2['f102r'] + lab2['f103r'])
    # CV grid: fit on one leaf's round-2 labels, score the other's
    grid = []
    for f, m, k in GRID:
        res = {}
        for tr, te in (('f102r', 'f103r'), ('f103r', 'f102r')):
            p = classify(os.path.join(T, f'labels_r2_{tr}.tsv'), os.path.join(T, f'cv_{f}_{m}_{k}_{tr}.tsv'), f, m, k)
            res[te] = cv_err(p, lab2[te])
        e1 = (res['f102r'][0] + res['f103r'][0]) / 2
        e3 = (res['f102r'][1] + res['f103r'][1]) / 2
        grid.append(dict(features=f, metric=m, knn=k, err1_f102r=round(res['f102r'][0], 4), err1_f103r=round(res['f103r'][0], 4),
                         err1_mean=round(e1, 4), err3_mean=round(e3, 4), n_f102r=res['f102r'][2], n_f103r=res['f103r'][2]))
        print(grid[-1], flush=True)
    # majority-class baseline per fold, for scale
    for tr, te in (('f102r', 'f103r'), ('f103r', 'f102r')):
        maj = collections.Counter(r['code'] for r in lab2[tr]).most_common(1)[0][0]
        rep[f'majority_{tr}_to_{te}'] = round(sum(r['code'] != maj for r in lab2[te]) / len(lab2[te]), 4)
    order = {'hog': 0, 'hog+zone+topo': 1, 'none': 0, 'lda': 1}
    best = min(grid, key=lambda g: (g['err1_mean'], order[g['features']], order[g['metric']], g['knn']))
    rep['grid'] = grid
    rep['chosen'] = best
    json.dump(rep, open(os.path.join(HERE, 'train_report.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in rep.items() if k != 'grid'}, indent=1))


def passa():
    return rd(PASSA)


def cmd_predict(a):
    T = os.path.join(HERE, 'train')
    O = os.path.join(HERE, a.tag)
    os.makedirs(O, exist_ok=True)
    lab = rd(os.path.join(T, 'labels_r2_both.tsv'))
    if a.permute is not None:
        rng = np.random.default_rng(a.permute)
        codes = [r['code'] for r in lab]
        perm = rng.permutation(len(codes))
        lab = [dict(r, code=codes[perm[i]]) for i, r in enumerate(lab)]
    tl = os.path.join(O, 'train_labels.tsv')
    write_labels(tl, lab)
    pred = classify(tl, os.path.join(O, 'classify_all.tsv'), a.features, a.metric, a.knn)
    tk = os.path.join(O, 'topk_f201r.tsv')
    wr(tk, ['box', 'k1', 'k2', 'k3', 'd1', 's1'], [r for b, r in pred.items() if b.startswith('f201r') or r.get('page', '').startswith('f201r')])
    read = [dict(line=r['line'], pos=r['pos'], sign=r['sign']) for r in passa()]
    rows, per = build('f201r', read, topk=tk, lam=bta.LAM)
    wr(os.path.join(O, 'map_r2_f201r.tsv'), ['sid', 'line', 'pos', 'op', 'labels', 'loo_pos'], rows)
    cov = covered(rows)
    hyb, top3 = [], []
    for r in passa():
        sid = cov.get((r['line'], str(r['pos'])))
        if sid:
            p = pred[sid]
            hyb.append(dict(line=r['line'], pos=r['pos'], sign=p['k1']))
            top3.append(dict(line=r['line'], pos=r['pos'], sid=sid, passA=r['sign'], k1=p['k1'], k2=p['k2'], k3=p['k3'], s1=p['s1']))
        else:
            hyb.append(dict(line=r['line'], pos=r['pos'], sign=r['sign']))
    wr(os.path.join(O, 'f201r_cls_hybrid.tsv'), ['line', 'pos', 'sign'], hyb)
    wr(os.path.join(O, 'f201r_cls_top3.tsv'), ['line', 'pos', 'sid', 'passA', 'k1', 'k2', 'k3', 's1'], top3)
    ops = collections.Counter(r['op'] for r in rows)
    info = dict(tag=a.tag, features=a.features, metric=a.metric, knn=a.knn, permute=a.permute, train_labels=len(lab),
                passA_tokens=len(hyb), covered_tokens=len(top3), changed_vs_passA=sum(t['k1'] != t['passA'] for t in top3),
                ops=dict(ops), sha256={n: hashlib.sha256(open(os.path.join(O, n), 'rb').read()).hexdigest()
                                       for n in ('f201r_cls_hybrid.tsv', 'f201r_cls_top3.tsv')})
    json.dump(info, open(os.path.join(O, 'predict.json'), 'w'), indent=1)
    print(json.dumps(info, indent=1))


def sign_test(a, b):
    n = a + b
    if n == 0:
        return 1.0
    k = min(a, b)
    p = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * p)


def cmd_score(a):
    O = os.path.join(HERE, a.tag)
    info = json.load(open(os.path.join(O, 'predict.json')))
    for n, h in info['sha256'].items():
        assert hashlib.sha256(open(os.path.join(O, n), 'rb').read()).hexdigest() == h, n
    truth = rd(TRUTH['f201r'])
    by_line = collections.defaultdict(list)
    for r in truth:
        by_line[r['line']].append(r)
    pa = collections.defaultdict(list)
    for r in passa():
        pa[r['line']].append(r)
    t3 = {(r['line'], str(r['pos'])): r for r in rd(os.path.join(O, 'f201r_cls_top3.tsv'))}
    rows_out = []
    for ln, rows in by_line.items():
        rows.sort(key=lambda r: float(r['pos']))
        toks = sorted(pa.get(ln, []), key=lambda r: int(r['pos']))
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        path = tx_bench.align(ref, ts, [t['sign'] for t in toks])
        j = 0
        for ri, osg in path:
            tok = None
            if osg is not None:
                tok = toks[j]; j += 1
            if ri is None or rows[ri]['status'] != 'scored' or tok is None:
                continue
            c = t3.get((ln, str(tok['pos'])))
            if not c:
                continue
            T = ts[ri]
            rows_out.append(dict(line=ln, tpos=rows[ri]['pos'], apos=tok['pos'], truth='|'.join(sorted(T)),
                                 flag=rows[ri].get('flag', ''), passA=tok['sign'], k1=c['k1'], k2=c['k2'], k3=c['k3'],
                                 a_ok=int(tok['sign'] in T), c_ok=int(c['k1'] in T), c3_ok=int(bool(T & {c['k1'], c['k2'], c['k3']}))))
    wr(os.path.join(O, 'per_position.tsv'), list(rows_out[0].keys()), rows_out)

    def summ(rs):
        n = len(rs)
        if not n:
            return {}
        aw = [r for r in rs if not r['a_ok']]
        fixed = sum(1 for r in rs if not r['a_ok'] and r['c_ok'])
        broken = sum(1 for r in rs if r['a_ok'] and not r['c_ok'])
        lines = collections.defaultdict(lambda: [0, 0])
        for r in rs:
            lines[r['line']][0] += 1 - r['a_ok']; lines[r['line']][1] += 1 - r['c_ok']
        imp = sum(1 for a0, c0 in lines.values() if c0 < a0); wor = sum(1 for a0, c0 in lines.values() if c0 > a0)
        return dict(n=n, passA_err=round(1 - sum(r['a_ok'] for r in rs) / n, 4), cls_err=round(1 - sum(r['c_ok'] for r in rs) / n, 4),
                    fixed=fixed, broken=broken, pos_sign_p=round(sign_test(fixed, broken), 4),
                    lines_improved=imp, lines_worsened=wor, lines_p=round(sign_test(imp, wor), 4),
                    passA_wrong=len(aw), truth_in_top3_of_passA_wrong=round(sum(r['c3_ok'] for r in aw) / len(aw), 4) if aw else None,
                    cls_top3_hit=round(sum(r['c3_ok'] for r in rs) / n, 4))
    unfl = [r for r in rows_out if not r['flag']]
    # chance: 1 - sum_c p_train(c) p_test(c), p_test over covered positions' truth-consistent single labels
    lab = rd(os.path.join(O, 'train_labels.tsv'))
    ptr = collections.Counter(r['code'] for r in lab); ntr = sum(ptr.values())
    acc = 0.0
    for r in rows_out:
        T = set(r['truth'].split('|'))
        acc += sum(ptr[c] for c in T) / ntr
    chance = 1 - acc / len(rows_out)
    sc = sum(1 for r in truth if r['status'] == 'scored')
    res = dict(tag=a.tag, as_measured=summ(rows_out), flagged_excluded=summ(unfl), chance_err=round(chance, 4),
               scored_f201r=sc, covered_scored=len(rows_out), coverage_vs_passA_map=round(len(rows_out) / sc, 4))
    # coverage against f.201r's own ref skeleton (width-only, as reported for the training leaves at round 1)
    rr = [dict(line=r['line'], pos=r['pos'], sign=r['ref_sign']) for r in truth]
    rows_ref, _ = build('f201r', rr, topk=os.path.join(O, 'topk_f201r.tsv'), lam=bta.LAM)
    cr = covered(rows_ref)
    res['coverage_vs_ref_skeleton'] = round(sum(1 for r in truth if r['status'] == 'scored' and (r['line'], str(r['pos'])) in cr) / sc, 4)
    json.dump(res, open(os.path.join(O, 'score.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest='cmd', required=True)
    sp.add_parser('train')
    p = sp.add_parser('predict')
    p.add_argument('--features', default='hog'); p.add_argument('--metric', default='none')
    p.add_argument('--knn', type=int, default=5); p.add_argument('--permute', type=int); p.add_argument('--tag', required=True)
    s = sp.add_parser('score'); s.add_argument('--tag', required=True)
    a = ap.parse_args()
    {'train': cmd_train, 'predict': cmd_predict, 'score': cmd_score}[a.cmd](a)


if __name__ == '__main__':
    main()
