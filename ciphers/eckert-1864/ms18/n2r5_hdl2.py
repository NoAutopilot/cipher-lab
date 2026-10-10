#!/usr/bin/env python3
"""N2R-5: follow-up to n2r5_hdl.py: corrected positive control (ledger spellings) and the title/transcription head of the non-self hits for Z3 and Z7. 3 requests, >= 3.3 s apart."""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for lab, q in [('control 9804 (ledger spellings)', 'Averill Castle Shepherdstown'), ('Z3', 'Shreveport gunboats Steele'), ('Z7', 'ocean steamers Ingalls')]:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    print(lab, '|', q, '|', d.get('pager', {}).get('total'), 'hits')
    for r in d.get('records', [])[:5]:
        print('  ', r.get('pointer'), '|', (r.get('title') or '')[:60], '|', ' '.join((r.get('transc') or '').split())[:260])
    time.sleep(3.3)
print('requests 3')
