#!/usr/bin/env python3
"""FM65-E second holder pass (same take): dmGetItemInfo for the 5915/1 candidate 7784, then shorter CISOSEARCHALL queries for rows whose long query gave 0 hits.
>= 3.3 s apart, no images."""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
def get(url):
    try: return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print('ERR', str(e)[:80], flush=True); time.sleep(25)
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
d = get(HB + "dmGetItemInfo/p16003coll11/7784/json"); print('info 7784:', json.dumps(d)[:1800]); time.sleep(3.3)
for tag, q in [('5904/1','Meagher Schofield'), ('5905/0','Meagher Morehead'), ('5898/1','Sheldon Eckert wessells'), ('5914/1','Trenchard Wilmington'),
               ('5915/0','Hastings Vincent station'), ('5917/1','Washburne Johnson rascal')]:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    d = get(url)
    print(f'{tag} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True); time.sleep(3.3)
