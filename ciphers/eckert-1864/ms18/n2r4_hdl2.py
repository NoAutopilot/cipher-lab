#!/usr/bin/env python3
"""N2R-4 (10 Oct 2026): retry of the one dropped hdl query of n2r4_hdl.py (one retry after a 25 s pause) plus one positive control (cipher words of 9701/0)."""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
time.sleep(25)
for q in ['Curtis Rosecrans recalled pursuit Price contrary repeated orders', 'Veteran Baltic Sugar Hoffman Niagara detained Baron']:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
