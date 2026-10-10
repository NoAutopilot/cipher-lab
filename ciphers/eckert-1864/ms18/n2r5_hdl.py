#!/usr/bin/env python3
"""N2R-5 (10 Oct 2026): Huntington CONTENTdm full-text queries (p16003coll11, CISOSEARCHALL, all pointers), three rare clear words per N2R-5 row, plus a positive
control (a word bag from the N2R-5 rows' own transcription must return its own pointer). >= 3.3 s apart, one retry after 25 s on a dropped connection, then stop.
A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control 9804', 'Averell Greencastle McCoy'), ('Z1 9678', 'Inspector Inquiry evidence'), ('Z2 9757', 'Hurlbut McCook abolished'), ('Z3 9724', 'Shreveport gunboats Steele'),
     ('Z4 9771', 'Moorefield Romney Stahel'), ('Z5 9804', 'Leitersburg Mercersburg Couch'), ('Z6 9727', 'Washburn Hurlbut Illinois'), ('Z7 9765', 'ocean steamers Ingalls'),
     ('Z8 9780', 'Urbana Parkersburg Dana'), ('Z9 9876', 'appointments Senate confirmation'), ('Z10 9764', 'Stahel ammunition perilous')]
n = 0
for lab, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    for attempt in (1, 2):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1; break
        except Exception as e:
            n += 1; print(lab, 'attempt', attempt, 'ERR', str(e)[:70], flush=True)
            if attempt == 2: print('requests', n); sys.exit('stopped after one retry (good-citizen rule)')
            time.sleep(25)
    recs = d.get('records', [])
    print(f'{lab} | {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
