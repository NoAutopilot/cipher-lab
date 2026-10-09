#!/usr/bin/env python3
"""TXP-D89: adjudication queue from rec/ (disagreements + agreed-uncertain), TXE-Q shape, plus the clear word a reader
wrote for a CLEAR neighbour so the adjudicator can find the place. Mechanical; no image."""
import csv, os
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, newline=''), delimiter='\t'))
draft = rd(os.path.join(H, 'rec/ciphertext_draft.tsv'))
seq = {}
for r in draft:
    seq.setdefault(r['line'], []).append(r['sign'])
words = {}
for r in rd(os.path.join(H, 'passA.tsv')):
    if r['sign_id'] == 'CLEAR':
        words.setdefault(r['passage'], []).append(r['note'])
q = []
for r in rd(os.path.join(H, 'rec/disagreements.tsv')):
    c = [x if x else '-' for x in (r['A'], r['B'])]
    q.append((r['line'], int(r['col']), 'disagree', ' | '.join(dict.fromkeys(c))))
for r in rd(os.path.join(H, 'rec/uncertain.tsv')):
    q.append((r['line'], int(r['col']), 'uncertain', r['A']))
q.sort()
out = ['line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours']
for ln, col, kind, cand in q:
    s = seq[ln]
    out.append('%s\t%d\t%s\t%s\t%s\t%s' % (ln, col, kind, cand, ' '.join(s[max(0, col - 4):col - 1]), ' '.join(s[col:col + 3])))
open(os.path.join(H, 'adjud_queue.tsv'), 'w').write('\n'.join(out) + '\n')
print(len(q), 'rows')
