#!/usr/bin/env python3
"""AUD2-LEDGER-23 (9 Oct 2026): Google Books API phrase queries for E302 (country=US, key from GOOGLE_BOOKS_KEY, never printed),
plus one positive control phrase from Butler to Sheldon, 28 May 1864 (printed OR I/36 pt 3 p.262). 1.6 s apart. A miss is a search result."""
import json, os, time, urllib.parse, urllib.request
Q = ['"chestnut poles" "Gloucester Point"', '"base of supplies" "chestnut poles"', '"have not rotted down" poles',
     '"very little wire on hand"', '"Sheldon" "Gloucester Point" "Mattapony" 1864 telegraph',
     'CONTROL "telegraph route most easily protected"']
k = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in Q:
    qq = q.replace('CONTROL ', '')
    u = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': qq, 'country': 'US', 'maxResults': 10, 'key': k})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=30))
        it = d.get('items', [])
        print(q, '| totalItems', d.get('totalItems'), '| returned', len(it))
        for i in it[:6]:
            v = i['volumeInfo']; s = i.get('searchInfo', {}).get('textSnippet', '')
            print('   ', v.get('title', '')[:70], v.get('publishedDate', ''), '|', s[:160])
    except Exception as e:
        print(q, '| ERROR', str(e)[:80])
    time.sleep(1.6)
