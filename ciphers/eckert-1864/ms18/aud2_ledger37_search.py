#!/usr/bin/env python3
"""AUD2-LEDGER-37 (10 Oct 2026): second-verifier Google Books (key from env, never printed, country=US) and Chronicling America (loc.gov, date windows)
queries for E371 (Meigs to R. Allen, Louisville, 15 Sept 1864, Colonel Ferry/Terry), E374 (Whiton to McCallum, 6 Feb 1864, Devereux / A. Anderson),
E375 (Eckert to L. C. Baker, Baltimore, 20 Oct 1865, Isaac Surratt) that FV-MS18n did not run. >= 1.7 s apart. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url):
    try: return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60))
    except Exception as e: return {'_err': str(e)[:80]}
n = {}
def tick(h): n[h] = n.get(h, 0) + 1; time.sleep(1.7)
only = sys.argv[1:]
GB = ['"Colonel Ferry" quartermaster Louisville 1864', '"Ferry" "chief quartermaster" Louisville 1864', '"Terry" quartermaster depot Louisville 1864 funds',
      '"Robert Allen" Louisville quartermaster 1864 "Ferry"', '"withdraw" "all Government funds" quartermaster 1864 Meigs Allen',
      '"Devereux" "go West" Stanton 1864 McCallum', '"Whiton" McCallum 1864 telegram', '"Devereux" Stanton "not willing" 1864',
      '"Isaac Surratt" Baltimore Baker October 1865', '"Isaac Surratt" "Baltimore" 1865 detective watch', '"Isaac Surratt" Eckert 1865',
      '"keep a very close watch" Surratt']
CA = [('Colonel Ferry quartermaster', '1864-09-01/1865-03-31'), ('Ferry quartermaster Louisville', '1864-09-01/1865-03-31'),
      ('Terry quartermaster Louisville', '1864-09-01/1864-12-31'), ('Devereux Anderson McCallum', '1864-01-25/1864-03-15'),
      ('Isaac Surratt', '1865-10-15/1865-11-30'), ('Surratt Baltimore watched', '1865-10-15/1865-12-31')]
if not only or 'gb' in only:
    for q in GB:
        d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')); tick('googleapis')
        print('GB', repr(q), d.get('_err') or d.get('totalItems'))
        for it in (d.get('items') or [])[:8]:
            v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', s[:240].replace('\n', ' '))
if not only or 'ca' in only:
    for q, dr in CA:
        d = get('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)); tick('loc.gov')
        print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'))
        for r in (d.get('results') or [])[:12]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:70], '|', r.get('id', '')[-70:])
print('requests', n)
