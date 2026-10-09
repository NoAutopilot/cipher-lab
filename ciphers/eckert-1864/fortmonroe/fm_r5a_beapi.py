#!/usr/bin/env python3
"""FM-R5a (9 Oct 2026): IA be-api full-text search (snippet only) of Grant Papers vols 10 (Jan-Apr 1864), 11 (May-Jun... see ident), 12 and unnumbered for FM-R5a rows' rare words,
>= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0012gran', '"Nineteenth Corps" Rawlins Sheldon'), ('papersofulyssess0011gran', '"Nineteenth Corps" arrived Rawlins'),
     ('papersofulyssess0012gran', 'Gillmore "Fort Monroe" start yesterday'), ('papersofulyssess0012gran', 'Beckwith Sheldon City Point fleet'),
     ('papersofulyssess0012gran', 'Terry Varina O\'Brien'), ('papersofulyssess0012gran', '"Captain Allen" boots'),
     ('papersofulyssess0010gran', 'Gillmore tents Eckert'), ('papersofulyssess0011gran', 'Gillmore pontoon train'),
     ('papersofulyssess0012gran', '"Colonel Howard" artillery Butler batteries'), ('papersofulyssess0000unse', 'Sheldon boots Allen'),
     ('papersofulyssess0000unse', 'Beckwith Gillmore Fort Monroe')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:4]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:6]: print('   ', s.replace('\n', ' ')[:320])
    except Exception as e:
        print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.9)
print('be-api requests', n)
