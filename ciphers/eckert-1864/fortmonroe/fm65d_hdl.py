#!/usr/bin/env python3
"""FM65-D (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare PLAIN words of each of the sixteen rows
(not key-dependent words), plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'), ('5879/0','Tribune Special Correspondent Vanderbilt garrison'), ('5883/0','Varina Blair passed lines'), ('5885/0','Cassandria Ranger Rucker'),
     ('5885/1+5886/0','torpedoes insulating wire Parker'), ('5887/0','Nevada Rucker Lynch torpedoes'), ('5887/1','Saugus Berrien turn'), ('5888/1','Ord absent several days operations'),
     ('5888/2','Palmer Newbern prepare accordingly'), ('5889/2','Schofield Willards Boyd batteries Kentucky mules'), ('5890/2','Portsmouth detached executive Parker'),
     ('5891/1','forgetting cipher book missed train pupils'), ('5895/2','Bates President Annapolis Point Lookout boat'), ('5896/2','Stager Schofield cipher operator construction'),
     ('5897/0','Blodget Anderson Schofield Sherman despatches'), ('5861/2b','Butler left Monroe Beckwith enquired')]
n = 0
for tag, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    except Exception as e:
        n += 1; print(tag, q, 'ERR', str(e)[:80], flush=True); time.sleep(25)
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print(f'{tag} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
