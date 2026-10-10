#!/usr/bin/env python3
"""AUD2-LEDGER15-3 (10 Oct 2026): Google Books API (keyed, country=US) phrase/name queries for E549 (Washington to Eckert at Fort Monroe, 2 Feb 1865,
Schofield's cipher operator, construction corps, Mack and party). Prints title, year, id and snippet per hit. 1.6 s apart. Never prints the key.
A miss is a search result, not a novelty verdict (rule 10). Usage: aud2_l15_3_gb.py 'query1' 'query2' ..."""
import json, os, sys, time, urllib.parse, urllib.request
K = os.environ['GOOGLE_BOOKS_KEY']
n = 0
for q in sys.argv[1:]:
    url = 'https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&maxResults=10&country=US&key=' + K
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
    except Exception as e:
        print(f'{q!r}: ERROR {type(e).__name__} {getattr(e, "code", "")}'); n += 1; time.sleep(1.6); continue
    n += 1
    items = d.get('items', [])
    print(f'{q!r}: {d.get("totalItems")} total, {len(items)} shown')
    for it in items:
        v = it.get('volumeInfo', {}); s = it.get('searchInfo', {}).get('textSnippet', '')
        print(f'   {it["id"]} | {v.get("title","")[:70]} | {v.get("publishedDate","")} | {s[:260]}')
    time.sleep(1.6)
print('requests', n)
