#!/usr/bin/env python3
"""FM-R3c: loose single-term / proximity grep (lowercase, whitespace-collapsed) in the scratch OR/ORN texts + cached Butler IV/V. Args: VOL.txt... Terms below.
Prints count and up to 3 snippets (+-110 chars) per term per volume. A miss is a search result (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = [t.split('@@') for t in os.environ.get('Q', '').split(';;') if t]
texts = {}
for p in ['privateofficialc04butl', 'privateofficialc05butl']:
    texts[p] = gzip.open(os.path.join(D, p + '_djvu.txt.gz'), 'rt', errors='ignore').read()
for p in sys.argv[1:]: texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
texts = {k: re.sub(r'\s+', ' ', v) for k, v in texts.items()}
for q in Q:
    label, pat = q[0], q[1]
    r = re.compile(pat, re.I)
    for v, t in texts.items():
        ms = list(r.finditer(t))
        if ms:
            print(f'## {label} | {v} x{len(ms)}')
            for m in ms[:int(os.environ.get('N', 3))]: print('   ', t[max(0, m.start()-110):m.end()+110])
