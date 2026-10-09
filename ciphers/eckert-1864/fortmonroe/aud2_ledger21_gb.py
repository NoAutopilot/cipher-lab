#!/usr/bin/env python3
"""AUD2-LEDGER-21 (9 Oct 2026, account 4): Google Books API phrase queries for E278 and E289 (eckert-1864), one at a time, 1.6 s apart,
key from GOOGLE_BOOKS_KEY with country=US (never printed). Prints per query: total, then title/year/textSnippet for the first 5.
A 0 is a search result for the log, not a statement about print (rule 10). Usage: aud2_ledger21_gb.py > aud2_ledger21_gb.out"""
import json, os, sys, time, urllib.parse, urllib.request
Q = [
 ('E289', '"Dewey" "court martial" 1864 "Taylor" witnesses Porter squadron'),
 ('E289', '"Taylor and Lieutenant Commander Dewey"'),
 ('E289', '"Captain Taylor" "Dewey" "court-martial" 1864'),
 ('E289', '"shall the witnesses leave"'),
 ('E289', '"prospect of this squadron leaving"'),
 ('E278', '"few remaining will get away"'),
 ('E278', '"Webster" "Ingalls" "fleet" December 1864 "Fort Monroe" quartermaster'),
 ('E278', '"most of the fleet left" 1864 Fortress Monroe'),
]
key = os.environ.get('GOOGLE_BOOKS_KEY', '')
for e, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': key})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=30))
        items = d.get('items', [])
        print(f'{e}\t{q}\ttotal={d.get("totalItems", 0)}')
        for it in items[:5]:
            v = it['volumeInfo']; s = it.get('searchInfo', {}).get('textSnippet', '')
            print(f'    {v.get("title","")} ({v.get("publishedDate","")}) [{it["accessInfo"].get("viewability")}] :: {s}')
    except Exception as ex:
        print(f'{e}\t{q}\tERROR {type(ex).__name__} {getattr(ex, "code", "")}')
    time.sleep(1.6)
