#!/usr/bin/env python3
"""TXP-B23: passZ_pipeline.tsv = rec/ciphertext_draft.tsv with every adjud_out.tsv row applied (NONE drops the column,
two labels split it). Line ids f23r_L01..L08. Run: python3 benchmark-tx/txeng2/bir1591-f23r-gloss/make_passZ.py"""
import csv, os, re
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
adj = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd(os.path.join(D, 'adjud_out.tsv'))}
out, cur, pos = [], None, 0
for r in rd(os.path.join(D, 'rec/ciphertext_draft.tsv')):
    key = (r['line'], int(r['position']))
    s = adj.get(key, r['sign'].strip())
    if r['line'] != cur:
        cur, pos = r['line'], 0
    if s in ('NONE', '-', ''):
        continue
    toks = []
    for w in s.split():  # a new sign starts at an upper-case label, NEW: or ?; lower-case words continue a NEW: description
        if toks and toks[-1].startswith('NEW:') and not re.match(r'(NEW:|\?|[A-Z]{1,6}$)', w):
            toks[-1] += ' ' + w
        else:
            toks.append(w)
    for t in toks:
        pos += 1
        out.append(('f23r_' + r['line'], pos, t))
with open(os.path.join(D, 'passZ_pipeline.tsv'), 'w', encoding='utf-8') as f:
    f.write('line\tpos\tsign\n')
    for o in out:
        f.write('%s\t%d\t%s\n' % o)
print(len(out), 'signs; adjudicated', len(adj))
