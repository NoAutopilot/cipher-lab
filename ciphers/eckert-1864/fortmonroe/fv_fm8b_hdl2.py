#!/usr/bin/env python3
"""FV-FM8b (9 Oct 2026): second hdl block under the same take: dmGetItemInfo for the other-pointer hits of fv_fm8b_hdl.out that could be a
clear copy (13060 fever; 9257 7968 close offices; 8544 Parker Onondaga; 10090 10092 8729 Tallahassee; 10302 tow off) and one retry of the 5819
page image. >= 3.2 s apart. Usage: fv_fm8b_hdl2.py SCRATCH_DIR."""
import json, os, sys, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]; n = 0
for p in ['13060', '9257', '7968', '8544', '10090', '10092', '8729', '10302']:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60))
        json.dump(d, open(os.path.join(out, f'item_{p}.json'), 'w'))
        print('=====', p, d.get('title')); print(str(d.get('transc') or ''), flush=True)
    except Exception as e: print(p, 'ERR', e, flush=True)
    n += 1; time.sleep(3.2)
try: open(os.path.join(out, 'p5819.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request('https://hdl.huntington.org/digital/iiif/p16003coll11/5819/full/2400,/0/default.jpg', headers=UA), timeout=180).read()); print('img 5819 ok')
except Exception as e: print('5819 ERR', e)
n += 1
print('requests', n)
