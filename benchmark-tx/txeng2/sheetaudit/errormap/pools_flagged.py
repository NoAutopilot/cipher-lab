#!/usr/bin/env python3
"""Eval-pool error-map re-run after V1/V2 (TXE2-SHEETAUDIT, 9 Oct 2026): the positions tables in this folder (tx_taxonomy.py
on the current truth files, which carry the V1/V2 verdicts: CORRECT re-forced, FLAG in the flag column), flagged positions
dropped (as tx_bench --exclude-flagged), baseline errors only (the first --pass of each run). Prints markdown.

    python3 benchmark-tx/txeng2/sheetaudit/errormap/pools_flagged.py

Pools: old = ERRORMAP's eval (no.87 eval_heldout f178v L13-23 + f179r L01-03, Spinelli); A4 = PREREG-txeng2-0 Amendment 4's
(old + f178r L01-03 + f152r)."""
import csv, os, re
from collections import Counter
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(D, '..', '..', '..', '..')
AC = ['all-same-wrong', 'all-wrong-split', 'majority-wrong', 'minority-wrong', 'baseline-only', 'no-other-pass']
EC = ['crop', 'look-alike', 'thin', 'other']
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def unit(item, line):
    if item != 'birago1572-no87':
        return {'spinelli-c1519-confirm': 'spinelli', 'birago1572-f152r': 'f152r'}[item]
    leaf, n = re.match(r'f(\d+[rv])_L(\d+)', line).groups()
    return {'178v': 'eval_heldout' if int(n) >= 13 else 'dev_tune', '179r': 'eval_heldout', '178r': 'f178r'}[leaf]


rows, nflag, scored = [], Counter(), Counter()
for item in ('birago1572-no87', 'spinelli-c1519-confirm', 'birago1572-f152r'):
    flag = {(t['line'], t['pos']): t.get('flag', '') for t in rd(os.path.join(R, f'benchmark-tx/{item}.truth.tsv'))}
    pos = rd(os.path.join(D, f'{item}_positions.tsv'))
    base = [c[4:] for c in pos[0] if c.startswith('err_')][0]
    for p in pos:
        u = unit(item, p['line'])
        if flag.get((p['line'], p['pos']), '').strip() and not flag[(p['line'], p['pos'])].startswith('corrected'):
            nflag[u] += p['err_' + base] == '1'; continue
        scored[u] += 1
        if p['err_' + base] == '1':
            rows.append((u, p['plain'], p['read_' + base] or 'deleted', p['agree_class'], p['err_class'] or 'other', p['line'], p['pos']))
units_old = ['eval_heldout', 'spinelli']; units_a4 = units_old + ['f178r', 'f152r']
print('| unit | baseline errors (flagged excluded) | scored | flagged baseline errors dropped |\n|---|---|---|---|')
for u in units_a4 + ['dev_tune']:
    print(f"| {u} | {sum(r[0] == u for r in rows)} | {scored[u]} | {nflag[u]} |")
for name, us in (('old ERRORMAP eval pool (eval_heldout + Spinelli)', units_old), ('Amendment 4 eval pool (+ f178r + f152r)', units_a4)):
    sel = [r for r in rows if r[0] in us]; n = len(sel)
    print(f'\n### {name}: {n} errors\n\n| agree_class | errors | share |\n|---|---|---|')
    for k, v in Counter(r[3] for r in sel).most_common():
        print(f'| {k} | {v} | {100 * v / n:.1f}% |')
    print('\n| err_class | errors | of which all-same-wrong |\n|---|---|---|')
    for k, v in Counter(r[4] for r in sel).most_common():
        print(f"| {k} | {v} | {sum(r[4] == k and r[3] == 'all-same-wrong' for r in sel)} |")
    print('\n| unit | truth <- read | n | agree_class |\n|---|---|---|---|')
    for (u, pl, rdg), v in Counter((r[0], r[1], r[2]) for r in sel).most_common():
        ac = Counter(r[3] for r in sel if (r[0], r[1], r[2]) == (u, pl, rdg))
        print(f"| {u} | {pl} <- {rdg} | {v} | {', '.join(f'{a} {b}' for a, b in ac.most_common())} |")
