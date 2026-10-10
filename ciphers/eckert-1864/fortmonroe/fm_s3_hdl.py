#!/usr/bin/env python3
"""FM-S3 (10 Oct 2026): Huntington CONTENTdm p16003coll11 CISOSEARCHALL, one rare plain-word query per row (all pointers), positive control 9678 first.
>= 3.4 s apart; one retry after 25 s then stop. Plain words only (no key-dependent words)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control', 'Inspector difficulty Evidence Nashville'), ('F1 5720/2', 'pontoon Yorktown'), ('F2 5547/1', 'Peck Syracuse Horner'), ('F3 5569/1', 'map Richmond Lockwood Baldwin'),
 ('F4 5546/0', 'cooper ration'), ('F5 5577/0', 'cable repaired Patrick'), ('F6 5673/1', 'wrong route corrected'), ('F7 5672/1', 'Richmond Danville Rail Road cut'),
 ('F8 5641/0', 'Ironclads Gillmore Culpepper'), ('F9 5804/2', 'Horner transportation Nov'), ('F10 5669/1', 'Danville Rail Road cut Potomac'), ('F11 5664/2', 'erase Hurlbut Canby'),
 ('F12 5679/0', 'Sheridan Forage James'), ('F13 5830/0', 'Beaufort Hampton Roads Porter'), ('F14 5633/1', 'Exchanges against orders Clark Norfolk'), ('F15 5798/1', 'Halifax hospital Caldwell'),
 ('F16 5833/2', 'Birney message too late'), ('F17 5828/1', 'Shepley Beckwith Norfolk'), ('F18 5829/1', 'Ingalls Webster fleet'), ('F19 5800/2', 'Beckwith start hour'), ('F20 5590/0', 'deliver Grant Monroe Norfolk')]
n = 0
for lab, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    for a in range(2):
        try:
            n += 1; d = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); break
        except Exception as e:
            print('ERR', lab, str(e)[:60], flush=True)
            if a == 1: print('requests', n); sys.exit('stopped after one retry')
            time.sleep(25)
    recs = d.get('records', [])
    print(f'{lab} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
    time.sleep(3.5)
print('requests', n)
