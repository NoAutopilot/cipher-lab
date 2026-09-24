#!/usr/bin/env python3
"""Compare two box-keyed confirm/correct passes (line,pos,code,marks,action,conf,note) by (line,pos).
Excludes rows where BOTH passes read '_' (plain), per the f54r precedent in NOTES.md.
Usage: python3 recon_box.py passA.tsv passB.tsv OUTDIR
Writes OUTDIR/agreement.tsv, OUTDIR/disagreements.tsv, prints base-code and with-marks agreement."""
import csv, sys, os

pa, pb, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(outdir, exist_ok=True)

def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        key = (r['line'].strip(), r['pos'].strip())
        rows[key] = r
    return rows

A = load(pa)
B = load(pb)
keys = sorted(set(A) | set(B), key=lambda k: (int(float(k[0])), float(k[1])))

agree_rows, dis_rows = [], []
n_base_match = n_marks_match = n_total = 0
for k in keys:
    ra, rb = A.get(k), B.get(k)
    if ra is None or rb is None:
        dis_rows.append((k[0], k[1], ra['code'] if ra else 'MISSING', ra['marks'] if ra else '',
                         rb['code'] if rb else 'MISSING', rb['marks'] if rb else '', 'one pass missing this box'))
        continue
    ca, cb = ra['code'].strip(), rb['code'].strip()
    ma, mb = ra['marks'].strip(), rb['marks'].strip()
    if ca == '_' and cb == '_':
        continue
    n_total += 1
    base_match = (ca == cb)
    marks_match = base_match and (set(m for m in ma.split('|') if m) == set(m for m in mb.split('|') if m))
    if base_match:
        n_base_match += 1
    if marks_match:
        n_marks_match += 1
    row = (k[0], k[1], ca, ma, cb, mb, 'base+marks match' if marks_match else ('base match' if base_match else 'DIFFER'))
    (agree_rows if base_match else dis_rows).append(row)

with open(f'{outdir}/agreement.tsv', 'w') as f:
    f.write('line\tpos\tcode_a\tmarks_a\tcode_b\tmarks_b\tnote\n')
    for r in agree_rows:
        f.write('\t'.join(r) + '\n')
with open(f'{outdir}/disagreements.tsv', 'w') as f:
    f.write('line\tpos\tcode_a\tmarks_a\tcode_b\tmarks_b\tnote\n')
    for r in dis_rows:
        f.write('\t'.join(r) + '\n')

print(f'compared {n_total} non-both-plain positions')
print(f'base code agreement: {n_base_match}/{n_total} = {100*n_base_match/n_total:.1f}%')
print(f'with marks agreement: {n_marks_match}/{n_total} = {100*n_marks_match/n_total:.1f}%')
print(f'disagreements: {len(dis_rows)} rows -> {outdir}/disagreements.tsv')
