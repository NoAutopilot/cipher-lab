#!/usr/bin/env python3
"""FM-UND: dump the 11 undated Fort Monroe entries (mssEC 25 / obj 5952) with their neighbours' dates (same page and adjacent pages)."""
import sys
sys.path.insert(0, '.')
import fm_entries as F
ROWS = "5568/0 5575/0 5616/0 5656/0 5658/0 5689/0 5759/0 5842/0 5902/0 5914/0 5951/0".split()
codes, ents = F.build()
byp = {}
for e in ents: byp.setdefault(e['pointer'], []).append(e)
out = []
for i, r in enumerate(ROWS, 1):
    p, n = map(int, r.split('/'))
    e = [x for x in byp[p] if x['entry_on_page'] == n][0]
    print(f"=== {r} page {e['page']} dir {e['direction']} words {e['words']} hdr={e['header']!r} addr={e['addr']!r} sender={e['sender']!r} cont={e['cont']}")
    for q in (p-1, p, p+1):
        for x in byp.get(q, []):
            print(f"   nb {q}/{x['entry_on_page']} {x['date']} {x['direction']} {x['header'][:50]!r} w{x['words']}")
    out.append(f"### U{i} | {r} | {p} | (FM-UND, row {r}, mssEC 25 / obj 5952)\n" + "\n".join(([e['header']] if e['header'] else []) + e['lines']) + "\n")
open('fmund_entries.txt', 'w').write("\n".join(out))
