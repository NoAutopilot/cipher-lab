#!/usr/bin/env python3
"""AUD2-LEDGER16-3 (10 Oct 2026, account 1, second audit; copied from fv_l16c_gb.py): Google Books API (keyed, country=US) phrase pass for E558 E564
E569 E574, fresh queries beyond FIX-FM65's, CLEAR-SWEEP's and FV-L16c's (names and numbers, clear-copy wording where a holder clear copy exists).
Mode 'grant': query + intitle:Grant, report only Grant Papers vols. 13/14 ids. Mode 'g3': the same query unrestricted, top 10 with snippet (G3).
Control first: E531 '"six vessels" Oriental' (FIX-FM65's positive control). >= 1.6 s apart; never prints the key. A miss is a search result."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('CTRL-E531', '"six vessels" Oriental'),
 ('E558', '"telegraph office at Yorktown" 1865'), ('E558', 'Ord Yorktown "telegraph station" February 1865 quartermaster'), ('E558', '"George D. Sheldon" Yorktown operators'),
 ('E564', '"William L. James" pilots monitors'), ('E564', '"two pilots" monitors "Fort Monroe" March 1865'), ('E564', 'Sangamon Montauk pilots "Fort Monroe" quartermaster 1865'),
 ('E569', '"Mrs. Ord" "Fort Monroe" telegraph office 1865'), ('E569', '"Mrs. Ord" Fortress Monroe room headquarters March 1865'), ('E569', 'Sheldon "telegraph office" removal "Fort Monroe" Ord 1865'),
 ('E574', 'Stanton "City Point" March 1865 "River Queen" visit Grant'), ('E574', 'Stanton left Washington "March 15" 1865 "City Point"'), ('E574', '"Dealy" telegraph "Fort Monroe" Stanton'),
 ('E574', 'Stanton visit "City Point" "March 16, 1865"')]
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
