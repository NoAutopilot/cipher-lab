#!/usr/bin/env python3
"""AUD2-LEDGERN2-2 (10 Oct 2026): second-verifier print, press and scholarship queries for N2-FA (Dana for the Secretary of War to Warren, 30 Oct 1864,
Felix McCloskey), N2-FB (Quartermaster General to Ingalls, 26 June 1864, sea-going steamers for the wounded) and N2-FE (Ingalls to Rawlins, 3 Dec 1864,
Sixth Corps embarking) that the first audit (FV-N2a) did not run: IA be-api (Papers of U. S. Grant 11-13; Fry 2020 as a positive control), Google Books API
(key from env, never printed, country=US), loc.gov Chronicling America by date, Semantic Scholar, CORE, OpenAlex. >= 1.7 s apart. A miss is a search
result (rule 10), never a novelty verdict. Usage: aud2_ledgern2_2_search.py [be|gb|ca|sch]"""
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
G = 'papersofulyssess00%02dgran'
if not only or 'be' in only:
    for ident, q in [('republicinranks0000zach', 'McCloskey'),                       # positive control (FV-N2a's citation)
                     (G % 12, 'McCloskey'), (G % 12, '"ballot-box stuffer"'), (G % 12, 'Seymour agents ballots'), (G % 12, 'Warren Seymour commissioner'),
                     (G % 12, '"Fifth Corps" ballots'),
                     (G % 11, '"hospital transports"'), (G % 11, '"sea-going"'), (G % 11, 'Ingalls "New Orleans" steamers'), (G % 11, '"Surgeon General" transports'),
                     (G % 11, '"wait upon the other"'),
                     (G % 13, '"Sixth Corps" embarked'), (G % 13, 'Ingalls Bradley steamers'), (G % 13, '"Third Division" "Sixth Corps"'),
                     (G % 13, '"river steamers"')]:
        d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&identifier=' + ident); tick('be-api')
        hits = (d.get('hits') or {}).get('hits', []) if isinstance(d.get('hits'), dict) else []
        print('BE', ident, repr(q), d.get('_err') or len(hits))
        for h in hits[:3]:
            for s in ((h.get('highlight') or {}).get('text') or [])[:5]: print('    ', s.replace('\n', ' ')[:320])
if not only or 'gb' in only:
    for q in ['"Felix McCloskey"', '"McCloskey" "ballot-box stuffer"', '"old ballot-box stuffer from California"', '"credibly reported to this Department" Seymour',
              'McCloskey Seymour commissioner "Fifth Corps" ballots 1864', 'Warren Dana McCloskey ballots October 1864',
              '"one service or duty must wait upon the other"', '"great accumulation of sick and wounded" "City Point"', 'Meigs Ingalls "hospital transports" "New Orleans" June 1864',
              '"Sixth Corps" Ingalls Rawlins "December 3, 1864"', '"river steamers" "Sixth Corps" Bradley December 1864']:
        d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
        print('GB', repr(q), d.get('_err') or d.get('totalItems'))
        for it in (d.get('items') or [])[:8]:
            v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:240].replace('\n', ' '))
if not only or 'ca' in only:
    for q, dr in [('McCloskey ballot', '1864-10-25/1864-11-30'), ('McCloskey Seymour commissioner', '1864-10-25/1864-11-30'), ('Felix McCloskey', '1864-06-01/1865-06-30'),
                  ('Seymour agents Fifth Corps ballots', '1864-10-28/1864-11-15'), ('hospital transports City Point New Orleans', '1864-06-24/1864-07-10'),
                  ('Sixth Corps embarking Washington City Point', '1864-12-02/1864-12-10')]:
        d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
        res = d.get('results') or []
        print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
        for r in res[:12]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-70:])
if not only or 'sch' in only:
    for q in ['soldier vote 1864 New York Seymour commissioners fraud army', 'hospital transports James River 1864 Medical Department steamers']:
        d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')}); tick('semanticscholar')
        print('S2', repr(q), d.get('_err') or d.get('total'), [(p.get('title', '')[:60], p.get('year')) for p in (d.get('data') or [])])
        d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
        print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:60] for r in (d.get('results') or [])])
        d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
        print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [(r.get('display_name') or '')[:60] for r in (d.get('results') or [])])
print('requests', n)
