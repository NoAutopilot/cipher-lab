#!/usr/bin/env python3
"""D3-BLA2 universe (PREREG-D3BLA2.md, amendment 1): glossed columns of the six key items where pass A is M or A/B differ,
using settle.py's aligned A/B columns (fix_a renumbering + Needleman-Wunsch), not raw (line,pos) keys.
  python3 d3bla2_universe.py [--check]   writes d3bla2_universe.tsv; seed 20261008, n=40; columns: line pos A_group A_conf B_group gloss sampled"""
import csv, os, sys, random
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import settle
SIX = ('BLA179', 'BLA185', 'BLA188', 'BLA189', 'BLA190', 'BLA194')
a = settle.fix_a(settle.load('passA.tsv'))
b = settle.load('passB.tsv')
C = {(r['line'], int(r['pos'])): r for r in csv.DictReader(open(os.path.join(H, 'ciphertext.tsv')), delimiter='\t')}
cand = []
for l in list(a) + [l for l in b if l not in a]:
    if l.split('_')[0] not in SIX:
        continue
    for k, (x, y) in enumerate(settle.align(a.get(l, []), b.get(l, [])), 1):
        c = C.get((l, k))
        gl = c['gloss'] if c else ''
        if not gl:
            continue
        ga, gb = (x[0] if x else '-'), (y[0] if y else '-')
        if (x and x[1] != 'H') or ga != gb:
            cand.append((l, k, ga, x[1] if x else '-', gb, gl))
cand.sort()
samp = set(random.Random(20261008).sample(range(len(cand)), 40)) if len(cand) > 40 else set(range(len(cand)))
out = 'line\tpos\tA_group\tA_conf\tB_group\tgloss\tsampled\n' + ''.join('%s\t%d\t%s\t%s\t%s\t%s\t%d\n' % (*r, i in samp) for i, r in enumerate(cand))
f = os.path.join(H, 'd3bla2_universe.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(f) and open(f).read() == out else 1)
open(f, 'w').write(out)
print(len(cand), 'candidates;', len(samp), 'sampled')
