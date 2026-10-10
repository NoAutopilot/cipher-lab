#!/usr/bin/env python3
"""AUD2-LEDGERN2-5 (10 Oct 2026, account 4): second-verifier press and print queries for eckert-1864 O9-DC (Meigs to Van Vliet, 5 Feb 1864, Marcia C. Day
costs), O9-DE (Fox to Olcott, 10 Mar 1864, seize Stover's books and papers), O9-DH/O9-DI (Fox to Olcott, 9 Mar 1864, Brady, Navy or Army; arrest Brady, Fort
Lafayette, Dix) that FV-O9a did not run: loc.gov Chronicling America Feb-Apr 1864, Google Books API (key from env, never printed, country=US), CORE, OpenAlex.
>= 1.7 s apart. A miss is a search result (rule 10), never a novelty verdict. Usage: aud2_ledgern2_5_search.py [ca|gb|sch]"""
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
if not only or 'ca' in only:
    for q, dr in [('Stover Fort Lafayette books papers', '1864-03-01/1864-04-30'), ('Brady arrested Fort Lafayette navy', '1864-03-08/1864-04-15'),
                  ('Olcott Brady arrest', '1864-03-08/1864-04-15'), ('Marcia C. Day', '1864-02-01/1864-03-31'), ('Isle a Vache Van Vliet', '1864-02-01/1864-04-15'),
                  ('Stover permits Fort Lafayette', '1864-02-10/1864-04-15')]:
        d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
        res = d.get('results') or []
        print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
        for r in res[:12]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:80], '|', r.get('id', '')[-70:])
if not only or 'gb' in only:
    k = os.environ.get('GOOGLE_BOOKS_KEY', '')
    for q in ['"Marcia C. Day" "separate and distinct account"', '"special expedition" "Marcia C. Day" Meigs', '"Van Vliet" "Marcia C. Day" 1864 charter',
              '"Stover" "books and papers" Olcott Fox 1864', '"Brady" Olcott Fox "Fort Lafayette" 1864 arrest', '"Is Brady connected"']:
        d = get('https://www.googleapis.com/books/v1/volumes?country=US&maxResults=10&q=' + urllib.parse.quote(q) + '&key=' + k); tick('googleapis')
        print('GB', repr(q), d.get('_err') or d.get('totalItems'))
        for it in (d.get('items') or [])[:10]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', v.get('publishedDate'), '|', str(v.get('title'))[:70], '|', s[:200].replace('\n', ' '))
if not only or 'sch' in only:
    for q in ['Ile a Vache colonization return 1864 Marcia C. Day', 'Henry Steel Olcott Navy Department fraud investigation 1864']:
        d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('CORE_API_KEY', '')}); tick('core')
        print('CORE', repr(q), d.get('_err') or d.get('totalHits'), [str(r.get('title'))[:90] for r in (d.get('results') or [])[:5]])
        d = get('https://api.openalex.org/works?per-page=5&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')}); tick('openalex')
        print('OA', repr(q), d.get('_err') or (d.get('meta') or {}).get('count'), [str(r.get('title'))[:90] for r in (d.get('results') or [])[:5]])
print('requests', n)
