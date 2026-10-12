#!/usr/bin/env python3
"""TXE4-3 A5 gate: atlas/secure_tokens.tsv (joined by secure_tokens.py's page-level LCS, not by box_token_align) as a map
(sid, line = <page>_L<nn> with nn the passage's index on its page in file order, pos = posA, op 1:1) against the agreement files' pass-A token sequence, checked by
tools/join_check.py with the step-2 kNN top-1 as check labels (unsteered: those labels never built the LCS join).
f152r rows are excluded (eval item). Writes labels/a5_map.tsv (+ .joincheck.json). Never reads a truth file."""
import csv, os, sys, subprocess, json
sys.path.insert(0, 'tools'); import box_token_align as BA
A = 'ciphers/nevers-birago-fr3251-1572/atlas'; H = 'ciphers/nevers-birago-fr3251-1572/harvest'; L = 'benchmark-tx/txeng4/3/labels'
FILES = {'f139v': 'f139v/passC_agreement.tsv', 'f144r': 'f144r/passC_agreement.tsv', 'f162r': 'f162r/passC_agreement.tsv',
         'f174r': 'f174r/passC_agreement.tsv', 'f174v': 'f174v/passC_agreement.tsv', 'f174vB': 'f174vB/passC_agreement.tsv',
         'f175v': 'f175v/passC_agreement.tsv', 'f184r': 'f184r/passC_agreement.tsv', 'f185r': 'f185r/passC_rest90_agreement.tsv'}
read = []
IDX = {}
def lname(page, passage):            # join_check parses <page>_L<nn>: number the passages per page in file order
    key = (page, passage)
    if key not in IDX:
        IDX[key] = 1 + sum(1 for k in IDX if k[0] == page)
    return f'{page}_L{IDX[key]:02d}'
for leaf, fn in FILES.items():
    for r in BA.rd(f'{H}/{fn}'):
        if r['posA'] and r['idA']:
            page = r['passage'].split('_')[0] if '_' in r['passage'] else leaf
            read.append(dict(line=lname(page, r['passage']), pos=r['posA'], sign=r['idA']))
# f174vB's R01/V0x rows name pages f175r/f175v in secure_tokens (page column); mirror that
for r in BA.rd(f'{H}/f174vB/passC_agreement.tsv'):
    if r['posA'] and r['idA'] and not r['passage'].startswith('L'):
        page = 'f175r' if r['passage'].startswith('R') else 'f175v'
        read.append(dict(line=lname(page, r['passage']), pos=r['posA'], sign=r['idA']))
BA.wr(f'{L}/a5_read.tsv', ['line', 'pos', 'sign'], read)
rows = [dict(sid=r['sid'], page=r['page'], line=lname(r['page'], r['passage']), pos=r['pos'], op='1:1', labels='', status='', loo_pos='')
        for r in BA.rd(f'{A}/secure_tokens.tsv') if r['page'] != 'f152r' and (r['page'], r['passage']) in IDX]
BA.wr(f'{L}/a5_map.tsv', ['sid', 'page', 'line', 'pos', 'op', 'labels', 'status', 'loo_pos'], rows)
print('A5 map rows (secure tokens minus f152r):', len(rows))
out = subprocess.run([sys.executable, 'tools/join_check.py', '--map', f'{L}/a5_map.tsv', '--check-labels', f'{L}/step2_top1.tsv',
                      '--read', f'{L}/a5_read.tsv'], capture_output=True, text=True)
print(out.stdout.strip()); res = json.load(open(f'{L}/a5_map.tsv.joincheck.json'))
print('A5 join verdict:', res['verdict'], res['overall'], 'lines', {l: d['verdict'] for l, d in res['lines'].items()})
