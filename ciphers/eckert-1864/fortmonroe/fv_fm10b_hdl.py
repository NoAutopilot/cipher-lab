#!/usr/bin/env python3
"""FV-FM10b (9 Oct 2026): first-verifier holder search for E319-E321. Huntington CONTENTdm full text across ALL pointers of
p16003coll11 (CISOSEARCHALL, suppressfulltext=1) on distinctive clear words of each entry, then the three entry pages at 2400 px
to a scratch dir for the eye check. >= 3.3 s apart, one retry at most. Usage: fv_fm10b_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['high masts', 'navigation must remain', 'Mattapony', 'string wire', 'half a mile', 'West Point',
     'regret having ordered', 'Bermuda hundreds', 'careful working', 'better posted', 'Nichols', 'builders',
     'dragged', 'anchors', 'cable', 'south shore', 'Doren']
IMG = ['5695', '5702', '5782']
out = sys.argv[1]; n = 0
def get(url, binary=False):
    global n
    for attempt in (1, 2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read(); n += 1; return r
        except Exception as e:
            n += 1; print('ERR', attempt, str(e)[:80], flush=True)
            if attempt == 2: sys.exit(f'stopped after one retry (good-citizen rule); requests {n}')
            time.sleep(15)
for q in Q:
    d = json.loads(get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"))
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
for p in IMG:
    fp = os.path.join(out, f'p{p}.jpg')
    if not (os.path.exists(fp) and os.path.getsize(fp) > 10000):
        open(fp, 'wb').write(get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'))
    print('img', p, flush=True); time.sleep(3.3)
print('requests', n)
