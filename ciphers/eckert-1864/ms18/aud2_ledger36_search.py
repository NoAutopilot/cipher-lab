#!/usr/bin/env python3
"""AUD2-LEDGER-36 (10 Oct 2026): second-verifier print, press and scholarship queries for E366 (Dana to Halleck, 8 May 1865, arrest William
Boulware), E369 (Secretary of War to the officer commanding Augusta via Lines, 24 May 1865, arrest Thomas J. Campbell) and E370 (W. H. Whiton
to McCallum, 7 Sept 1864, horses / forage by rail) in the families the first audit FV-MS18l did not cover: Google Books (key from env, never
printed, country=US; Steers's volume by restricted query), loc.gov Chronicling America by date window, IA advancedsearch + be-api full text,
Semantic Scholar, CORE, OpenAlex. >= 1.7 s apart, one host at a time. A miss is a search result (rule 10), never a novelty verdict.
Usage: aud2_ledger36_search.py [gb|ca|ia|sch|be IDENT::QUERY ...]"""
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
GB = ['Boulware inauthor:Steers', '"Boulware" "King and Queen" 1865 arrest', '"arrest William Boulware"', '"Boulware" Dana Halleck 1865',
      '"Norwell" Boulware', '"Boulware" Bingham "Judge Advocate" 1865 assassination',
      '"Thomas J. Campbell" Augusta arrest 1865', '"T. J. Campbell" receiver Knoxville arrested 1865', '"confiscating officer" Knoxville Campbell',
      '"Campbell" "confiscating officer" "Rebel Government"',
      '"in excess of those now in" Sherman forage rail', '"forage can be supplied by rail"', 'McCallum Whiton 1864 forage horses Sherman rail',
      '"Whiton" McCallum "military railroads" 1864']
if not only or 'gb' in only:
    for q in GB:
        d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
        print('GB', repr(q), d.get('_err') or d.get('totalItems'))
        for it in (d.get('items') or [])[:8]:
            v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:240].replace('\n', ' '))
if not only or 'ca' in only:
    for q, dr in [('Boulware arrested', '1865-05-01/1865-06-30'), ('Boulware King Queen', '1865-05-01/1865-07-31'),
                  ('Campbell arrested Augusta Knoxville', '1865-05-20/1865-07-15'), ('Campbell confiscating Knoxville', '1865-05-01/1865-08-31'),
                  ('Campbell receiver Knoxville arrested', '1865-05-20/1865-08-31'), ('McCallum forage horses rail Sherman', '1864-09-01/1864-09-30')]:
        d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
        res = d.get('results') or []
        print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
        for r in res[:12]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-70:])
if not only or 'ia' in only:
    for q in ['title:("report of bvt. brig. gen. D. C. McCallum")', 'McCallum AND "military railroads" AND date:[1866 TO 1867]',
              'title:("war of the rebellion") AND "series III" AND "volume 5"', 'title:("papers of andrew johnson")',
              'title:("lincoln assassination") AND creator:(Steers)']:
        d = get('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(q) + '&fl[]=identifier&fl[]=title&fl[]=volume&fl[]=date&rows=15&output=json'); tick('archive.org')
        print('IA', repr(q), d.get('_err') or [(x.get('identifier'), str(x.get('title'))[:50], x.get('volume'), str(x.get('date'))[:4]) for x in (d.get('response') or {}).get('docs', [])])
if not only or 'iag' in only:
    for q in ['"William Boulware"', '"Thomas J. Campbell" confiscating', '"Masury and Whiton" McCallum']:
        d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q)); tick('be-api')
        print('BEG', repr(q), d.get('_err') or json.dumps(d)[:1500])
if 'be' in only:
    for ident, q in [a.split('::') for a in only[only.index('be') + 1:]]:
        d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&identifier=' + ident); tick('be-api')
        print('BE', ident, repr(q), d.get('_err') or json.dumps(d)[:1200])
if not only or 'sch' in only:
    for q in ['William Boulware arrest 1865 King and Queen', 'Thomas J. Campbell Confederate receiver Knoxville sequestration', 'McCallum military railroads forage Sherman 1864']:
        d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')}); tick('semanticscholar')
        print('S2', repr(q), d.get('_err') or d.get('total'), [(p.get('title', '')[:60], p.get('year')) for p in (d.get('data') or [])])
        d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
        print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:60] for r in (d.get('results') or [])])
        d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
        print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [(r.get('display_name') or '')[:60] for r in (d.get('results') or [])])
print('requests', n)
