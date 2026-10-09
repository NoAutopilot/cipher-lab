#!/usr/bin/env python3
"""AUD2-LEDGER-31 (9 Oct 2026): Chronicling America (loc.gov JSON) by date window for E346's affair (Keith, Halifax, locomotives, Gordon Bruce,
Norris). >= 2 s apart. OCR- and rank-dependent: a miss is a weak search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
CA = [('Keith Halifax locomotives', '1864-08-01/1864-09-30'), ('Gordon Bruce', '1864-08-01/1864-09-30'), ('Keith rebel agent Halifax', '1864-08-01/1864-09-30'),
      ('Norris locomotives Halifax', '1864-08-01/1864-10-31'), ('Keith machinery Montreal', '1864-08-01/1864-10-31')]
n = 0
for q, dr in CA:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=' + dr + '&q=' + urllib.parse.quote(q), headers=UA), timeout=90))
    except Exception as e:
        d = {'_err': str(e)[:100]}
    n += 1; time.sleep(2)
    print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'), flush=True)
    for r in (d.get('results') or [])[:12]:
        print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:70], '|', r.get('id', '')[-60:], flush=True)
print('requests', n)
