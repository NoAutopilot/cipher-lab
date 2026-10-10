#!/usr/bin/env python3
"""AUD2-LEDGER14-2: Google Books API snippet queries (keyed, country=US), 1.6 s apart. Usage: aud2_l14_2_gb.py QUERYFILE"""
import json, os, sys, time, urllib.parse, urllib.request
key = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith('#')]:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': key})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=40))
    except Exception as e:
        print(f'Q {q}\n  ERROR {type(e).__name__} {getattr(e, "code", "")}'); time.sleep(1.6); continue
    items = d.get('items', [])
    print(f'Q {q}\n  total {d.get("totalItems", 0)}')
    for it in items:
        v = it['volumeInfo']; s = it.get('searchInfo', {}).get('textSnippet', '')
        print(f'  - {v.get("title","")[:70]} | {v.get("publishedDate","")} | {it["id"]} | {s[:260]}')
    time.sleep(1.6)
