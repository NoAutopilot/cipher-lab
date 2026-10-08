#!/usr/bin/env python3
"""AUD2-LEDGER-7 (8 Oct 2026): second-audit G3 on the Huntington CONTENTdm full text (p16003coll11, CISOSEARCHALL, transcription in
the result) for E185 (Saugus/Onondaga/monitors, Dec 1864) and E191 (Chestnut arrest, Baltimore, Mar 1864). >= 3.2 s apart.
Usage: aud2_ledger7_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['saugus', 'onondaga', 'canonicus', 'mahopac', 'chesnut', 'hold him safe', 'high intelligence', 'oakum at once', 'nights boat']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(f'{q!r}: ERROR {str(e)[:80]}'); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs))
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.2)
print('requests', n)
