#!/usr/bin/env python3
"""FM-R6c (9 Oct 2026, account 1): IA be-api full-text snippet search of Grant Papers vols. 10-12 and Butler's Correspondence III-V for the FM-R6c rows,
>= 1.8 s apart. Vol. 13 (Nov 1864-) is not an IA item (FM-R4b). A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0012gran', 'Rucker steamers'), ('papersofulyssess0012gran', '"Illinois" steamers Rucker'), ('papersofulyssess0012gran', 'Chambersburg Sheldon'),
     ('papersofulyssess0011gran', 'Albemarle Sound Sheldon'), ('privateofficialc05butl', 'Rucker steamers Illinois'), ('privateofficialc05butl', 'Chambersburg'),
     ('privateofficialc04butl', 'Albemarle Christian Advocate'), ('privateofficialc04butl', 'Albemarle Sound ram'), ('privateofficialc05butl', 'Sheldon leave of absence')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:4]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:5]: print('   ', s.replace('\n', ' ')[:320])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
