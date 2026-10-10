#!/usr/bin/env python3
"""N2R-1 (10 Oct 2026): IA be-api full-text snippet search of Grant Papers vols. 11-13 (ids by the 00NN pattern; vol 12/15 ids confirmed by MS18-R2; a miss on an unconfirmed id is 'id unverified') for the unlocated N2R-1 rows, >= 1.8 s apart.
A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0012gran', 'Patrick Seymour election agents frauds forgeries'), ('papersofulyssess0012gran', 'ballot box stuffer'),
     ('papersofulyssess0011gran', 'hospital transports sick wounded Surgeon General Ingalls'), ('papersofulyssess0013gran', 'Rawlins Sixth Corps embarked Division arrive'),
     ('papersofulyssess0013gran', 'Savannah vessels ordered Sherman Bradley quartermaster'), ('papersofulyssess0011gran', 'Surgeon General sick Brimstone transports sea squadron')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
