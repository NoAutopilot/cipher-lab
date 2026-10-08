#!/usr/bin/env python3
"""D3-BLA2 universe (PREREG-D3BLA2.md): glossed columns of the six key items where pass A is M or A/B differ.
  python3 d3bla2_universe.py [--check]   writes d3bla2_universe.tsv (all 185 candidates + sampled flag), seed 20261008, n=40"""
import csv, os, sys, random, collections
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(H, f)), delimiter='\t')}
A, B, C = rd('passA.tsv'), rd('passB.tsv'), rd('ciphertext.tsv')
SIX = ('BLA179', 'BLA185', 'BLA188', 'BLA189', 'BLA190', 'BLA194')
cand = []
for k, a in A.items():
    if k[0].split('_')[0] not in SIX:
        continue
    b, c = B.get(k), C.get(k)
    if not c or not c['gloss']:
        continue
    if a['conf'] == 'M' or (b and b['group'] != a['group']):
        cand.append((k[0], int(k[1])))
cand.sort()
samp = set(random.Random(20261008).sample(range(len(cand)), 40)) if len(cand) > 40 else set(range(len(cand)))
out = 'line\tpos\tsampled\n' + ''.join('%s\t%d\t%d\n' % (l, p, i in samp) for i, (l, p) in enumerate(cand))
f = os.path.join(H, 'd3bla2_universe.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(f) and open(f).read() == out else 1)
open(f, 'w').write(out)
print(len(cand), 'candidates;', len(samp), 'sampled')
