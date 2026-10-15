#!/usr/bin/env python3
"""C1161-EXC (15 Oct 2026): score the blind exemplar passes as PREREG-C1161-EXC.md registers.
  python3 exc/exc_score.py   -> exc/score_out.txt, exc/concordance_exc.tsv, exc/split_labels.txt (labels for reconciliation C)"""
import csv, collections, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
CTRL = {'qb': 'a', '9': 's', 'sd': 'g', 'y': 'r'}
def col(s):
    s = (s or '').strip().lower()
    if s in ('', 'none'): return 'none'
    if s.startswith(('nom', 'null')): return s
    c = s.split(':')[0]
    return 'u' if c in ('u/v', 'u', 'v') else c
def load(P):
    ids = {r['id']: (int(r['group']), r['label']) for r in csv.DictReader(open(os.path.join(H, f'ids_{P}.tsv')), delimiter='\t')}
    ans = {}
    for g in (1, 2, 3, 4) if P != 'C' else (1,):
        f = os.path.join(H, f'pass_{P}_g{g}.tsv')
        if os.path.exists(f):
            for r in csv.DictReader(open(f), delimiter='\t'):
                if r['id'].strip() in ids:
                    ans[ids[r['id'].strip()][1]] = (col(r['sheet']), r['sheet'].strip(), r.get('confidence', ''))
    grp = {lab: g for g, lab in ids.values()}
    return ans, grp
out = []
A, grp = load('A'); B, _ = load('B')
power = {}
for P, X in (('A', A), ('B', B)):
    for lab, c in CTRL.items():
        ok = X.get(lab, ('none',))[0] == c; power[(P, grp[lab])] = ok
        out.append(f'POWER pass {P} group {grp[lab]}: control {lab} -> {X.get(lab, ("missing", "missing"))[1]} (agreed {c}) {"PASS" if ok else "FAIL"}')
C = {}
if os.path.exists(os.path.join(H, 'ids_C.tsv')):
    C, _ = load('C')
keyv = {r['sign']: r for r in csv.DictReader(open(os.path.join(T, 'lkey', 'concordance.tsv')), delimiter='\t')}
rows, split = [], []
for lab, g in sorted(grp.items(), key=lambda x: (x[1], x[0])):
    if lab in CTRL: continue
    a, b = A.get(lab, ('none', 'missing', '')), B.get(lab, ('none', 'missing', ''))
    if not (power[('A', g)] and power[('B', g)]):
        v, his = 'NON-TEST (power)', ''
    elif a[0] == b[0] and a[0] != 'none':
        v, his = 'MAPPED', a[0]
    elif a[0] != 'none' and b[0] != 'none':
        split.append(lab)
        if lab in C:
            votes = collections.Counter([a[0], b[0], C[lab][0]]); top, n = votes.most_common(1)[0]
            v, his = (f'FINAL (2 of 3, C={C[lab][1]})', top) if n >= 2 and top != 'none' else (f'UNDECIDED (C={C[lab][1]})', '')
        else:
            v, his = 'SPLIT', ''
    else:
        v, his = 'NO MATCH', ''
    ours = keyv[lab]['ours_value'] if lab in keyv else ''
    conc = '' if not his else ('agree' if his.split(':')[0] == ours or (his == 'u' and ours in 'uv') else 'disagree')
    rows.append((lab, g, a[1], a[2], b[1], b[2], C.get(lab, ('', ''))[1] if lab in C else '', v, his, ours, conc))
    out.append(f'{lab:8s} g{g} A={a[1]}({a[2]}) B={b[1]}({b[2]}){" C=" + C[lab][1] if lab in C else ""} -> {v} {his} ours={ours} {conc}')
with open(os.path.join(H, 'concordance_exc.tsv'), 'w') as f:
    f.write('label\tgroup\tpassA\tconfA\tpassB\tconfB\tpassC\tverdict\this_value_blind\tours_value\tconcordance\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
open(os.path.join(H, 'split_labels.txt'), 'w').write(','.join(split) + '\n')
cnt = collections.Counter(r[7].split(' (')[0] for r in rows)
out.append('SUMMARY ' + ', '.join(f'{k} {v}' for k, v in sorted(cnt.items())) + ' | untestable (no S-anchored token): 0, spiralG')
open(os.path.join(H, 'score_out.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
