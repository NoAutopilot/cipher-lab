#!/usr/bin/env python3
"""FV-L16d (10 Oct 2026; copied from fv_l15d_beapi.py): IA be-api full-text queries for E441 E472 E442 E473 E469 E466 (Apr-May 1864):
whole-collection phrase queries (no identifier; later histories, Plum, O'Brien, the press). Positive control first: 'Suwo Nada' in OR I/46
pt 2 (warofrebellion014602rootrich) must hit. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion014602rootrich', '"Suwo Nada"'),
     (None, '"boat probably delayed"'), (None, '"No. 14 wire" Yorktown cable'), (None, '"chance for poles"'),
     (None, '"forage him by the other line"'),
     (None, '"Homan and Collings"'), (None, '"via Jamestown Island" cable "City Point" O\'Brien'),
     (None, '"New Regime" Norfolk Clark 1864'), (None, '"Edgar\'s name"'),
     (None, '"heavy and continuous firing" O\'Brien'),
     (None, '"do not believe a word against him"')]
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
