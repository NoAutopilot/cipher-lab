#!/usr/bin/env python3
"""TXE4-9 CALIB: score once and apply the pre-registered gate (benchmark-tx/PREREG-txeng4-9.md), word for word.
Inputs: norm/P{1,2}_{F,C}.tsv (normalised f.89 reads), reads/P{1,2}_C1.tsv (calibration reads, for the feedback pairs).
Runs tools/tx_bench.py --item dint-f89-gloss --exclude-flagged --strict --ci [--json --top 999] per output and --paired F vs C
(C as BASE) per pass, saving text and JSON under scores/. The transfer-check pairs of a pass = (plain value of the calibration
truth position, the reader's wrong label or '<deleted>') at every wrong unflagged scored calibration position (tx_bench.align, the
same alignment tx_calibrate feedback used); their count on f.89 = the arm's tx_bench top_confusions 'value<-label' entries, summed.
    python3 score.py [--passes 1,2]   (the f.89 truth is opened by tx_bench only; the calibration truths by this script's pair step)"""
import argparse, json, math, os, subprocess, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench, tx_calibrate
TRUTHS = [('dint-f98v-gloss', 'benchmark-tx/dint-f98v-gloss.truth.tsv', 'f98v'), ('dint-f113-gloss', 'benchmark-tx/dint-f113-gloss.truth.tsv', '')]


def wilson(k, n):
    lo, hi = tx_bench.wilson(k, n); return '%.3f-%.3f' % (lo, hi)


def bench(args, out_txt):
    cmd = [sys.executable, 'tools/tx_bench.py', '--bench', 'BENCHMARK-TX.tsv', '--item', 'dint-f89-gloss', '--exclude-flagged', '--strict', '--ci'] + args
    t = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    open(out_txt, 'w').write('$ ' + ' '.join(cmd) + '\n' + t.stdout + t.stderr)
    j = subprocess.run(cmd + ['--json', '--top', '999'], cwd=ROOT, capture_output=True, text=True)
    open(out_txt.replace('.txt', '.json'), 'w').write(j.stdout)
    if t.returncode or j.returncode:
        sys.exit('tx_bench failed: ' + t.stderr + j.stderr)
    return json.loads(j.stdout)['items'][0]


def calib_pairs(read_path):
    """{(plain, wrong label)} over wrong unflagged scored calibration positions, with the same alignment as the feedback."""
    read = tx_calibrate.load_read(read_path, lambda ln: 'f98v_' + ln)
    pairs = Counter()
    for item, tp, _ in TRUTHS:
        by = defaultdict(list)
        for r in tx_calibrate.read_tsv(os.path.join(ROOT, tp)):
            by[r['line']].append(r)
        for ln, rows in by.items():
            out = read.get(ln)
            if not out:
                continue
            rows.sort(key=lambda r: float(r['pos']))
            ref = [r['ref_sign'] for r in rows]; ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
            for ri, osg in tx_bench.align(ref, ts, out):
                if ri is None or rows[ri]['status'] != 'scored' or tx_bench.is_flagged(rows[ri]):
                    continue
                if osg is None:
                    pairs[(rows[ri]['plain'], '<deleted>')] += 1
                elif osg not in ts[ri] and osg != rows[ri]['ref_sign']:
                    pairs[(rows[ri]['plain'], osg)] += 1
    return pairs


def conf_counts(rec, pairs):
    c = Counter()
    for e in rec['top_confusions']:
        lab, n = e.rsplit(' x', 1); v, s = lab.split('<-', 1)
        c[(v, s)] = int(n)
    return {p: c.get(p, 0) for p in pairs}


