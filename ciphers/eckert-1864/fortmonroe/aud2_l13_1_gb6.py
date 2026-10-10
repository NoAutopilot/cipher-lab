#!/usr/bin/env python3
"""AUD2-LEDGER13-1 (10 Oct 2026): fifth snippet round, Grant Papers vol. 13: the notes of 16-17 Jan 1865 (E534, E535) and last tries for E504, E519.
>= 1.6 s apart; never prints the key."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"Jan. 16" Morgan telegraphed intitle:Grant', '"Jan. 17" Morgan telegraphed intitle:Grant', '"Jan. 17" Porter Rawlins intitle:Grant',
     '"three vessels" disabled intitle:Grant', '"ready by tomorrow noon" intitle:Grant', '"Fort Fisher" "your instructions" intitle:Grant',
     '"thirty five hundred" wagons intitle:Grant', '"Haze" intitle:Grant', 'Small rations vessels "Quartermaster" designates intitle:Grant',
     '"all we have" vessels intitle:Grant', '"Atlantic" Howell steamers intitle:Grant', '"Baltic" Newport intitle:Grant']
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 8, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        hits = [it for it in d.get('items', []) if 'Ulysses' in (it.get('volumeInfo', {}).get('title') or '')]
        print(q, '| total', d.get('totalItems'), '| Grant Papers', len(hits))
        seen = set()
        for it in hits:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            if s in seen: continue
            seen.add(s); print('   ', it.get('id'), v.get('publishedDate'), (v.get('subtitle') or v.get('title'))[:50], '|', s[:420])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    time.sleep(1.6)
