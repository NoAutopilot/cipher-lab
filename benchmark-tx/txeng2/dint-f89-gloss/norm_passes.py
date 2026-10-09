#!/usr/bin/env python3
"""TXP-D89 (9 Oct 2026): join each blind pass's two part files (L01-L07, L08-L14) into passA.tsv / passB.tsv.
Mechanical only, no image looked at: (1) rows whose sign_id is an English note word (reader B wrote its note text
on new rows: form/through/from/above/on/stem/over/lambda/shape/loop) are folded into the previous row's note and
positions renumbered; (2) each reader's NEW:<description> labels are mapped to one shared X_ code by description
(table NEWMAP); any NEW label not in the table stays as written. Raw part files are kept unchanged.
    python3 norm_passes.py [--check]
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
NOTEWORDS = {'form', 'through', 'from', 'above', 'on', 'stem', 'over', 'lambda', 'shape', 'loop'}
NEWMAP = {
    'NEW:delta-d': 'X_DELTA', 'NEW:delta (o with rising stem)': 'X_DELTA',
    'NEW:crossed-4': 'X_4BAR', 'NEW:4-with-crossbar': 'X_4BAR',
    'NEW:v-with-stem': 'X_VSTEM', 'NEW:v-slashed': 'X_VSTEM',
    'NEW:o-with-cross-above': 'X_OCROSS',
    'NEW:h-barred': 'X_HBAR', 'NEW:h-shape-crossed': 'X_HBAR',
    'NEW:8': 'X_8', 'NEW:8-shape': 'X_8',
    'NEW:comma': 'X_COMMA', 'NEW:c-tailed': 'X_CTAIL', 'NEW:c-with-tail': 'X_CTAIL',
    'NEW:z-barred': 'X_ZBAR', 'NEW:F-barred': 'X_FBAR', 'NEW:eb-shape': 'X_EB',
    'NEW:double-barred-dagger': 'X_DDAG', 'NEW:N-shape': 'X_N', 'NEW:M-with-baseline': 'X_MBASE',
}
HDR = ['passage', 'pos', 'sign_id', 'alt', 'conf', 'note']


def build(P):
    rows = []
    for part in (1, 2):
        with open(os.path.join(HERE, 'pass%s_part%d.tsv' % (P, part)), newline='') as f:
            rows += list(csv.DictReader(f, delimiter='\t'))
    out = []
    for r in rows:
        s = r['sign_id'].strip()
        if s in NOTEWORDS and out and out[-1]['passage'] == r['passage']:
            out[-1]['note'] = (out[-1]['note'] + ' ' + s).strip()
            continue
        r = {k: (r.get(k) or '').strip() for k in HDR}
        r['sign_id'] = NEWMAP.get(s, s)
        r['alt'] = NEWMAP.get(r['alt'], r['alt'])
        out.append(r)
    n = {}
    lines = ['\t'.join(HDR)]
    for r in out:
        n[r['passage']] = n.get(r['passage'], 0) + 1
        r['pos'] = str(n[r['passage']])
        lines.append('\t'.join(r[k] for k in HDR))
    return '\n'.join(lines) + '\n'


stale = 0
for P in 'AB':
    p = os.path.join(HERE, 'pass%s.tsv' % P)
    t = build(P)
    old = open(p).read() if os.path.exists(p) else None
    if old != t:
        stale += 1
        if '--check' not in sys.argv:
            open(p, 'w').write(t)
print('pass A/B', 'stale' if stale and '--check' in sys.argv else 'written' if stale else 'up to date')
sys.exit(1 if stale and '--check' in sys.argv else 0)
