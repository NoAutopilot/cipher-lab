#!/usr/bin/env python3
"""FV-FM7c (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, suppressfulltext=1, all pointers) on
distinctive clear words of E267 (5790), E268 (5742), E269 (5775), then dmGetItemInfo for pointers given with -i, then IIIF page images
(2400 px) given with -p, all to a scratch dir. >= 3.2 s apart. Usage: fv_fm7c_hdl.py SCRATCH_DIR [QUERY ...] [-i PTR ...] [-p PTR ...].
A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]; args = sys.argv[2:]; n = 0; i = 0
def get(url, t=60):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t).read()
while i < len(args):
    a = args[i]
    try:
        if a in ('-i', '-p'):
            p = args[i + 1]; i += 2
            if a == '-i':
                d = json.loads(get(HB + f"dmGetItemInfo/p16003coll11/{p}/json"))
                json.dump(d, open(os.path.join(out, f'item_{p}.json'), 'w'))
                print('== item', p, d.get('title'), '\n', str(d.get('transc'))[:3000])
            else:
                open(os.path.join(out, f'p{p}.jpg'), 'wb').write(get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg', 180))
                print('image', p)
        else:
            i += 1
            d = json.loads(get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(a) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"))
            json.dump(d, open(os.path.join(out, 'q_' + a.replace(' ', '_') + '.json'), 'w'))
            print(f'{a!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])))
    except Exception as e:
        print(a, 'ERROR', e)
    n += 1; time.sleep(3.2)
print('requests', n)
