#!/usr/bin/env python3
"""AUD2-LEDGER-4 (8 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, transcription in the result) for
the G3 re-search of E165, E167, E168 (second audit), and the page image of 5818 (E167, never image-read) to a scratch dir. >= 3.2 s
apart. Usage: aud2_ledger4_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['horner', 'russia', 'sanborn', 'breedford', 'orphan', 'endless', 'sigel', 'additional arbitraries', 'lewis wallace',
     'godfrey', 'gazette', 'rousseau native', 'following additions', 'editions']
IMG = ['5818']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(f'{q!r}: ERROR {e}'); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs))
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.2)
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    open(os.path.join(out, f'p{p}.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); n += 1
    time.sleep(3.2)
print('requests', n)
