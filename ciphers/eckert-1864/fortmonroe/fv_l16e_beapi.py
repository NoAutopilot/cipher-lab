#!/usr/bin/env python3
"""FV-L16e (10 Oct 2026, for LANE LEDGER-16; copied from fv_l15d_beapi.py): IA be-api full-text queries for the N3 candidates E447 E471 E474 E443 E445 E446 E448:
whole-collection phrase queries (no identifier; the press of the day, later histories). Positive control first: 'Suwo Nada' in OR I/46
pt 2 (warofrebellion014602rootrich) must hit. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion014602rootrich', '"Suwo Nada"'),
     (None, '"Saugus" "will start down" Colhoun'), (None, '"send no ciphers till"'), (None, '"has General Butler\'s fleet left"'),
     (None, '"yellow fever is prevailing to considerable extent at"'), (None, '"have him sent here with his instruments"'),
     (None, '"Dunn formerly employed"'), (None, '"don\'t fail to be at the wharf"')]
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
