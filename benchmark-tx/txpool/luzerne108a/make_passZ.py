#!/usr/bin/env python3
"""TX-POOL-LEAF-2 (copied from gunther8246-p2): passZ_pipeline.tsv = rec/ciphertext_draft.tsv with every adjud_out.tsv row applied (NONE drops the column,
two labels split it), as TXP-B23's make_passZ.py. Line ids p1_L01..p6_L08 (the crop stems).
Run: python3 benchmark-tx/txpool/luzerne108a/make_passZ.py"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
adj = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd(os.path.join(D, 'adjud_out.tsv'))}
out, cur, pos = [], None, 0
for r in rd(os.path.join(D, 'rec/ciphertext_draft.tsv')):
    s = adj.get((r['line'], int(r['position'])), r['sign'].strip())
    if r['line'] != cur:
        cur, pos = r['line'], 0
    if s in ('NONE', '-', ''):
        continue
    for t in s.split():
        pos += 1
        out.append((r['line'], pos, t))
with open(os.path.join(D, 'passZ_pipeline.tsv'), 'w', encoding='utf-8') as f:
    f.write('line\tpos\tsign\n')
    for o in out:
        f.write('%s\t%d\t%s\n' % o)
print(len(out), 'signs; adjudicated', len(adj))
