#!/usr/bin/env python3
"""BAL103-200: join a pass's s1/s2 rows into one row per line (s2 from its |> marker on), sorted by line, for
tools/reconcile_passes.py. Usage: join_lines.py IN.tsv OUT.tsv"""
import sys, re
rows = {}
for ln in open(sys.argv[1]):
    if ln.startswith('#') or '\t' not in ln: continue
    cid, tt = ln.rstrip('\n').split('\t', 1)
    m = re.match(r'(.*_L\d+)_s([12])$', cid.strip())
    if not m: continue
    rows.setdefault(m.group(1), {})[m.group(2)] = tt.split()
out = []
for line in sorted(rows, key=lambda c: int(c.rsplit('_L', 1)[1])):
    s1 = rows[line].get('1', []); s2 = rows[line].get('2', [])
    i = next((k for k, t in enumerate(s2) if t.startswith('|>')), None)
    tail = [] if i is None else [s2[i][2:]] + s2[i + 1:]
    if i is None and s2: sys.stderr.write(f'{line}: no |> marker in s2, s2 dropped\n')
    out.append(f"{line}_s1\t{' '.join(s1 + tail)}")
open(sys.argv[2], 'w').write('\n'.join(out) + '\n')
