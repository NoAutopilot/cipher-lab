#!/usr/bin/env python3
"""O9R-1 (10 Oct 2026): IA be-api full-text snippet search (no login) of the Fox Confidential Correspondence (vol. 2 = 1864-65) and a second Fox copy for the Olcott / Stover / Brady / Painter rows, and of the Grant Papers vol. 10 for the Meigs/Van Vliet rows;
>= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('confidentialcorr02foxg', 'Olcott'), ('confidentialcorr02foxg', 'Stover'), ('confidentialcorr02foxg', 'Brady Fort Lafayette'), ('confidentialcorr02foxg', 'Brooklyn Navy Yard Painter absconded'),
     ('confidentialcorr01foxg', 'Olcott'), ('confidentialcorr02foxg', 'Miss Dix Fulton'),
     ('papersofulyssess0010gran', 'Meigs Van Vliet New York Fulton transports'), ('papersofulyssess0010gran', 'Kelley Cumberland Sigel Ohio militia')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
