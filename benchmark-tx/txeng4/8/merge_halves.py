#!/usr/bin/env python3
"""TXE4-8: join a pass's two half-call reads (scratch r/<PASS>a/read.tsv + r/<PASS>b/read.tsv) into reads/<PASS>.tsv,
header once, rows in call order (a = L02-L20, b = L24-L36). python3 merge_halves.py PASS SCRATCH_ROOT"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
p, root = sys.argv[1], sys.argv[2]
out = []
for h in 'ab':
    rows = [l.rstrip('\n') for l in open(os.path.join(root, 'r', p + h, 'read.tsv'), encoding='utf-8') if l.strip()]
    if not out:
        out.append(rows[0])
    assert rows[0].split('\t') == out[0].split('\t'), 'half headers differ'
    out += rows[1:]
open(os.path.join(HERE, 'reads', p + '.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
lines = {}
for r in out[1:]:
    lines[r.split('\t')[0]] = lines.get(r.split('\t')[0], 0) + 1
print(p, len(out) - 1, 'rows;', ' '.join(f'{k} {v}' for k, v in lines.items()))
