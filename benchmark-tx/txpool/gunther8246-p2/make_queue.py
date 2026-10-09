#!/usr/bin/env python3
"""TX-POOL-LEAF: adjud_queue.tsv from rec/ (disagreements + agreed-uncertain), neighbours from ciphertext_draft.tsv,
as TXP-B23's queue. Run: python3 benchmark-tx/txpool/gunther8246-p2/make_queue.py"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
draft = rd(os.path.join(D, 'rec/ciphertext_draft.tsv'))
seq = {}
for r in draft:
    seq.setdefault(r['line'], []).append(r['sign'])
rows = [('disagree', r) for r in rd(os.path.join(D, 'rec/disagreements.tsv'))] + \
       [('uncertain', r) for r in rd(os.path.join(D, 'rec/uncertain.tsv'))]
rows.sort(key=lambda kr: (kr[1]['line'], int(kr[1]['col'])))
with open(os.path.join(D, 'adjud_queue.tsv'), 'w', encoding='utf-8') as f:
    f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
    for k, r in rows:
        s, c = seq[r['line']], int(r['col'])
        f.write('\t'.join([r['line'], str(c), k, '%s | %s' % (r['A'] or '-', r['B'] or '-'),
                           ' '.join(s[max(0, c - 3):c - 1]), ' '.join(s[c:c + 2])]) + '\n')
print(len(rows), 'queue rows')
