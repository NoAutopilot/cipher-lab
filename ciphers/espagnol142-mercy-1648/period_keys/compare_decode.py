#!/usr/bin/env python3
"""Compare each DECODE Brussels letter table (decode_<record>.tsv) with ../key.tsv, code by code.

For every numeric code key.tsv carries that a table also carries (any row), count agreement (same letter,
u/v and i/j folded). Writes comparison.tsv; --check exits 1 if the committed comparison.tsv is stale.
Written 28 Sept 2026 by DECODE-OPEN (campaign row H17).
"""
import csv, glob, io, os, sys
here = os.path.dirname(os.path.abspath(__file__))
fold = lambda s: s.lower().replace('v', 'u').replace('j', 'i')
key = {}
for r in csv.DictReader(open(os.path.join(here, '..', 'key.tsv')), delimiter='\t'):
    if r['code'].isdigit():
        key[r['code']] = (fold(r['letter']), r['grade'])
out = io.StringIO()
out.write('record\ttable\tshared\tagree\tagree_codes\tdisagree (code:key.tsv/table)\n')
for f in sorted(glob.glob(os.path.join(here, 'decode_*.tsv'))):
    rec = os.path.basename(f)[7:-4]
    rows = [r for r in csv.DictReader((l for l in open(f) if not l.startswith('#')), delimiter='\t')]
    for tab in sorted({r['table'] for r in rows}):
        t = {}
        for r in rows:
            if r['table'] == tab and r['code'].isdigit() and r['grade'] != 'U':
                t.setdefault(r['code'], set()).add(fold(r['letter']))
        shared = sorted(set(key) & set(t), key=int)
        agree = [c for c in shared if key[c][0] in t[c]]
        dis = [f"{c}:{key[c][0]}/{'|'.join(sorted(t[c]))}" for c in shared if c not in agree]
        out.write(f"R{rec}\t{tab}\t{len(shared)}\t{len(agree)}\t{' '.join(agree)}\t{' '.join(dis)}\n")
res = out.getvalue()
path = os.path.join(here, 'comparison.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(path) and open(path).read() == res
    print('comparison.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(path, 'w').write(res); print(res, end='')
