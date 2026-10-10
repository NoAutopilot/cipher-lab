#!/usr/bin/env python3
"""N2R-2 (10 Oct 2026): IA be-api full-text snippet search of the Papers of U. S. Grant vols. 10-13 (ids by the 0010..0013 pattern) for the N2R-2 rows, >= 1.8 s apart.
A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess00%02dgran'
Q = [(10, 'Hardee Jacksonville Longstreet West Virginia Halleck'), (10, 'Burnside Alexandria Fairfax column ammunition'), (10, 'Mosby Upperville Warrenton cavalry Augur'),
     (10, 'Stanton direct telegraphic communication Nashville telegraph office'), (11, 'Sixth Corps rear embark supplied paid Hunter Shenandoah'), (11, 'Sigel Martinsburg Beverly Staunton Lexington dispatches'),
     (12, 'Forsyth paymasters Martinsburg Nineteenth Corps Brice'), (13, 'Canby Hilton Head Pensacola supplies vessels Savannah'), (13, 'Brice paymasters Sixth Corps City Point unpaid'),
     (13, 'Brice paymasters Relay House unpaid August Sheridan')]
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
