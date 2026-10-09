#!/usr/bin/env python3
"""AUD2-LEDGER-17 (9 Oct 2026, account 4): Chronicling America on www.loc.gov (advanced form, as aud2_ledger12_loc.py, which honours the
date window) for E267 (date of Stanton's Keyport trip to City Point, Oct 1864) and E269 (York River light vessel, Jul-Aug 1864). The first
query is a positive control (Cedar Creek, 19 Oct 1864, must hit). Prints each window's returned date range, then the hits. >= 2 s apart.
A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('Sheridan "Cedar Creek"', '1864-10-20', '1864-10-24'),
     ('Stanton Keyport', '1864-10-08', '1864-10-22'), ('"Secretary of War" Keyport', '1864-10-08', '1864-10-22'),
     ('"Secretary Stanton" "City Point"', '1864-10-10', '1864-10-22'), ('"Secretary Stanton" "Fortress Monroe"', '1864-10-10', '1864-10-22'),
     ('Stanton Meigs "City Point"', '1864-10-10', '1864-10-22'),
     ('"light vessel" "York river"', '1864-07-20', '1864-08-31'), ('"light ship" "York river"', '1864-07-20', '1864-08-31')]
n = 0
for qs, a, b in Q:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode(
        {'dl': 'page', 'start_date': a, 'end_date': b, 'ops': 'AND', 'qs': qs, 'searchType': 'advanced', 'fo': 'json', 'c': 25,
         'at': 'results,pagination'})
    d = None
    for attempt in (1, 2):
        try:
            n += 1
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)); break
        except Exception as e:
            print('ERR', qs, str(e)[:100])
            if '429' in str(e): print('429: host left'); print('requests', n); sys.exit()
            time.sleep(8)
    if not d: continue
    res = d.get('results', [])
    dates = sorted({r.get('date', '') for r in res})
    print('##', qs, a, b, '|', d.get('pagination', {}).get('of'), 'hits; returned dates', dates[:1], '..', dates[-1:])
    for r in res:
        print('   ', r.get('date'), '|', (r.get('partof_title') or [''])[0][:55], '|', r.get('id'))
    time.sleep(2.2)
print('requests', n)
