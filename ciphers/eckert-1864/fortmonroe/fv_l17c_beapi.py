#!/usr/bin/env python3
"""FV-L17c (10 Oct 2026, account 1; copied from fmund2_beapi.py): IA be-api full-text snippet search for E622 relay and E623, fresh wording: whole-collection (no identifier) queries on the readable
clauses plus Grant Papers 13-14 and Butler Corr. V by identifier where known. >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None,'Suwo Nada'),
 (None,'Shore correspondent of the World Baltimore arrest Butler May 1864'),
 (None,'W. W. Shore World correspondent arrested Baltimore 1864'),
 (None,'send steamers to Chesapeake City to meet and escort the tows down the Bay'),
 (None,'Meigs Biggs Rucker officer steamer Potomac stop vessels Fort Monroe April 20 1864')]
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

