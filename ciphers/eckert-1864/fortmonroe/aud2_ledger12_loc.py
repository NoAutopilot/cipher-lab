#!/usr/bin/env python3
"""AUD2-LEDGER-12 (9 Oct 2026, account 4): Chronicling America on www.loc.gov, advanced form (dl=page, start_date/end_date, qs), which
honours the date window (the plain q/dates form in aud2_ledger12_net.py did not: its results span the year). Prints each window's returned
date range as its own validation, then the page hits. >= 2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('Grant Monroe Greyhound', '1864-08-27', '1864-09-03'), ('Grant "Fortress Monroe" Mrs', '1864-08-27', '1864-09-03'),
     ('Perit Monroe', '1864-11-05', '1864-11-14'), ('"Ninth Vermont" Monroe', '1864-11-05', '1864-11-14'),
     ('"Ninth Vermont" New York', '1864-11-05', '1864-11-14')]
n = 0
for qs, a, b in Q:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode(
        {'dl': 'page', 'start_date': a, 'end_date': b, 'ops': 'AND', 'qs': qs, 'searchType': 'advanced', 'fo': 'json', 'c': 20,
         'at': 'results,pagination'})
    for attempt in (1, 2):
        try:
            n += 1
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90)); break
        except Exception as e:
            print('ERR', qs, str(e)[:100]); d = None; time.sleep(8)
    if not d: continue
    res = d.get('results', [])
    dates = sorted({r.get('date', '') for r in res})
    print('##', qs, a, b, '|', d.get('pagination', {}).get('of'), 'hits; returned dates', dates[:1], '..', dates[-1:])
    for r in res:
        print('   ', r.get('date'), '|', (r.get('partof_title') or [''])[0][:55], '|', r.get('id'))
    time.sleep(2)
print('requests', n)
