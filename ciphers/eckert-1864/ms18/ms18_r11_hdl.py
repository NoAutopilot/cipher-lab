#!/usr/bin/env python3
"""MS18-R11: Huntington CONTENTdm clear-copy queries (p16003coll11, CISOSEARCHALL, all pointers) for the one filed row 9730/1 (+ the N2R-6 positive control), then its IIIF leaf at 2400 px to scratch. >= 3.3 s apart. Usage: ms18_r10_hdl.py SCRATCH_DIR"""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Inspector Inquiry evidence', 'Rapidan crossed Grant Butler Richmond enemy battle', 'pocketed the Audit Judah message Germana', 'Sheldon Grant army crossed Rapidan effected']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
fp = os.path.join(out, 'p9730.jpg')
open(fp, 'wb').write(urllib.request.urlopen(urllib.request.Request('https://hdl.huntington.org/digital/iiif/p16003coll11/9730/full/2400,/0/default.jpg', headers=UA), timeout=120).read()); n += 1
print('img 9730', os.path.getsize(fp), 'requests', n)
