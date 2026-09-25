#!/usr/bin/env python3
"""Majority vote passA/passB/passC on the 78 disagreement positions of f57v: 2 of 3 agree on base code ->
that call (marks taken from an agreeing pass, preferring one that also gives a mark); the one three-way
split (all three codes differ) is settled from pass C's crop note at conf H, source noted as 3-way.
Writes recon_box_f57v/settled.tsv (line,pos,code,marks,source,reason) and prints the agreement recount
("rows where C agrees with A or B") and the three-way split count. Same structure as settle_passC.py
(f55v, LANE R6 L1c), leaf changed."""
import csv

def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(r['line'].strip(), r['pos'].strip())] = r
    return rows

A = load('passA_f57v.tsv')
B = load('passB_f57v.tsv')
C = load('passC_f57v.tsv')

dis = list(csv.DictReader(open('recon_box_f57v/disagreements.tsv'), delimiter='\t'))

# One three-way split (A, B and C all gave different base codes): C's own crop call is kept, at conf H --
# a clean circle-with-centered-dot, an exact match to the 'o.' atlas plate, closer than A's plain read or
# B's 'H' guess (H atlas shapes are open loop/hook forms, not a filled circle-with-dot).
THREE_WAY_OVERRIDE = {
    ('11', '14'): ('o.', 'dot', 'C', "C's independent 'circle with centered dot' is an exact match to the 'o.' atlas plate; neither A's plain read nor B's 'H' (open loop/hook shapes) matches this filled-circle-plus-dot shape"),
}

settled = []
n_c_agrees = 0
n_three_way = 0
for r in dis:
    key = (r['line'], r['pos'])
    ra, rb, rc = A.get(key), B.get(key), C.get(key)
    ca = ra['code'].strip() if ra else 'MISSING'
    cb = rb['code'].strip() if rb else 'MISSING'
    cc = rc['code'].strip()
    ma = ra['marks'].strip() if ra else ''
    mb = rb['marks'].strip() if rb else ''
    mc = rc['marks'].strip()

    if cc == ca or cc == cb:
        n_c_agrees += 1
    if len({ca, cb, cc}) == 3:
        n_three_way += 1
        ov_code, ov_marks, ov_kept, ov_reason = THREE_WAY_OVERRIDE[key]
        code, marks = ov_code, ov_marks
        source = f'3-way->{ov_kept}'
        reason = f'A={ca} B={cb} C={cc}, all differ; {ov_reason}'
    elif ca == cb:
        code, marks, source = ca, ma, 'AB'
        reason = f'A and B agree ({ca}); C read {cc} independently ({rc["note"]})' if cc != ca else f'A, B and C all agree ({ca})'
    elif cc == ca:
        code, marks, source = ca, ma, 'AC'
        reason = f'C agrees with A ({ca}) against B ({cb}): {rc["note"]}'
    elif cc == cb:
        code, marks, source = cb, mb, 'BC'
        reason = f'C agrees with B ({cb}) against A ({ca}): {rc["note"]}'
    else:
        raise AssertionError(key)
    settled.append((r['line'], r['pos'], code, marks, source, reason))

with open('recon_box_f57v/settled.tsv', 'w') as f:
    f.write('line\tpos\tcode\tmarks\tsource\treason\n')
    for row in settled:
        f.write('\t'.join(row) + '\n')

print(f'{len(dis)} disagreement rows settled')
print(f'C agrees with A or B: {n_c_agrees}/{len(dis)} = {100*n_c_agrees/len(dis):.1f}%')
print(f'three-way splits (A, B, C all differ): {n_three_way}')
from collections import Counter
print('source counts:', Counter(s[4] for s in settled))
