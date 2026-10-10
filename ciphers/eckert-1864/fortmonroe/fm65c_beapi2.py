#!/usr/bin/env python3
"""FM65-C batch 2 (short per-volume queries after batch 1 returned 0 for over-long ANDs; control Fort Fisher): FM65-C (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM65-C rows (Jan 1865): OR I/46-47 pts 1-3 (not in the local
cache), Butler Corr. V, Grant Papers 13 and whole-collection queries (no identifier). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
OR = ['warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion463unit', 'warofrebellion471unit', 'warofrebellion014702rootrich', 'warofrebellion014703rootrich']
Q = [(OR[0], 'Fisher')]
for ident in OR:
    for q in ['Sedgwick Ariel', 'Cosgrove Robie', 'Dupont Thames Haze', 'Carney Janeway']:
        Q.append((ident, q))
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:4]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('   id', src.get('identifier') or h.get('_id'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
