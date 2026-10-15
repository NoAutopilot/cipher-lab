#!/usr/bin/env python3
"""MERCY-M33: longest contiguous H/C/S run in letters within one cipher segment (a clear word breaks a run, lines run on;
any non-HCS cipher token breaks it), before and after setting the given positions to S. Usage: runs.py [line:pos ...]"""
import csv, os, sys
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
acc = {tuple(a.split(':')) for a in sys.argv[1:]}
tok = {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv')), delimiter='\t')}
rows = []
for r in csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'):
    t = tok.get((r['line'], r['position']))
    rows.append(t if t else dict(line=r['line'], pos=r['position'], sign=r['sign'], grade='clear', value=''))
def runs(accepted):
    out, cur, start, prev_ok = [], 0, None, False
    best = []
    for r in rows:
        sign = r['sign']
        if sign.startswith('[PLAIN') or not r['grade'] or r['grade'] == 'clear':
            if cur: out.append((cur, start, last))
            cur, start = 0, None; continue
        g = 'S' if (r['line'], r['pos']) in accepted else r['grade']
        if g in 'HCS' and g:
            if cur == 0: start = f"{r['line']}:{r['pos']}"
            cur += len(r['value']); last = f"{r['line']}:{r['pos']}"
        else:
            if cur: out.append((cur, start, last))
            cur = 0
    if cur: out.append((cur, start, last))
    return sorted(out, reverse=True)
b, a = runs(set()), runs(acc)
print('before top3', b[:3]); print('after  top3', a[:3])
if '--joins' in os.environ.get('M33', ''):
    def seg_of(accepted, p):
        return [x for x in runs(accepted) if x]
    bl = {x for x in b}; al = [x for x in a if x not in bl]
    print('runs new or changed after:', sorted(al, reverse=True)[:6])
