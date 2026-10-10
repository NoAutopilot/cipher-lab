#!/usr/bin/env python3
"""AUD2-LEDGER-35 (10 Oct 2026): second-verifier press, print and scholarship queries for E357 (Leet to Bowers, City Point, 19 Aug 1864: no troops joined
or left Early; rumour at Orange C.H. that Fitzhugh Lee's cavalry was badly beaten) that the first audit (FV-MS18k) did not run: Google Books API (key from
env, never printed, country=US), loc.gov Chronicling America 19-31 Aug 1864, IA be-api (Grant Papers 12), Semantic Scholar, CORE, OpenAlex. >= 1.7 s apart.
A miss is a search result (rule 10), never a novelty verdict. Usage: aud2_ledger35_search.py [gb|ca|be|sch]"""
import json, os, sys, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url, hdr=None):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, **(hdr or {})}), timeout=60))
    except Exception as e:
        return {'_err': str(e)[:80]}
n = {}
def tick(h): n[h] = n.get(h, 0) + 1; time.sleep(1.7)
only = sys.argv[1:]
if not only or 'gb' in only:
    for q in ['"Fitzhugh Lee\'s cavalry had been badly beaten"', '"Lee\'s cavalry had been badly beaten" Orange', '"rumored at Orange"', '"no other troops than those already reported"',
              'Leet Bowers "August 19, 1864" Early Orange', '"joined Early" "Orange Court House" rumor Fitzhugh Lee beaten 1864', '"Fitz Lee" "badly beaten" August 1864 Orange',
              'Leet "Elgin" cipher telegram 1864']:
        d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
        print('GB', repr(q), d.get('_err') or d.get('totalItems'))
        for it in (d.get('items') or [])[:8]:
            v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:220].replace('\n', ' '))
if not only or 'ca' in only:
    for q, dr in [('Fitz Lee badly beaten', '1864-08-19/1864-08-31'), ('Fitzhugh Lee cavalry beaten artillery', '1864-08-17/1864-08-31'), ('Orange Court House rumor Fitz Lee', '1864-08-17/1864-08-31'),
                  ('Fitz Lee lost artillery prisoners', '1864-08-17/1864-08-31'), ('Leet Bowers', '1864-08-19/1864-09-15')]:
        d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
        res = d.get('results') or []
        print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
        for r in res[:12]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-60:])
if not only or 'be' in only:
    for ident, q in [('papersofulyssess0012gran', '"Orange Court House" Fitzhugh'), ('papersofulyssess0012gran', '"badly beaten"'), ('papersofulyssess0012gran', 'Leet "August 19"'),
                     ('papersofulyssess0012gran', '"joined Early"'), ('papersofulyssess0012gran', '"no troops had moved to or from the Valley"')]:
        d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&identifier=' + ident); tick('be-api')
        print('BE', ident, repr(q), d.get('_err') or json.dumps(d)[:1500])
if not only or 'sch' in only:
    for q in ['Fitzhugh Lee cavalry August 1864 Guard Hill Front Royal', 'Bureau of Military Information Sharpe scouts Orange Court House 1864']:
        d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')}); tick('semanticscholar')
        print('S2', repr(q), d.get('_err') or d.get('total'), [(p.get('title', '')[:60], p.get('year')) for p in (d.get('data') or [])])
        d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
        print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:60] for r in (d.get('results') or [])])
        d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
        print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [(r.get('display_name') or '')[:60] for r in (d.get('results') or [])])
print('requests', n)
