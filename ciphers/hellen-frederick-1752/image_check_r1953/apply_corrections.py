#!/usr/bin/env python3
"""R7A-HEL53 (6 Oct 2026): apply corrections.tsv (image check of R1953 against DECODE's transcription) to
../key_r4369/R1953_pipe.txt and write R1953_pipe_high.txt (high-confidence corrections only) and R1953_pipe_all.txt
(high + medium). ciphertext_R1953.txt is not touched (rule 2: never silently repaired). Then
`python3 tools/decode_key.py ciphers/hellen-frederick-1752/image_check_r1953 [--check]` decodes both with the R4369 key.
Usage: python3 apply_corrections.py"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', 'key_r4369', 'R1953_pipe.txt')).read().split()
head, toks = src[:3], src[3:]
assert len(toks) == 846, len(toks)
rows = list(csv.DictReader(open(os.path.join(HERE, 'corrections.tsv')), delimiter='\t'))
for level, keep in (('high', {'high'}), ('all', {'high', 'medium'})):
    out = list(toks)
    for r in rows:
        if r['confidence'] in keep:
            out[int(r['pos'])] = r['image_value']  # a split ('1426 903') becomes two groups on write
    open(os.path.join(HERE, f'R1953_pipe_{level}.txt'), 'w').write(' '.join(head + out) + '\n')
    print(level, sum(r['confidence'] in keep for r in rows), 'corrections')
