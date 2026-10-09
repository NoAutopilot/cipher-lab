#!/usr/bin/env python3
"""AUD2-LEDGER-22 (9 Oct 2026, account 4): follow-up be-api snippet queries in Papers of U. S. Grant vol. 12 (papersofulyssess0012gran)
around its Coggins Point footnotes, to test whether E292's relay (Wilson/Small to Morgan, 16 Sept 1864) is quoted there. >= 2 s apart.
A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['"Michael R"', '"lines are down"', '"1200 head"', '"Wilson" commissary', '"cattle herd"']  # second run (first run: cattle herd 502, unsuitable position, Small, Morgan, head of cattle; timed out before the rest)
for q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': 'papersofulyssess0012gran'})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print('be-api vol12 |', q, '|', len(hits))
        for h in hits[:1]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:12]: print('   ', ' '.join(s.split())[:340])
    except Exception as e: print('be-api vol12 |', q, '| ERROR', e)
    time.sleep(2)
print('be-api requests', len(Q))
