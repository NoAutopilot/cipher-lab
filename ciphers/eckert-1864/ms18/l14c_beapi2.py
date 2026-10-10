#!/usr/bin/env python3
"""L14-C be-api round 2: the whole-collection control returned 0, so it cannot license a miss; here the control is inside the known volume (warofrebellion371unit) and the row phrases
are searched inside the volume that should carry the date (identifier given). >= 2.2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion371unit', 'control 9764/1', '"attacked Lynchburg and been repulsed"'),
 ('warofrebellion393unit', '9869/4', 'Meredith Paducah judicious'), ('warofrebellion393unit', '9862/0', 'Garrett Harper arms delayed'),
 ('warofrebellion432unit', '9897/1', '"Beverly Tucker" Niagara'), ('warofrebellion432unit', '9848/0b', 'Imboden prisoners veteran regiment'),
 ('warofrebellion413unit', '9850/2', 'frauds inefficiencies Fort Smith'), ('warofrebellion372unit', '9811/0', 'frankly Hunter Sheridan Halleck'),
 (None, '9848/0', '"veteran regiment was sent from here yesterday"')]
for ident, lab, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident, lab, '|', q, '|', len(hits), flush=True)
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', ' '.join(s.split())[:300])
    except Exception as e: print(ident, lab, '|', q, '| ERROR', e)
    time.sleep(2.2)
print('be-api requests', len(Q))
