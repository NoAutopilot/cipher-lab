#!/usr/bin/env python3
"""AUD2-LEDGER-33 (9 Oct 2026): second-verifier press, print and scholarship queries for E358 (Secretary of War to Bvt Brig. Gen. E. Barton, Memphis,
23 July 1865; prisoner J. N. Ryan per holder 7976-7978, 9258/2, 10043/2) that the first audit (FV-MS18i) did not run: Google Books API (key from env, never
printed, country=US), loc.gov Chronicling America by date window, IA advancedsearch + be-api full text (Papers of Andrew Johnson; Pitman trial record),
Semantic Scholar, CORE, OpenAlex. >= 1.7 s apart, one host at a time. A miss is a search result (rule 10), never a novelty verdict."""
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
    for q in ['"J. N. Ryan" 1865 arrested Memphis', '"Ryan" Memphis July 1865 arrested "Secretary of War" papers cipher', '"Barton" "provost marshal" Memphis 1865 Ryan',
              '"signed Canada" 1865 letter rebel', '"over the signature of Canada" 1865', '"Ryan" Memphis 1865 "Old Capitol" prisoner rebel cipher',
              'Stanton Barton Memphis "close custody" 1865', '"Ryan" "Memphis" 1865 Confederate agent Canada assassination']:
        d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
        print('GB', repr(q), d.get('_err') or d.get('totalItems'))
        for it in (d.get('items') or [])[:8]:
            v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:220].replace('\n', ' '))
if not only or 'ca' in only:
    for q, dr in [('Ryan arrested Memphis', '1865-07-15/1865-08-31'), ('Ryan Memphis prisoner Washington', '1865-07-20/1865-08-31'), ('Ryan Barton Memphis', '1865-07-15/1865-08-31'),
                  ('signed Canada', '1865-06-15/1865-07-31'), ('Ryan rebel papers cipher', '1865-07-20/1865-08-31'), ('Ryan Old Capitol Memphis', '1865-07-25/1865-09-15')]:
        d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
        res = d.get('results') or []
        print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
        for r in res[:12]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-60:])
if not only or 'ia' in only:
    for q in ['title:("papers of andrew johnson")', 'title:("assassination of President Lincoln and the trial of the conspirators")']:
        d = get('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(q) + '&fl[]=identifier&fl[]=title&fl[]=volume&fl[]=date&rows=20&output=json'); tick('archive.org')
        print('IA', repr(q), d.get('_err') or [(x.get('identifier'), str(x.get('title'))[:40], x.get('volume'), str(x.get('date'))[:4]) for x in (d.get('response') or {}).get('docs', [])])
if 'be' in only:
    for ident, q in [a.split('::') for a in only[only.index('be') + 1:]]:
        d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&identifier=' + ident); tick('be-api')
        print('BE', ident, repr(q), d.get('_err') or json.dumps(d)[:1200])
if not only or 'sch' in only:
    for q in ['J. N. Ryan Memphis 1865 arrest Confederate', 'Memphis provost marshal 1865 Barton']:
        d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')}); tick('semanticscholar')
        print('S2', repr(q), d.get('_err') or d.get('total'), [(p.get('title', '')[:60], p.get('year')) for p in (d.get('data') or [])])
        d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
        print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:60] for r in (d.get('results') or [])])
        d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
        print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [(r.get('display_name') or '')[:60] for r in (d.get('results') or [])])
print('requests', n)
