#!/usr/bin/env python3
"""TXE-R reporting glue: build ../ciphertext_f117_txer.tsv from rec/ciphertext_draft.tsv + adjudication.tsv, applying the
conf rule fixed in ../PREREG-TXE-R.md before any read:
  agreed sign, neither reader L                      -> conf H
  agreed sign, either reader L (both-L rows included) -> conf M; a both-L row the third reader moved to another cell -> that cell, L
  split, third reader chose reader1 or reader2       -> that sign, conf M ('-' chosen = no sign, row dropped)
  split, third reader chose another cell or unsure   -> its cell (unsure: reader1's sign), conf L; 'none' -> row dropped
Positions are renumbered per line. Never overwrites the committed ciphertext_f117_top1.tsv.
"""
import csv, os
H = os.path.dirname(os.path.abspath(__file__))
draft = list(csv.DictReader(open(os.path.join(H, 'rec/ciphertext_draft.tsv')), delimiter='\t'))
queue = {(r['line'], int(r['col'])): r for r in csv.DictReader(open(os.path.join(H, 'adjudicate_queue.tsv')), delimiter='\t')}
adj = {r['qid']: r for r in csv.DictReader(open(os.path.join(H, 'adjudication.tsv')), delimiter='\t')}
conf_both = {(r['line'], int(r['col'])): r['both_conf'] for r in csv.DictReader(open(os.path.join(H, 'rec/uncertain.tsv')), delimiter='\t')}
dis = {(r['line'], int(r['col'])): r for r in csv.DictReader(open(os.path.join(H, 'rec/disagreements.tsv')), delimiter='\t')}
out, per = [], {}
for r in draft:
    line, col = r['line'], int(r['position'])
    key = (line, col)
    q = queue.get((line.split('_')[1], col))
    if key in dis:
        a = adj[q['qid']]; ch = a['choice'].strip()
        if ch in ('1', '2'):
            sign = q['reader1'] if ch == '1' else q['reader2']; conf = 'M'
        elif ch == 'none':
            sign = '-'; conf = ''
        elif ch == 'other':
            sign = a['sign'].strip(); conf = 'L'
        else:
            sign = q['reader1']; conf = 'L'
        why = f"split {q['reader1']}/{q['reader2']} -> third reader {ch}"
    else:
        sign = r['sign']; bc = conf_both.get(key, '')
        if 'L' in bc.replace('A:', '').replace('B:', ''):
            conf = 'M'; why = f'agreed, {bc}'
            if q is not None and adj[q['qid']]['choice'].strip() == 'other' and adj[q['qid']]['sign'].strip():
                sign = adj[q['qid']]['sign'].strip(); conf = 'L'; why += ' -> third reader other'
        else:
            conf = 'H'; why = 'agreed' + (f', {bc}' if bc else '')
    if sign in ('-', ''):
        continue
    per[line] = per.get(line, 0) + 1
    out.append([line, per[line], sign, conf, why])
with open(os.path.join(H, '..', 'ciphertext_f117_txer.tsv'), 'w') as f:
    w = csv.writer(f, delimiter='\t', lineterminator='\n')
    w.writerow(['line', 'pos', 'sign', 'conf', 'why']); w.writerows(out)
import collections
print('signs', len(out), dict(collections.Counter(o[3] for o in out)))
