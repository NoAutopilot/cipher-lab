#!/usr/bin/env python3
"""Build ciphertext_f55v.tsv (line,pos,code,marks,grade) exactly as ciphertext_f55r.tsv: every
box/split position gets a final code+marks and a grade -- 'AB' where A and B already agreed (both
non-plain match, or both read the box plain), 'settled' where the 87 A/B disagreements were resolved
by recon_box_f55v/settled.tsv (2-of-3 majority with pass C, or a reasoned arbitration on a 3-way split)."""
import csv

def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(r['line'].strip(), r['pos'].strip())] = r
    return rows

A = load('passA_f55v.tsv')
B = load('passB_f55v.tsv')
settled = load('recon_box_f55v/settled.tsv')

keys = sorted(set(A) | set(B), key=lambda k: (int(float(k[0])), float(k[1])))

out = []
n_ab = n_settled = 0
for k in keys:
    if k in settled:
        s = settled[k]
        out.append((k[0], k[1], s['code'], s['marks'], 'settled'))
        n_settled += 1
        continue
    ra, rb = A.get(k), B.get(k)
    # not in disagreements.tsv means both passes agreed (same code, or both '_')
    r = ra or rb
    code = r['code'].strip()
    marks = r['marks'].strip()
    out.append((k[0], k[1], code, marks, 'AB'))
    n_ab += 1

with open('ciphertext_f55v.tsv', 'w') as f:
    f.write('line\tpos\tcode\tmarks\tgrade\n')
    for row in out:
        f.write('\t'.join(row) + '\n')

n_sign = sum(1 for r in out if r[2] != '_')
n_plain = len(out) - n_sign
types = sorted(set(r[2] for r in out if r[2] != '_'))
print(f'{len(out)} rows -> ciphertext_f55v.tsv (AB {n_ab}, settled {n_settled})')
print(f'{n_sign} sign tokens across {len(types)} distinct types, {n_plain} boxes plain')
print('types:', ', '.join(types))
