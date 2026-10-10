#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026): be-api snippet queries inside IA papersofulyssess0014gran (Grant Papers vol. 14, found by the whole-collection
query in fv_l15b_beapi.out) for E567's note, and IA advancedsearch for any Grant Papers vol. 13 item. >= 1.8 s apart."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n = 0
for ident, q in [('papersofulyssess0014gran', '"two engines and some flat cars"'), ('papersofulyssess0014gran', '"None have arrived at this place"'),
                 ('papersofulyssess0014gran', '"Schofield telegraphed to USG"'), (None, '"one battery with each division"')]:
    p = {'q': q}
    if ident: p['identifier'] = ident
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p), headers=UA), timeout=90))
        hits = d.get('hits', {}).get('hits', []); print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:4]:
            f = h.get('fields', {}) or {}; print('   ', f.get('identifier'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:4]: print('      ', s.replace('\n', ' ')[:600])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
u = 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode({'q': 'identifier:papersofulyssess00*gran', 'fl[]': ['identifier', 'title', 'volume'], 'rows': 50, 'output': 'json'}, doseq=True)
try:
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
    print('advancedsearch:', ' '.join(sorted(x['identifier'] for x in d['response']['docs'])))
except Exception as e: print('advancedsearch ERR', str(e)[:100])
print('requests be-api', n, 'archive.org 1')
