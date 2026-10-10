#!/usr/bin/env python3
"""FM65-C batch 3 (10 Oct 2026): ORN ser. I vols. 11-12 (IA officialrecordso0011unse / 0012unse), Butler Corr. V, Grant Papers 13 via short queries; control: 'Fisher'. >= 1.8 s apart."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('officialrecordso0011unse', 'Fisher'), ('officialrecordso0011unse', 'Cosgrove'), ('officialrecordso0011unse', 'Ericsson'), ('officialrecordso0011unse', 'Eckert'),
     ('officialrecordso0012unse', 'Cosgrove'), ('officialrecordso0012unse', 'Eckert'), ('officialrecordso0012unse', 'Sheldon'),
     ('privateofficialc05butl', 'Sheldon Monroe'), ('privateofficialc05butl', 'Carney'), ('papersofulyssess0013gran', 'Fisher'), ('papersofulyssess0013gran', 'Sedgwick'), ('papersofulyssess0013gran', 'Carney')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:2]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('     ', ' '.join(s.split())[:240])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
