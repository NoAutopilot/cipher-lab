#!/usr/bin/env python3
"""FV-FM65b (10 Oct 2026): Google Books API (keyed, country=US) quoted-phrase queries for E502 E507 E512 E520 E530 E532, plus one positive
control printed in OR I/46 pt 2. >= 1.5 s apart. Never prints the key. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"Steamers all ready coaled and loaded with proper rations"', '"turn them over to Colonel Morgan"', '"if the steamer Russia is at"',
     '"Winants is hardly capable"', '"Eliza Hancox has already been sent"', '"sailed in perfect order" Sedgwick Ariel',
     '"what time can this transportation"', '"were all ordered to Baltimore" Ariel']
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 5, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        print(q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:5]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('   ', v.get('title'), v.get('publishedDate'), '|', s[:200])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    time.sleep(1.5)
