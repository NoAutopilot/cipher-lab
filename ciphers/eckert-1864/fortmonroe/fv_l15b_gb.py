#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026, account 1, for LANE LEDGER-15; copy of fv_fm65b_gb2.py): Google Books API (keyed, country=US) queries for
E545 E560 E505 E567 E525 E572, most restricted to The Papers of Ulysses S. Grant (intitle:Grant; vols 13/14 = mnRjmhe3QLoC, ij8fAQAAMAAJ /
DVLPEPsH1_oC, 1D8fAQAAMAAJ), two more phrases per entry than FIX-FM65 (names and numbers), plus the E545 near-miss expanded and two positive
controls. Prints volume id and snippet. >= 1.6 s apart; never prints the key. A miss is query-bound (FIX-FM65 controls), not a verdict."""
import json, os, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = [('CTRL', '"sailed in perfect order" intitle:Grant'), ('CTRL', '"Steamers all ready coaled" intitle:Grant'),
     ('E545', '"Artillerests" intitle:Grant'), ('E545', '"batteries of Schofields Corps" intitle:Grant'), ('E545', '"two companies of" Artillerists Schofield intitle:Grant'),
     ('E545', '"each Division" Schofield battery Boyd intitle:Grant'), ('E545', 'Schofield mules Kentucky Washington transportation intitle:Grant'), ('E545', '"G. W. Schofield" intitle:Grant'),
     ('E560', 'Yorktown telegraph James quartermaster intitle:Grant'), ('E560', '"telegraph station" Yorktown 1865'),
     ('E505', '"other service" Rawlins steamer coal "no rations" intitle:Grant'), ('E505', 'Beckwith Sheldon Rawlins steamer "other service" intitle:Grant'),
     ('E567', '"flat cars" Schofield Wright engines intitle:Grant'), ('E567', '"two engines" Schofield Wilmington intitle:Grant'), ('E567', '"commence work" Wright Schofield intitle:Grant'),
     ('E525', 'Newport Baltic Annapolis Webster intitle:Grant'), ('E525', '"Baltic" "Annapolis" Newport coal 1865 intitle:Grant'),
     ('E572', '"Champion" Fayetteville Wilmington scouts intitle:Grant'), ('E572', '"steamship Champion" Wilmington Fayetteville 1865'), ('E572', '"Champion arrived" Wilmington Fayetteville')]
n = 0
for e, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 6, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        print(e, '|', q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:6]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('   ', it.get('id'), (v.get('title') or '')[:50], v.get('publishedDate'), it.get('accessInfo', {}).get('viewability'), '|', s[:500])
    except Exception as ex: print(e, '|', q, '| ERR', str(ex)[:80])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
