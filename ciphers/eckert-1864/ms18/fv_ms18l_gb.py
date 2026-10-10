#!/usr/bin/env python3
"""FV-MS18l (10 Oct 2026): Google Books (key, country=US) and IA be-api full-text queries for E366 E369 E370. 1.6 s apart. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
GB = ['"Boulware" "King and Queen" arrested 1865', '"William Boulware" arrest 1865 Dana', '"Thomas J. Campbell" confiscating Knoxville', '"T. J. Campbell" "receiver" Knoxville Confederate', '"Masury" "Whiton" McCallum 1864', '"Whiton" "military railroad" horses forage Sherman 1864']
IA = ['"Boulware" "King and Queen" 1865 arrest', '"Thomas J. Campbell" Knoxville confiscat', '"Masury and Whiton"']
n = 0
for q in GB:
    u = 'https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        print('GB', q, d.get('totalItems'))
        for it in d.get('items', [])[:8]:
            v = it['volumeInfo']; print('   ', v.get('title', '')[:70], v.get('publishedDate'), '|', (it.get('searchInfo', {}).get('textSnippet') or '')[:220])
    except Exception as e: print('GB', q, 'ERR', str(e)[:80])
    n += 1; time.sleep(1.6)
for q in IA:
    u = 'https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&size=8'
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print('IA', q, d.get('hits', {}).get('total'))
        for h in hits[:8]:
            f = h.get('fields', {}); print('   ', f.get('identifier'), '|', str(h.get('highlight', {}).get('text', ''))[:220])
    except Exception as e: print('IA', q, 'ERR', str(e)[:80])
    n += 1; time.sleep(1.6)
print('requests', n)
