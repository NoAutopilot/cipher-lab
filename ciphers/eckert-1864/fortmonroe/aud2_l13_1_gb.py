#!/usr/bin/env python3
"""AUD2-LEDGER13-1 (10 Oct 2026): Google Books API (keyed, country=US) queries for E504 E516 E519 E531 E534 E535 -- the families FV-FM65a did not
reach: The Papers of Ulysses S. Grant vols. 13-14 (intitle:Grant; vol. 13 is not on IA) and Google Books at large. Positive control first (FV-FM65b's
E530 hit). Prints volume id, viewability and snippet. >= 1.5 s apart; never prints the key. Usage: aud2_l13_1_gb.py [q1|q2]"""
import json, os, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q1 = ['"sailed in perfect order" intitle:Grant',                                   # control (E530, FV-FM65b)
      '"Suwo Nada" intitle:Grant', '"Oriental" "half an hour" intitle:Grant', '"six vessels" Oriental intitle:Grant', '"all as ordered" intitle:Grant',
      '"returned from the expedition disabled" intitle:Grant', '"Fort Fisher news" intitle:Grant', '"ready by to-morrow noon" intitle:Grant',
      '"mortars, troops or ammunition" intitle:Grant', '"fifty wagons" vessels Monroe intitle:Grant',
      '"Haze" "Sentinel" intitle:Grant', '"fifteen days rations on such vessels" intitle:Grant', '"are all we have" Thames intitle:Grant',
      '"as the Quartermaster designates" intitle:Grant',
      '"draws too much water" Atlantic intitle:Grant', 'Weybosset Towanda intitle:Grant', 'Euterpe Prometheus Varuna intitle:Grant',
      '"overcoat pocket" intitle:Grant', '"kept by Mr. Phillips" intitle:Grant', 'Butler report Wilmington lost Beckwith intitle:Grant',
      '"Baltic" Annapolis docks intitle:Grant', '"approach the docks" Annapolis intitle:Grant']
Q2 = ['"Suwo Nada" "half an hour"', '"Oriental" "Suwo Nada" sailed 1865', '"returned from the expedition disabled"', '"Fort Fisher news change"',
      '"Haze and Sentinel"', '"Dupont, Thames, Haze"', '"fifteen days rations on such vessels"', '"overcoat pocket" "Wilmington expedition"',
      '"Butler\'s report" lost overcoat Beckwith', '"cannot approach the docks at Annapolis"', '"soonest ship troops"', '"Weybossett and Towanda"',
      '"Champion, Weybosset" Towanda', '"draws too much water to go up"']
Q = Q2 if sys.argv[1:] == ['q2'] else Q1
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 5, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        print(q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:5]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('   ', it.get('id'), (v.get('title') or '')[:70], v.get('publishedDate'), it.get('accessInfo', {}).get('viewability'), '|', s[:400])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    time.sleep(1.6)
