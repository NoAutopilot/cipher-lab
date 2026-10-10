#!/usr/bin/env python3
"""AUD2-LEDGERN2-3 (10 Oct 2026, account-4): G3 decoded-phrase pass on Google Books, phrases not run by FV-N2c. Key from env, country=US,
never printed. Positive control first. >= 1.6 s apart. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"requisite ammunition and supplies with the column"',
     '"escort at Martinsburg" paymasters', '"funds for the payment of the Nineteenth"', '"paymasters" "Nineteenth Corps" escort Martinsburg October 1864',
     'Brice "acting paymaster general" Forsyth escort', '"Relay House" paymasters Sheridan December 1864', '"paymasters may be sent"',
     '"notified by telegraph in cipher" paymasters', '"unpaid since the 31st of August" 1864', '"two regiments of the Sixth Corps" unpaid',
     '"paymasters will leave to-morrow" "City Point"', 'Brice Meade paymasters "Sixth Corps" December 1864']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        it = d.get('items', [])
        print(q, '|', d.get('totalItems'), 'total |', len(it))
        for v in it[:6]:
            vi = v.get('volumeInfo', {}); sn = (v.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', v['id'], '|', vi.get('title', '')[:70], vi.get('publishedDate', ''), '|', v.get('accessInfo', {}).get('viewability'), '|', sn[:200])
    except Exception as e: print(q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
