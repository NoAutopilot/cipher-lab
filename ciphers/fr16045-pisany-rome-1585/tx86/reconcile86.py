#!/usr/bin/env python3
"""Rule-based reconciliation of the f.244r blind passes (RUN3-PISA, 4 Oct 2026) -> tx86/ciphertext_f244r.tsv.
Rules were fixed from the crops and SIGNSHEET86 by shape only, before any decode, so the reconciler's knowledge of the
Colbert clear copy cannot enter sign choices:
 1. A wrote ?[shape], B a label -> B's label (A's ?[qcross]/[t]/[longs] are cells B identified: T14/T44/T18|T03).
 2. A wrote ?[...] and B nothing -> kept as ? (dropped from decodes).
 3. one reader has a label and the other nothing -> the label (a sign one reader skipped).
 4. label vs label: T37/T43 -> T43 (the hand writes lambda, not a caret); T48/T09 -> T09 (plain 6); T30/T44 -> T44
    (o under a cross-stroke, A split it into ?[t] + o); T45/T31 -> T31 (the hand's x/gamma form); otherwise B's label
    (B left 0 unmatched signs against A's 52), flagged M in the alt column.
"""
import csv, os
H = os.path.dirname(os.path.abspath(__file__))
PAIR = {frozenset(('T37', 'T43')): 'T43', frozenset(('T48', 'T09')): 'T09', frozenset(('T30', 'T44')): 'T44',
        frozenset(('T45', 'T31')): 'T31'}
rows = list(csv.DictReader(open(os.path.join(H, 'ciphertext_draft.tsv')), delimiter='\t'))
dis = {(r['line'], r['col']): r for r in csv.DictReader(open(os.path.join(H, 'disagreements.tsv')), delimiter='\t')}
out, n = {}, {'agree': 0, 'r1': 0, 'r2': 0, 'r3': 0, 'r4pair': 0, 'r4B': 0}
for r in rows:
    k = (r['line'], r['position'])
    if k not in dis:
        s = r['sign']; n['agree'] += 1
    else:
        a, b = dis[k]['A'], dis[k]['B']
        if a.startswith('?') and b.startswith('T'):
            s = b; n['r1'] += 1
        elif a.startswith('?') and b == '-':
            s = a; n['r2'] += 1
        elif a == '-' or b == '-':
            s = b if a == '-' else a; n['r3'] += 1
        else:
            a0, b0 = a.rstrip('?'), b.rstrip('?')
            if frozenset((a0, b0)) in PAIR:
                s = PAIR[frozenset((a0, b0))]; n['r4pair'] += 1
            else:
                s = b; n['r4B'] += 1
    out.setdefault(r['line'], []).append(s)
with open(os.path.join(H, 'ciphertext_f244r.tsv'), 'w') as f:
    for l in sorted(out):
        f.write(l + '\t' + ' '.join(out[l]) + '\n')
print(n, sum(len(v) for v in out.values()), 'tokens')
