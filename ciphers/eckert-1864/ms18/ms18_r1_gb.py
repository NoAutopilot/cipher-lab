#!/usr/bin/env python3
"""MS18-R1: Google Books API (country=US, key from env) quoted-phrase queries, >= 1.6 s apart; prints totalItems and up to 3 titles + snippets. A miss is a search result, not a verdict (rule 10)."""
import json, os, re, sys, time, urllib.parse, urllib.request
key = os.environ.get('GOOGLE_BOOKS_KEY', '')
for ph in sys.argv[1:]:
    u = 'https://www.googleapis.com/books/v1/volumes?country=US&maxResults=5&q=' + urllib.parse.quote('"' + ph + '"') + ('&key=' + key if key else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=40))
        print(f'{ph!r}: totalItems {d.get("totalItems")}')
        for it in d.get('items', [])[:3]:
            v = it['volumeInfo']; s = re.sub(r'</?[a-z]+>', '', it.get('searchInfo', {}).get('textSnippet', ''))[:150]
            print('   ', v.get('title', '')[:70], v.get('publishedDate', ''), '|', s)
    except Exception as e:
        print(f'{ph!r}: ERROR {e}')
    time.sleep(1.8)
