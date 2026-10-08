#!/usr/bin/env python3
"""FV-FM3c (8 Oct 2026): be-api full-text search, optionally inside one IA identifier (Grant Papers are lending-only: snippet, no page).
Args: 'term' or 'term@identifier'. >= 2.2 s apart; stops the host at the second error (good-citizen rule). A miss is a search result."""
import json, re, sys, time, urllib.parse, urllib.request
err = 0
for a in sys.argv[1:]:
    q, _, ident = a.partition('@')
    url = 'https://be-api.us.archive.org/fts/v1/search?size=6&q=' + urllib.parse.quote('"' + q + '"') + (('&identifier=' + ident) if ident else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        h = d['hits']; print(f'{a!r}: total {h["total"]}')
        for x in h['hits'][:3]:
            s = re.sub(r'\s+', ' ', re.sub(r'</?[a-z]+>|\{\{\{|\}\}\}', '', ' '.join(x.get('highlight', {}).get('text', [''])[:2])))[:400]
            print('   ', x.get('fields', {}).get('identifier', x.get('_id')), '|', s)
    except Exception as e:
        err += 1; print(f'{a!r}: ERROR {e}')
        if err >= 2: print('host stopped after 2 errors'); break
    time.sleep(2.2)
