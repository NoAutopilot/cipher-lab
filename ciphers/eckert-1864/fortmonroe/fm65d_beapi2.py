#!/usr/bin/env python3
"""FM65-D (10 Oct 2026): IA be-api whole-collection exact-phrase queries (no identifier), >= 1.8 s apart; positive control is in fm65d_beapi_ctl.out
(7 hits). A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['"Fort Fisher is ours"', '"until Mr. Blair arrives"', '"passed through the lines" Varina Blair Ord', '"insulating wire" torpedoes "nine hundred pounds"',
     '"The Saugus left this morning"', '"take charge of army operations"', '"prepare accordingly" Newbern Palmer "6000 men"', '"one battery with each division"',
     '"bring those from Kentucky" mules Washington', '"ordered to Portsmouth" "New Hampshire" "do not wish to go"', '"what boat the President left Annapolis"',
     '"cipher operator" Stager Schofield "construction corps"', '"important despatches" Schofield Sherman Annapolis', '"if General Butler has left Monroe"',
     '"Cassandria" "El Cid" Ranger Rucker', '"Nevada" Rucker "torpedoes of the kind you name"']
n = 0
for q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        h = d.get('hits', {}); h = h.get('hits', []) if isinstance(h, dict) else h
        print(q, '|', len(h))
        for x in h[:4]:
            print('   id', x.get('fields', {}).get('identifier'))
            for s in (x.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:260])
    except Exception as e: print(q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
