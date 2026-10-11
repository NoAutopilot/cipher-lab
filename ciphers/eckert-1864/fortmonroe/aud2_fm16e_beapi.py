#!/usr/bin/env python3
"""AUD2-FM16e (11 Oct 2026, for LANE DEFAULT-A1-0540): IA be-api full-text queries for E443 E445 E446 E448, fresh (none of fv_l16e_beapi.py's):
identifier-scoped name queries in the Grant Papers vols. 10, 12, 13 and Butler's correspondence vol. III (not cached on disk), each volume with
its own positive control, and whole-collection phrase queries. Control 'Suwo Nada' in OR I/46 pt 2 first. >= 1.8 s apart. A miss is a search
result (rule 10); an identifier that returns an error or 0 on its control is unreachable, not a negative."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion014602rootrich', '"Suwo Nada"'),
     ('privateofficialc03butl', 'Cherrystone'), ('privateofficialc03butl', 'Dunn'),
     ('papersofulyssess0010gran', 'Cherrystone'), ('papersofulyssess0012gran', 'Manhattan'), ('papersofulyssess0012gran', '"yellow fever"'),
     ('papersofulyssess0013gran', 'Baird'),
     (None, '"thought best to notify you at once"'), (None, '"Baird will arrive"'), (None, '"same W. A. Dunn"'),
     (None, '"don\'t mention his coming"'), (None, '"presume Bates has posted you"')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        tot = d.get('hits', {}).get('total')
        print(ident or '(all)', '|', q, '|', tot if isinstance(tot, int) else (tot or {}).get('value', len(hits)) if isinstance(tot, dict) else len(hits))
        for h in hits[:4]:
            idn = (h.get('fields', {}) or {}).get('identifier', '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('    ', idn, '|', ' '.join(s.split())[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
