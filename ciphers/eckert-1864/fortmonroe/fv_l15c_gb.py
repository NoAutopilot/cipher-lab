#!/usr/bin/env python3
"""FV-L15c (10 Oct 2026, account 1, for LANE LEDGER-15; after fixfm65_gb.py): Google Books API (keyed, country=US) phrase pass for E513 E515
E529 E549 E551 E552, two queries per entry beyond FIX-FM65's two (names and numbers, clear-copy wording where a holder clear copy exists).
Mode 'grant': query + intitle:Grant, report only Grant Papers vols. 13/14 ids. Mode 'g3': the same query unrestricted, top 10 with snippet (G3).
Control first: E531 '"six vessels" Oriental' (FIX-FM65's positive control). >= 1.6 s apart; never prints the key. A miss is a search result."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('CTRL-E531', '"six vessels" Oriental'),
 ('E513', '"muster rolls" Binney paymaster Butler'), ('E513', '"Amos Binney" paymaster Norfolk 1865'),
 ('E515', '"William L. James" Ariel Illinois Baltic'), ('E515', 'Newport Ariel Victor Illinois Sedgwick Baltic "Quartermaster General"'),
 ('E529', '"John Rodgers" Ericsson Puritan shaft'), ('E529', 'blockade runner Julia Beaufort buoys lighted Porter'),
 ('E549', 'Schofield Stager "cipher operator" Eckert February 1865'), ('E549', 'Schofield telegraph "construction corps" operators North Carolina Eckert'),
 ('E551', 'Berrien "Rhode Island" "Cape Henry" patrol'), ('E551', 'Berrien vessels patrol "Cape Fear" troops moving south'),
 ('E552', 'Dumbarton "Commodore Bell" "James River"'), ('E552', 'Dumbarton Cambridge Berrien Tuesday')]
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
