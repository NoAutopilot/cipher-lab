#!/usr/bin/env python3
"""Quick raw pass-agreement stat for the two blind AX-4612TR passes (positional, no settling).
p1 passB is offset by +1 line vs passA (passB's r01 is the date header line passA skipped)."""
import csv, sys, collections

def load(path):
    rows = collections.defaultdict(dict)
    with open(path, encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            rows[row['line']][int(row['position'])] = row['token']
    return rows

def shift_p1b(rows):
    out = {}
    for line, toks in rows.items():
        n = int(line[4:])
        if n == 1:
            continue  # header line, no counterpart in passA
        out[f'p1_r{n-1:02d}'] = toks
    return out

base = 'ciphers/lodewijk-van-nassau-1573-74/ax4612tr/'
a1 = load(base+'passA_p1.tsv'); b1 = shift_p1b(load(base+'passB_p1.tsv'))
a2 = load(base+'passA_p2.tsv'); b2 = load(base+'passB_p2.tsv')

def compare(a, b, label):
    total = 0; agree = 0; disagree = []
    lines = sorted(set(a) | set(b))
    for line in lines:
        ta, tb = a.get(line, {}), b.get(line, {})
        positions = sorted(set(ta) | set(tb))
        for p in positions:
            va, vb = ta.get(p), tb.get(p)
            total += 1
            if va is not None and vb is not None and va.strip().lower() == vb.strip().lower():
                agree += 1
            else:
                disagree.append((line, p, va, vb))
    print(f'{label}: {agree}/{total} = {100*agree/total:.1f}% positional agreement')
    return total, agree, disagree

t1, a1n, d1 = compare(a1, b1, 'p1')
t2, a2n, d2 = compare(a2, b2, 'p2')
print(f'combined: {a1n+a2n}/{t1+t2} = {100*(a1n+a2n)/(t1+t2):.1f}%')
print(f'disagreements: p1 {len(d1)}, p2 {len(d2)}')
