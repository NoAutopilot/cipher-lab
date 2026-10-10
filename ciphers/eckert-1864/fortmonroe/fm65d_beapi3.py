#!/usr/bin/env python3
"""FM65-D (10 Oct 2026): IA be-api whole-collection phrase queries for the F1 (5879/0) Tribune dispatch of 17 Jan 1865, >= 1.8 s apart. Snippets only."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['"well sustained assault" Fisher Terry Sunday', '"nothing could withstand the bravery" Fisher', 'Vanderbilt "bright flash" Fisher magazine explosion anxiety',
     '"greatest anxiety prevailed on board the Vanderbilt"', 'Tribune "special correspondent" Fisher "New Inlet" prisoners "loss will not exceed"', 'Fisher Terry "garrison was composed" assault Sunday prisoners']
for q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        h = d.get('hits', {}); h = h.get('hits', []) if isinstance(h, dict) else h
        print(q, '|', len(h))
        for x in h[:5]:
            print('   id', x.get('fields', {}).get('identifier'))
            for s in (x.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:300])
    except Exception as e: print(q, '| ERR', str(e)[:100])
    time.sleep(1.8)
