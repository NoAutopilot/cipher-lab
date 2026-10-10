#!/usr/bin/env python3
"""FM-S2 (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare plain words of each of the ten rows,
plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'), ('5698/0','Colonel Biggs'), ('5638/0','Dunn endorsed'), ('5632/2','moments notice mandate'),
     ('5627/1','Spencer Rifles Edson'), ('5810/1','Beckwith admire Imogene'), ('5756/1','Sheridan Beckwith Caldwell cipher'),
     ('5720/0','continuous firing battery'), ('5814/0','Mahopac Saugus'), ('5768/3','Shaffer chief of staff fine morning'), ('5680/2','Extra arbitraries')]
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
