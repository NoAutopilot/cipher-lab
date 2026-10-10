#!/usr/bin/env python3
"""L14-C be-api round 3: whole-collection (no identifier) shorter phrases, after round 2 found 9848/0 in the Grant Papers; prints ids and snippets. >= 2.2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('9848/0 ids', '"veteran regiment was sent from here yesterday"', 7), ('9811/0', '"Had you asked my opinion"', 4), ('9811/0b', '"excused from deciding"', 4),
 ('9850/2', '"alleged frauds and inefficiencies"', 4), ('9897/1', '"Beverly Tucker" "Niagara Falls" Dix Dana', 4), ('9869/4', '"assignment of General Meredith"', 4),
 ('9862/0', '"arms were sent from here to Harper"', 4)]
for lab, q, k in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(lab, '|', q, '|', len(hits), flush=True)
        for h in hits[:k]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('  id', h.get('_id') or src.get('identifier'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', ' '.join(s.split())[:420])
    except Exception as e: print(lab, '|', q, '| ERROR', e)
    time.sleep(2.2)
print('be-api requests', len(Q))
