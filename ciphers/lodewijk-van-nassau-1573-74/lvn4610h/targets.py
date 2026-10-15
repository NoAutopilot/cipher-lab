#!/usr/bin/env python3
"""LVN-4610H targets: H numeral rows of ciphertext_4610.tsv ending in 1 or 8, outside p1_L04/p1_L09. Writes targets.tsv
(line, position, pre_pos, sign). pre_pos maps the current row back to lvn10/ciphertext_4610_pre.tsv (apply.py's key);
split rows (no pre_pos of their own) are written with pre_pos '-'. Offline. targets.tsv is the pre-registration snapshot (pushed in the PREREG commit, before any image look); the two rows LVN-4610H changed to M no longer select, so a re-run after the apply differs by those two rows by design."""
import csv, os, sys, re
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
cur = rd(os.path.join(T, 'ciphertext_4610.tsv')); pre = rd(os.path.join(T, 'lvn10', 'ciphertext_4610_pre.tsv'))
from collections import defaultdict
P = defaultdict(list); C = defaultdict(list)
for r in pre: P[r['line']].append(r)
for r in cur: C[r['line']].append(r)
mp = {}
for ln, rows in C.items():
    i = 0
    for p in P[ln]:
        m = re.search(r'from pre pos (\d+)', rows[i]['why']) if i < len(rows) else None
        if m and rows[i]['why'].startswith('split') and m.group(1) == p['position']:
            while i < len(rows) and rows[i]['why'].startswith('split') and re.search(r'from pre pos (\d+)', rows[i]['why']).group(1) == p['position']:
                mp[(ln, rows[i]['position'])] = '-'; i += 1
        else:
            mp[(ln, rows[i]['position'])] = p['position']; i += 1
    assert i == len(rows), ln
out = 'line\tposition\tpre_pos\tsign\n' + ''.join(
    f"{r['line']}\t{r['position']}\t{mp[(r['line'], r['position'])]}\t{r['sign']}\n" for r in cur
    if r['confidence'] == 'H' and r['sign'].isdigit() and r['sign'][-1] in '18' and r['line'] not in ('p1_L04', 'p1_L09'))
p = os.path.join(H, 'targets.tsv')
if '--check' in sys.argv: sys.exit(0 if open(p).read() == out else 1)
open(p, 'w').write(out); print(out.count('\n') - 1, 'targets')
