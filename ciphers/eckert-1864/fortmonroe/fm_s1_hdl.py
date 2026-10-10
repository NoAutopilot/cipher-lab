#!/usr/bin/env python3
"""FM-S1 (10 Oct 2026): Huntington CONTENTdm (p16003coll11) CISOSEARCHALL on a rare plain word or name per row (all pointers), positive control 9678
once, then ten IIIF full pages (2400 px) to a scratch dir for the eye check. >= 3.3 s apart; one retry after a pause then stop. Usage: fm_s1_hdl.py SCRATCH_DIR."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control 9678', 'Inspector difficulty Evidence Nashville'), ('F1 5785/1', 'Newbern McDougall'), ('F2 5799/0', 'Schoonmaker Patrick Caldwell'), ('F3 5816/2', 'Baird instruments'),
     ('F4 5583/2', 'Dunn Cherry Stone'), ('F5 5827/0', 'Saugus Cole'), ('F6 5647/0', 'Gillmore Culpepper'), ('F7 5793/1', 'Manhattan wharf Bates'),
     ('F8 5636/2', 'Clarke staff North Carolina'), ('F9 5822/2', 'Demolay'), ('F10 5731/0', 'Rand Bliss Cowan Ryan')]
IMG = ['5785', '5799', '5816', '5583', '5827', '5647', '5793', '5636', '5822', '5731']
out = sys.argv[1]; n = 0
def get(url, tries=2):
    global n
    for a in range(tries):
        try:
            n += 1; return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()
        except Exception as e:
            print('ERR', url[-60:], str(e)[:60], flush=True)
            if a == tries - 1: sys.exit('stopped after one retry (good-citizen rule)')
            time.sleep(25)
for lab, q in Q:
    if True:
        url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
        d = json.loads(get(url)); recs = d.get('records', [])
        print(f'{lab} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
        json.dump(d, open(os.path.join(out, 'q_' + lab.split()[0] + '.json'), 'w'))
    time.sleep(3.4)
for p in IMG:
    fp = os.path.join(out, f'p{p}.jpg')
    if not (os.path.exists(fp) and os.path.getsize(fp) > 10000):
        open(fp, 'wb').write(get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'))
    print('img', p, flush=True); time.sleep(3.4)
print('requests', n)
