#!/usr/bin/env python3
"""R8-HEL (6 Oct 2026): apply zero_eight/corrections.tsv (0/8 pass, rows with confidence 'high' only; 'ambiguous' rows are
listed, never applied) on top of image_check_r1953/R1953_pipe_all.txt (R7A-HEL53 high + medium) and write R1953_pipe_08.txt.
ciphertext_R1953.txt is not touched (rule 2). Positions are R7A-HEL53 'all'-stream positions (after the 1426/903 split).
Then `python3 tools/decode_key.py ciphers/hellen-frederick-1752/zero_eight [--check]` decodes with the R4369 key unchanged.
Usage: python3 apply_corrections.py"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'image_check_r1953', 'R1953_pipe_all.txt')).read().split()
head, toks = src[:3], src[3:]
assert len(toks) == 847, len(toks)
n = 0
for r in csv.DictReader(open(os.path.join(HERE, 'corrections.tsv')), delimiter='\t'):
    if r['confidence'] != 'high':
        continue
    p = int(r['pos'])
    assert toks[p].strip('_=?') == r['decode_tx'], (p, toks[p], r['decode_tx'])
    toks[p] = toks[p].replace(r['decode_tx'], r['image_value']).replace('?', '')  # a settled doubt mark is dropped
    n += 1
open(os.path.join(HERE, 'R1953_pipe_08.txt'), 'w').write(' '.join(head + toks) + '\n')
print(n, 'corrections applied')
