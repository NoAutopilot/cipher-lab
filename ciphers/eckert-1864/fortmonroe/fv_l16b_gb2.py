#!/usr/bin/env python3
"""FV-L16b (10 Oct 2026, account 1, for LANE LEDGER-16): short Google Books API queries restricted by intitle:Grant (Grant Papers vols. 13/14 ids
reported, every other id listed with its title), after fv_l16b_gb.py's long queries returned 0 in Grant mode. Keyed, country=US, 1.6 s apart, never
prints the key. A miss is a search result."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('E553', 'Vogdes "Eastern District"'), ('E553', 'Gordon "all my time and attention"'), ('E553', 'Vogdes Gordon "respectfully suggest"'),
     ('E554', '"progress quietly"'), ('E554', 'Gordon "for the present" investigation Vogdes'),
     ('E546', 'Lanman Portsmouth'), ('E546', 'Lanman Minnesota detached'),
     ('E518', '"Elias Smith"'), ('E518', 'Tribune correspondent expedition permit'),
     ('E527', 'Carney "Negro Affairs"'), ('E527', '"Frank J. White"'), ('E526', 'Emerick Abbott')]
n = 0
for e, q in P:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q + ' intitle:Grant', 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); n += 1
        items = d.get('items', [])
        print(f'{e}\t{q}\ttotal {d.get("totalItems")}')
        for it in items:
            vi = it.get('volumeInfo', {}); s = (it.get('searchInfo') or {}).get('textSnippet', '')
            tag = 'v13' if it.get('id') in V13 else 'v14' if it.get('id') in V14 else ''
            if tag or 'Papers of Ulysses' in vi.get('title', ''):
                print(f'    {it.get("id")} {tag} {vi.get("title","")[:70]} ({vi.get("publishedDate","")}) :: {re.sub(r"\s+"," ",s)[:400]}')
    except Exception as ex:
        print(f'{e}\t{q}\tERR {str(ex)[:80]}')
    sys.stdout.flush(); time.sleep(1.6)
print('# requests', n)
