#!/usr/bin/env python3
"""AUD2-LEDGER15-4 (10 Oct 2026, second audit; copied from fv_l15d_beapi.py, new queries for E539 E528 E500 E517): IA be-api full-text queries for E539 E528 E500 E557 E517 (E573 is printed, ORN I/12 p.66):
whole-collection phrase queries (no identifier; the press of the day, later histories). Positive control first: 'Suwo Nada' in OR I/46
pt 2 (warofrebellion014602rootrich) must hit. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion014602rootrich', '"Suwo Nada"'),
     (None, '"Phlox" "torpedoes" Parker Lynch 1865'), (None, '"insulating wire" "St. Lawrence" Lynch'),
     (None, '"Ariel" "Sedgwick" Ingalls forage "City Point" 1865'),
     (None, '"Baltic" Newport anchor chain "New York" expedition 1865'), (None, '"William L. James" Baltic'),
     (None, '"Baltic" Newport countermanded Monroe 1865'), (None, '"embark troops as before ordered"')]
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
