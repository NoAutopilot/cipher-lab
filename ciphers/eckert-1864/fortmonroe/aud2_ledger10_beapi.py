#!/usr/bin/env python3
"""AUD2-LEDGER-10 (9 Oct 2026, account 3): IA be-api full-text search (snippet only) of Grant Papers volumes for E220/E222/E223/E224
phrases, >= 1.6 s apart. Vol. 10 = Jan-May 1864 (E224, 27 May), vol. 11 = June-Aug 1864 (E222, 13 June), vol. 13 (Nov 1864-Feb 1865,
E220/E223) is not an IA item (advancedsearch 9 Oct 2026 lists 1-12, 14-20 and an unnumbered 0000unse, probed here). A miss is a search
result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0010gran', 'Farquhar'), ('papersofulyssess0010gran', 'Weitzel'), ('papersofulyssess0010gran', '"chief engineer"'),
     ('papersofulyssess0011gran', 'Biggs'), ('papersofulyssess0011gran', '"ferry boats"'), ('papersofulyssess0011gran', 'lumber'),
     ('papersofulyssess0012gran', '"Sixth Corps" steamers'), ('papersofulyssess0000unse', 'Sixth Corps'),
     ('papersofulyssess0000unse', 'Weybosset'), ('papersofulyssess0000unse', '"Western Metropolis"'), ('papersofulyssess0000unse', 'Baltic'),
     ('papersofulyssess0014gran', 'Baltic'), ('papersofulyssess0014gran', '"Western Metropolis"')]
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
