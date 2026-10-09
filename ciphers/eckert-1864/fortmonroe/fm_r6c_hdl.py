#!/usr/bin/env python3
"""FM-R6c (9 Oct 2026): ten IIIF full pages (2400 px, to a scratch dir) for the eye check, and Huntington CONTENTdm full-text queries
(p16003coll11, CISOSEARCHALL) for rare names in the decodes. >= 3.2 s apart. Usage: fm_r6c_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['chambersburg', 'gaughey', 'christian advocate', 'albemarle sound', 'carlton and porter', 'illinois knox', 'wrangled knox', 'my mother nearly insane']
IMG = ['5777', '5659', '5786']
out = sys.argv[1]; n = 0
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    fp = os.path.join(out, f'p{p}.jpg')
    if os.path.exists(fp) and os.path.getsize(fp) > 10000: continue
    for attempt in (1, 2):
        try:
            open(fp, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); n += 1; break
        except Exception as e:
            n += 1; print('img', p, 'attempt', attempt, 'ERR', str(e)[:60], flush=True)
            if attempt == 2: sys.exit('stopped after one retry (good-citizen rule)')
            time.sleep(15)
    print('img', p, flush=True); time.sleep(3.3)
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
print('requests', n)
