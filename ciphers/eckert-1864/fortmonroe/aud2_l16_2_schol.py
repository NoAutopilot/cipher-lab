#!/usr/bin/env python3
"""AUD2-LEDGER16-2 (10 Oct 2026): open-index scholarship pass (OpenAlex keyed via header, CrossRef) for E518 E526 E527 E546 E553 E554:
the Fort Monroe telegraph ledger and the parties. Never prints a key. A miss is a search result, not a novelty verdict (rule 10)."""
import json, os, time, urllib.parse, urllib.request
OA = os.environ.get('OPENALEX_KEY', '')
Q = ['Fort Monroe telegraph cipher ledger 1865', 'Gordon commission Norfolk contraband trade 1865', 'Lanman Minnesota 1865 Portsmouth',
     'Elias Smith New York Tribune correspondent Fort Fisher', 'Carney superintendent Negro affairs Norfolk 1865']
for q in Q:
    for name, url, hdr in [('openalex', 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': q, 'per-page': 5}), {'Authorization': 'Bearer ' + OA} if OA else {}),
                           ('crossref', 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query': q, 'rows': 5}), {})]:
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)', **hdr}), timeout=60))
            items = d.get('results') if name == 'openalex' else d.get('message', {}).get('items', [])
            print(name, '|', q, '|', ' ;; '.join(((it.get('display_name') or (it.get('title') or [''])[0]) or '')[:90] for it in items))
        except Exception as e:
            print(name, '|', q, '| ERROR', str(e)[:80])
        time.sleep(1.6)
