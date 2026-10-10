#!/usr/bin/env python3
"""FM65-D: dump the ten Fort Monroe rows (mssEC 25 / obj 5952) into fm65d_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5879/0 5883/0 5885/0 5885/1 5886/0 5887/0 5887/1 5888/1 5888/2 5889/2 5890/2 5891/1 5895/2 5896/2 5897/0 5861/2".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM65-D, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fm65d_entries.txt', 'w').write("\n".join(out))
