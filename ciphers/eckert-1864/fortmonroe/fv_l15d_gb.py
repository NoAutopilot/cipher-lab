#!/usr/bin/env python3
"""FV-L15d (10 Oct 2026): Google Books API (keyed, country=US) snippet queries for E539 E528 E500 E573 E557 E517 against The Papers of Ulysses S.
Grant vols. 13-14 (ids mnRjmhe3QLoC, ij8fAQAAMAAJ = vol. 13; DVLPEPsH1_oC, 1D8fAQAAMAAJ = vol. 14), two more per entry beyond FIX-FM65's two, names and
numbers included, plus one positive control (E531, FIX-FM65's hit). A hit = a snippet from one of the four ids. Other volumes' snippets are printed
too (ORN/OR/press). >= 1.6 s apart; never prints the key. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
IDS = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ', 'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
Q = [('CTRL', '"Suwo Nada" "half an hour" intitle:Grant'),
     ('E539', 'Phlox torpedoes "900 pounds" Parker'), ('E539', '"insulating wire" torpedoes Lynch Parker 1865'),
     ('E528', 'Ariel Sedgwick "forage vessels" Ingalls intitle:Grant'), ('E528', '"any reason for delay" Ariel Sedgwick'),
     ('E500', 'Baltic "anchor and chain" Newport intitle:Grant'), ('E500', '"anchor & chain" Baltic James Newport 1865'),
     ('E573', '"No news of the Montauk"'), ('E573', 'Lehigh Charleston Montauk Kinston Glisson'),
     ('E557', '"submarine torpedoes" Lynch Wise 1865 "James River"'), ('E557', 'Lynch "Inspector of Ordnance" torpedoes "James River" February 1865'),
     ('E517', 'Baltic countermanded Newport "Quartermaster General" intitle:Grant'), ('E517', '"Baltic" "embark troops" Newport Monroe January 1865')]
for e, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        its = d.get('items', [])
        hit = [it['id'] for it in its if it['id'] in IDS]
        print(e, '|', q, '| total', d.get('totalItems'), '| GRANT HIT ' + ','.join(hit) if hit else '| no Grant 13/14 hit')
        for it in its[:6]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('    ', it['id'], v.get('title', '')[:70], v.get('publishedDate'), '|', s[:260])
    except Exception as ex: print(e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.6)
