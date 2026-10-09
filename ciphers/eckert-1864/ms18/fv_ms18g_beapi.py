#!/usr/bin/env python3
"""FV-MS18g (9 Oct 2026): IA be-api full-text search (no login) of Grant Papers vols 11 and 12 for E347 and E349 phrases.
A miss is a search result (rule 10); be-api page_num is not a page locator."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0011gran', '"profound secret"'), ('papersofulyssess0011gran', 'refreshments'), ('papersofulyssess0011gran', '"W. P. Smith"'),
     ('papersofulyssess0011gran', 'Relay Monocacy'), ('papersofulyssess0012gran', '"long cipher"'), ('papersofulyssess0012gran', 'Meade Baltimore arrival'),
     ('papersofulyssess0012gran', '"your arrival here"')]
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident, q, 'hits', len(hits))
        for h in hits[:4]:
            hl = h.get('highlight') or h.get('_source', {})
            print('   ', ' '.join(str(hl).split())[:600])
    except Exception as e:
        print(ident, q, 'ERR', e)
    time.sleep(2)
