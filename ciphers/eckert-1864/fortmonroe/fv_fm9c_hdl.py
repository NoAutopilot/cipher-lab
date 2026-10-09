#!/usr/bin/env python3
"""FV-FM9c (9 Oct 2026, verifier, for LANE LEDGER): Huntington CONTENTdm full text across ALL pointers (p16003coll11, CISOSEARCHALL,
suppressfulltext=1) on distinctive clear words of E304-E306, dmGetItemInfo of the E304 clear copy 4610-4611, and the three ledger pages at
2400 px for the eye check (to SCRATCH, never committed). >= 3.3 s apart, one retry at most. Usage: fv_fm9c_hdl.py SCRATCH_DIR.
A miss is a search result for the log (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['axes', 'gloster', 'many pieces', 'jamestown cable', 'more direct route', 'escort guerillas',
     'powhatan city point', 'perkins party', 'obrien', 'closing out', 'circumstances will allow', 'unable to find',
     'sheridan hunter white house', 'headquarters removed', 'cable mile long']
INFO = ['4610', '4611']
IMG = ['5662', '5740', '5744']
out = sys.argv[1]; n = 0
def get(url, timeout=90):
    global n
    for attempt in (1, 2):
        try:
            n += 1
            return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()
        except Exception as e:
            print('ERR', url[-60:], str(e)[:60], flush=True)
            if attempt == 2: return None
            time.sleep(15)
for p in INFO:
    b = get(HB + f"dmGetItemInfo/p16003coll11/{p}/json")
    if b: open(os.path.join(out, f'info{p}.json'), 'wb').write(b); print('info', p, flush=True)
    time.sleep(3.3)
for q in Q:
    b = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json", 60)
    if b:
        d = json.loads(b); recs = d.get('records', [])
        print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
        json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
for p in IMG:
    fp = os.path.join(out, f'p{p}.jpg')
    if not (os.path.exists(fp) and os.path.getsize(fp) > 10000):
        b = get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg', 120)
        if b: open(fp, 'wb').write(b); print('img', p, flush=True)
        time.sleep(3.3)
print('requests', n)
