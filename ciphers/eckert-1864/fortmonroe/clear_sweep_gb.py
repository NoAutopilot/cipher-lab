#!/usr/bin/env python3
"""CLEAR-SWEEP (10 Oct 2026, for LANE LEDGER-15): Google Books API (keyed, country=US) one phrase query per 1865 entry (24) plus the in-volume control used by FV-L15d
('"Suwo Nada" "half an hour" intitle:Grant' -> Grant Papers vol. 13). A hit = a result whose id is one of the Grant Papers 13/14 ids. >= 1.6 s apart, <= 26 requests; never prints the key."""
import json, os, sys, time, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.argv = sys.argv[:1]
from clear_sweep_beapi_phrases import P
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
IDS = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ', 'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
E65 = [e for e in P if e in 'E509 E511 E514 E518 E526 E527 E542 E543 E546 E548 E550 E553 E554 E558 E562 E564 E566 E569 E571 E574 E577 E506 E508 E521'.split()]
jobs = [('CTRL', '"Suwo Nada" "half an hour" intitle:Grant')] + [(e, '"' + P[e] + '" intitle:Grant') for e in E65]
n = 0
for e, q in jobs:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); n += 1
        its = d.get('items', []); hit = [it['id'] for it in its if it['id'] in IDS]
        print(e, '|', q, '| total', d.get('totalItems'), '| GRANT HIT ' + ','.join(hit) if hit else '| no Grant 13/14 hit')
        for it in its[:4]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('    ', it['id'], v.get('title', '')[:60], v.get('publishedDate'), '|', s[:200])
    except Exception as ex: print(e, '|', q, '| ERR', str(ex)[:80]); n += 1
    sys.stdout.flush(); time.sleep(1.7)
print('# requests', n)
