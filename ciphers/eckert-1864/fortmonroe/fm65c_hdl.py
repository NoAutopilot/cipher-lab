#!/usr/bin/env python3
"""FM65-C (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare PLAIN words of each of the twelve rows
(not key-dependent words), plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'), ('5867/0','Cosgrove Robie bearings'), ('5868/0','Annapolis coal Sampson impossible'), ('5867/2','Emerick Abbott'),
     ('5869/1','Carney Tappan Janeway'), ('5870/0','Beckwith Ariel Sedgwick arrived'), ('5871/0','Ericsson approbation puritans'), ('5871/1','Sedgwick Ariel sailed perfect order'),
     ('5873/1','Oriental Morgan half hour'), ('5877/0','Bradley mule teams complete'), ('5877/1','splendid outside entrenched Fisher'), ('5877/2','Haze Sentinel Thames Dupont'),
     ('5878/1','disabled wagons mortars Fisher')]
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
