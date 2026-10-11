#!/usr/bin/env python3
"""AUD2-FM16e (11 Oct 2026): OpenAlex (Bearer key), Semantic Scholar (x-api-key), CORE v3 (Bearer) scholarship queries for E443 E445 E446 E448.
One request at a time, >= 1.5 s (S2 1.1 s rule kept); stops a host on its first 429/403. Never prints keys. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
Q = ['yellow fever New Berne 1864 epidemic', 'Fort Monroe military telegraph 1864 cipher operators',
     'Cherrystone telegraph cable Chesapeake 1864', 'Stanton City Point visit October 1864 Manhattan',
     'Butler Porter December 1864 powder boat Fort Fisher telegraph']
H = {'openalex': lambda q: ('https://api.openalex.org/works?' + urllib.parse.urlencode({'search': q, 'per-page': 5}), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}),
     's2': lambda q: ('https://api.semanticscholar.org/graph/v1/paper/search?' + urllib.parse.urlencode({'query': q, 'limit': 5, 'fields': 'title,year'}), {'x-api-key': os.environ.get('S2_KEY', '')}),
     'core': lambda q: ('https://api.core.ac.uk/v3/search/works/?' + urllib.parse.urlencode({'q': q, 'limit': 5}), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')})}
n = {}
for h, f in H.items():
    n[h] = 0
    for q in Q:
        url, hd = f(q); hd['User-Agent'] = 'cipher-lab research script (contact via repository)'
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=hd), timeout=60)); n[h] += 1
        except Exception as ex:
            n[h] += 1; print(h, '|', q, '| ERR', str(ex)[:60]); 
            if '429' in str(ex) or '403' in str(ex): break
            continue
        rs = d.get('results') or d.get('data') or []
        print(h, '|', q, '| total', d.get('meta', {}).get('count', d.get('total', d.get('totalHits'))))
        for r in rs[:5]: print('    ', (r.get('title') or r.get('display_name') or '')[:110], r.get('year') or r.get('publication_year') or r.get('yearPublished'))
        time.sleep(1.6)
print('requests', n)
