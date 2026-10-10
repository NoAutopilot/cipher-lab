#!/usr/bin/env python3
"""FM65-A: dump the ten Fort Monroe rows (mssEC 25 / obj 5952) into fm65a_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5847/2 5849/0 5849/1 5850/1 5851/0 5851/1 5852/1 5852/2 5853/1 5854/0 5854/1 5855/2".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM65-A, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fm65a_entries.txt', 'w').write("\n".join(out))
