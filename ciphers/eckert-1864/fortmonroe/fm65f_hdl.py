#!/usr/bin/env python3
"""FM65-F (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare PLAIN words of each of the fifteen rows
(not key-dependent words), plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'), ('5919/2','Sumner mounted rifles Emerick'), ('5920/1','Wright commence work flat plank'), ('5923/1','foreman diggers shovels vices plyers Climbers'),
     ('5924/0','moving office accommodation precedent instigation'), ('5924/1','Sheridan Lynchburg Sherman cavalry Beckwith'), ('5929/1','Glisson Convoy pilot Roberts Babcock'),
     ('5929/2','Champion Fayetteville Kennebec Wilmington'), ('5930/1','Hurlbut Montauk Senior Officer'), ('5931/0','Windsor Dealy boat arrival deliver'),
     ('5931/1','Gordon Emerick gunboats cavalry land Norfolk'), ('5933/0','guide Boyle Blackwater Broad Ford Gordon'), ('5933/2','Hartsuff Gordon district relieved continue'),
     ('5936/0','Sinclair Tribune Goldsboro Sherman occupied'), ('5941/1','Roanoke Chowan maps Russia Steamer'), ('5943/1','barges geese Morehead exertions spared')]
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
