#!/usr/bin/env python3
"""AUD2-LEDGER13-1 (10 Oct 2026): follow-up Google Books API snippet queries (keyed, country=US) restricted to The Papers of Ulysses S. Grant vol. 13
(volumes mnRjmhe3QLoC, ij8fAQAAMAAJ) after aud2_l13_1_gb.py found E531 and E516 printed there: phrases chosen to pull the head and tail of each printed
text, and further tries for E504 E519 E534 E535. Prints only snippets from Grant Papers volumes. >= 1.6 s apart; never prints the key."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = [# E516 head/tail/source line
     '"last night I lost" intitle:Grant', '"some place from my overcoat" intitle:Grant', '"inquiries made at both places" intitle:Grant',
     '"Beckwith" "Shepley" intitle:Grant', '"travel very much" intitle:Grant', '"Wilmington Expedition" Beckwith Sheldon intitle:Grant',
     # E531 head/tail
     '"If in summing up today I said six vessels" intitle:Grant', '"seven hundred & seventy eight" intitle:Grant', '"5109 men" intitle:Grant',
     # E535
     '"three of the vessels" disabled intitle:Grant', '"returned from the expedition" intitle:Grant', '"thirty five hundred men" intitle:Grant',
     '"fifty wagons" intitle:Grant', '"Fort Fisher news" mortars intitle:Grant', '"instructions in regard to mortars" intitle:Grant',
     '"each vessel leaves here" intitle:Grant', '"every effort will be made" vessels noon intitle:Grant',
     # E534
     '"Sentinel are all" intitle:Grant', '"sufficient for the teams" intitle:Grant', '"obtain the remainder" intitle:Grant',
     '"Have you nothing at City Point" intitle:Grant', '"put fifteen days rations" intitle:Grant', '"each vessel will carry" Small intitle:Grant',
     # E504
     '"Atlantic" "1400" troops intitle:Grant', '"ordered to report to Col. Bradley" intitle:Grant', '"Gen. Lyon" Varuna intitle:Grant',
     '"Euterpe" intitle:Grant', '"Weybossett" intitle:Grant',
     # E519
     '"ship troops on the Baltic" intitle:Grant', '"Coal at Annapolis" intitle:Grant', '"Baltic" Newport Sampson intitle:Grant',
     '"own judgment after seeing the captain" intitle:Grant']
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
