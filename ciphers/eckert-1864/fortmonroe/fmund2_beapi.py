#!/usr/bin/env python3
"""FM-UND2 (10 Oct 2026, account 1): IA be-api full-text snippet search for E622 head and 5658/0 tel 2: whole-collection (no identifier) queries on the readable
clauses plus Grant Papers 13-14 and Butler Corr. V by identifier where known. >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None,'Suwo Nada'),
 (None,'all quiet and ready to move in the morning O\'Brien Eckert Butler May 1864'),
 (None,'O\'Brien left General Butler headquarters miles from Bermuda landing Harrison\'s landing to join us'),
 ('papersofulyssess0010gran','Butler O\'Brien Eckert telegraph May 9 1864 Bermuda'),
 (None,'Rucker will send an officer in a steamer down the Potomac stop all vessels Biggs Wise April 1864'),
 (None,'Wise Philadelphia April 19 1864 side-wheel boats Highland Light Tallaca Kingston Meigs Biggs Fort Monroe Eckert'),
 (None,'Van Vliet list not yet received vessels chartered for the expedition Fort Monroe April 1864 Biggs')]
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
            f = h.get('fields', {}) or {}
            print('   ', f.get('identifier'), (f.get('title', '') or '')[:60] if isinstance(f.get('title', ''), str) else '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('      ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
