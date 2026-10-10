#!/usr/bin/env python3
"""FV-L15d (10 Oct 2026; copied from fv_fm65a_beapi.py): IA be-api full-text queries for E539 E528 E500 E557 E517 (E573 is printed, ORN I/12 p.66):
whole-collection phrase queries (no identifier; the press of the day, later histories). Positive control first: 'Suwo Nada' in OR I/46
pt 2 (warofrebellion014602rootrich) must hit. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion014602rootrich', '"Suwo Nada"'),
     (None, '"torpedoes of nine hundred pounds"'), (None, '"900 pounds each" torpedoes insulating'), (None, 'Phlox torpedoes Parker Lynch "St. Lawrence"'),
     (None, '"Ariel and General Sedgwick"'), (None, '"no forage vessels"'),
     (None, '"anchor and chain" Baltic expedition Newport'), (None, '"will not be sent on the expedition"'),
     (None, '"submarine torpedoes" Lynch Wise "James River"'),
     (None, '"Baltic" "consider the order" countermanded Newport'), (None, '"Let her embark troops"')]
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
