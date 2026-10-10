#!/usr/bin/env python3
"""FM-S3: dump the twenty Fort Monroe rows (mssEC 25 / obj 5952) into fm_s3_entries.txt in the ### format decode.load_ciphertext reads,
and print the share scorer's three shares from HEAD code (fm_entries.build())."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5720/2 5547/1 5569/1 5546/0 5577/0 5673/1 5672/1 5641/0 5804/2 5669/1 5664/2 5679/0 5830/0 5633/1 5798/1 5833/2 5828/1 5829/1 5800/2 5590/0".split()
codes, ents = F.build()
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in ents if x['pointer'] == p and x['entry_on_page'] == n][0]
    print(r, e['date'], e['direction'], 'shares', e['s1'], e['s2'], e['s9'], 'share_book', e['share_book'], 'cont', e['cont'])
    out.append(f"### F{i} | {r} | {p} | (FM-S3, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fm_s3_entries.txt', 'w').write("\n".join(out))
