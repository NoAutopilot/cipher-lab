#!/usr/bin/env python3
"""AUD2-LEDGER13-1 (10 Oct 2026): fourth snippet round, Grant Papers vol. 13 only: the heads and tails of the printed E516 and E531 (sender, date,
addressee, source line). >= 1.6 s apart; never prints the key."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"telegh me the result" intitle:Grant', '"enquiries made at both places" intitle:Grant', '"Beckwith telegraphed" intitle:Grant',
     '"Beckwith" "Wilmington Expedition" intitle:Grant', '"Oriental" "has sailed" intitle:Grant', '"Jan. 15" Morgan Rawlins Oriental intitle:Grant',
     '"six vessels I" intitle:Grant', '"Suwo Nada" intitle:"Ulysses"', '"overcoat" intitle:"Ulysses" 1865']
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
