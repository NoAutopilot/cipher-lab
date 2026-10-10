#!/usr/bin/env python3
"""FV-L16c (10 Oct 2026; copied from fv_l15c_beapi.py): IA be-api full-text phrase queries, by identifier (Grant Papers 14 = papersofulyssess0014gran) and
whole-collection, for E558 E564 E566 E569 E574 E577. >= 1.8 s apart. A miss is a search result."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
def get(u):
    return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
Q = [l.split('|', 1) for l in sys.argv[1:]]
n = 0
for ident, q in Q:
    u = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, **({'identifier': ident} if ident else {})})
    try:
        d = get(u); n += 1
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        tot = d.get('hits', {}).get('total') if isinstance(d.get('hits'), dict) else len(hits)
        print(f'{ident or "ALL"} | {q} | total {tot}')
        for h in hits[:8]:
            f = h.get('fields', {}); hl = h.get('highlight', {})
            print('    ', f.get('identifier'), '|', str(f.get('title'))[:70], '|', ' '.join(' '.join(v) if isinstance(v, list) else str(v) for v in hl.values())[:300])
    except Exception as e:
        print(f'{ident or "ALL"} | {q} | ERROR {e}'); n += 1
    time.sleep(1.8)
print('# requests', n)
