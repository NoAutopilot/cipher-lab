#!/usr/bin/env python3
"""TXE2-MODEL (X21) scorer, run ONLY after every pass/pipeline output and its sha256 are committed. Thin wrapper over
tools/tx_bench.py's own functions (score_item, paired, drop_flagged, sign_test, wilson): per item and pooled over
dev_tune + dint-f128-print + ceppo-f87-S, err_true with Wilson CI per arm, paired Opus pipeline vs Sonnet pipeline both
directions, as measured and --exclude-flagged; controls L (labels_dev_tune) and the folder's committed passC on ceppo.
    python3 benchmark-tx/txeng2/model/score.py > benchmark-tx/txeng2/model/score.txt"""
import json, os, sys
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.insert(0, os.path.join(R, 'tools'))
import tx_bench as T  # noqa: E402

O = R + '/benchmark-tx/outputs/'
ITEMS = [('birago1572-no87', None, {'L (committed Sonnet pipeline + relabels)': R + '/benchmark-tx/txeng/units/labels_dev_tune.tsv',
                                    'opus raw (no relabel transfer)': O + 'birago1572-no87/passX21_opus_pipeline_raw.tsv',
                                    'sonnet raw (no relabel transfer)': O + 'birago1572-no87/passX21_sonnet_pipeline_raw.tsv'}),
         ('dint-f128-print', R + '/benchmark-tx/dint128_label_map.tsv', {}),
         ('ceppo-f87-S', None, {'passC (committed folder Sonnet pipeline)': O + 'ceppo-f87-S/passC.tsv'})]
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


pool = {}
res = {}
for item, lmf, extra in ITEMS:
    lm = T.load_label_map(lmf) if lmf else None
    truth = T.read_tsv(os.path.join(R, bench[item]['truth']))
    if lm:
        truth = T.map_truth(truth, lm)
    truth_fx = T.drop_flagged(truth)
    files = {'opus pipeline': O + item + '/passX21_opus_pipeline.tsv', 'sonnet pipeline': O + item + '/passX21_sonnet_pipeline.tsv'}
    for arm in ('opus', 'sonnet'):
        for rd in (('r1', 'r2') if arm == 'opus' else ('A', 'B')):
            files['%s reader %s' % (arm, rd)] = O + item + '/passX21_%s_%s.tsv' % (arm, rd)
        files['%s reconcile (pre-adjudication)' % arm] = O + item + '/passX21_%s_reconcile.tsv' % arm
    files.update(extra)
    print('== %s%s' % (item, ' (label-mapped)' if lm else ''))
    outs = {}
    for name, fn in files.items():
        out = load(fn, lm); keep = {k: v for k, v in out.items() if any(r['line'] == k for r in truth)}
        outs[name] = out
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
    if item == 'birago1572-no87':
        for t_name, tr in (('as measured', truth), ('flagged excluded', truth_fx)):
            for a in ('sonnet pipeline', 'opus pipeline'):
                pr = T.paired(tr, outs['L (committed Sonnet pipeline + relabels)'], outs[a])
                print('  control [%s] %s vs base L: fixed %d, broken %d, p %.4f' % (t_name, a, pr['fixed'], pr['broken'], pr['p']))
            pr = T.paired(tr, outs['sonnet reader A'], outs['sonnet reader B'])
            print('  reader spread [%s] Sonnet B vs base Sonnet A: fixed %d, broken %d' % (t_name, pr['fixed'], pr['broken']))
            pr = T.paired(tr, outs['opus reader r1'], outs['opus reader r2'])
            print('  reader spread [%s] Opus r2 vs base Opus r1: fixed %d, broken %d' % (t_name, pr['fixed'], pr['broken']))
print('== POOLED (dev_tune + dint-f128-print + ceppo-f87-S)')
for arm in ('opus pipeline', 'sonnet pipeline'):
    k = sum(res[(i, arm)][0] for i, _, _ in ITEMS); n = sum(res[(i, arm)][1] for i, _, _ in ITEMS)
    fk = sum(res[(i, arm)][2] for i, _, _ in ITEMS); fn_ = sum(res[(i, arm)][3] for i, _, _ in ITEMS)
    print('  %-16s err_true %s | flagged-excluded %s' % (arm, fmt(k, n), fmt(fk, fn_)))
for (t_name, a), (f, b, n) in sorted(pool.items()):
    print('  pooled paired [%s] %s vs the other: n %d, fixed %d, broken %d, two-sided sign test p %.4f'
          % (t_name, a, n, f, b, T.sign_test(f, b)))
