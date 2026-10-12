#!/usr/bin/env python3
"""TXE4-9: normalise a reader's f.89 output (passage L01..L14, CLEAR rows, '.' rows) to the committed scoring convention of
benchmark-tx/outputs/dint-f89-gloss/pass*.tsv: drop CLEAR rows and '.' rows (the item has no dots, RESULTS.md 'Dots dropped'),
prefix f89_, renumber pos from 1. Mechanical; no image, no truth.    python3 norm.py IN.tsv OUT.tsv"""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1], newline=''), delimiter='\t'))
n, out = {}, ['line\tpos\tsign']
for r in rows:
    s = (r.get('sign_id') or r.get('sign') or '').strip(); ln = (r.get('passage') or r.get('line') or '').strip()
    if not ln or not s or s in ('CLEAR', '.'):
        continue
    ln = ln if ln.startswith('f89_') else 'f89_' + ln
    n[ln] = n.get(ln, 0) + 1
    out.append('%s\t%d\t%s' % (ln, n[ln], s))
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
print('%s: %d rows -> %d signs on %d lines' % (sys.argv[1], len(rows), len(out) - 1, len(n)))
