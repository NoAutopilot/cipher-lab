#!/usr/bin/env python3
"""R9-MANTPC (6 Oct 2026): per-code shuffle test on R9-MANTPOOL's 24 agreeing codes, per PREREG-R9-MANTPC.md.
Reuses pooled_multi.py's runs, aligner and within-bin gloss shuffles (seeds 9501+d). Fixed key = ../key.tsv minus the rows
whose source names R9-MANTPOOL. For each code: A = runs carrying its most frequent non-empty chunk; p = (1 + #draws A_shuf >= A_real)/(N+1);
Benjamini-Hochberg q 0.10. Positive control: the 5 known-answer C codes unfixed, same test.
Usage: per_code.py [--draws N]   (writes per_code_r9pc.tsv, per_code_ka_r9pc.tsv here)"""
import csv, os, sys, random
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import pooled_multi as pm
ia = pm.ia
R9 = {r['code'] for r in pm.rd('key.tsv') if 'R9-MANTPOOL' in r['source']}
FIX0 = {k: v for k, v in pm.ALLFIX.items() if str(k) not in R9}
KA = [35, 33, 10, 66, 14]
FIXKA = {k: v for k, v in FIX0.items() if k not in KA}
TARGET = [int(r['code']) for r in csv.DictReader(open(os.path.join(HERE, 'codes_r9.tsv')), delimiter='\t') if r['licence'] == 'M']
Q = 0.10

def stats(per, codes):
    out = {}
    for v in codes:
        d = per.get(v, {})
        best = max(((len(s), ch) for ch, s in d.items() if ch), default=(0, ''))
        n = len(set().union(*d.values())) if d else 0
        out[v] = (n, best[0], best[1])
    return out

def draw(args):
    d, which = args
    runs = pm.load(); rng = random.Random(pm.SEED + d)
    fx, codes = (FIX0, TARGET) if which == 't' else (FIXKA, KA)
    per = pm.align(runs, pm.shuffle_glosses(runs, rng), fx)
    return {v: a for v, (n, a, ch) in stats(per, codes).items()}

def bh(ps, q):
    m = len(ps); order = sorted(range(m), key=lambda i: ps[i]); k = 0
    for r, i in enumerate(order, 1):
        if ps[i] <= q * r / m: k = r
    return {order[r] for r in range(k)}

def klass(v, ch, per, runs, glosses):
    if len(ch) == 1: return 'letter'
    for i in per[v][ch]:
        if ch in {ia.fold(w) for w in glosses[i].split()}: return 'word'
    return 'syllable'

def test(which, codes, fx, draws, pool):
    runs = pm.load(); gl = [r['gloss'] for r in runs]
    per = pm.align(runs, gl, fx); real = stats(per, codes)
    sh = pool.map(draw, [(d, which) for d in range(draws)])
    rows = []
    for v in codes:
        n, a, ch = real[v]; null = [s[v] for s in sh]
        ge = sum(x >= a for x in null)
        rows.append(dict(code=v, n_runs=n, chunk=ch, A_real=a, share='%.3f' % (a / n if n else 0),
                         null_mean='%.2f' % (sum(null) / draws), null_p95=sorted(null)[int(0.95 * draws) - 1],
                         null_max=max(null), null_distinct=len(set(null)), p='%.4f' % ((1 + ge) / (draws + 1)),
                         klass=klass(v, ch, per, runs, gl) if ch else '-'))
    sig = bh([float(r['p']) for r in rows], Q)
    for i, r in enumerate(rows): r['BH_q010'] = 'PASS' if i in sig else 'FAIL'
    return rows

def main():
    a = sys.argv[1:]; draws = int(a[a.index('--draws') + 1]) if '--draws' in a else pm.DRAWS
    with Pool(4) as pool:
        t = test('t', TARGET, FIX0, draws, pool)
        k = test('k', KA, FIXKA, draws, pool)
    for name, rows in (('per_code_r9pc.tsv', t), ('per_code_ka_r9pc.tsv', k)):
        with open(os.path.join(HERE, name), 'w') as f:
            w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
    for r in t + k: print('\t'.join(str(x) for x in r.values()))
    print('target pass', sum(r['BH_q010'] == 'PASS' for r in t), '/', len(t), '; known-answer pass', sum(r['BH_q010'] == 'PASS' for r in k), '/ 5')

if __name__ == '__main__':
    main()
