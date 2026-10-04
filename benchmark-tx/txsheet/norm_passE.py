#!/usr/bin/env python3
"""TX-SHEET (4 Oct 2026): normalise the blind pass E (per-hand exemplar sheet) files to the benchmark output format
(line, pos, sign), the same way benchmark-tx/build_birago87.py normalises pass A. Prose-split runs (L01.1, L01.2) are
joined into their line in order. Run from the repo root: python3 benchmark-tx/txsheet/norm_passE.py"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, '..', 'outputs', 'birago1572-no87', 'passE_sheet.tsv')
FILES = [('f178r', 'passE_f178r.tsv'), ('f178v', 'passE_f178v_L01-10.tsv'), ('f178v', 'passE_f178v_L11-23.tsv'),
         ('f179r', 'passE_f179r.tsv')]
out = []
for leaf, fn in FILES:
    rows = list(csv.DictReader((l for l in open(os.path.join(D, fn)) if not l.startswith('#')), delimiter='\t'))
    n = {}
    for r in rows:
        ln = '%s_%s' % (leaf, r['passage'].split('.')[0])
        n[ln] = n.get(ln, 0) + 1
        out.append((ln, str(n[ln]), r['sign_id']))
with open(OUT, 'w') as f:
    f.write('line\tpos\tsign\n')
    for o in out:
        f.write('\t'.join(o) + '\n')
print(len(out), 'signs ->', OUT)
