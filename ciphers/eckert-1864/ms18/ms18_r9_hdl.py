#!/usr/bin/env python3
"""MS18-R9 (10 Oct 2026): Huntington CONTENTdm full-text queries (p16003coll11, CISOSEARCHALL, all pointers) on clear words of the four filed rows, then their four IIIF leaves
(2400 px, scratch) for the eye check. >= 3.3 s apart, one retry then stop. Usage: ms18_r9_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Comstock Monocacy Hunter Grant Ord headquarters', 'Maxon State agent McHenry Dana arrest', 'Rockville Edwards Ferry Offutts Wright Hunter junction', 'Rawlins Saint Louis Thomas Hood Rosecrans reinforcements']
IMG = [9811, 9877, 9793, 9882]
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'; fp = os.path.join(out, f'p{p}.jpg')
    for attempt in (1, 2):
        try:
            open(fp, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); n += 1; break
        except Exception as e:
            n += 1; print('img', p, 'attempt', attempt, 'ERR', str(e)[:60], flush=True)
            if attempt == 2: sys.exit('stopped after one retry')
            time.sleep(25)
    print('img', p, flush=True); time.sleep(3.3)
print('requests', n)
