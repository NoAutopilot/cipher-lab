#!/usr/bin/env python3
"""FM-S65A: dump the ten Fort Monroe rows (mssEC 25 / obj 5952) into fms65a_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5845/2 5857/2 5858/2 5862/0 5862/2 5872/0 5872/1 5872/2 5874/1 5883/2 5892/0".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM-S65A, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fms65a_entries.txt', 'w').write("\n".join(out))
