#!/usr/bin/env python3
"""GAPS36: row-by-row comparison of the image reading (reconciled.tsv, from NA 2.01.08 inv. 281 scans 81-82/85)
against Bourdeau's letter_groups.txt / annex_groups.txt (sources/cyphersolver/2026-10-03/spaen1808/, credit
D. Bourdeau, cyphersolver, CC BY 4.0). Writes compare.tsv; --check exits 1 if the committed compare.tsv is stale."""
import difflib, sys, os
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(H, '../../../sources/cyphersolver/2026-10-03/spaen1808')
def rows(p): return [l.split() for l in open(p) if l.strip()]
bour = rows(f'{SRC}/letter_groups.txt') + rows(f'{SRC}/annex_groups.txt')
img = []
for l in open(os.path.join(H, 'reconciled.tsv')):
    if l.startswith('#') or not l.strip(): continue
    crop, g = l.rstrip('\n').split('\t')[:2]
    if g.startswith('CLEAR'): continue
    img.append((crop, [x.rstrip('-').rstrip('?') for x in g.split()]))
assert len(img) == len(bour), (len(img), len(bour))
out = ['row\tcrop\tbourdeau_n\timage_n\tagree\tdiffs']
tb = ti = ta = 0
for i, ((crop, a), b) in enumerate(zip(img, bour), 1):
    sm = difflib.SequenceMatcher(a=b, b=a, autojunk=False)
    agree = sum(m.size for m in sm.get_matching_blocks())
    d = ['%s:%s->%s' % (op, ' '.join(b[i1:i2]) or '-', ' '.join(a[j1:j2]) or '-')
         for op, i1, i2, j1, j2 in sm.get_opcodes() if op != 'equal']
    tb += len(b); ti += len(a); ta += agree
    out.append(f'{i}\t{crop}\t{len(b)}\t{len(a)}\t{agree}\t{"; ".join(d)}')
out.append(f'total\t-\t{tb}\t{ti}\t{ta}\t')
txt = '\n'.join(out) + '\n'
p = os.path.join(H, 'compare.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(p) and open(p).read() == txt else 1)
open(p, 'w').write(txt); print(txt)
