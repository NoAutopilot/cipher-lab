#!/usr/bin/env python3
"""AUD2-LEDGER-13 (9 Oct 2026, account 4): second-audit Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL,
suppressfulltext=1) across ALL pointers on clear words of E228 (5814), E229 (5833), E240 (5784) that FV-FM6b (fv_fm6b_hdl.py)
did not query. >= 3.2 s apart. Usage: aud2_l13_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['woods', 'mister woods', 'herald', 'cloudy', 'yell', 'dock tours', 'surgeon hand', 'wise']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        recs = d.get('records', [])
        print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs))
        json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    except Exception as e: print(q, 'ERR', e)
    n += 1; time.sleep(3.2)
print('requests', n)
