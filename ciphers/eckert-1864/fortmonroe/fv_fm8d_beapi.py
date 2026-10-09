#!/usr/bin/env python3
"""FV-FM8d (9 Oct 2026; FV-FM8b script adapted): IA be-api full-text search (snippet only) of the Grant Papers vols. 10 and 13 for
E278/E288/E289 phrases (vol. 10 May-June 1864, vol. 13 Nov 1864-Feb 1865), >= 1.6 s apart; stops the host after a 502 and one retry. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0013gran', '"few remaining"'), ('papersofulyssess0013gran', 'Webster fleet Ingalls'),
     ('papersofulyssess0013gran', 'Dewey "court martial"'), ('papersofulyssess0010gran', '"millions of rations" "White House"')]
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
