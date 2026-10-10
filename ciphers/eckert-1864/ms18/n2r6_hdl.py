#!/usr/bin/env python3
"""N2R-6 (10 Oct 2026): Huntington CONTENTdm full-text queries (p16003coll11, CISOSEARCHALL, all pointers), three rare clear words per N2R-6 row, plus a positive
control (a word bag from the N2R-6 rows' own transcription must return its own pointer). >= 3.3 s apart, one retry after 25 s on a dropped connection, then stop.
A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control 9678', 'Inspector Inquiry evidence'), ('Z4 9729 KA', 'instructions Cairo telegraphed President'), ('Z5 9697 KB', 'regiment heavy artillery Harpers Ferry Sigel'),
     ('Z7 9908 KC', 'New Creek disaster Canby Mobile Ohio'), ('Z8 9798 KD', 'heavy artillery spare Wright Washington'), ('Z9 9832 KE', 'Onondaga Atlanta Saugus Canonicus')]
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
