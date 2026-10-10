#!/usr/bin/env python3
"""AUD2-LEDGER15-1 (10 Oct 2026): open-index scholarship queries (OpenAlex with OPENALEX_KEY header, CrossRef, Semantic Scholar with S2_KEY)
for E555 E568 E541 E576 E575. Keys from the environment, never printed. Writes aud2_l15_1_schol.out. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l15_1_schol.out')
Q = ['Fort Monroe telegraph cipher 1865', 'military telegraph Wilmington Goldsboro 1865 construction', 'Gordon Ord Blackwater Suffolk cavalry 1865',
     'Stromboli torpedoes 1865 Wise Bureau of Ordnance', 'Meagher division Annapolis February 1865 transports']
def get(url, h):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60))
with open(OUT, 'w') as f:
    n = 0
    for q in Q:
        for name, url, h, pick in [
            ('openalex', 'https://api.openalex.org/works?' + urllib.parse.urlencode({'search': q, 'per-page': 5}),
             {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', ''), 'User-Agent': 'cipher-lab research script'},
             lambda d: [(w.get('display_name'), w.get('publication_year')) for w in d.get('results', [])]),
            ('crossref', 'https://api.crossref.org/works?' + urllib.parse.urlencode({'query': q, 'rows': 5}),
             {'User-Agent': 'cipher-lab research script (contact via repository)'},
             lambda d: [((w.get('title') or [''])[0], (w.get('issued', {}).get('date-parts') or [[None]])[0][0]) for w in d.get('message', {}).get('items', [])]),
            ('s2', 'https://api.semanticscholar.org/graph/v1/paper/search?' + urllib.parse.urlencode({'query': q, 'limit': 5, 'fields': 'title,year'}),
             {'x-api-key': os.environ.get('S2_KEY', ''), 'User-Agent': 'cipher-lab research script'},
             lambda d: [(w.get('title'), w.get('year')) for w in d.get('data', []) or []])]:
            n += 1
            try: f.write(f'{name} | {q} | ' + ' || '.join(f'{t} ({y})' for t, y in pick(get(url, h))) + '\n')
            except Exception as e: f.write(f'{name} | {q} | ERROR {type(e).__name__} {str(e)[:60]}\n')
            time.sleep(1.2)
    f.write(f'requests {n}\n')
print(open(OUT).read())
