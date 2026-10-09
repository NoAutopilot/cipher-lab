#!/usr/bin/env python3
"""FM-R4b (9 Oct 2026, account 1): IA be-api full-text search (snippet only) of Grant Papers volumes for FM-R4b rows
phrases, >= 1.6 s apart. Vol. 10 = Jan-May 1864 (E224, 27 May), vol. 11 = June-Aug 1864 (E222, 13 June), vol. 13 (Nov 1864-Feb 1865,
E220/E223) is not an IA item (advancedsearch 9 Oct 2026 lists 1-12, 14-20 and an unnumbered 0000unse, probed here). A miss is a search
result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0010gran', 'Farquhar'), ('papersofulyssess0010gran', '"Truman Seymour"'), ('papersofulyssess0010gran', '"shelter tents"'),
     ('papersofulyssess0011gran', 'scantling'), ('papersofulyssess0011gran', 'Shaffer'), ('papersofulyssess0011gran', '"light vessel"'),
     ('papersofulyssess0011gran', 'Appomattox cable'), ('papersofulyssess0012gran', '"City of Hudson"'), ('papersofulyssess0012gran', 'Keyport'),
     ('papersofulyssess0012gran', '"Secretary of War" Dealy')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:4]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:6]: print('   ', s.replace('\n', ' ')[:320])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.6)
print('be-api requests', n)
