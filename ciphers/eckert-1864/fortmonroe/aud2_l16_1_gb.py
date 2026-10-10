#!/usr/bin/env python3
"""AUD2-LEDGER16-1 (10 Oct 2026), second audit of E506 E508 E509 E511 E514 E521: Google Books API, keyed, country=US, key never printed;
>= 1.6 s apart. Fresh queries, aimed at The Papers of Ulysses S. Grant vol. 13's index entries (person names with telegram dates) and at
any other book; prints the title and snippet of the first 6 items. A miss is a search result, not a novelty verdict (rule 10)."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
Q = [l.strip() for l in open(sys.argv[1]) if l.strip()]
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90)); its = d.get('items', []) or []
        print('GB |', q, '| total', d.get('totalItems'))
        for i in its[:6]:
            v = i.get('volumeInfo', {}); s = re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))
            print('   ', ('GRANT-PAPERS vol %d' % GP[i['id']]) if i['id'] in GP else i['id'], '|', (v.get('title') or '')[:70], v.get('publishedDate', ''), '::', s[:420])
    except Exception as ex: print('GB |', q, '| ERR', str(ex)[:80])
    time.sleep(float(os.environ.get("GAP", "1.6")))
