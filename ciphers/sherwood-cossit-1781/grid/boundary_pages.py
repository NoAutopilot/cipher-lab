#!/usr/bin/env python3
"""Letter-section boundary pages of Entick 1781 from the OCR grid (SHERWOOD-GRID, 20 Oct 2026). Script only.

A page is a boundary page when the dominant headword initial of the page before differs from the page after (the OCR
of single columns is too noisy to place a centred heading, e.g. p.165 c1, so the flag is page-level and covers both
columns). Positive controls: p.153 (F->G, the 153 c2 rule) and p.165 (G->H, SHERWOOD-CELLS) must be flagged.
Crosses the flagged pages with every pair reading.tsv cites. Writes grid/boundary_cells.tsv.
  python3 grid/boundary_pages.py
"""
import csv, os, re
from collections import Counter
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pg = {}
for r in csv.reader(open(os.path.join(HERE, 'book', 'entick_lines.tsv'), encoding='utf-8'), delimiter='\t',
                    quoting=csv.QUOTE_NONE):
    if r[0] == 'page' or not r[0].isdigit():
        continue
    m = re.match(r"[^A-Za-z]*([A-Z][a-z]{2,})", r[5] if len(r) > 5 else '')
    if m:
        pg.setdefault(int(r[0]), Counter())[m.group(1)[0]] += 1
dom = {p: c.most_common(1)[0][0] for p, c in pg.items() if sum(c.values()) >= 8}
ps = sorted(dom)
flag = set()
for i in range(1, len(ps) - 1):
    a, b = dom[ps[i - 1]], dom[ps[i + 1]]
    if a != b and ps[i + 1] - ps[i - 1] == 2:
        flag.add(ps[i])
        if dom[ps[i]] == b:  # the boundary may sit at the foot of the page before
            flag.add(ps[i - 1])
assert {153, 165} <= flag, 'positive control missed'
cited = [r for r in csv.DictReader(open(os.path.join(HERE, 'reading.tsv'), encoding='utf-8'), delimiter='\t')
         if r['kind'] == 'pair' and r['page'] and int(r['page']) in flag]
with open(os.path.join(HERE, 'grid', 'boundary_cells.tsv'), 'w') as f:
    f.write('page\tW\tcol\tentry\tgrade\tline\n')
    for r in sorted(cited, key=lambda r: (int(r['page']), int(r['W']))):
        f.write('\t'.join([r['page'], r['W'], r['col'], r['entry'], r['grade'], r['line']]) + '\n')
print('boundary pages flagged (dictionary + gazetteer):', len(flag), sorted(flag))
print('cited pages among them:', sorted({int(r['page']) for r in cited}))
print('cited cells on flagged pages:', len(cited), Counter(r['grade'] for r in cited))
