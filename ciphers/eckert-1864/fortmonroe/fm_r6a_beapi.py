#!/usr/bin/env python3
"""FM-R6a (9 Oct 2026): IA be-api full-text search (snippet only) of Grant Papers vols 10 (Jan-Apr 1864), 11 (May-Jun... see ident), 12 and unnumbered for FM-R6a rows' rare words,
>= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion393unit', 'Ships Gap Snake Creek Pass delay our trains'), ('warofrebellion393unit', '"Hood contemplated" invasion Tennessee reoccupy'),
     ('warofrebellion393unit', 'Roddy Tuscumbia Thomas Sherman Ship\'s Gap'), ('warofrebellion393unit', 'Glass Nashville Beckwith Sherman Ship\'s Gap'),
     ('papersofulyssess0012gran', 'Ship\'s Gap Sherman Hood Snake Creek'), ('warofrebellion363unit', 'White House base of supplies Gloucester Point cable'),
     ('warofrebellion362unit', 'White House base of supplies Sheldon Eckert telegraph'), ('papersofulyssess0011gran', 'telegraph White House Gloucester Point Eckert cable'),
     ('warofrebellion363unit', 'chestnut poles Eckert telegraph line Peninsula'), ('privateofficialc04butl', 'White House telegraph line Eckert Sheldon'),
     ('papersofulyssess0010gran', 'Plymouth evacuated Lee Fort Monroe')]
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
