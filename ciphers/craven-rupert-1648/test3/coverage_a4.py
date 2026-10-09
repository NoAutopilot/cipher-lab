#!/usr/bin/env python3
"""CRAV-8450 amendment A4 (../PREREG-D2-CRAV.md): the A1 coverage-exclusion gate, unchanged, on test3/T_8450.tsv
(Edward Hyde to Prince Rupert, Hague 28 Feb 1648/9, DECODE R8450). Writes coverage_a4.tsv; --check exits 1 if stale."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'test2'))
import key_family_test as k
k.HERE = HERE  # load_table reads test3/*.tsv; load_target reads ../ciphertext.txt (same folder depth)
TABLES = ['T_8450']
def run():
    rng = random.Random(20261008); target = k.load_target(); lens = [len(l) for l in target]; rows = []
    for name in TABLES:
        T = k.load_table(name); cov = k.score(target, T)[0]
        c1 = k.controls(target, T, rng, 1000)[0]
        kt = sorted(k.score(k.synth(T, lens, rng), T)[0] for _ in range(200)); p01 = k.pct(kt, 0.01)
        if p01 <= c1: v = 'non-test'
        elif cov < p01: v = 'EXCLUDED'
        else: v = 'NOT EXCLUDED'
        hits = sorted({t for l in target for t in l if t in T})
        rows.append([name, name, str(cov), str(c1), str(p01), str(kt[len(kt)//2]), v,
                     'upper bound (partial sample enciphers itself); target codes in table: ' + ' '.join(map(str, hits))])
    return 'table\tenciphered_with\ttarget_COV\tC1_p99\tkeytrue_p01\tkeytrue_median\tverdict\tnote\n' + '\n'.join('\t'.join(r) for r in rows) + '\n'
if __name__ == '__main__':
    out = run(); path = os.path.join(HERE, 'coverage_a4.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out; print('check OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out); print(out)
