#!/usr/bin/env python3
"""GAPS9 (2 Oct 2026): fold the native-resolution second gloss pass into no4/reconcile.tsv.

Reads no4/gaps9_cells.tsv (id -> leaf, order), no4/gaps9_passA.tsv and no4/gaps9_passB.tsv (two blind Opus reads of
the 82 doubtful cells, scripts/no4_cells.py sheets) and the GAPS8 table read (no4/gloss_*.tsv + reconcile.tsv).
A cell changes ONLY when both passes agree on the gloss (accents/case/trailing punctuation folded) and on the code
digits, and the agreed gloss differs from the current one; a struck cell (crossed-out) is never changed. Split cells
stay as they are (M via no4_align's plain-copy check). Writes no4/gaps9_compare.tsv (every cell, A, B, outcome) and
adds/updates reconcile.tsv rows (basis 'GAPS9 native 2-pass agree'). Idempotent. Usage: python3 scripts/no4_gaps9_apply.py
"""
import csv, unicodedata
def f(s):
    s = unicodedata.normalize('NFD', s or '')
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn').lower().strip(' -=.')
dig = lambda s: ''.join(c for c in s or '' if c.isdigit())
L = lambda p: {r['id']: r for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t')}
A, B = L('no4/gaps9_passA.tsv'), L('no4/gaps9_passB.tsv')
cells = list(csv.DictReader(open('no4/gaps9_cells.tsv', encoding='utf-8'), delimiter='\t'))
rec = list(csv.DictReader(open('no4/reconcile.tsv', encoding='utf-8'), delimiter='\t'))
fields = list(rec[0].keys())
recd = {r['where']: r for r in rec}
cur = {}
for p in ('205R', '206L', '206R', '207L'):
    for r in csv.DictReader(open(f'no4/gloss_{p}.tsv', encoding='utf-8'), delimiter='\t'):
        w = f'{p}:{r["order"]}'
        code, gloss, note = dig(r['code']), r['gloss'], r.get('note') or ''
        if w in recd and recd[w]['basis'].startswith('GAPS9'):
            pass   # re-run: compare against the GAPS8 value kept in the row's table_read/basis
        elif w in recd:
            code = dig(recd[w]['settled_code']) or code; gloss = recd[w]['settled_gloss'] or gloss
        cur[w] = (code, gloss, note)
out = []; n = 0
for c in cells:
    w = c['leaf'][4:] + ':' + c['order']; a, b = A[c['id']], B[c['id']]
    code, gloss, note = cur[w]
    same_g = f(a['gloss']) == f(b['gloss']); same_c = dig(a['code']) == dig(b['code'])
    if 'crossed' in note.lower() or '[' in a['gloss'] + b['gloss'] and same_g and f(a['gloss']).startswith(f(gloss)):
        res = 'kept (struck cell)'
    elif not (same_g and same_c):
        res = 'kept (passes split)'
    elif f(a['gloss']) == f(gloss) and dig(a['code']) == code:
        res = 'confirmed'
    else:
        new = a['gloss'].strip()
        if b['conf'] == 'H' and a['conf'] != 'H': new = b['gloss'].strip()
        new = new.rstrip(' -=')
        if gloss.rstrip().endswith(('-', '=')): new += gloss.rstrip()[-1]
        res = f'changed {gloss} -> {new}'; n += 1
        recd[w] = {**{k: '' for k in fields}, 'where': w, 'table_read': f'{code} {gloss}', 'raw_read': '',
                   'settled_code': dig(a['code']), 'settled_gloss': new, 'conf': 'H' if 'H' in (a['conf'], b['conf']) else 'L',
                   'basis': f'GAPS9 native 2-pass agree (A {a["gloss"]} {a["conf"]}, B {b["gloss"]} {b["conf"]}); GAPS8 value {gloss}'}
    out.append([c['id'], w, code, gloss, a['code'], a['gloss'], a['conf'], b['code'], b['gloss'], b['conf'], res])
with open('no4/gaps9_compare.tsv', 'w', encoding='utf-8', newline='') as fh:
    wr = csv.writer(fh, delimiter='\t', lineterminator='\n')
    wr.writerow(['id', 'where', 'gaps8_code', 'gaps8_gloss', 'A_code', 'A_gloss', 'A_conf', 'B_code', 'B_gloss', 'B_conf', 'outcome'])
    wr.writerows(out)
with open('no4/reconcile.tsv', 'w', encoding='utf-8', newline='') as fh:
    wr = csv.DictWriter(fh, fieldnames=fields, delimiter='\t', lineterminator='\n'); wr.writeheader()
    for r in recd.values(): wr.writerow(r)
from collections import Counter
print(Counter(o[-1].split(' ')[0] for o in out), 'changed', n)
