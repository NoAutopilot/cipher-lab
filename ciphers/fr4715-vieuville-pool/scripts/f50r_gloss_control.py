#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-12 (3 Oct 2026): rule 3's per-unit gate for no.27 f.50r's interlinear glosses.
f62r_gloss_control.py (letter-cipher gloss spans vs the printed key) cannot vary here: every f.50r gloss sits on a
word-code, none on a letter-cipher span (n = 0, a non-test). Two statistics that can vary instead:
(1) within-leaf: f44r_gloss_control.py's consistency of a code glossed twice or more on this leaf;
(2) cross-leaf: over f.50r C/M sites whose code is also glossed C/M on a sibling leaf (f.44r, f.60r, f.62r
reconciled files), the number whose gloss matches a sibling gloss of the same code (normaliser: lower case, u=v,
i=j=y, letters only, first 4 letters). Control: f.50r's glosses permuted among f.50r's own sites (codes kept),
N shuffles; the statistic depends on which gloss sits on which code, so the shuffle can move it.
Scope: catches a leaf whose glosses agree with its siblings no better than chance; it must NOT be read as testing
a code glossed on this leaf only (that stays at its reading grade, by adjacency).
GAPS-fr4715-vieuville-pool-13 (3 Oct 2026): --sib LEAF=PATH (repeatable) adds a sibling reconciled file with columns
code/gloss/grade (f.51r; or f.50r when the leaf under test is f.51r); the leaf under test is named from its file and is
never its own sibling.
usage: f50r_gloss_control.py witness/f50r_glosses_reconciled.tsv [--sib f51r=witness/f51r_glosses_reconciled.tsv]
       [--shuffles 1000] [--seed 1]"""
import csv, random, sys, os
from collections import Counter
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIB = {'f44r': ('witness/f44r_glosses_reconciled.tsv', 'code', 'gloss', 'grade'),
       'f60r': ('witness/f60r_glosses_reconciled.tsv', 'group', 'gloss', 'grade'),
       'f62r': ('witness/f62r_glosses_reconciled.tsv', 'code', 'gloss', 'grade')}

def norm(g):
    g = ''.join(c for c in g.lower() if c.isalpha())
    return g.replace('v', 'u').replace('j', 'i').replace('y', 'i')[:4]

def rows(path, ck, gk, rk):
    for r in csv.DictReader((l for l in open(os.path.join(HERE, path)) if not l.startswith('#')), delimiter='\t'):
        c = r[ck].strip().lstrip('.')
        if r[rk].strip() in ('C', 'M') and c.isdigit() and r[gk].strip() not in ('', '-'):
            yield c, norm(r[gk])

def main():
    a = sys.argv[1:]
    S = int(a[a.index('--shuffles') + 1]) if '--shuffles' in a else 1000
    rnd = random.Random(int(a[a.index('--seed') + 1]) if '--seed' in a else 1)
    me = list(rows(a[0], 'code', 'gloss', 'grade'))
    name = os.path.basename(a[0]).split('_')[0]
    sibs = dict(SIB)
    for i, x in enumerate(a):
        if x == '--sib':
            leaf, path = a[i + 1].split('=', 1); sibs[leaf] = (path, 'code', 'gloss', 'grade')
    sibs.pop(name, None)
    print(f'leaf under test: {name}; siblings: {", ".join(sorted(sibs))}')
    sib = {}
    for leaf, spec in sibs.items():
        for c, g in rows(*spec):
            sib.setdefault(c, set()).add((leaf, g))
    codes = [c for c, _ in me]; gl = [g for _, g in me]
    def within(pairs):
        by = {}
        for c, g in pairs: by.setdefault(c, []).append(g)
        h = n = 0
        for gs in by.values():
            if len(gs) >= 2: h += Counter(gs).most_common(1)[0][1]; n += len(gs)
        return h, n
    def cross(pairs):
        return sum(1 for c, g in pairs if c in sib and g in {x for _, x in sib[c]})
    h, n = within(me); rc = cross(me)
    shared = [(c, g) for c, g in me if c in sib]
    print(f'{name} C/M glossed sites: {len(me)} on {len(set(codes))} codes; shared with a sibling leaf: {len(shared)}')
    for c, g in shared:
        print(f'  {c}: {name} {g} vs siblings {sorted(sib[c])}')
    wv, cv = [], []
    for _ in range(S):
        rnd.shuffle(gl); p = list(zip(codes, gl))
        hh, nn = within(p); wv.append(hh / nn if nn else float('nan')); cv.append(cross(p))
    wv.sort(); cv.sort()
    if n:
        r = h / n; ge = sum(1 for v in wv if v >= r)
        print(f'within-leaf: REAL {h}/{n} = {r:.3f}; shuffle mean {sum(wv)/S:.3f} p95 {wv[int(.95*S)-1]:.3f}; '
              f'shuffles >= REAL {ge}/{S} (p {(ge+1)/(S+1):.4f})')
    else:
        print('within-leaf: no code glossed twice (n = 0, a non-test)')
    ge = sum(1 for v in cv if v >= rc)
    print(f'cross-leaf: REAL agree {rc} of {len(shared)}; shuffle mean {sum(cv)/S:.2f} p95 {cv[int(.95*S)-1]} '
          f'max {cv[-1]}; shuffles >= REAL {ge}/{S} (p {(ge+1)/(S+1):.4f})')

main()
