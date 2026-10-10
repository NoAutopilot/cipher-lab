#!/usr/bin/env python3
"""AUD2-LEDGERN2-3 (10 Oct 2026): Grant Papers vol. 13 (Nov 1864-Feb 1865) is not on IA (papersofulyssess0013gran does not exist: metadata empty,
'Nashville'/'Butler' 0 -- aud2_n2_3_vol13.out), so FV-N2c's vol. 13 be-api zeros are non-tests. Google Books snippet search reaches vol. 13 (LS4-V2a,
N2-BX). Positive control first ('"come this way if possible on your return"'). Key from env, country=US, never printed. >= 1.6 s apart."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
T = ''  # intitle: filter returned 0 even for the control (first run, aud2_n2_3_gb13.out top); plain queries, Grant Papers hits read from titles
Q = [T + '"come this way if possible on your return"', T + 'Brice paymasters Grant', T + 'Brice paymaster December 1864', T + '"Relay House" paymasters',
     T + 'paymasters "Sixth Corps" unpaid', T + 'paymasters Meade "City Point" December 1864 Brice', T + 'Brice Sheridan paymasters',
     T + '"acting paymaster general"', T + 'Brice "Nineteenth Corps" escort Martinsburg']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        it = d.get('items', [])
        print(q, '|', d.get('totalItems'), 'total |', len(it))
        for v in it[:8]:
            vi = v.get('volumeInfo', {}); sn = (v.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', v['id'], '|', vi.get('title', '')[:40], vi.get('subtitle', '')[:40], vi.get('publishedDate', ''), '|', v.get('accessInfo', {}).get('viewability'), '|', sn[:240])
    except Exception as e: print(q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
