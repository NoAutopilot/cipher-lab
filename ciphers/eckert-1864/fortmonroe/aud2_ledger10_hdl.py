#!/usr/bin/env python3
"""AUD2-LEDGER-10 (9 Oct 2026, account 3): G3 in the holder's own transcription -- Huntington CONTENTdm full text (p16003coll11,
CISOSEARCHALL) for the recipient-side, staff and same-day traffic of E220 (Sixth Corps steamers, 29 Nov 1864), E222 (Biggs, 13 June 1864),
E223 (Surgeon General Barnes / hospital transports, Dec 1864), E224 (Farquhar, 27 May 1864). >= 3.2 s apart. Prints each hit's pointer,
title and the transcription window around the term. A miss is a search result, not a statement about print (rule 10)."""
import json, re, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('sixth corps', r'sixth corps|6th corps'), ('rucker', r'rucker'), ('farquhar', r'farquhar'), ('biggs', r'biggs'),
     ('surgeon general', r'surgeon gen'), ('baltic', r'baltic'), ('atlantic', r'atlantic'), ('hospital boats', r'hospital')]
n = 0
for q, rx in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/200/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(q, 'ERR', str(e)[:80]); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'== {q!r}: {d.get("pager", {}).get("total")} hits')
    for r in recs:
        t = str(r.get('transc') or '')
        for m in list(re.finditer(rx, t, re.I))[:2]:
            print(f'  {r.get("pointer")} | {str(r.get("title"))[:40]} | ...{t[max(0, m.start()-160):m.end()+160]}...'.replace('\n', ' '))
    time.sleep(3.2)
print('requests', n)
