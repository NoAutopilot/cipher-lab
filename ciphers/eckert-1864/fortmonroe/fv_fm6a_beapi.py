#!/usr/bin/env python3
"""FV-FM6a (9 Oct 2026): IA be-api full-text search (snippet only) of the Grant Papers vols. 11-12 (June-Nov 1864) for
E217/E219/E226/E227 phrases, >= 1.6 s apart; stops the host after a 502 and one retry. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0012gran', 'Greyhound'), ('papersofulyssess0012gran', '"Fort Monroe" family'),
     ('papersofulyssess0012gran', 'Webster'), ('papersofulyssess0011gran', '"boats enough"'), ('papersofulyssess0011gran', 'Ingalls Wright 11,000'),
     ('papersofulyssess0011gran', '"Charles City" Blood')]
n = 0; fails = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    for attempt in (1, 2):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
            hits = d.get('hits', {}).get('hits', [])
            print(ident, q, len(hits))
            for h in hits[:6]:
                for s in (h.get('highlight', {}) or {}).get('text', [])[:4]: print('   ', s.replace('\n', ' ')[:300])
            break
        except Exception as e:
            n += 1; print(ident, q, 'ERR', str(e)[:80])
            if attempt == 1: time.sleep(20)
            else: fails += 1
    if fails: print('be-api failed twice: host stopped'); break
    time.sleep(1.6)
print('be-api requests', n)
