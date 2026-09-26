#!/usr/bin/env python3
"""AX-MERGE3: token-level diff of the four *_full readings, key_full v2 (snapshot in axmerge3/v2/) -> v3 (current).
  python3 axmerge3/diff_v2_v3.py [--check]   writes axmerge3/diff_v2_v3.tsv; --check exits 1 if stale"""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)

def rows(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def build():
    o = io.StringIO(); w = csv.writer(o, delimiter='\t', lineterminator='\n')
    w.writerow(['letter', 'line', 'idx', 'sign', 'v2_value', 'v2_grade', 'v3_value', 'v3_grade', 'kind'])
    for n in ['5797', '4610', '4611', '4616']:
        a = rows(os.path.join(H, 'v2', f'reading_{n}_full_tokens.tsv'))
        b = rows(os.path.join(T, f'reading_{n}_full_tokens.tsv'))
        assert [(r['line'], r['idx'], r['sign']) for r in a] == [(r['line'], r['idx'], r['sign']) for r in b], n
        for x, y in zip(a, b):
            if (x['value'], x['grade']) != (y['value'], y['grade']):
                kind = 'value' if x['value'] != y['value'] else 'grade'
                w.writerow([n, x['line'], x['idx'], x['sign'], x['value'], x['grade'], y['value'], y['grade'], kind])
    return o.getvalue()

t = build(); p = os.path.join(H, 'diff_v2_v3.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(p) and open(p).read() == t; print('up to date' if ok else 'stale'); sys.exit(0 if ok else 1)
open(p, 'w').write(t)
