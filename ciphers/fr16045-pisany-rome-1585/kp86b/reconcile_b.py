#!/usr/bin/env python3
"""kp86b reconciliation (PREREG_kp86b.md): the RUN3 shape rules of tx86/reconcile86.py, unchanged, applied to
tx86b/ciphertext_draft.tsv + tx86b/disagreements.tsv (from tools/reconcile_passes.py on tx86b/passA.tsv passB.tsv)
-> tx86b/ciphertext_f244v_f245r.tsv. No sign-by-sign judgement."""
import csv, os
H = os.path.dirname(os.path.abspath(__file__)); X = os.path.join(os.path.dirname(H), 'tx86b')
PAIR = {frozenset(('T37', 'T43')): 'T43', frozenset(('T48', 'T09')): 'T09', frozenset(('T30', 'T44')): 'T44',
        frozenset(('T45', 'T31')): 'T31'}
rows = list(csv.DictReader(open(os.path.join(X, 'ciphertext_draft.tsv')), delimiter='\t'))
dis = {(r['line'], r['col']): r for r in csv.DictReader(open(os.path.join(X, 'disagreements.tsv')), delimiter='\t')}
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
with open(os.path.join(X, 'ciphertext_f244v_f245r.tsv'), 'w') as f:
    for l in sorted(out):
        f.write(l + '\t' + ' '.join(out[l]) + '\n')
print(n)
