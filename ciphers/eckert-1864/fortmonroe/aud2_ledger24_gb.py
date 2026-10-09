#!/usr/bin/env python3
"""AUD2-LEDGER-24 (9 Oct 2026): Google Books API phrase queries for E305/E306 (key from GOOGLE_BOOKS_KEY, never printed; country=US;
2 s apart, one pass). Prints totalItems and the first titles/snippets. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
Q = ['"impossible to save all the wire"', '"with axes or otherwise" Bickford', '"cable at West Point" "Gloucester" 1864 Eckert',
     '"no trouble from guerillas"', '"Perkins and party" Bermuda Hundred', '"Abercrombie wishes" "White House" office',
     '"Grant\'s headquarters are removed"', 'Sheldon Eckert Bickford "White House" line June 1864 "closing out"']
key = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in Q:
    u = ('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&maxResults=5&country=US' + ('&key=' + key if key else ''))
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=30))
        print(q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:5]:
            v = it['volumeInfo']; print('   ', v.get('title'), v.get('publishedDate'), '|', (it.get('searchInfo', {}).get('textSnippet') or '')[:160])
    except Exception as e:
        print(q, '| error', type(e).__name__, getattr(e, 'code', ''))
    time.sleep(2)
