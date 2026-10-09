#!/usr/bin/env python3
"""AUD2-LEDGER-27 (9 Oct 2026): follow-up of the one print_check Google Books return with a telegraph-trade title
(The Telegrapher 1865, e9YfAQAAMAAJ, under the E320 phrase); tight queries, keyed, country=US; prints id, title, year, snippet
for the top 10. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['"ordered O\'Brien away"', '"OBrien away from Bermuda"', '"Caldwell will attend to all cipher"', '"dragged up by anchors" cable 1864',
     '"string wire across" Yorktown', 'Telegrapher 1865 O\'Brien Bermuda Eckert']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': os.environ.get('GOOGLE_BOOKS_KEY', '')})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        print(q, '|', d.get('totalItems'))
        for it in d.get('items', [])[:10]:
            v = it.get('volumeInfo', {}); sn = (it.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', it.get('id'), (v.get('title') or '')[:50], v.get('publishedDate'), '::', ' '.join(sn.split())[:200])
    except Exception as e: print(q, '| ERROR', str(e)[:60])
    n += 1; time.sleep(1.6)
print('requests', n)
