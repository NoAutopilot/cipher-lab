#!/usr/bin/env python3
"""AUD2-LEDGER-32 (9 Oct 2026): second-verifier press, print and scholarship queries for E347, E349 msg 1, E350 that the first audit (FV-MS18g) did not run:
Google Books API (key from env, never printed, country=US), loc.gov Chronicling America by date window, IA advancedsearch + be-api full text
(Grant Papers vol. 11 around 4-6 Aug 1864; Army and Navy Official Gazette; OR ser. III vol. 4), Semantic Scholar, CORE, OpenAlex.
>= 1.7 s apart, one host at a time. A miss is a search result (rule 10), never a novelty verdict."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url, hdr=None):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, **(hdr or {})}), timeout=60))
    except Exception as e:
        return {'_err': str(e)[:80]}
n = {}
def tick(h): n[h] = n.get(h, 0) + 1; time.sleep(1.7)
GB = ['"W. P. Smith" Grant Monocacy car August 1864', '"master of transportation" Smith Grant Monocacy 1864 car', 'Grant "Relay House" Monocacy "August 5" 1864',
      'Meigs Donaldson Crane "disbursing officer" 1864 Nashville', '"J. C. Crane" "Inspector" quartermaster "military railroads"', '"incompatible" Meigs Crane inspector disbursing',
      '"A. G. Brackett" "Special Inspector" cavalry 1864', '"Redwood Price" "Cavalry Bureau" November 1864 Brackett', 'Grierson Pleasonton "St. Louis" remount November 1864 horses Brackett']
for q in GB:
    d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
    print('GB', repr(q), d.get('_err') or d.get('totalItems'))
    for it in (d.get('items') or [])[:8]:
        v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
        print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:200].replace('\n', ' '))
CA = [('Grant Monocacy', '1864-08-05/1864-08-12'), ('Grant Relay House', '1864-08-05/1864-08-12'), ('Lieutenant General Grant Baltimore Monocacy', '1864-08-05/1864-08-12'),
      ('Colonel Crane quartermaster Nashville', '1864-09-10/1864-11-30'), ('Crane disbursing officer', '1864-09-10/1864-12-31'),
      ('Brackett cavalry inspector', '1864-11-01/1864-12-15'), ('Price Cavalry Bureau', '1864-11-01/1864-12-15'), ('Grierson St. Louis horses', '1864-11-01/1864-12-15')]
for q, dr in CA:
    d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
    res = d.get('results') or []
    print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
    for r in res[:12]:
        print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-60:])
for q in ['title:("army and navy official gazette")', 'title:(official records) AND title:(series III) AND volume:4', 'title:("war of the rebellion") AND title:(ser. 3)']:
    d = get('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(q) + '&fl[]=identifier&fl[]=title&fl[]=volume&rows=15&output=json'); tick('archive.org')
    print('IA', repr(q), d.get('_err') or [(x.get('identifier'), str(x.get('title'))[:50], x.get('volume')) for x in (d.get('response') or {}).get('docs', [])])
BE = [('papersofulyssess0011gran', 'Smith Baltimore'), ('papersofulyssess0011gran', 'Relay House'), ('papersofulyssess0011gran', 'special car'), ('papersofulyssess0011gran', 'Garrett'),
      ('papersofulyssess0012gran', 'Donaldson'), ('papersofulyssess0012gran', 'Brackett'), ('papersofulyssess0012gran', 'Grierson horses'), ('papersofulyssess0013gran', 'Brackett')]
for ident, q in BE:
    d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&identifier=' + ident); tick('be-api')
    hits = (d.get('value') or {}).get('docs') if isinstance(d.get('value'), dict) else d.get('hits') or d.get('value')
    print('BE', ident, repr(q), d.get('_err') or json.dumps(d)[:900])
S2 = ['Grant Monocacy August 1864 Baltimore and Ohio railroad secret', 'Cavalry Bureau 1864 remounts inspection Price', 'Union quartermaster military railroads Nashville 1864 disbursing']
for q in S2:
    d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')}); tick('semanticscholar')
    print('S2', repr(q), d.get('_err') or d.get('total'), [(p.get('title', '')[:60], p.get('year')) for p in (d.get('data') or [])])
for q in ['"Cavalry Bureau" 1864 remount Price Brackett', 'Grant Monocacy Hunter Sheridan August 1864 railroad']:
    d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
    print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:60] for r in (d.get('results') or [])])
for q in ['Cavalry Bureau Civil War remounts 1864', 'military railroads quartermaster Nashville 1864 Donaldson']:
    d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
    print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [(r.get('display_name') or '')[:60] for r in (d.get('results') or [])])
print('requests', n)
