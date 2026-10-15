#!/usr/bin/env python3
"""CLIN-3004C: build pNNN_reconciled.tsv from the one blind pass (pNNN_passA.tsv) plus the worker's image-only settlements
(pNNN_settle.tsv: crop, row, entry, underline, kind, grade, note; a row listed there overrides the pass). Consecutive clear rows are
merged into one clear cell (as CLIN-3004B did). Usage: recon_build.py 232|233"""
import sys
p = sys.argv[1]
def tsv(f):
    L = [l.rstrip('\n').split('\t') for l in open(f, encoding='utf-8') if l.strip() and not l.startswith('#')]
    return [dict(zip(L[0], r + [''] * (len(L[0]) - len(r)))) for r in L[1:]]
A = tsv(f'p{p}_passA.tsv')
try:
    S = {(r['crop'], r['row']): r for r in tsv(f'p{p}_settle.tsv')}
except FileNotFoundError:
    S = {}
out, idx = [], {}
for r in A:
    s = S.get((r['crop'], r['row']))
    kind = (s['kind'] if s and s['kind'] else r['kind'])
    kind = {'fig': 'letter'}.get(kind, kind)
    entry = s['entry'] if s and s['entry'] else r['entry']
    ul = s['underline'] if s and s['underline'] else r['underline']
    grade = s['grade'] if s and s['grade'] else 'H'
    note = s['note'] if s else ''
    col = r['crop']
    if kind == 'clear' and out and out[-1][0] == col and out[-1][2] == 'clear':
        out[-1][3] += ' ' + entry; out[-1][7] += ' | ' + r['entry']; continue
    idx[col] = idx.get(col, 0) + 1
    out.append([col, str(idx[col]), kind, entry, ul, '', grade, f"{r['entry']}/{r['underline']}",
                (f"{entry}/{ul}" if s else 'as pass'), note])
with open(f'p{p}_reconciled.tsv', 'w', encoding='utf-8') as f:
    f.write(f'# CLIN-3004C (15 Oct 2026): B.147 p.{p}, a closing page of the cipher of item 3004 (Clinton to Haldimand, 9 Sept 1780).\n'
            f'# ONE blind Sonnet pass p{p}_passA.tsv (column "passA") + worker image-only reconciliation p{p}_settle.tsv (column "worker"),\n'
            f'# settled on 2x zooms before any decode or score (PREREG-CLIN-3004.md Addendum CLIN-3004C). Built by recon_build.py {p}.\n')
    f.write('col\tidx\tkind\tentry\tunderline\tgloss\tgrade\tpassA\tworker\tnote\n')
    for o in out:
        f.write('\t'.join(o) + '\n')
print(p, len(out), 'cells;', sum(o[2] == 'letter' for o in out), 'letter;', {g: sum(o[6] == g for o in out if o[2] == 'letter') for g in 'HM'})
