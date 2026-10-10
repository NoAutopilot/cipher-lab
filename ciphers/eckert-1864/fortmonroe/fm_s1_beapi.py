#!/usr/bin/env python3
"""FM-S1 (10 Oct 2026): IA be-api full-text phrase queries WITHOUT identifier (whole collection) for the FM-S1 rows not found in the cached volumes,
>= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('F1', '"yellow fever is prevailing to considerable extent"'), ('F1', 'McDougall yellow fever Newbern Sheldon 1864 notify'), ('F2', '"copy of all dispatches sent north from your office"'),
     ('F3', '"Baird will arrive tomorrow morning" instruments'), ('F4', '"W. A. Dunn" Cherrystone operator'), ('F5', 'Saugus "above City Point" Porter Beckwith'),
     ('F7', '"Manhattan" Eckert Dealy wharf Stanton Fort Monroe October 1864'), ('F9', '"Demolay" Butler Porter December 1864 shipped'), ('F10', '"keep Cowan and Ryan at West Point"')]
n = 0
for lab, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(lab, '|', q, '|', len(hits), flush=True)
        for h in hits[:4]:
            print('   ', (h.get('fields', {}) or {}).get('identifier'), h.get('_source', {}).get('title', '') if isinstance(h.get('_source'), dict) else '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', s.replace('\n', ' ')[:260])
    except Exception as e: print(lab, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.9)
print('be-api requests', n)
