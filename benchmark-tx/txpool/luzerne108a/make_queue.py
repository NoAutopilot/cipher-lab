#!/usr/bin/env python3
"""TX-POOL-LEAF-2: adjud_queue.tsv from rec/ = every disagreement + agreed rows where either reader gave an alt or conf L
(the 657 agreed-M rows are not queued: M is this pair's default on most pages). Neighbours from rec/ciphertext_draft.tsv.
Run: python3 benchmark-tx/txpool/luzerne108a/make_queue.py"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
seq = {}
for r in rd(os.path.join(D, 'rec/ciphertext_draft.tsv')):
    seq.setdefault(r['line'], []).append(r['sign'])
weak = set()
for p in ('passA.tsv', 'passB.tsv'):
    for r in rd(os.path.join(D, p)):
        if r['alt'].strip() or r['conf'].strip() == 'L':
            weak.add((r['passage'], r['sign_id']))
rows = [('disagree', r) for r in rd(os.path.join(D, 'rec/disagreements.tsv'))]
for r in rd(os.path.join(D, 'rec/uncertain.tsv')):
    if (r['line'], r['A']) in weak or (r['line'], r['B']) in weak:
        rows.append(('uncertain', r))
rows.sort(key=lambda kr: (kr[1]['line'], int(kr[1]['col'])))
with open(os.path.join(D, 'adjud_queue.tsv'), 'w', encoding='utf-8') as f:
    f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
    for k, r in rows:
        s, c = seq[r['line']], int(r['col'])
        f.write('\t'.join([r['line'], str(c), k, '%s | %s' % (r['A'] or '-', r['B'] or '-'),
                           ' '.join(s[max(0, c - 3):c - 1]), ' '.join(s[c:c + 2])]) + '\n')
print(len(rows), 'queue rows')
