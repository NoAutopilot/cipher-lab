#!/usr/bin/env python3
"""FM65-E (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare PLAIN words of each of the fifteen rows
(not key-dependent words), plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'), ('5898/1','Sheldon wessells sligo wileys Rhode Island yard'), ('5899/0','Dumbarton Came bridge Tuesday promised convey'),
     ('5902/1','Vogdes Gordon investigation Eastern District Commission'), ('5902/2','Vogdes Gordon investigation progress quietly Emerick'), ('5904/1','Meagher Schofield Rucker ambulances mule teams'),
     ('5905/0','Meagher Morehead Palmer arriving transportation'), ('5907/1','Lynch Bureau letter ultimo immediate use squadron'), ('5912/1','Hastings Vinton anxious inquiry office imperative'),
     ('5914/1','Newbern Cape Fear Trenchard Wilmington Hampton Roads'), ('5915/0','Hastings station established Acting Chief Quartermaster James Asst. Supt'), ('5915/1','Cuyler Fisher Wilmington evacuation Terry supplies haste'),
     ('5917/1','Washburne Committee of Commerce Johnson rascal state evidence'), ('5918/0','Wilder Plato moneys negroes public property rescinded'), ('5918/1','pilots monitors Bradley furnish Navy James'),
     ('5919/1','Bowers Roberts proceed Beckwith ready Shall I go')]
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
