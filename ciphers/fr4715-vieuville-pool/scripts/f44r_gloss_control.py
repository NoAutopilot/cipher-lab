#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-10 (2 Oct 2026): rule 3's per-unit gate for no.21 f.44r's interlinear glosses
(CLAUDE.md rule 3, the Szembek bSZL65/66/67 paragraph) before any of its codes enter a key.

Statistic: over the glossed occurrences of codes glossed two or more times on the leaf, the share whose gloss
equals that code's modal gloss (normalised: lower case, u=v, i=j, y=i, accents and '?' dropped, first 4 letters).
Control: the same glosses permuted among the same occurrences (the code at each site kept), N shuffles; the
statistic depends on which gloss sits on which code, so the shuffle can move it (not a non-test).
Second, cross-leaf check: codes glossed on both f.44r and no.37 f.60r (key_wordcodes_f60r.tsv), same normaliser,
real agreement vs the f.44r glosses shuffled among f.44r sites.
usage: f44r_gloss_control.py RECONCILED.tsv [--shuffles 1000] [--seed 1]
RECONCILED.tsv needs columns code, gloss, grade (rows graded L are left out)."""
import csv, random, sys, os, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def norm(g):
    g = unicodedata.normalize('NFKD', g.lower())
    g = ''.join(c for c in g if c.isalpha())
    g = g.replace('v', 'u').replace('j', 'i').replace('y', 'i')
    return g[:4]

def consistency(pairs):
    by = {}
    for c, g in pairs:
        by.setdefault(c, []).append(g)
    n = hit = 0
    for c, gs in by.items():
        if len(gs) < 2:
            continue
        top = Counter(gs).most_common(1)[0][1]
        hit += top; n += len(gs)
    return hit, n

def main():
    a = sys.argv[1:]
    path = a[0]
    S = int(a[a.index('--shuffles') + 1]) if '--shuffles' in a else 1000
    rnd = random.Random(int(a[a.index('--seed') + 1]) if '--seed' in a else 1)
    rows = [r for r in csv.DictReader((l for l in open(path) if not l.startswith('#')), delimiter='\t')
            if r['grade'].strip() in ('C', 'M') and r['code'].strip() not in ('', '-', '?')]
    pairs = [(r['code'].strip().lstrip('.'), norm(r['gloss'])) for r in rows]
    hit, n = consistency(pairs)
    print(f'glossed sites used (C/M): {len(pairs)}; codes: {len(set(c for c, _ in pairs))}; '
          f'codes glossed >=2x: {sum(1 for c, k in Counter(c for c, _ in pairs).items() if k >= 2)}')
    real = hit / n if n else float('nan')
    codes = [c for c, _ in pairs]; gl = [g for _, g in pairs]
    vals = []
    for _ in range(S):
        rnd.shuffle(gl)
        h, m = consistency(list(zip(codes, gl)))
        vals.append(h / m if m else float('nan'))
    vals.sort()
    ge = sum(1 for v in vals if v >= real)
    print(f'within-leaf consistency: REAL {hit}/{n} = {real:.3f}; shuffle mean {sum(vals)/S:.3f} '
          f'p95 {vals[int(0.95*S)-1]:.3f} max {vals[-1]:.3f}; shuffles >= REAL {ge}/{S} (p {(ge+1)/(S+1):.4f})')
    # cross-leaf
    k60 = {}
    for r in csv.DictReader((l for l in open(os.path.join(HERE, 'key_wordcodes_f60r.tsv')) if not l.startswith('#')), delimiter='\t'):
        k60[r['sign'].lstrip('.')] = norm(r['value'])
    shared = [(c, g) for c, g in pairs if c in k60]
    if shared:
        agree = sum(1 for c, g in shared if g == k60[c])
        cv = []
        gl = [g for _, g in pairs]
        for _ in range(S):
            rnd.shuffle(gl)
            m = dict()
            sh = [(c, g) for (c, _), g in zip(pairs, gl) if c in k60]
            cv.append(sum(1 for c, g in sh if g == k60[c]))
        cv.sort()
        ge = sum(1 for v in cv if v >= agree)
        print(f'cross-leaf vs f.60r: {len(shared)} sites on {len(set(c for c,_ in shared))} shared codes; REAL agree {agree}; '
              f'shuffle mean {sum(cv)/S:.2f} max {cv[-1]}; shuffles >= REAL {ge}/{S}')
        for c in sorted(set(c for c, _ in shared)):
            print(f'  {c}: f44r {sorted(set(g for cc, g in shared if cc == c))} vs f60r {k60[c]}')
    else:
        print('cross-leaf vs f.60r: no shared codes')

main()
