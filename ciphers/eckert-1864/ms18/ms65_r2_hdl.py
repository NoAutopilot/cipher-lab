#!/usr/bin/env python3
"""MS65-R2 (10 Oct 2026): Huntington CONTENTdm full-text queries (p16003coll11, CISOSEARCHALL, all pointers) on clear words of Y4 (10030/2) plus one positive control.
>= 3.3 s apart. A miss is a search result (rule 10). Usage: ms65_r1_hdl.py OUTDIR"""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Vance arrest Schofield Raleigh Wash', 'Chamberlain Isaacs and company July 1865', 'McCausland Emory Cumberland']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs[:60]), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
print('requests', n)
