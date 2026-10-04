#!/usr/bin/env python3
"""N7-HEL86 (copied from ../key_r4388/reconcile.py, N7-HELBC): merge passA.tsv/passB.tsv (order, state) into disagreements and cells_read.tsv.
  reconcile.py A.tsv B.tsv --settle settle.tsv   (settle.tsv: order, state from my look at the crop)"""
import argparse, csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('a'); ap.add_argument('b'); ap.add_argument('--settle')
x = ap.parse_args()
rd = lambda p: {int(r['order']): r['state'].strip().upper() for r in csv.DictReader(open(p), delimiter='\t')}
A, B = rd(x.a), rd(x.b); S = rd(x.settle) if x.settle else {}
cells = list(csv.DictReader(open(os.path.join(HERE, 'cells.tsv')), delimiter='\t'))
cls = lambda s: {'F': 'F', 'Z': 'F'}.get(s, s)
both = [int(c['order']) for c in cells if A.get(int(c['order'])) not in (None, '?') and B.get(int(c['order'])) not in (None, '?')]
diff = [o for o in both if cls(A[o]) != cls(B[o])]
print(f'err_2reader (blank/filled/X class) {len(diff)}/{len(both)} = {len(diff)/len(both):.3f}')
need = [int(c['order']) for c in cells if int(c['order']) not in both or int(c['order']) in diff]
print('to settle:', ' '.join(map(str, need)))
with open(os.path.join(HERE, 'cells_read.tsv'), 'w') as f:
    f.write('order\tcode\tset\ttokens\tA\tB\tstate\tflag\n')
    for c in cells:
        o = int(c['order']); a, b = A.get(o, '?'), B.get(o, '?')
        if o in S: st, fl = cls(S[o]), 'r'
        elif o in both and o not in diff: st, fl = cls(a), ''
        else: st, fl = '?', 'unsettled'
        f.write(f"{o}\t{c['code']}\t{c['set']}\t{c['tokens']}\t{a}\t{b}\t{st}\t{fl}\n")
