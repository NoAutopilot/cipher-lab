#!/usr/bin/env python3
"""FV-FM65b (10 Oct 2026): Google Books API (keyed, country=US) queries restricted to The Papers of Ulysses S. Grant (intitle) for the six
entries, after the gb.py hit for E530 (Q2 list: simpler intitle:Grant queries, run as fv_fm65b_gb2.py q2); prints volume id and snippet. >= 1.5 s apart; never prints the key."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"sailed in perfect order" intitle:Grant', '"two hundred and seventy men" Ashland intitle:Grant', 'Morgan Sedgwick Ariel Ashland intitle:"Papers of Ulysses"',
     'Winants Hancox intitle:"Papers of Ulysses"', 'Russia "flag ship" Dodge intitle:"Papers of Ulysses"', 'Howell Webster Morgan commissary intitle:"Papers of Ulysses"',
     '"mule teams" Bradley Webster intitle:"Papers of Ulysses"', 'Webster Ingalls Baltic Baltimore Illinois Victor intitle:"Papers of Ulysses"',
     '"each steamer will carry" intitle:"Papers of Ulysses"', '"Steamers all ready coaled" intitle:"Papers of Ulysses"']
import sys
if sys.argv[1:] == ['q3']:
    Q = ['"Victor and Illinois" Baltimore intitle:Grant', '"six mule teams complete" intitle:Grant', '"4000 men" "mule teams" Webster intitle:Grant',
         '"Russia" Dodge Butler "flag" intitle:Grant', '"Steamers" "Morgan" "Rawlins wishes" intitle:Grant', '"Hancox" intitle:"Ulysses"']
if sys.argv[1:] == ['q2']:
    Q = ['"Two steamers" Ariel Sedgwick intitle:Grant', '"Winants" intitle:Grant', '"Eliza Hancox" intitle:Grant', '"Russia" "flag ship" intitle:Grant',
         '"each steamer will carry" intitle:Grant', '"coaling and watering" intitle:Grant', '"Colonel Morgan" "chief commissary" Howell intitle:Grant',
         '"mule teams" Bradley "what time" intitle:Grant', '"heard from them since" Baltic intitle:Grant', '"steamers named had left" intitle:Grant']
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 5, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        print(q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:5]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('   ', it.get('id'), v.get('title'), v.get('subtitle'), v.get('publishedDate'), it.get('accessInfo', {}).get('viewability'), '|', s[:400])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    time.sleep(1.5)
