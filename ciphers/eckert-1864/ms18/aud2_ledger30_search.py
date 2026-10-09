#!/usr/bin/env python3
"""AUD2-LEDGER-30 (9 Oct 2026): second-verifier scholarship and press queries for E333, E335, E340 the first audit (FV-MS18d) did not run:
Google Books API (key from env, never printed, country=US), loc.gov Chronicling America by date window, Semantic Scholar, CORE, OpenAlex.
>= 1.6 s apart, one host at a time. A miss is a search result (rule 10), never a novelty verdict."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url, hdr=None):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, **(hdr or {})}), timeout=60))
    except Exception as e:
        return {'_err': str(e)[:80]}
n = {}
def tick(h): n[h] = n.get(h, 0) + 1; time.sleep(1.7)
GB = ['"Mouthrey" OR "Monthny" Lasalle 1864', '"Captain Edwards" Havana plot steamer 1864 Dix', 'Phelps Havana steamer plot 1864 New York arrested',
      '"Berrien" Pittsburgh powder 1864 navy ordnance', '"Pennock" Cairo powder 1864 "Berrien"', '"Wise" "Bureau of Ordnance" Pennock powder Cairo 1864',
      '"Alberger" Lynchburg 1865', '"Morris H. Alberger"', '"Alberger" Baker detective 1865 safe']
for q in GB:
    d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
    print('GB', repr(q), d.get('_err') or d.get('totalItems'))
    for it in (d.get('items') or [])[:8]:
        v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
        print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:160].replace('\n', ' '))
CA = [('Havana plot steamer', '1864-05-25/1864-06-10'), ('Phelps Havana', '1864-05-25/1864-06-15'), ('Edwards Havana rebels', '1864-05-25/1864-06-15'),
      ('Berrien powder', '1864-03-25/1864-04-30'), ('powder Cairo Pittsburgh', '1864-03-25/1864-04-30'),
      ('Alberger', '1865-09-15/1865-12-31'), ('Alberger', '1866-01-01/1866-12-31')]
for q, dr in CA:
    d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
    res = d.get('results') or []
    print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
    for r in res[:12]:
        print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-60:])
S2 = ['Havana Confederate plot seize steamer 1864', 'Lafayette C. Baker secret service Lynchburg 1865', 'Navy Bureau of Ordnance Cairo powder 1864 Pennock']
for q in S2:
    d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')}); tick('semanticscholar')
    print('S2', repr(q), d.get('_err') or d.get('total'), [(p.get('title', '')[:60], p.get('year')) for p in (d.get('data') or [])])
for q in ['"Thomas Savage" Havana consul 1864 plot steamers', 'Alberger Lynchburg 1865']:
    d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
    print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:60] for r in (d.get('results') or [])])
for q in ['Confederate plot Havana New York steamers 1864', 'Lafayette Baker detective Lynchburg 1865']:
    d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
    print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [(r.get('display_name') or '')[:60] for r in (d.get('results') or [])])
print('requests', n)
