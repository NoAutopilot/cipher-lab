#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026, account 1, for LANE LEDGER-15; copy of fv_fm65b_beapi.py): IA be-api full-text snippet search, whole collection
(no identifier: Grant Papers volumes and digitised press where IA holds them), quoted decoded phrases of E545 E560 E505 E567 E525 E572, one
positive control first. Then Chronicling America (loc.gov JSON) for E572, March 1865. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['"Steamers all ready coaled and loaded with proper rations"', '"one battery with each division"', '"bring those from Kentucky"',
     '"station be established at Yorktown"', '"one of the going steamers"', '"so that Colonel Wright can commence work"', '"Col Wright can commence work"',
     '"the Baltic got off for"', '"return to Annapolis where she can take"', '"steamship Champion arrived"', '"Champion arrived here from Wilmington"',
     '"reached Fayetteville" "intact"']
n = 0
for q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print('(all) |', q, '|', len(hits))
        for h in hits[:5]:
            f = h.get('fields', {}) or {}
            print('   ', f.get('identifier'), str(f.get('title', ''))[:60])
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', s.replace('\n', ' ')[:300])
    except Exception as e: print('(all) |', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
m = 0
for q in ['Champion Fayetteville Wilmington', 'steamship Champion arrived Wilmington', 'Champion Fayetteville intact']:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode({'q': q, 'dates': '1865-03-14/1865-03-25', 'fo': 'json', 'c': 25})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
        res = d.get('results', [])
        print('LOC |', q, '|', d.get('pagination', {}).get('of'), 'results')
        for r in res[:25]:
            print('   ', r.get('date'), (r.get('title') or '')[:50] if isinstance(r.get('title'), str) else r.get('partof_title'), r.get('id'))
    except Exception as e: print('LOC |', q, '| ERR', str(e)[:100])
    m += 1; time.sleep(2)
print('loc requests', m)
