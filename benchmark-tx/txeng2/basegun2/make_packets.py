#!/usr/bin/env python3
"""TXE2-BASE-GUN2: adjud_queue.tsv from rec/ (disagreements + agreed-uncertain, as TX-POOL-LEAF make_queue.py), split
into packets of <= 16 rows (packets/Pnn_queue.tsv) with one task file each from adjud_task_template.txt.
Run: python3 benchmark-tx/txeng2/basegun2/make_packets.py"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
seq = {}
for r in rd(os.path.join(D, 'rec/ciphertext_draft.tsv')):
    seq.setdefault(r['line'], []).append(r['sign'])
rows = [('disagree', r) for r in rd(os.path.join(D, 'rec/disagreements.tsv'))] + \
       [('uncertain', r) for r in rd(os.path.join(D, 'rec/uncertain.tsv'))]
rows.sort(key=lambda kr: (kr[1]['line'], int(kr[1]['col'])))
H = 'line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n'
out = []
for k, r in rows:
    s, c = seq[r['line']], int(r['col'])
    out.append([r['line'], str(c), k, '%s | %s' % (r['A'] or '-', r['B'] or '-'),
                ' '.join(s[max(0, c - 3):c - 1]), ' '.join(s[c:c + 2])])
open(os.path.join(D, 'adjud_queue.tsv'), 'w', encoding='utf-8').write(H + ''.join('\t'.join(o) + '\n' for o in out))
tpl = open(os.path.join(D, 'adjud_task_template.txt'), encoding='utf-8').read()
os.makedirs(os.path.join(D, 'packets'), exist_ok=True)
n = 0
for i in range(0, len(out), 16):
    n += 1
    chunk = out[i:i + 16]
    q = os.path.join(D, 'packets', 'P%02d_queue.tsv' % n)
    open(q, 'w', encoding='utf-8').write(H + ''.join('\t'.join(o) + '\n' for o in chunk))
    lines = sorted({o[0] for o in chunk})
    crops = ', '.join('/home/user/cipher-lab/benchmark-tx/txpool/gunther8246-p2/crops/p2_%s.jpg' % l for l in lines)
    t = tpl.replace('{QUEUE}', q).replace('{OUT}', os.path.join(D, 'packets', 'P%02d_out.tsv' % n)).replace('{CROPS}', crops)
    open(os.path.join(D, 'packets', 'P%02d_task.txt' % n), 'w', encoding='utf-8').write(t)
print(len(out), 'queue rows;', n, 'packets')
