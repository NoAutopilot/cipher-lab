#!/usr/bin/env python3
"""FM-R6a (9 Oct 2026): hdl.huntington.org under the LANE LEDGER token -- 9 IIIF page images (2400 px) to a scratch dir for the eye check, and CONTENTdm
CISOSEARCHALL queries (p16003coll11, suppressfulltext=1, the holder's own transcription across ALL pointers) on the clear words of the FM-R6a rows.
>= 3.3 s apart. Prints each hit's pointer, title and the transcription window. A miss is a search result, not a statement about print (rule 10).
Usage: python3 fm_r4a_hdl.py SCRATCH_DIR"""
import json, re, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
OUT = sys.argv[1]
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
PAGES = [5639, 5764, 5697, 5797]
Q = [('plymouth relayed leaving', r'plymouth'), ('plymouth abandoned Butler informed', r'plymouth'), ('Malvern sand in bags', r'sand in bags|malvern'),
     ('rebel ironclad lads sand bags', r'sand|malvern'), ('white house base of supplies', r'white house'), ('chestnut poles not rotted down', r'chestnut|poles'),
     ('Garysburg Weldon construction', r'weldon|garysburg|g\. ?vernon'), ('ships gap snake creek pass', r'snake creek|ships gap|ship.s gap'),
     ('Hood obstructed snake creek pass', r'snake creek|obstructed'), ('Kingston Roddy moved Gregory', r'roddy|gregory'),
     ('reoccupy Weldon construction train repair break tunnel', r'tunnel|weldon')]
n = 0
for p in PAGES:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    try:
        b = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read()
        open(f'{OUT}/{p}.jpg', 'wb').write(b); print('IIIF', p, len(b))
    except Exception as e:
        print('IIIF', p, 'ERR', str(e)[:80])
    n += 1; time.sleep(3.3)
for q, rx in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/200/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(q, 'ERR', str(e)[:80]); n += 1; time.sleep(3.3); continue
    n += 1
    print(f'== {q!r}: {d.get("pager", {}).get("total")} hits')
    for r in d.get('records', []):
        t = str(r.get('transc') or '')
        for m in list(re.finditer(rx, t, re.I))[:2]:
            print(f'  {r.get("pointer")} | {str(r.get("title"))[:40]} | ...{t[max(0, m.start()-160):m.end()+160]}...'.replace('\n', ' '))
    time.sleep(3.3)
print('requests', n)
