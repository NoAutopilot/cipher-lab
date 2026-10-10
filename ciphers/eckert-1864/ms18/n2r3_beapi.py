#!/usr/bin/env python3
"""N2R-3 (10 Oct 2026): IA be-api full-text snippet search of the Papers of U. S. Grant vols. 10-12 for the N2R-3 rows not found in OR, >= 1.8 s apart.
A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess00%02dgran'
Q = [(12, 'inspectors Arkansas Little Rock Bingham Biggs Rutherford inspection'), (11, 'Torbert Grover Sixth Corps landed Washington Rockville Averell'),
     (11, 'steamers Baltimore Philadelphia New York transports Rucker capacity infantry Halleck'), (12, 'Delaware regiments Petersburg election furlough home to vote'),
     (12, 'Key West Tortugas Newton Delafield engineer district West Florida'), (10, 'Triplett escaped Woodstock Lee ordered transportation April Cumberland'),
     (12, 'Halleck Price Steele Selma Mobile and Ohio Beauregard Canby Sherman coast'), (12, 'Halleck Alexandria vessels demurrage Rucker Sheridan Missouri Curtis'),
     (12, 'A. J. Smith Rosecrans Price St. Louis Rolla expedition countermanded'), (10, 'Banks junction Sherman Red River Steele demonstration Halleck')]
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
