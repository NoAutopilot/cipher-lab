#!/usr/bin/env python3
"""AUD2-LEDGER13-1 (10 Oct 2026): third Google Books snippet round (keyed, country=US), Grant Papers only: the head of the printed E516, and digit/
spelling variants for E535 E534 E504 E519 as the edition prints telegrams verbatim ('Three (3)', '3500'). >= 1.6 s apart; never prints the key."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['Beckwith overcoat intitle:Grant', '"Butler\'s report of the Wilmington" intitle:Grant', '"report of the Wilmington Expedition" lost intitle:Grant',
     '"Mr. Phillips" theatre intitle:Grant', '"Shepley" Norfolk Beckwith intitle:Grant', '"Has it been lost again" intitle:Grant',
     '"vessels returned" disabled intitle:Grant', '"disabled" "Fort Fisher" mortars intitle:Grant', '"3500 men" intitle:Grant', '"Coehorn" Fisher Monroe intitle:Grant',
     '"Thames" "Haze" intitle:Grant', '"Haze" Sentinel Dupont intitle:Grant', '"Sentinel" Monroe Bradley intitle:Grant', '"rations on such vessels" intitle:Grant',
     '"Atlantic" "draws too much water" intitle:Grant', '"Towanda" intitle:Grant', '"Howell" steamers Bradley intitle:Grant', '"Baltic" Annapolis coal intitle:Grant',
     '"Baltic" Swann Point intitle:Grant', '"Morgan telegraphed to Rawlins" intitle:Grant', '"Sheldon" Rawlins Jan. 17 intitle:Grant']
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
