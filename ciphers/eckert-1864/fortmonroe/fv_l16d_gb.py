#!/usr/bin/env python3
"""FV-L16d (10 Oct 2026): Google Books API (keyed via $GOOGLE_BOOKS_KEY, never printed; country=US) G3 phrase queries for E441 E472 E442 E473 E469 E466.
Control first: '"Butler favors crossing at Yorktown"' (OR I/36 pt 3 p.822 [page per running head], must hit). 1.6 s apart. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ['GOOGLE_BOOKS_KEY']
Q = ['"Butler favors crossing at Yorktown"', '"boat probably delayed"', '"dread necessity for use of cables"', '"forage him by the other line"',
     '"Homan and Collings" Jamestown', '"New Regime" Edgar Butler Clark', '"Stop your exchanges"', '"heavy and continuous firing" O\'Brien 1864',
     '"do not believe a word against him" Dunn']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        it = d.get('items', [])
        print(q, '| total', d.get('totalItems'))
        for x in it[:10]:
            v = x.get('volumeInfo', {}); s = (x.get('searchInfo') or {}).get('textSnippet', '')
            print('    ', x.get('id'), '|', v.get('title', '')[:70], v.get('publishedDate', ''), '|', ' '.join(s.split())[:220])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
