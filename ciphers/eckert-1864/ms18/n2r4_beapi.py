#!/usr/bin/env python3
"""N2R-4 (10 Oct 2026): IA be-api full-text snippet search of the Papers of U. S. Grant vols. 10-12 for the N2R-4 rows not found in OR, >= 1.8 s apart.
A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess00%02dgran'
Q = [(10, 'veteran Maryland regiment detained Baltimore Twelfth Corps battery transportation Halleck'), (12, 'Heintzelman remove Hooker Crook major-general vacancy muster out'),
     (11, 'Meigs Canby Vicksburg Monroe railroad gauge Shreveport'), (12, 'Buyers Georgetown hotels searched detectives Washington Grant'),
     (11, 'Hardie Canby Vicksburg Monroe railroad Secretary of War expediency referred Grant'), (10, 'Stanton Grant assigned command of the armies of the United States act of Congress February 29'),
     (12, 'Ingalls Rucker Bridgeport vessels assembled Monroe Grant December'), (10, 'Canby Hurlbut combined departments Gulf Arkansas Banks relieved Dana'),
     (11, 'Halleck Grant Nineteenth Corps uncertain Sixth Corps sent to this place Baltimore troops stopped'), (12, 'Halleck Curtis Rosecrans pursuit of Price recalled contrary to repeated orders')]
n = 0
for vol, q in Q:
    ident = G % vol
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
