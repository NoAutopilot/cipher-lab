#!/usr/bin/env python3
"""FM65-F: dump the ten Fort Monroe rows (mssEC 25 / obj 5952) into fm65f_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5919/2 5920/1 5923/1 5924/0 5924/1 5929/1 5929/2 5930/1 5931/0 5931/1 5933/0 5933/2 5936/0 5941/1 5943/1".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM65-F, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fm65f_entries.txt', 'w').write("\n".join(out))
