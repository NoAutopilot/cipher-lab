#!/usr/bin/env python3
"""FV-MS18g (9 Oct 2026): Google Books API (country=US, key from env, never printed) phrase queries for E347, E349, E350. A miss is a search result."""
import json, os, time, urllib.parse, urllib.request
Q = ['"profound secret" Grant Monocacy Relay 1864', '"Frederick train" Grant Monocacy 1864 Smith', '"relieve Colonel Crane" disbursing', 'Crane "disbursing officer" Inspector Donaldson Nashville 1864',
     '"Burnet House" Brackett Price 1864 horses', '"Redwood Price" Brackett 1864 "Planters House"']
for q in Q:
    p = {'q': q, 'country': 'US', 'maxResults': 5}
    if os.environ.get('GOOGLE_BOOKS_KEY'): p['key'] = os.environ['GOOGLE_BOOKS_KEY']
    try:
        d = json.load(urllib.request.urlopen('https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode(p), timeout=60))
        print(q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:5]:
            v = it['volumeInfo']; print('   ', it['id'], v.get('title'), v.get('publishedDate'), '|', ' '.join(str(it.get('searchInfo', {}).get('textSnippet', '')).split())[:250])
    except Exception as e:
        print(q, 'ERR', str(e)[:80])
    time.sleep(1.6)
