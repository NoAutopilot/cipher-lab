#!/usr/bin/env python3
"""FV-FM5b (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, transcription in the result) for the
decoded substance of E220 (5811), E222 (5747), E223 (5823), E224 (5701), E225 (5626), and the two IIIF page images to a scratch dir for the eye check. >= 3.2 s apart.
Usage: fv_fm5b_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['western metropolis', 'deford', 'ferry boats', 'quickest possible', 'charlottesville', 'number large', 'chief engineer',
     'military necessity', 'capacity in all', 'livingston']
IMG = ['5823', '5626']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs))
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.2)
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/full/0/default.jpg'
    open(os.path.join(out, f'p{p}.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()); n += 1
    time.sleep(3.2)
print('requests', n)
