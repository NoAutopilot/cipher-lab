#!/usr/bin/env python3
"""A3V3-SAVT stop point: decode ONE line of c370 (the open 29 Apr 1587 duplicata) with savt/table_proposed.tsv, as is.
Usage: python3 savt/c370_line_test.py [--line 5]"""
import argparse, os
from align import load_tokens, decode, HERE
ap = argparse.ArgumentParser(); ap.add_argument('--line', type=int, default=5); a = ap.parse_args()
vals = {}
for l in open(os.path.join(HERE, 'table_proposed.tsv')):
    if l.startswith('#') or l.startswith('pile\t'): continue
    f = l.split('\t')
    if f[3] not in ('?', '-'): vals[f[0]] = f[3]
toks = [t for t in load_tokens('c370') if t[0] == a.line]
print('piles :', ' '.join(t[2] for t in toks))
print('decode:', ''.join(c for c, _ in decode(toks, vals)))
print('tokens', len(toks), 'unmapped', sum(1 for t in toks if t[2] not in vals))
