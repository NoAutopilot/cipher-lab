#!/usr/bin/env python3
"""AUD2-LEDGER-29 (9 Oct 2026): E326 second audit -- Google Books (keyed, country=US), Semantic Scholar (keyed, 1.1 s) and CORE v3 (keyed)
queries on Tunstall's arrest in Nov 1864. Keys read from the environment only, never printed. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url, hdr=None):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA, **(hdr or {})}), timeout=60))
    except Exception as e:
        return {'error': str(e)[:80]}
GB = ['"Tunstall" "rebel agent" 1864', '"Tunstall" Nashville arrested November 1864', '"T. T. Tunstall" Nashville 1864',
      '"Thomas T. Tunstall" arrested 1864', '"Tunstall" "Van Duzer"', '"Tunstall" Dana arrest "seizure of his papers"']
for q in GB:
    d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ['GOOGLE_BOOKS_KEY'])
    print('GB', repr(q), d.get('totalItems', d.get('error')))
    for it in d.get('items', [])[:8]:
        v = it['volumeInfo']; sn = it.get('searchInfo', {}).get('textSnippet', '')
        print('   ', v.get('title', '')[:60], v.get('publishedDate', ''), '|', sn[:200].replace('\n', ' '))
    time.sleep(1.6)
for q in ['Tunstall arrest Nashville 1864', 'Thomas Tate Tunstall consul Confederate', 'Union arrests rebel agents Nashville 1864 Dana']:
    d = get('https://api.semanticscholar.org/graph/v1/paper/search?limit=5&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ['S2_KEY']})
    print('S2', repr(q), d.get('total', d.get('error')), [(p.get('title', '')[:60], p.get('year')) for p in d.get('data', [])[:5]])
    time.sleep(1.1)
for q in ['"Tunstall" Nashville 1864 arrest', '"Thomas T. Tunstall"']:
    d = get('https://api.core.ac.uk/v3/search/works/?limit=5&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ['CORE_API_KEY']})
    print('CORE', repr(q), d.get('totalHits', d.get('error')), [(r.get('title', '')[:60], r.get('yearPublished')) for r in d.get('results', [])[:5]])
    time.sleep(1.6)
