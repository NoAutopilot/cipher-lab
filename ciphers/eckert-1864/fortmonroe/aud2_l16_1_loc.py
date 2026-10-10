#!/usr/bin/env python3
"""AUD2-LEDGER16-1 (10 Oct 2026): the press of 5-12 Jan 1865 for E521 (Butler at Fort Monroe 5-6 Jan) and the ships of E509/E514, through the
www.loc.gov JSON API over Chronicling America (dates filter); >= 2 s apart; prints title, date and a text snippet around the first query word.
A miss is a search result, not a novelty verdict (rule 10). Usage: aud2_l16_1_loc.py 'QUERY' ..."""
import json, re, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for q in sys.argv[1:]:
    u = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode({'q': q, 'dates': '1865-01-05/1865-01-12', 'fo': 'json', 'c': 15})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
        R = d.get('results', [])
        print('LOC |', q, '| total', d.get('pagination', {}).get('of'))
        for r in R[:10]:
            txt = ' '.join(r.get('description') or []) if isinstance(r.get('description'), list) else str(r.get('description') or '')
            w = q.split()[0].strip('"').lower(); i = txt.lower().find(w)
            print('   ', r.get('date'), '|', (r.get('title') or '')[:60], '|', ' '.join(txt[max(0, i-200):i+300].split()) if i >= 0 else '-')
    except Exception as e: print('LOC |', q, '| ERROR', str(e)[:80])
    time.sleep(2)
