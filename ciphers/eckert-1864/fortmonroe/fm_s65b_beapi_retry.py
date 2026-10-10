#!/usr/bin/env python3
"""FM-S65B (10 Oct 2026, account 1, for LANE LEDGER-17): IA be-api full-text snippet search, whole collection and named volumes, for the filing candidates
(Feb-Mar 1865). Control first (quoted OR I/47 pt 2 sentence). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None, '"referred to in our dispatch" "staff officer" "retained no copy" Grant Seward'),
 (None, 'Cammann gold "Sell gold" naval officer Cooper Sheldon Eckert approval'),
 (None, 'ponchos "not on hand" Canby Sheridan Ingalls March 1865')]
time.sleep(1)  # one retry after the 502s of fm_s65b_beapi2.out, then stop
import sys

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
