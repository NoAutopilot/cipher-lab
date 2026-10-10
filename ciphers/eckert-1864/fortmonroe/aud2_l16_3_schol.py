#!/usr/bin/env python3
"""AUD2-LEDGER16-3 (10 Oct 2026; copied from aud2_l15_4_schol.py), second audit of eckert-1864 E558 E564 E569 E574: open-index scholarship pass (OpenAlex keyed header, Semantic Scholar keyed, CrossRef), titles of top hits only."""
import json, os, time, urllib.parse, urllib.request
QS = ['Ord Yorktown telegraph office February 1865 military telegraph Fort Monroe', 'pilots monitors James River March 1865 quartermaster Fort Monroe',
      'Mrs. Ord Fort Monroe 1865 telegraph office', 'Stanton visit City Point March 1865 River Queen', 'George D. Sheldon military telegraph Fort Monroe cipher ledger']
UA = 'cipher-lab research script (contact via repository)'
def get(url, hdr):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=dict(hdr, **{'User-Agent': UA})), timeout=40))
for q in QS:
    try:
        d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')})
        print('OA |', q, '|', d['meta']['count'], '|', ' ;; '.join((w.get('title') or '')[:80] for w in d['results'][:5]))
    except Exception as e: print('OA |', q, '| ERR', e)
    time.sleep(1.2)
    try:
        d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')})
        print('S2 |', q, '|', d.get('total'), '|', ' ;; '.join(f"{p['title'][:80]} ({p.get('year')})" for p in d.get('data', [])[:5]))
    except Exception as e: print('S2 |', q, '| ERR', e)
    time.sleep(1.2)
    try:
        d = get('https://api.crossref.org/works?rows=5&query=' + urllib.parse.quote(q), {})
        print('CR |', q, '|', ' ;; '.join(((w.get('title') or [''])[0])[:80] for w in d['message']['items'][:5]))
    except Exception as e: print('CR |', q, '| ERR', e)
    time.sleep(1.2)