ap = argparse.ArgumentParser(); ap.add_argument('--passes', default='1,2'); a = ap.parse_args()
P = [int(x) for x in a.passes.split(',')]
S = os.path.join(HERE, 'scores'); os.makedirs(S, exist_ok=True)
res, lines = {}, []
for p in P:
    for arm in 'FC':
        f = os.path.join(HERE, 'norm', 'P%d_%s.tsv' % (p, arm))
        res[(p, arm)] = bench([f], os.path.join(S, 'P%d_%s.txt' % (p, arm)))
    bench([os.path.join(HERE, 'norm', 'P%d_F.tsv' % p), '--paired', os.path.join(HERE, 'norm', 'P%d_C.tsv' % p)], os.path.join(S, 'P%d_paired_F_vs_C.txt' % p))
    pairs = calib_pairs(os.path.join(HERE, 'reads', 'P%d_C1.tsv' % p))
    cf, cc = conf_counts(res[(p, 'F')], pairs), conf_counts(res[(p, 'C')], pairs)
    res[(p, 'pairs')] = (pairs, cf, cc)
    lines.append('pass %d transfer: %d feedback pairs (%d events); on f.89 F %d vs C %d -> %s' % (
        p, len(pairs), sum(pairs.values()), sum(cf.values()), sum(cc.values()), 'F < C' if sum(cf.values()) < sum(cc.values()) else 'NOT F < C'))
    lines.append('  per pair (label only shown; value hidden): ' + ', '.join('%s: F %d C %d' % (s, cf[(v, s)], cc[(v, s)]) for (v, s) in sorted(pairs)))
for p in P:
    for arm in 'FC':
        r = res[(p, arm)]; fe = r['flagged_excluded']
        lines.append('pass %d arm %s as measured: edits %d (S %d D %d I %d) SER %.3f ci %s | err_true %.3f (%d/%d) Wilson %s | strict err_true %.3f edits %d'
                     % (p, arm, r['ser_errors'], r['ser_S'], r['ser_D'], r['ser_I'], r['ser'], '%.3f-%.3f' % tuple(r['ci95_ser']), r['err_true'], r['errors'], r['scored'], wilson(r['errors'], r['scored']), r['strict']['err_true'], r['strict']['ser_errors']))
        lines.append('  flagged excluded: edits %d (S %d D %d I %d) SER %.3f | err_true %.3f (%d/%d) Wilson %s [%d flagged] | strict err_true %.3f edits %d'
                     % (fe['ser_errors'], fe['ser_S'], fe['ser_D'], fe['ser_I'], fe['ser'], fe['err_true'], fe['errors'], fe['scored'], wilson(fe['errors'], fe['scored']), fe['flagged'], fe['strict']['err_true'], fe['strict']['ser_errors']))
if len(P) == 2:
    mF = sum(res[(p, 'F')]['ser_errors'] for p in P) / 2; mC = sum(res[(p, 'C')]['ser_errors'] for p in P) / 2
    spread = max(abs(res[(1, 'F')]['ser_errors'] - res[(2, 'F')]['ser_errors']), abs(res[(1, 'C')]['ser_errors'] - res[(2, 'C')]['ser_errors']))
    fF = sum(res[(p, 'F')]['flagged_excluded']['ser_errors'] for p in P) / 2; fC = sum(res[(p, 'C')]['flagged_excluded']['ser_errors'] for p in P) / 2
    g1 = mC >= 1.2 * mF; g2 = (mC - mF) > spread; g3 = (fC - fF) > 0
    g4 = all(sum(res[(p, 'pairs')][1].values()) < sum(res[(p, 'pairs')][2].values()) for p in P)
    lines.append('GATE mean edits as measured: C %.1f, F %.1f; mean(C) >= 1.2 x mean(F): %s' % (mC, mF, g1))
    lines.append('GATE gap %.1f > max within-arm pass spread %.1f: %s' % (mC - mF, spread, g2))
    lines.append('GATE flagged-excluded direction (C %.1f - F %.1f > 0): %s' % (fC, fF, g3))
    lines.append('GATE transfer check in both passes (F < C on the named pairs): %s' % g4)
    lines.append('VERDICT: %s' % ('calibration feedback ADOPTED (all four hold)' if g1 and g2 and g3 and g4 else "'not distinguishable'"))
else:
    lines.append("VERDICT: 'not distinguishable (one pass)' -- the gate needs two passes")
txt = '\n'.join(lines); print(txt); open(os.path.join(S, 'summary.txt'), 'w').write(txt + '\n')
