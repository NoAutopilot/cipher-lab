#!/usr/bin/env python3
"""FV-FM5c (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, transcription in the result) for the
decoded substance of E230 (5839), E234 (5683), E235 (5831), E236 (5670), E237 (5729), and the three IIIF page images FM-R3c did not
eye-check (5831 5670 5729) to a scratch dir. >= 3.2 s apart. Usage: fv_fm5c_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['brasses', 'cuyler', 'finck', 'hanoverian', 'tallifinny', 'coosawatchie', 'kingsland', 'powhattan', 'press despatches',
     'manhattan', 'exchanged prisoners', 'beauregard courier']
IMG = ['5831', '5670', '5729']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(q, 'ERROR', e); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs))
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.2)
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/full/0/default.jpg'
    open(os.path.join(out, f'p{p}.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()); n += 1
    time.sleep(3.2)
print('requests', n)
