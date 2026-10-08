#!/usr/bin/env python3
"""D2-CRAV amendment A1 (../PREREG-D2-CRAV.md): coverage-exclusion gate. For each table, target COV vs the key-true COV distribution of 200
synthetic N=41 letters (enciphered with the full table, or T_8446x for T_8446) and vs the random-code control C1 p99.
Writes coverage_exclusion.tsv; --check exits 1 if stale."""
import sys, os, random
import key_family_test as k
HERE = os.path.dirname(os.path.abspath(__file__))
ENC = {'T_8446': 'T_8446x', 'T_8446x': 'T_8446x', 'T_NR': 'T_NR', 'T_8448': 'T_8448', 'T_8445': 'T_8445'}
def run():
    rng = random.Random(20261008); target = k.load_target(); lens = [len(l) for l in target]; rows = []
    for name in k.TABLES:
        T = k.load_table(name); E = k.load_table(ENC[name]); cov = k.score(target, T)[0]
        c1 = k.controls(target, T, rng, 1000)[0]
        kt = sorted(k.score(k.synth(E, lens, rng), T)[0] for _ in range(200)); p01 = k.pct(kt, 0.01)
        if p01 <= c1: v = 'non-test'
        elif cov < p01: v = 'EXCLUDED'
        else: v = 'NOT EXCLUDED'
        note = 'upper bound (partial sample enciphers itself)' if name in ('T_8448', 'T_8445') else ''
        rows.append([name, ENC[name], str(cov), str(c1), str(p01), str(kt[len(kt)//2]), v, note])
    return 'table\tenciphered_with\ttarget_COV\tC1_p99\tkeytrue_p01\tkeytrue_median\tverdict\tnote\n' + '\n'.join('\t'.join(r) for r in rows) + '\n'
if __name__ == '__main__':
    out = run(); path = os.path.join(HERE, 'coverage_exclusion.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path).read() == out; print('check OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w').write(out); print(out)
