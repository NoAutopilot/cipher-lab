#!/usr/bin/env python3
"""AUD2-LEDGER17-1 (10 Oct 2026; after fv_l17a_gb.py): Google Books API (keyed, country=US, key from the environment, never printed), The Papers of
Ulysses S. Grant vol. 13 (ids mnRjmhe3QLoC / ij8fAQAAMAAJ) and vol. 14 for E585 E581; positive control E531 first; fresh queries (not FM-S65A's or
FV-L17a's). Stops the whole run at the first 429/503 after one retry at 25 s. >= 2 s apart. A miss is a search result, not a novelty verdict."""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
GB = [('CTRL-E531', '"six vessels" Oriental intitle:Grant'),
 ('E585', 'Grover "Second Division" "Nineteenth Corps" Monroe ammunition intitle:Grant'), ('E585', 'Grover "take more" ammunition intitle:Grant'),
 ('E585', '"Grover" "January 15, 1865" Rawlins intitle:Grant'), ('E585', 'Grover Savannah transports Monroe January 1865 ammunition intitle:"Papers of Ulysses"'),
 ('E581', '"River Queen" "January 6" Butler intitle:Grant'), ('E581', 'Butler "River Queen" Beckwith Sheldon intitle:Grant'),
 ('E581', 'Butler relieved "January 8, 1865" "River Queen" intitle:"Papers of Ulysses"')]
n = 0
def call(q):
    global n
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    n += 1
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90))
for e, q in GB:
    try:
        try: d = call(q)
        except urllib.error.HTTPError as ex:
            if ex.code not in (429, 503): raise
            print('GB', e, '|', q, '| HTTP', ex.code, '- one retry after 25 s'); time.sleep(25); d = call(q)
    except urllib.error.HTTPError as ex:
        print('GB', e, '|', q, '| HTTP', ex.code, 'again: run stopped'); break
    except Exception as ex: print('GB', e, '|', q, '| ERR', str(ex)[:80]); continue
    its = d.get('items', []) or []
    g = [(GP[i['id']], re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))) for i in its if i.get('id') in GP]
    print('GB', e, '|', q, '| total', d.get('totalItems'), '| grant-papers', len(g))
    for v, s in g: print('      vol', v, '::', s[:300])
    for i in its[:3]:
        vi = i.get('volumeInfo', {}); print('      top:', (vi.get('title') or '')[:60], vi.get('publishedDate'), '::', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', ''))[:160])
    time.sleep(2)
print('# requests', n)
