#!/usr/bin/env python3
"""FM-S65B: dump the ten Fort Monroe rows (mssEC 25 / obj 5952) into fm_s65b_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5892/1 5893/1 5896/0 5896/1 5908/0 5910/1 5914/2 5928/2 5936/2 5941/2 5942/1".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM-S65B, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fm_s65b_entries.txt', 'w').write("\n".join(out))
