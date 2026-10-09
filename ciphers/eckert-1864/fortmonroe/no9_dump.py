#!/usr/bin/env python3
"""NO9-KEY (9 Oct 2026): dump five clean-fm.tsv rows whose best_book is 9 (shortest 1864 rows) into no9_entries.txt in the ### format
decode.load_ciphertext reads (same shape as fm_r5a_dump.py)."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = sys.argv[1:] or "5641/2 5717/0 5746/1 5576/1 5581/1".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### K{i} | row {r} | NO9-KEY, mssEC 25 / obj 5952, pointer {p}\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('no9_entries.txt', 'w').write("\n".join(out))
