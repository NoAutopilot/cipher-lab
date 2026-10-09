#!/usr/bin/env python3
"""CONF-FM (9 Oct 2026, account 1): holder full-text search (p16003coll11 CISOSEARCHALL, all pointers) for a clear copy of E254
(Brice to Sheldon, 12 Dec 1864, Binney). >= 3.2 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, re, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n = 0
for q, rx in [('binney outlay', r'outlay'), ('binney brice', r'binney')]:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/200/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print(f'== {q!r}: {d.get("pager", {}).get("total")} hits')
    for r in d.get('records', [])[:40]:
        t = str(r.get('transc') or ''); m = re.search(rx, t, re.I)
        print(f'  {r.get("pointer")} | {str(r.get("title"))[:30]} | ' + (t[max(0, m.start()-150):m.end()+150].replace('\n', ' ') if m else '(not in window)'))
    time.sleep(3.2)
print('requests', n)
