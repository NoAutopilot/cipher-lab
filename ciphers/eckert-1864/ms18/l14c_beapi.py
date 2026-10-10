#!/usr/bin/env python3
"""L14-C: IA be-api full-text search (snippets; no page numbers; CLAUDE.md access item 3), no identifier = whole collection, for the six rows not found in the cached volumes;
positive control: the 9764/1 phrase (known present in warofrebellion371unit). >= 2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control 9764/1', '"I have no orders to give you, except to carry out General Hunter"'),
 ('9869/4', '"assignment of General Meredith" Paducah Washburn'), ('9869/4b', '"no troops available to reinforce Paducah"'),
 ('9897/1', '"Beverly Tucker will cross at Niagara Falls"'), ('9862/0', '"Garrett" "arms were sent from here to Harper" Ferry'),
 ('9848/0', '"veteran regiment was sent from here yesterday" Imboden'), ('9811/0', '"asked my opinion in regard to General Hunter" Sheridan'),
 ('9811/0b', '"freely and frankly given" Halleck Grant Hunter'), ('9850/2', '"frauds and inefficiencies" Fort Smith Canby Halleck')]
for lab, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(lab, '|', q, '|', len(hits), flush=True)
        for h in hits[:4]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('  id', h.get('_id') or src.get('identifier'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', ' '.join(s.split())[:300])
    except Exception as e: print(lab, '|', q, '| ERROR', e)
    time.sleep(2.2)
print('be-api requests', len(Q))
