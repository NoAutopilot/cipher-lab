#!/usr/bin/env python3
"""FV-FM65a (10 Oct 2026): IA be-api full-text queries for E504 E516 E519 E531 E534 E535: Grant Papers vol. 13 and Butler Corr. V and ORN I/12
by identifier, then whole-collection phrase queries (no identifier; Grant Papers 14 and the press). Positive control first: 'Suwo Nada' in OR I/46
pt 2 (warofrebellion014602rootrich) must hit. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion014602rootrich', '"Suwo Nada"'),
     ('papersofulyssess0013gran', 'Baltic'), ('papersofulyssess0013gran', '"Suwo Nada"'), ('papersofulyssess0013gran', 'overcoat'),
     ('papersofulyssess0013gran', 'Sheldon'), ('papersofulyssess0013gran', 'mortars Fisher'),
     ('privateofficialc05butl', 'overcoat'), ('privateofficialc05butl', 'Beckwith'),
     ('officialrecordso0012unse', 'Sentinel'), ('officialrecordso0012unse', 'Haze'),
     (None, '"Haze and Sentinel"'), (None, '"Suwo Nada" Oriental sailed'), (None, '"overcoat pocket" Butler report Wilmington'),
     (None, '"kept by Mr. Phillips"'), (None, '"returned from the expedition disabled"'), (None, '"cannot approach the docks"'),
     (None, '"Weybosset" "Towanda" Euterpe'), (None, '"enough are here to carry"')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident or '(all)', '|', q, '|', d.get('hits', {}).get('total', len(hits)) if isinstance(d.get('hits', {}).get('total'), int) else len(hits))
        for h in hits[:4]:
            idn = (h.get('fields', {}) or {}).get('identifier', '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('    ', idn, '|', ' '.join(s.split())[:260])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
