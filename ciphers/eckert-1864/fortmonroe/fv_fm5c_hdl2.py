#!/usr/bin/env python3
"""FV-FM5c (9 Oct 2026), second hdl block: dmGetItemInfo (full transcription) for pointers given with -i, and further CISOSEARCHALL
queries given as plain arguments. >= 3.2 s apart. Usage: fv_fm5c_hdl2.py SCRATCH_DIR [-i PTR ...] [QUERY ...]."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]; args = sys.argv[2:]; n = 0; i = 0
while i < len(args):
    if args[i] == '-i':
        p = args[i + 1]; i += 2
        d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60))
        json.dump(d, open(os.path.join(out, f'item_{p}.json'), 'w')); print('== item', p, d.get('title'), '\n', str(d.get('transc'))[:2500])
    else:
        q = args[i]; i += 1
        url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
        print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])))
    n += 1; time.sleep(3.2)
print('requests', n)
