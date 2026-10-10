#!/usr/bin/env python3
"""AUD2-LEDGER16-3 (10 Oct 2026): two follow-up Google Books API (keyed, country=US) queries on Grant Papers vol. 14 (DVLPEPsH1_oC / 1D8fAQAAMAAJ),
for the note to Grant to Stanton 14 Mar 1865 3 PM (Stanton's trip to City Point, context for E574). 1.6 s apart; never prints the key."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in ['"other matters tomorrow" Stanton', '"Secretary Stanton is" Rawlins Ord March']:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q + ' intitle:Grant', 'country': 'US', 'maxResults': 20, 'key': K})
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    print(q, 'total', d.get('totalItems'))
    for it in d.get('items', []):
        s = (it.get('searchInfo') or {}).get('textSnippet', '')
        print('   ', it.get('id'), it['volumeInfo'].get('title', '')[:50], '::', re.sub(r'\s+', ' ', s))
    time.sleep(1.6)
print('# requests 2')
