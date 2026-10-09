#!/usr/bin/env python3
"""FM-R3d (9 Oct 2026): be-api.us.archive.org full-text queries (no identifier), >=2 s apart, stop on any non-200. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
Q = ['"yellow fever is raging in Newbern"', '"Surgeon Hand" "yellow fever" Newbern 1864 Freeman Philadelphia', '"signal field cord" Butler 1864', '"steamer Brady" Matilda Portsmouth "Bermuda Hundred" cavalry',
     '"Florida" "Monticello" "Mount Vernon" Malvern telegram Welles July 1864 Lee', '"Fulton and Craig" Butler Kautz Hicksford May 1864']
for q in Q:
    u = 'https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
    except Exception as e:
        print(q, 'ERR', e); break
    hits = d.get('hits', {}).get('hits', [])
    print(q, '->', len(hits), 'hits;', ' | '.join((h.get('fields', {}).get('identifier') or ['?'])[0] if isinstance(h.get('fields', {}).get('identifier'), list) else str(h.get('fields', {}).get('identifier')) for h in hits[:4]))
    time.sleep(2.2)
