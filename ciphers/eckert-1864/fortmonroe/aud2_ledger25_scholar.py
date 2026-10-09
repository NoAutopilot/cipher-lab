#!/usr/bin/env python3
"""AUD2-LEDGER-25 (9 Oct 2026): scholarship and press families the first audit (FV-FM9d) did not cover, for E307 and E309.
Semantic Scholar (S2_KEY header, 1.1 s), CORE v3 (CORE_API_KEY bearer), Chronicling America via loc.gov JSON (1864 only).
Keys read from the environment, never printed. A miss is a search result (rule 10), not a novelty verdict."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url, h=None):
    hh = {'User-Agent': UA}; hh.update(h or {})
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=hh), timeout=60))
SQ = ['Gilmore military telegraph Newbern 1864', 'Waterhouse McGaughey telegraph yellow fever Newbern',
      'Rucker Webster quartermaster Fort Monroe steamers 1864', 'Eckert Sheldon Fort Monroe cipher telegrams']
n = {}
for q in SQ:
    try:
        d = get('https://api.semanticscholar.org/graph/v1/paper/search?' + urllib.parse.urlencode({'query': q, 'limit': 10, 'fields': 'title,year'}),
                {'x-api-key': os.environ.get('S2_KEY', '')})
        print('S2 |', q, '|', d.get('total'), '|', '; '.join(f"{p.get('title','')[:70]} ({p.get('year')})" for p in d.get('data', [])[:6]))
    except Exception as e: print('S2 |', q, '| ERROR', str(e)[:80])
    n['s2'] = n.get('s2', 0) + 1; time.sleep(1.1)
for q in SQ:
    try:
        d = get('https://api.core.ac.uk/v3/search/works/?' + urllib.parse.urlencode({'q': q, 'limit': 10}),
                {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')})
        print('CORE |', q, '|', d.get('totalHits'), '|', '; '.join(f"{(r.get('title') or '')[:70]} ({r.get('yearPublished')})" for r in d.get('results', [])[:6]))
    except Exception as e: print('CORE |', q, '| ERROR', str(e)[:80])
    n['core'] = n.get('core', 0) + 1; time.sleep(1.6)
LQ = ['"spare boats" Illinois Webster', 'Gilmore operator Newbern Chambersburg mother', 'steamer Illinois Fortress Monroe October 1864']
for q in LQ:
    try:
        d = get('https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode({'q': q, 'dates': '1864/1864', 'fo': 'json', 'c': 10}))
        res = d.get('results', [])
        print('LOC-CA |', q, '| total', d.get('pagination', {}).get('of'), '|', '; '.join(f"{(r.get('title') or '')[:60]} {r.get('date')}" for r in res[:6]))
    except Exception as e: print('LOC-CA |', q, '| ERROR', str(e)[:80])
    n['loc'] = n.get('loc', 0) + 1; time.sleep(2)
print('requests', n)
