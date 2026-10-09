#!/usr/bin/env python3
"""FM-R4b (9 Oct 2026): be-api snippet search of Butler's Private and Official Correspondence vol. III (identifier privateofficialc03butl, tried first)
for the April-June 1864 rows. >= 1.6 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
ID = 'privateofficialc03butl'
Q = ['Farquhar pontoon mules', '"shelter tents"', 'scantling', '"cable" Appomattox', 'Seymour Olustee']
n = 0
for q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ID})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []); print(ID, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight') or {}).get('text', [])[:4]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ID, '|', q, '| ERR', str(e)[:120])
    n += 1; time.sleep(1.6)
print('be-api requests', n)
