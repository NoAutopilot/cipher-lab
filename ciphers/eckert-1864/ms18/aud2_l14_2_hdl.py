#!/usr/bin/env python3
"""AUD2-LEDGER14-2 (10 Oct 2026, second verifier; copy of fvl14b_hdl.py): Huntington CONTENTdm full-text queries (p16003coll11, CISOSEARCHALL, all pointers) on the clear words of E611 E612 E620 E621 N2-SA (positive control 9678 first), then IIIF leaves (2400 px, to a scratch dir) for the eye check.
>= 3.3 s apart. Usage: o9r1_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Inspector Inquiry evidence', 'Odell Bunker', 'Ferry Memphis', 'Ferry Louisville', 'Biggs forage', 'Brown forage', 'arms Harpers Ferry arrived']
IMG = [int(a) for a in sys.argv[2:]]
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs[:60]), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
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
print('requests', n)
