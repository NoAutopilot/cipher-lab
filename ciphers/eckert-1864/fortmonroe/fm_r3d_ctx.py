#!/usr/bin/env python3
"""FM-R3d: print the original-text context of a letters-only phrase hit. Usage: fm_r3d_ctx.py VOL 'phrase' [before] [after]; VOL = cached gz id or scratch .txt path."""
import re, gzip, os, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
v, ph = sys.argv[1], sys.argv[2]; b = int(sys.argv[3]) if len(sys.argv) > 3 else 600; a = int(sys.argv[4]) if len(sys.argv) > 4 else 1400
p = os.path.join(D, v + '_djvu.txt.gz')
t = gzip.open(p, 'rt', errors='ignore').read() if os.path.exists(p) else open(v, errors='ignore').read()
idx = [i for i, c in enumerate(t) if c.isalpha()]; L = ''.join(t[i].lower() for i in idx)
k = L.find(re.sub(r'[^a-z]', '', ph.lower()))
if k < 0: print('NO HIT'); sys.exit(1)
s = idx[k]; print(re.sub(r'\n\s*\n', '\n', t[max(0, s - b):s + a]))
