#!/usr/bin/env python3
"""FM-S2 (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM-S2 rows: Grant Papers 10-11, Butler's Correspondence IV-V, and four
whole-collection queries (no identifier). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('privateofficialc05butl', 'Mahopac Canonicus Saugus ready monitors'), (None, 'monitors Mahopac Canonicus Saugus ready for service Parker Onondaga'),
     ('papersofulyssess0011gran', 'Sheridan White House Beckwith Caldwell cipher'), (None, 'Sheridan will probably get here tonight Beckwith Caldwell cipher'),
     ('papersofulyssess0011gran', 'Shaffer New Orleans troops arrived Fort Monroe Rawlins'), (None, 'none of the troops from New Orleans have arrived yet Shaffer Monroe'),
     (None, 'add to the list of extra arbitraries Eckert Butler cipher'), ('privateofficialc04butl', 'Dunn Eckert Sheldon Monroe referred'),
     ('privateofficialc04butl', 'Spencer rifles cartridges Edson Ramsay')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:4]:
            print('   ', (h.get('fields', {}) or {}).get('identifier'), (h.get('fields', {}) or {}).get('title', '')[:60] if isinstance((h.get('fields', {}) or {}).get('title', ''), str) else '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('      ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
