#!/usr/bin/env python3
"""FM-R5b (9 Oct 2026): second hdl block: full record of pointer 10267 (clear copy of F3's telegram) and CISOSEARCHALL queries on rare words of F2/F4/F6/F9/F10.
>= 3.3 s apart. Usage: fm_r5b_hdl2.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]; n = 0
d = json.load(urllib.request.urlopen(urllib.request.Request(HB + "dmGetItemInfo/p16003coll11/10267/json", headers=UA), timeout=60)); n += 1
json.dump(d, open(os.path.join(out, 'item_10267.json'), 'w')); print('10267 transc len', len(str(d.get('transc', d))))
for q in ['gloster', 'onondaga', 'montauk', 'dewey', 'm p small']:
    time.sleep(3.3)
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
print('requests', n)
