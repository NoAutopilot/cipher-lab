#!/usr/bin/env python3
"""TXE2-MODEL2 (PREREG-txeng2-6 X21b) scorer, run ONLY after every pass/pipeline output and its sha256 are committed. Copy of
model/score.py with the item list changed: pooled over the independent-truth items ONLY -- dev_tune (birago1572-no87, X21's
committed passX21_* arms reused as they are), dint-f128-print (passX21b_*: fresh Opus pair; Sonnet = folder passes A/B, the
X21 reconcile/adjudication, byte-identical), ceppo-f36v-gloss (passX21b_*: fresh Sonnet and Opus pairs). Never ceppo-f87-S or
f21v (Amendment 4). err_true with Wilson CI per arm, paired Opus pipeline vs Sonnet pipeline both directions, as measured and
flagged-excluded; reader spread per arm.
    python3 benchmark-tx/txeng2/model2/score.py > benchmark-tx/txeng2/model2/score.txt"""
import os, sys
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(R, 'tools'))
import tx_bench as T  # noqa: E402

O = R + '/benchmark-tx/outputs/'
ITEMS = [('birago1572-no87', 'passX21', None, {'L (committed Sonnet pipeline + relabels)': R + '/benchmark-tx/txeng/units/labels_dev_tune.tsv'}),
         ('dint-f128-print', 'passX21b', R + '/benchmark-tx/dint128_label_map.tsv', {}),
         ('ceppo-f36v-gloss', 'passX21b', None, {'folder recon (committed)': O + 'ceppo-f36v-gloss/recon.tsv'})]
bench = {r['item']: r for r in T.read_tsv(R + '/BENCHMARK-TX.tsv')}


def load(fn, lm):
    L = T.load_output([fn], None)
    return {k: [lm.get(x, x) for x in v] for k, v in L.items()} if lm else L


def err(truth, out):
    k, n, e, lo, hi = T.summarise(T.score_item(truth, out))
    return k, n


def fmt(k, n):
    lo, hi = T.wilson(min(k, n), n)
    return '%.3f (%d/%d) [%.3f-%.3f]' % (k / n, k, n, lo, hi)


pool, res = {}, {}
for item, pre, lmf, extra in ITEMS:
    lm = T.load_label_map(lmf) if lmf else None
    truth = T.read_tsv(os.path.join(R, bench[item]['truth']))
    if lm:
        truth = T.map_truth(truth, lm)
    truth_fx = T.drop_flagged(truth)
    files = {'opus pipeline': O + item + '/%s_opus_pipeline.tsv' % pre, 'sonnet pipeline': O + item + '/%s_sonnet_pipeline.tsv' % pre}
    for arm in ('opus', 'sonnet'):
        for rd in (('r1', 'r2') if arm == 'opus' else ('A', 'B')):
            files['%s reader %s' % (arm, rd)] = O + item + '/%s_%s_%s.tsv' % (pre, arm, rd)
        files['%s reconcile (pre-adjudication)' % arm] = O + item + '/%s_%s_reconcile.tsv' % (pre, arm)
    files.update(extra)
    print('== %s%s' % (item, ' (label-mapped)' if lm else ''))
    outs = {}
    for name, fn in files.items():
        out = load(fn, lm); outs[name] = out
        k, n = err(truth, out); fk, fn_ = err(truth_fx, out)
        print('  %-44s err_true %s | flagged-excluded %s' % (name, fmt(k, n), fmt(fk, fn_)))
        res[(item, name)] = (k, n, fk, fn_)
    for t_name, tr in (('as measured', truth), ('flagged excluded', truth_fx)):
        for a, b in (('opus pipeline', 'sonnet pipeline'), ('sonnet pipeline', 'opus pipeline')):
            pr = T.paired(tr, outs[b], outs[a])
            print('  paired [%s] %s vs base %s: n %d, base wrong %d, out wrong %d, fixed %d, broken %d, p %.4f'
                  % (t_name, a, b, pr['n'], pr['base_wrong'], pr['out_wrong'], pr['fixed'], pr['broken'], pr['p']))
            pool.setdefault((t_name, a), [0, 0, 0])
            pool[(t_name, a)][0] += pr['fixed']; pool[(t_name, a)][1] += pr['broken']; pool[(t_name, a)][2] += pr['n']
        pr = T.paired(tr, outs['sonnet reader A'], outs['sonnet reader B'])
        print('  reader spread [%s] Sonnet B vs base Sonnet A: fixed %d, broken %d' % (t_name, pr['fixed'], pr['broken']))
        pr = T.paired(tr, outs['opus reader r1'], outs['opus reader r2'])
        print('  reader spread [%s] Opus r2 vs base Opus r1: fixed %d, broken %d' % (t_name, pr['fixed'], pr['broken']))
        for c in extra:
            pr = T.paired(tr, outs[c], outs['sonnet pipeline'])
            print('  control [%s] sonnet pipeline vs base %s: fixed %d, broken %d, p %.4f' % (t_name, c, pr['fixed'], pr['broken'], pr['p']))
print('== POOLED (dev_tune + dint-f128-print + ceppo-f36v-gloss; independent truths only)')
for arm in ('opus pipeline', 'sonnet pipeline'):
    k = sum(res[(i, arm)][0] for i, *_ in ITEMS); n = sum(res[(i, arm)][1] for i, *_ in ITEMS)
    fk = sum(res[(i, arm)][2] for i, *_ in ITEMS); fn_ = sum(res[(i, arm)][3] for i, *_ in ITEMS)
    print('  %-16s err_true %s | flagged-excluded %s' % (arm, fmt(k, n), fmt(fk, fn_)))
for (t_name, a), (f, b, n) in sorted(pool.items()):
    print('  pooled paired [%s] %s vs the other: n %d, fixed %d, broken %d, two-sided sign test p %.4f'
          % (t_name, a, n, f, b, T.sign_test(f, b)))
