#!/usr/bin/env python3
"""FV-FM8d (9 Oct 2026): dmGetItemInfo (title + transcription) on the other-pointer CONTENTdm hits that could be a clear copy of E278/E286/
E288 (4529, 4530, 4676, 4601, 2917; then 3237, 6157, 5456 via the optional second argument). >= 3.2 s apart. Usage: fv_fm8d_hdl2.py SCRATCH_DIR."""
import json, os, sys, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n = 0
for p in (sys.argv[2].split(',') if len(sys.argv) > 2 else ['4529', '4530', '4676', '4601', '2917']):
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60))
        json.dump(d, open(os.path.join(sys.argv[1], f'info_{p}.json'), 'w'))
        print('=====', p, d.get('title')); print(d.get('transc') if isinstance(d.get('transc'), str) else '', flush=True)
    except Exception as e: print(p, 'ERR', e, flush=True)
    n += 1; time.sleep(3.2)
print('requests', n)
