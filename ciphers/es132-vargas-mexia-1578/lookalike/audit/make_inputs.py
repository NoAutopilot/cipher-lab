#!/usr/bin/env python3
"""ES132-AUDIT: write passA/B/C as (line,pos,sign) TSVs for tools/lookalike_pass.py audit, from the folder's own passes (test2.load_pass)
and committed ciphertext_<page>.tsv, same normalisation as lookalike/build_agreement.py. No label is changed."""
import sys, csv
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent.parent
sys.path[:0] = [str(HERE), str(HERE.parent.parent / 'tools')]
from test2 import load_pass
from test0 import load_lines
out = HERE / 'lookalike/audit'
for page in ('f51v', 'f52r'):
    srcs = {'A': load_pass(HERE / f'passes/{page}_passA.tsv'), 'B': load_pass(HERE / f'passes/{page}_passB.tsv'),
            'C': load_lines(HERE / f'ciphertext_{page}.tsv')}
    for k, d in srcs.items():
        with open(out / f'{page}_pass{k}.tsv', 'w', newline='') as f:
            w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['line', 'pos', 'sign'])
            for ln in sorted(d):
                for i, t in enumerate(d[ln], 1): w.writerow([ln, i, t.rstrip('?')])
