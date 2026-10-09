#!/usr/bin/env python3
"""FV-FM8b (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, suppressfulltext=1) across ALL pointers on
pairs of distinctive clear words of E280 (5785), E281 (5706), E283 (5819), E284 (5804), E285 (5798), and the five IIIF pages at 2400 px to a
scratch dir for the line eye check. >= 3.2 s apart. Usage: fv_fm8b_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print
(rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['fever alarming', 'fever fatal', 'change air', 'close offices', 'morehead fever',
     'cut poles', 'paying out', 'detail axes', 'gloster cables', 'white house connect',
     'white shoal', 'tow off', 'chain ready', 'anchor shore', 'parker onondaga',
     'mulford boats', 'transferred authority', 'babcock respects', 'boats transfer',
     'halifax', 'tallahassee', 'montauk point', 'latitude steering', 'miles shore']
IMG = ['5785', '5706', '5819', '5804', '5798']
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
