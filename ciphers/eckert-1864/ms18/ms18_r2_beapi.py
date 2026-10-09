#!/usr/bin/env python3
"""MS18-R2 (9 Oct 2026): IA be-api full-text snippet search of Grant Papers vols. 12 and 15 (ids guessed from the 0010/0011 pattern; a positive control query first) for the MS18-R2 rows,
>= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0012gran', 'Halleck Schofield Louisville Thomas Nashville'), ('papersofulyssess0012gran', 'Kendall Ritchie arrest agents Rosecrans'),
     ('papersofulyssess0012gran', 'Cavalry Bureau unserviceable horses Gallipolis'), ('papersofulyssess0015gran', 'Campbell Hunter Seddon Pulaski'),
     ('papersofulyssess0015gran', 'Hurlbut Sheridan Reynolds Canby'), ('papersofulyssess0015gran', 'Lines Macon Port Royal quartermaster funds'),
     ('papersofulyssess0015gran', 'Pope horses Reynolds Arkansas replaced')]
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
