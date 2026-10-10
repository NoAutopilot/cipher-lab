#!/usr/bin/env python3
"""AUD2-LEDGER16-2 (10 Oct 2026; copied from fv_l16b_gb.py with fresh queries, none repeated from FV-L16b or CLEAR-SWEEP): Google Books API (keyed, country=US) phrase pass for E518 E526
E527 E546 E553 E554, three fresh queries per entry beyond FIX-FM65's and CLEAR-SWEEP's (names, rare words, numbers).
Mode 'grant': query + intitle:Grant, report only Grant Papers vols. 13/14 ids. Mode 'g3': the same query unrestricted, top 10 with snippet (G3).
Control first: E531 '"six vessels" Oriental' (FIX-FM65's positive control). >= 1.6 s apart; never prints the key. A miss is a search result."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('CTRL-E531', '"six vessels" Oriental'),
 ('E518', '"Smith of the Tribune" Fort Fisher Terry 1865'), ('E518', '"Colonel Webster" Ingalls Tribune correspondent pass'), ('E518', '"Elias Smith" "Fort Fisher"'),
 ('E526', '"Captain James" quartermaster "Fort Monroe" forage January 1865'), ('E526', 'Webster Ingalls forage "Fort Monroe" "City Point" January 9 1865'),
 ('E527', '"Carney" Eastville White Norfolk 1865'), ('E527', '"Major Carney" Negro affairs Norfolk'), ('E527', '"Colonel White" Eastville Butler relieved'),
 ('E546', '"Commodore Lanman" detached 1865'), ('E546', '"Lanman" "Portsmouth" Minnesota Foster telegraph'), ('E546', '"Lanman" "Hampton Roads" detached "Portsmouth, N. H."'),
 ('E553', '"General Vogdes" Gordon commission Norfolk 1865'), ('E553', 'Gordon "protested" command "Eastern Virginia" 1865'),
 ('E554', 'Ord Gordon "for the present" investigation Norfolk Vogdes')]
mode = sys.argv[1]; n = 0
for e, q in P:
    qq = q + (' intitle:Grant' if mode == 'grant' else '')
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': qq, 'country': 'US', 'maxResults': 15 if mode == 'grant' else 10, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); n += 1
        items = d.get('items', [])
        if mode == 'grant': items = [it for it in items if it.get('id') in V13 | V14]
        print(f'{e}\t{q}\ttotal {d.get("totalItems")}\tshown {len(items)}')
        for it in items:
            vi = it.get('volumeInfo', {}); s = (it.get('searchInfo') or {}).get('textSnippet', '')
            tag = 'v13' if it.get('id') in V13 else 'v14' if it.get('id') in V14 else ''
            print(f'    {it.get("id")} {tag} {vi.get("title","")[:60]} ({vi.get("publishedDate","")}) :: {re.sub(r"\s+"," ",s)[:300]}')
    except Exception as ex:
        print(f'{e}\t{q}\tERR {str(ex)[:80]}')
    sys.stdout.flush(); time.sleep(1.6)
print('# requests', n)
