#!/usr/bin/env python3
"""AUD2-LEDGERN2-3 (10 Oct 2026, account-4): second audit of N2-GA, N2-GC, N2-GI. IA be-api full-text search with short phrases and single
rare words not run by FV-N2c (Grant Papers vols. 12-13 single words; then whole-IA searches with no identifier). Positive controls first.
>= 1.8 s apart. A miss is a search result (rule 10), never a novelty verdict."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0010gran', '"requisite ammunition"'),          # positive control (N2-GH, FV-N2c hit)
     ('papersofulyssess0012gran', 'Brice'), ('papersofulyssess0012gran', 'paymasters'), ('papersofulyssess0012gran', 'Forsyth Martinsburg'),
     ('papersofulyssess0013gran', 'Brice'), ('papersofulyssess0013gran', 'paymasters'), ('papersofulyssess0013gran', 'unpaid'),
     ('papersofulyssess0013gran', '"Relay House"'),
     (None, '"requisite ammunition and supplies"'),                   # positive control, whole IA
     (None, '"sufficient escort at Martinsburg"'), (None, '"leave here Monday morning" paymasters'),
     (None, '"paymasters ready to go"'), (None, '"sent to Relay House" paymasters'), (None, '"unpaid to the 31st of August"'),
     (None, '"unpaid to August 31"'), (None, '"by river for City Point" paymasters'), (None, '"two regiments of the Sixth Corps" paymasters'),
     (None, 'Brice paymasters "City Point" 1864'), (None, 'Brice paymasters Sheridan "Relay House"')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
        hits = d.get('hits', {}).get('hits', [])
        tot = d.get('hits', {}).get('total')
        print(ident or 'ALL-IA', '|', q, '|', len(hits), '| total', tot)
        for h in hits[:6]:
            src = h.get('fields', {}).get('identifier') or h.get('_source', {}).get('identifier') or h.get('_id')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', src, '::', s.replace('\n', ' ')[:260])
    except Exception as e: print(ident or 'ALL-IA', '|', q, '| ERR', str(e)[:120])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
