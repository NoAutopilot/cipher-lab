#!/usr/bin/env python3
"""FM65-E: dump the fifteen Fort Monroe rows (mssEC 25 / obj 5952) into fm65e_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5898/1 5899/0 5902/1 5902/2 5904/1 5905/0 5907/1 5912/1 5914/1 5915/0 5915/1 5917/1 5918/0 5918/1 5919/1".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM65-E, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fm65e_entries.txt', 'w').write("\n".join(out))
