#!/usr/bin/env python3
"""FM-S65A (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM-S65A rows: whole-collection (no identifier) queries on the readable
clauses plus Grant Papers 13-14 and Butler Corr. V by identifier where known. >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None,'Suwo Nada'),
 (None,'Sheldon Fort Monroe River Queen left Butler on board gone up the James Beckwith City Point January 1865'),
 (None,'Illinois goes to sea eleven o\'clock 1200 men Rawlins Morgan Beckwith January 1865'),
 (None,'Grover forty rounds of ammunition shall I take more Rawlins Beckwith January 1865'),
 (None,'nothing has arrived today and the end is not yet Rawlins Morgan'),
 (None,'wait at Monroe until I get there General Palmer Eckert Grant January 1865'),
 (None,'Ord Foster relieve Grant January 6 1865 either will be good Beckwith'),
 ('papersofulyssess0014gran','Grover rounds ammunition Rawlins January 1865'),
 ('papersofulyssess0014gran','Palmer Monroe wait Grant Washington January 1865'),
 ('papersofulyssess0014gran','River Queen Illinois January 1865'),
 ('papersofulyssess0014gran','Foster relieve Ord Sheldon January 6 1865'),
 ('papersofulyssess0014gran','Savannah Stanton Draper Sheridan instructions January 5 1865')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:4]:
            f = h.get('fields', {}) or {}
            print('   ', f.get('identifier'), (f.get('title', '') or '')[:60] if isinstance(f.get('title', ''), str) else '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('      ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
