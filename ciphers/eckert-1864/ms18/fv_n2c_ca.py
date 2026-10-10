#!/usr/bin/env python3
"""FV-N2c (10 Oct 2026): Chronicling America via loc.gov JSON (press of the day) for the three Brice paymaster telegrams. >= 2 s apart. A miss is a search result."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('paymasters Sheridan escort Martinsburg', '10/20/1864', '10/31/1864'), ('paymasters Relay House', '12/08/1864', '12/20/1864'),
     ('paymasters Sixth Corps City Point', '12/12/1864', '12/24/1864')]
n = 0
for q, a, b in Q:
    dr = a[6:] + '-' + a[:2] + '-' + a[3:5] + '/' + b[6:] + '-' + b[:2] + '-' + b[3:5]
    url = 'https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
        print(q, dr, '|', (d.get('pagination') or {}).get('of'))
        for r in (d.get('results') or [])[:8]:
            print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:60], '|', r.get('id', '')[-60:], '|', str(r.get('description', ''))[:200])
    except Exception as e: print(q, '| ERR', str(e)[:80])
    n += 1; time.sleep(2)
print('chroniclingamerica requests', n)
