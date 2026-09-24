#!/usr/bin/env python3
"""Compare the two blind f.30 passes row by row (difflib on codes; '?' and '.' ignored for agreement).
Usage: reconcile_f30.py passA_f30.tsv passB_f30.tsv [--rows]  -> agreement summary (and per-row lines with --rows)."""
import sys, difflib
def load(fn):
    d = {}
    for l in open(fn, encoding='utf-8'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 2 or p[0] == 'row': continue
        d[p[0]] = [t.rstrip('?') for t in p[1].split() if t != '.']
    return d
A, B = load(sys.argv[1]), load(sys.argv[2])
tot = agr = 0; rows = []
for r in sorted(set(A) | set(B)):
    a, b = A.get(r, []), B.get(r, [])
    m = sum(x.size for x in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    n = max(len(a), len(b)); tot += n; agr += m
    rows.append((r, len(a), len(b), m, m / n if n else 1))
print(f'rows {len(rows)}  signs A {sum(x[1] for x in rows)}  B {sum(x[2] for x in rows)}  agree {agr}/{tot} = {agr/tot:.1%}')
print(f'rows with agreement < 90%: {sum(1 for x in rows if x[4] < .9)}')
if '--rows' in sys.argv:
    for x in rows: print('\t'.join(map(str, x[:4])) + f'\t{x[4]:.2f}')
