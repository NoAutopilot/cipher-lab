#!/usr/bin/env python3
"""FV-N2c (10 Oct 2026): Huntington CONTENTdm (p16003coll11) for N2-GH (9725/0, 27 Apr 1864, Burnside to Grant), N2-GA (9874/1, 22 Oct 1864),
N2-GC (9913/0, 10 Dec 1864), N2-GI (9914/1, 14 Dec 1864) -- the three B. W. Brice paymaster telegrams.
Usage: fv_n2c_hdl.py q SCRATCH -> CISOSEARCHALL queries (all pointers, suppressfulltext=1); i SCRATCH PTR ... -> item info (transc);
       m SCRATCH PTR ... -> IIIF 2400 px to SCRATCH (never committed).
>= 3.3 s apart, one retry after a pause at most. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Brice', 'Paymasters', 'Pay masters', 'Relay house', 'Paymrs', 'requisite', 'Fairfax Burnside', 'start south',
     'Forsyth', 'escort Martinsburg', 'Sixth Corps unpaid', 'unpaid']
def get(url, raw=False):
    for a in (1, 2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)
            return r.read() if raw else json.load(r)
        except Exception as e:
            print('ERR', str(e)[:60], flush=True)
            if a == 2: return None
            time.sleep(20)
mode, out = sys.argv[1], sys.argv[2]; n = 0
if mode == 'q':
    for q in Q:
        d = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"); n += 1
        if d: print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])), flush=True)
        time.sleep(3.3)
elif mode == 'i':
    for p in sys.argv[3:]:
        d = get(HB + f"dmGetItemInfo/p16003coll11/{p}/json"); n += 1
        if d: print(p, '|', d.get('title'), '|', str(d.get('transc', '')).replace('\n', ' / '), flush=True)
        time.sleep(3.3)
else:
    for p in sys.argv[3:]:
        b = get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg', raw=True); n += 1
        if b: open(os.path.join(out, f'p{p}.jpg'), 'wb').write(b); print(p, len(b), flush=True)
        time.sleep(3.3)
print('requests', n)
