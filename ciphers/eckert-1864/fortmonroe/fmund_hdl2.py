#!/usr/bin/env python3
"""FM-UND third fresh query per row without a located clear copy (lesson 5): control 9678 + one more per row. 3.3 s apart."""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'),
 ('5616/0c','steam tugs canal barges average capacity propellers'),
 ('5656/0c','oakumed sent to me under guard Shore'),
 ('5658/0c','Jamestown Eckert reserves retiring Meigs Ingalls'),
 ('5689/0c','Weitzell Chief Pelham Nankin Hunter Ransom Burton'),
 ('5759/0c','Hampton Fitz Lee Picketts Weldon Columbia'),
 ('5902/0c','Edisto windsor tarquinty obedient servant Lester')]
for tag, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(tag, 'ERR', str(e)[:80]); time.sleep(25)
        try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        except Exception as e2: print('stop', e2); break
    print(f'{tag} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
