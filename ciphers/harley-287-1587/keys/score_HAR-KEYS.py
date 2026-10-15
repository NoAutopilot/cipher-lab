#!/usr/bin/env python3
"""HAR-KEYS (PREREG-HAR-KEYS.md): Fit A and Fit B per key, each with 20 shuffled-referent permutations (seed 0).
python3 score_HAR-KEYS.py [--check]  -- --check exits 1 if score_HAR-KEYS.tsv is stale."""
import csv, random, sys, os
D = os.path.dirname(os.path.abspath(__file__))
COB = {'n': '#', 'e': '7', 'c': '8', 'u': ':', 't': 'A', 'd': 'D', 'g': 'G', 'f': 'H', 'i': 'I', 'a': 'U',
       'r': 'V', 'l': 'l', 'h': 'p', 'w': 'w', 'y': 'y', 'o': 'z'}   # key_f84_f90.tsv principal sign, gloss n >= 10
COB_CODES = {'7': 'queen', '10': 'admiral', '15': 'parma', '16': 'spain'}
REF = {'The Queen': 'queen', 'The Q. Matie': 'queen', 'The Q. Ma.': 'queen', 'L. Admiral': 'admiral',
       'Duke of Parma': 'parma', 'The K. of Spaine': 'spain'}
def rows(name):
    return [r for r in csv.DictReader((l for l in open(os.path.join(D, name)) if not l.startswith('#')), delimiter='\t')]
def fitA(m):
    return sum(1 for L, s in COB.items() if s in m.get(L, set()))
def main():
    rng = random.Random(0); out = []
    keys = {}
    for r in rows('period_signs_HAR-KEYS.tsv'):
        keys.setdefault((r['record'], r['alphabet']), {})[r['letter']] = set(x for x in r['cobham'].split(',') if x != '-')
    for k, m in keys.items():
        s = fitA(m); letters = list(m); vals = [m[L] for L in letters]; ctl = []
        for _ in range(20):
            rng.shuffle(vals); ctl.append(fitA(dict(zip(letters, vals))))
        out.append(['A', k[0], k[1], len(m), s, max(ctl), 'FIT' if s >= 6 and s > max(ctl) else 'no fit'])
    codes = {}
    for r in rows('codes_HAR-KEYS.tsv'):
        codes.setdefault(r['record'], []).append((r['code'], REF.get(r['referent'], r['referent'])))
    for rec, cl in codes.items():
        f = lambda pairs: sum(1 for c, v in pairs if COB_CODES.get(c) == v)
        s = f(cl); cs = [c for c, _ in cl]; vs = [v for _, v in cl]; ctl = []
        for _ in range(20):
            rng.shuffle(vs); ctl.append(f(list(zip(cs, vs))))
        out.append(['B', rec, '', len(cl), s, max(ctl), 'FIT' if s >= 2 and s > max(ctl) else 'no fit'])
    text = 'fit\trecord\talphabet\tn\tscore\tcontrol_max\tverdict\n' + ''.join('\t'.join(map(str, o)) + '\n' for o in out)
    p = os.path.join(D, 'score_HAR-KEYS.tsv')
    if '--check' in sys.argv:
        sys.exit(0 if open(p).read() == text else 1)
    open(p, 'w').write(text); print(text, end='')
main()
