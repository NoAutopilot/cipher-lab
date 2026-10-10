#!/usr/bin/env python3
"""AUD2-LEDGER-38 (10 Oct 2026; second audit, after FV-MS18o): Huntington CONTENTdm (p16003coll11) for E378 (9820/3, 16 Aug 1864, Princess / Keith) and E381 (9258/2, 27 July 1865, Ryan witness).
Usage: aud2_ledger38_hdl.py q SCRATCH  -> CISOSEARCHALL queries (all pointers, suppressfulltext=1);  aud2_ledger38_hdl.py i SCRATCH PTR ... -> item info (transc).
>= 3.3 s apart, one retry after a pause at most. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Princess released', 'Princess detectives', 'Princess Dana', 'Princess proceed', 'Keith Dana',
     'Ryan approved', 'Ryan Barton', 'Ryan witness']
def get(url):
    for a in (1, 2):
        try: return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        except Exception as e:
            print('ERR', str(e)[:60], flush=True)
            if a == 2: return None
            time.sleep(20)
mode, out = sys.argv[1], sys.argv[2]; n = 0
if mode == 'q':
    for q in Q:
        d = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/60/1/0/0/1/0/json"); n += 1
        if d: print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])), flush=True)
        time.sleep(3.3)
else:
    for p in sys.argv[3:]:
        d = get(HB + f"dmGetItemInfo/p16003coll11/{p}/json"); n += 1
        if d: print(p, '|', d.get('title'), '|', str(d.get('transc', '')).replace('\n', ' / '), flush=True)
        time.sleep(3.3)
print('requests', n)
