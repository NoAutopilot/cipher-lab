#!/usr/bin/env python3
"""FV-L16b (10 Oct 2026, account 1, for LANE LEDGER-16; copied from fv_l15c_gb.py): Google Books API (keyed, country=US) phrase pass for E518 E526
E527 E546 E553 E554, three fresh queries per entry beyond FIX-FM65's and CLEAR-SWEEP's (names, rare words, numbers).
Mode 'grant': query + intitle:Grant, report only Grant Papers vols. 13/14 ids. Mode 'g3': the same query unrestricted, top 10 with snippet (G3).
Control first: E531 '"six vessels" Oriental' (FIX-FM65's positive control). >= 1.6 s apart; never prints the key. A miss is a search result."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('CTRL-E531', '"six vessels" Oriental'),
 ('E518', '"Elias Smith" Tribune expedition Ingalls'), ('E518', '"Elias Smith" correspondent Grant permit pass'), ('E518', 'Tribune correspondent "next boat" expedition Fort Monroe January 1865'),
 ('E526', 'Emerick Abbott forage vessels "Fort Monroe"'), ('E526', '"nor sailed" troops forage Ingalls'), ('E526', '"William L. James" forage Abbott'),
 ('E527', '"Frank J. White" Eastville resign Butler relieved'), ('E527', 'Carney "Negro affairs" Norfolk Butler relieved resign'), ('E527', '"I think I will resign" Butler 1865'),
 ('E546', 'Lanman Minnesota "Portsmouth" detached Foster senator'), ('E546', 'Lanman "executive officer" Parker Minnesota Portsmouth 1865'), ('E546', '"Lafayette S. Foster" Lanman'),
 ('E553', 'Gordon Vogdes commission "Eastern District" Ord'), ('E553', 'Gordon "purposes of the commission" Vogdes'), ('E553', 'Gordon investigation Norfolk Vogdes Shepley February 1865 Ord'),
 ('E554', '"progress quietly" investigation Gordon Ord'), ('E554', 'Ord Gordon "take the command" Vogdes investigation'), ('E554', 'Ord Gordon Shepley Vogdes commission Norfolk February 8 1865')]
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
