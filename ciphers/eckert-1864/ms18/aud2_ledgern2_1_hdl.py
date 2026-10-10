#!/usr/bin/env python3
"""AUD2-LEDGERN2-1 (account 4, 10 Oct 2026; copied from fv_n2b_hdl.py with new queries): Huntington CONTENTdm (p16003coll11) for N2-FH (9916/2, 17 Dec 1864 vessels to Sherman), N2-GE (9916/1, 16 Dec 1864 Halleck to Canby),
N2-GF (9722/1, 25 Apr 1864 Augur to Meade, Mosby near Upperville).
Usage: fv_n2b_hdl.py q OUT -> CISOSEARCHALL queries (all pointers); fv_n2b_hdl.py i OUT PTR ... -> item info (transc); fv_n2b_hdl.py img OUTDIR PTR ... -> IIIF 2400 px.
>= 3.3 s apart, one retry after a pause at most. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ["Guide Escort Louise", "Collyer", "Collier Cossack", "transports Sherman James", "Bradley steamers", "Bradley Savannah", "Ingalls Savannah vessels", "Mosby corn", "Augur Mosby", "Upperville", "Meade Warrenton cavalry Augur", "Mosby horses"]
def get(url, raw=False):
    for a in (1, 2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)
            return r.read() if raw else json.load(r)
        except Exception as e:
            print('ERR', str(e)[:60], flush=True)
            if a == 2: return None
            time.sleep(20)
mode, out = sys.argv[1], sys.argv[2]; n = 0
if mode == 'q':
    for q in Q:
        d = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/60/1/0/0/1/0/json"); n += 1
        if d: print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])), flush=True)
        time.sleep(3.3)
elif mode == 'i':
    for p in sys.argv[3:]:
        d = get(HB + f"dmGetItemInfo/p16003coll11/{p}/json"); n += 1
        if d: print(p, '|', d.get('title'), '|', str(d.get('transc', '')).replace('\n', ' / '), flush=True)
        time.sleep(3.3)
else:
    for p in sys.argv[3:]:
        b = get(f"https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg", raw=True); n += 1
        if b: open(os.path.join(out, f'p{p}.jpg'), 'wb').write(b); print(p, len(b), flush=True)
        time.sleep(3.3)
print('requests', n)
