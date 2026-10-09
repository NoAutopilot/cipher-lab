#!/usr/bin/env python3
"""AUD2-LEDGER-12 (9 Oct 2026, account 4): second audits of E219 and E227. (1) IA be-api full-text search (snippet only) of Grant
Papers vol. 12 and Julia Dent Grant's Personal Memoirs (1975; lending-only items, be-api answers without login); (2) Chronicling America
on www.loc.gov (collection JSON), dated windows, each window validated by checking the returned dates. >= 1.6 s apart. A miss is a search
result, not a statement about print (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
BE = [('papersofulyssess0012gran', 'Greyhound'), ('papersofulyssess0012gran', 'Ingalls Webster'),
      ('papersofulyssess0012gran', '"Fort Monroe" Julia'), ('papersofulyssess0012gran', '"Ninth Vt."'),
      ('personalmemoirso1975gran', 'Greyhound'), ('personalmemoirso1975gran', '"Fortress Monroe"'),
      ('personalmemoirso1975gran', '"Fort Monroe"'), ('personalmemoirso1975gran', '"City Point"')]
LOC = [('"Lieutenant General Grant" "Fortress Monroe"', '1864-08-27', '1864-09-03'),
       ('Grant "Fortress Monroe" Greyhound', '1864-08-27', '1864-09-03'),
       ('"Ninth Vermont" "Fortress Monroe"', '1864-11-05', '1864-11-14'),
       ('Perit "Fortress Monroe"', '1864-11-05', '1864-11-14'),
       ('"Ninth Vermont" election New York', '1864-11-05', '1864-11-14')]
n = 0
def get(url):
    global n
    n += 1
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
for ident, q in BE:
    try:
        d = get('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident}))
        hits = d.get('hits', {}).get('hits', [])
        print('be-api', ident, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:8]: print('   ', s.replace('\n', ' ')[:360])
    except Exception as e: print('be-api', ident, '|', q, '| ERR', str(e)[:120])
    time.sleep(1.6)
for q, a, b in LOC:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode(
        {'q': q, 'start_date': a, 'end_date': b, 'dates': a[:4] + '/' + b[:4], 'fo': 'json', 'c': 25})
    try:
        d = get(url)
        res = d.get('results', [])
        dates = sorted({r.get('date', '') for r in res})
        print('loc', '|', q, a, b, '|', d.get('pagination', {}).get('of'), 'results; dates', dates[:3], '..', dates[-3:])
        for r in res[:12]:
            print('   ', r.get('date'), '|', str(r.get('partof_title') or r.get('title'))[:60], '|', r.get('id'))
    except Exception as e: print('loc', '|', q, '| ERR', str(e)[:120])
    time.sleep(1.6)
print('requests', n)
