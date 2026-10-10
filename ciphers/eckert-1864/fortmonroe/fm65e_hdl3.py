#!/usr/bin/env python3
"""FM65-E third holder pass (same take): dmGetItemInfo for candidate clear-copy pointers 7721 8538 8561 (Meagher Schofield) and 7782 (Trenchard). 3.3 s apart."""
import json, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for p in (7721, 8538, 8561, 7782):
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(HB+f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60))
    except Exception as e: print(p, 'ERR', e); time.sleep(25); continue
    print('=====', p, d.get('title'), d.get('callid')); print(d.get('transc')); time.sleep(3.3)
