#!/usr/bin/env python3
"""AUD2-LEDGER15-2 (10 Oct 2026, account 1, for LANE LEDGER-15; second audit of E525 and E505 msg 2): Google Books API queries (keyed, country=US;
never prints the key; 1.6 s apart), phrases and names FV-L15b and FIX-FM65 did not query (fv_l15b_gb*.out); control first.
A miss is a search result, not a statement about print (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['CONTROL | "sailed in perfect order" intitle:Grant',
     'E505 | "best going steamers"', 'E505 | "one of the best going" steamers Rawlins', 'E505 | "Rawlins wishes you to send"',
     'E505 | "no rations will be required"', 'E505 | "in addition to the steamers named"', 'E505 | Howell Webster steamer "City Point" January 1865 intitle:Grant',
     'E505 | Howell quartermaster "for other service" steamer 1865', 'E505 | "best going" steamer "Fort Monroe" 1865 Rawlins Howell',
     'E525 | "Baltic got off"', 'E525 | "countermand the order" Baltic Newport', 'E525 | "where she can take troops"',
     'E525 | "impossible for her to come up"', 'E525 | "let me know what orders you give her"', 'E525 | "The Baltic" Annapolis coal Newport 1865 quartermaster',
     'E525 | "Baltic" Annapolis "Fort Monroe" January 1865 transport brigade', 'E525 | Newport Webster Baltic 1865 telegram']
n = 0
for line in Q:
    tag, q = [s.strip() for s in line.split('|', 1)]
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 6, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        print(tag, '|', q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:6]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('   ', it.get('id'), (v.get('title') or '')[:50], v.get('publishedDate'), it.get('accessInfo', {}).get('viewability'), '|', s[:400])
    except Exception as ex: print(tag, '|', q, '| ERR', str(ex)[:80])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
