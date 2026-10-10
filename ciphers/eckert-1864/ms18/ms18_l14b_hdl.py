#!/usr/bin/env python3
"""L14-B: Huntington CONTENTdm clear-copy queries (p16003coll11, CISOSEARCHALL, all pointers), one rare-plain-word query per row + control 'Inspector Inquiry evidence' (-> 9678) once. 9 requests, 3.3 s apart. A hit on another pointer is printed with title; own pointer ignored by the reader."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'),('9787','Acton Heights Edwards Wright Howe'),('9733','busshels Biggs Brown forage'),('9883','Robt Allen Ferry Memphis conduct'),
     ('9802','Gillem Schurz Johnston'),('9874','Hilton Head Van Vliet Brown'),('9779','Boons boro Middle town Urbana Monocacy'),('9743','Duffin Dover Stall'),('9686','Shelton Curtes Fort worth limits Department')]
n = 0
for tag, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    for att in (1, 2):
        try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); break
        except Exception as e:
            print('ERR', tag, e, flush=True)
            if att == 2: sys.exit(1)
            time.sleep(25)
    n += 1
    print(f'{tag} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
