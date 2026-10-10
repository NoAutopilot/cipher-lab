#!/usr/bin/env python3
"""FV-N2c (10 Oct 2026): G3 decoded-phrase pass on Google Books (key from env, country=US, never printed). >= 1.5 s apart.
Positive control first: a phrase of the printed OR I/33 p.994 Burnside telegram of the same day. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"proceed direct to Fairfax Court-House with five days"',
     '"will reach Fairfax to-night" Burnside', '"column in motion" Burnside Fairfax 1864', '"requisite ammunition and supplies with the column"',
     '"paymasters will leave here Monday morning"', '"sufficient escort at Martinsburg"', 'Brice paymasters "Nineteenth Corps" escort Martinsburg October 1864',
     '"paymasters ready to go" Brice', 'paymasters "Relay House" Brice Sheridan December 1864', '"unpaid to the 31st of August" paymasters 1864',
     '"paymasters will leave to-morrow" "City Point"', 'Brice paymasters "Sixth Corps" "City Point" December 1864']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        items = d.get('items', [])
        print(q, '|', d.get('totalItems'), 'items')
        for it in items[:5]:
            v = it.get('volumeInfo', {}); s = it.get('searchInfo', {}).get('textSnippet', '')
            print('   ', v.get('title', '')[:70], v.get('publishedDate', ''), '|', s[:200])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    n += 1; time.sleep(1.5)
print('googleapis requests', n)
