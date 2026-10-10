#!/usr/bin/env python3
"""AUD2-LEDGER17-3 (10 Oct 2026): Chronicling America (loc.gov JSON) for E623, the arrest of W. W. Shore, New York World correspondent,
Baltimore / Fort Monroe, May 1864. 2 s apart, <= 12 requests; a miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('Butler', '1864-05-01/1864-05-31'),   # control: Butler in the May 1864 press must hit
     ('"Shore" "World" correspondent Butler', '1864-04-01/1864-07-31'),
     ('"Shore" correspondent arrested Baltimore', '1864-04-01/1864-07-31'),
     ('"W. W. Shore"', '1863-01-01/1866-12-31'),
     ('Shore "World" correspondent Fortress Monroe', '1864-01-01/1864-12-31'),
     ('correspondent "New York World" arrested Butler', '1864-04-15/1864-06-15')]
n = 0
for q, dates in Q:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode({'q': q, 'dates': dates, 'fo': 'json', 'c': 25, 'at': 'results,pagination'})
    for attempt in (1, 2):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
            res = d.get('results', [])
            print('Q', q, dates, '| total', (d.get('pagination') or {}).get('of'), '| shown', len(res))
            for r in res[:12]:
                print('   ', r.get('date'), '|', (r.get('title') or '')[:70], '|', r.get('id') or r.get('url'))
            break
        except Exception as e:
            n += 1; print('Q', q, '| ERR', attempt, str(e)[:120])
            if attempt == 1: time.sleep(25)
    time.sleep(2)
print('loc.gov requests', n)
