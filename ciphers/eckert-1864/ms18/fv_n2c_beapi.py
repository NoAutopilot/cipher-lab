#!/usr/bin/env python3
"""FV-N2c (10 Oct 2026): IA be-api full-text search, short phrases (the N2R-2 multi-word AND queries were too strict), Papers of U. S. Grant vols. 10, 12, 13.
Positive controls first ('leaves Alexandria this morning' vol. 10; 'Relay House' vol. 12). >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess00%02dgran'
Q = [(10, '"leaves Alexandria this morning"'), (10, '"reach Fairfax"'), (10, 'Fairfax Burnside column'), (10, '"requisite ammunition"'),
     (10, '"in motion"  Burnside Fairfax'), (10, '"start south"'),
     (12, 'paymasters escort Martinsburg'), (12, 'Brice paymaster'), (12, '"Nineteenth Corps" paymasters'),
     (13, 'Brice paymaster'), (13, '"Relay House"'), (13, 'paymasters "Sixth Corps"'), (13, 'paymasters "City Point" unpaid')]
n = 0
for vol, q in Q:
    ident = G % vol
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:4]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
