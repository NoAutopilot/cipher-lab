#!/usr/bin/env python3
"""FM-S2: dmGetItemInfo for the three other-pointer hits of fm_s2_hdl.py (10266 10356 10364) -> ../sources/fortmonroe/. 3.3 s apart."""
import json, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16003coll11/{}/json"
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for p in (10266, 10356, 10364):
    d = json.load(urllib.request.urlopen(urllib.request.Request(HB.format(p), headers=UA), timeout=60))
    json.dump(d, open(f'../sources/fortmonroe/p{p}.json', 'w')); print(p, d.get('title'), len(d.get('transc') or ''), flush=True); time.sleep(3.3)
