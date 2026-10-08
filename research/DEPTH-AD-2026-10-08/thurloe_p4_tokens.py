#!/usr/bin/env python3
"""DEPTH-AD: P4 cipher tokens in depth_stats order, from decode_stamford.decode_p4 with the committed key_stamford.tsv.
Clear words become a line break (new 'line' id), so a run never bridges a clear word; --bridge keeps one line."""
import sys
from pathlib import Path
P = Path(__file__).resolve().parents[2] / 'ciphers/thurloe-printed/pool_1654'
sys.path.insert(0, str(P))
import align_stamford as A, decode_stamford as D
rows = {}
for i, ln in enumerate(open(P / 'key_stamford.tsv')):
    f = ln.rstrip('\n').split('\t')
    if i:
        rows[int(f[0]) if f[0].isdigit() else f[0]] = (f[1], int(f[2]), int(f[3]), f[5], f[6])
toks, counts = D.decode_p4(A.djvu_lines(), rows)
bridge = '--bridge' in sys.argv
out, seg, n = ['line\tpos\tsign\tconf\tvalue\tgrade'], 0, 0
for kind, key, x, g in toks:
    if kind == 'W':
        if not bridge: seg += 1
        continue
    v = '' if x in ('_',) or x.startswith('[') else x.split('/')[0]
    if kind == 'T': v = x
    out.append(f'P4.s{seg:03d}\t{n}\t{key}\t\t{v}\t{g}'); n += 1
open(sys.argv[1], 'w').write('\n'.join(out) + '\n')
print(n, dict(counts), file=sys.stderr)
