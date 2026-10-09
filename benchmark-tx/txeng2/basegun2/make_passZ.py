#!/usr/bin/env python3
"""TXE2-BASE-GUN2: adjud_out.tsv = packets/P*_out.tsv concatenated; passZ_gv2.tsv = rec/ciphertext_draft.tsv with every
adjud_out row applied (NONE drops the column, two labels split it), as TX-POOL-LEAF make_passZ.py. Line ids p2_L01..p2_L25.
Run: python3 benchmark-tx/txeng2/basegun2/make_passZ.py"""
import csv, glob, os
D = os.path.dirname(os.path.abspath(__file__))
R = os.path.abspath(os.path.join(D, '..', '..', '..'))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
q = rd(os.path.join(D, 'adjud_queue.tsv'))
rows = []
for p in sorted(glob.glob(os.path.join(D, 'packets', 'P*_out.tsv'))):
    rows += rd(p)
assert [(r['line'], r['col']) for r in rows] == [(r['line'], r['col']) for r in q], 'adjudication rows do not match the queue'
with open(os.path.join(D, 'adjud_out.tsv'), 'w', encoding='utf-8') as f:
    f.write('line\tcol\tsign\tconf\tviewed\tnote\n')
    for r in rows:
        f.write('\t'.join((r.get(k) or '').strip() for k in ('line', 'col', 'sign', 'conf', 'viewed', 'note')) + '\n')
adj = {(r['line'], int(r['col'])): r['sign'].strip() for r in rows}
out, cur, pos = [], None, 0
for r in rd(os.path.join(D, 'rec/ciphertext_draft.tsv')):
    s = adj.get((r['line'], int(r['position'])), r['sign'].strip())
    if r['line'] != cur:
        cur, pos = r['line'], 0
    if s in ('NONE', '-', ''):
        continue
    for t in s.split():
        pos += 1
        out.append(('p2_' + r['line'], pos, t))
op = os.path.join(R, 'benchmark-tx/outputs/gunther8246-p2/passZ_gv2.tsv')
with open(op, 'w', encoding='utf-8') as f:
    f.write('line\tpos\tsign\n')
    for o in out:
        f.write('%s\t%d\t%s\n' % o)
cand = {(r['line'], int(r['col'])): r['candidates'].split(' | ')[0] for r in q}
ch = sum(1 for k, v in adj.items() if v != cand[k])
vw = sum(1 for r in rows if (r.get('viewed') or '').strip().lower() == 'yes')
print(len(out), 'signs; adjudicated', len(adj), '; changed from first candidate', ch, '; viewed yes', vw)
