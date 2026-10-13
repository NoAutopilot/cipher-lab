#!/usr/bin/env python3
"""BAL167-GHV adoption (PREREG-BAL-GHV.md 'Target and adoption'): f.228 tokens of the hook and v classes, CONFIRMED by
balshape/ghv/score2.out (read 2; gates G1 1.000 / G2 0.000 PASS), move M -> S class-wide; values never change (asserted against the
ciphertext). Writes balshape/ghv/exceptions_b170f228.tsv = BAL-WL rows (balshape/wl/exceptions_b170f228.tsv) + these rows; decode.json
reads it. Token walk as balshape/wl/regrade.py. Run from the target folder."""
import re, collections
TOK = re.compile(r'\{[^}]*\}|\S+')
CLASS = {'hook': 's', 'v': 's'}
cipher = [l for l in open('ciphertext_b170f228.txt') if not l.startswith('#') and l.strip()]
rows = []
for f in ('passes/reconciled_b170f228r.tsv', 'passes/reconciled_b170f228v.tsv'):
    folio = f.split('_')[1].split('.')[0]
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        lid, toks = ln.rstrip('\n').split('\t'); line = lid.split('_', 1)[1]
        ct = next(c for c in cipher if c.startswith(f'{folio} {line} |')).split('|', 1)[1].split()
        pos = 0
        for t in TOK.findall(toks):
            if t.startswith('{'):
                pos += len(t[1:-1].split()); continue
            sh = t.rstrip('?')[2:] if t.startswith('s:') else None
            val = CLASS.get(sh)
            if val:
                assert ct[pos] == f'L:{val}?', (folio, line, pos, ct[pos], t, val)
                rows.append((folio, line, pos, val, 'S', f'BAL167-GHV: class {sh} CONFIRMED (PREREG-BAL-GHV, read 2 G1 1.000 G2 0.000, score2.out)'))
            pos += 1
wl = open('balshape/wl/exceptions_b170f228.tsv').read().rstrip('\n') + '\n'
with open('balshape/ghv/exceptions_b170f228.tsv', 'w') as o:
    o.write(wl + ''.join('\t'.join(map(str, r)) + '\n' for r in rows))
print(len(rows), 'tokens M -> S', dict(collections.Counter(r[5].split('class ')[1].split(' CONF')[0] for r in rows)))
