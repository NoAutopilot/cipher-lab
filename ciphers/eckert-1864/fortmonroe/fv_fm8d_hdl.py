#!/usr/bin/env python3
"""FV-FM8d (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, suppressfulltext=1) across ALL pointers on
pairs of distinctive clear words of E278 (5829), E286 (5605), E288 (5724), E289 (5814), and the four IIIF pages at 2400 px to a scratch
dir for the line eye check. >= 3.2 s apart. Usage: fv_fm8d_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print
(rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['few remaining', 'fleet remaining', 'fleet last night', 'presume evening', 'ingalls fleet',
     'jersey battery', 'spared defences', 'spared defenses', 'pleased ordered', 'direct forward',
     'millions rations', 'head cattle', 'cattle white house', 'commissary taylor', 'small commissary',
     'court martial', 'dewey', 'witness leave', 'squadron leaving', 'taylor dewey']
IMG = ['5829', '5605', '5724', '5814']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        recs = d.get('records', [])
        print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
        json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    except Exception as e: print(q, 'ERR', e, flush=True)
    n += 1; time.sleep(3.2)
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    try: open(os.path.join(out, f'p{p}.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read())
    except Exception as e: print(p, 'ERR', e, flush=True)
    n += 1; time.sleep(3.2)
print('requests', n)
