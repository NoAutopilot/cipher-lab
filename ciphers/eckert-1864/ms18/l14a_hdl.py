#!/usr/bin/env python3
"""L14-A (10 Oct 2026): Huntington CONTENTdm CISOSEARCHALL (p16003coll11, all pointers) on rare plain words of the eight L14-A rows; control 9678 once. >= 3.3 s apart, one retry then stop.
A hit at a pointer other than the row's own is a candidate holder clear copy. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control 9678', 'Schermerhorn Maxon Amos State agent'),
     ('Y1 9835', 'mischief Pacific coast associates'), ('Y2 9877', 'furlough vote Delaware cavalry Hurlbut'),
     ('Y3 9793', 'Rockville Edwards Ferry Offutts Cross Roads Hunter'), ('Y4 9826', 'Mosby exempt Upperville conscripting'),
     ('Y5 9806', 'Noland Ferry Hancock guerrillas Couch'), ('Y6 9777', 'Ricketts ambulances wagons Banks Depot'),
     ('Y7 9823', 'Muddy Branch wharf scout'), ('Y8 9865', 'Pope regiments Schofield Kent Hood Tennessee')]
n = 0
for lab, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    for att in (1, 2):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1; break
        except Exception as e:
            n += 1; print('ERR', lab, str(e)[:60]); 
            if att == 2: print('requests', n); sys.exit('stopped after one retry')
            time.sleep(25)
    print(f'{lab} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
