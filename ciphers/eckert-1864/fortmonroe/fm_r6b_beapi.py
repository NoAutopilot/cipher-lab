#!/usr/bin/env python3
"""FM-R6b (9 Oct 2026, account 1): IA be-api snippet search for F2 (5740/0) and F3 (5744/1), 12-13 June 1864 wire/telegraph-line telegrams, >= 1.8 s apart.
A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
IDS = ['warofrebellion363unit', 'warofrebellion401unit', 'warofrebellion402unit', 'papersofulyssess0011gran', 'militarytelegrap02plum', 'privateofficialc04butl']
Q = ['Bickford', '"wire between White House"', '"White House and West Point"', 'Wilcox Landing telegraph', 'Abercrombie "White House" office']
n = 0
for ident in IDS:
    for q in Q:
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
