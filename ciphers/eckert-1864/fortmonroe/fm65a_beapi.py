#!/usr/bin/env python3
"""FM65-A (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM65-A rows: whole-collection (no identifier) queries on the readable
clauses plus Grant Papers 13-14 and Butler Corr. V by identifier where known. >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None,'Illinois Sedgwick Victor Baltic ordered Atlantic McClellan Tonowanda Champion Fort Monroe January 1865'),
     (None,'Eliza Hancox Winants light draft steamers not over feet Rawlins wishes held in readiness'),
     (None,'unable to furnish anchor chain in time Baltic will not be sent on the expedition Sampson Baltimore'),
     (None,'ordered the steamers Leary Ariel Victor to report to Colonel Newport Ingalls consumed all surplus transportation'),
     (None,'Rawlins directs me to inform you steamers coaling watering turn them over to Colonel Morgan commissary Chattahoochee'),
     (None,'Euterpe Livingston Varuna Prometheus Idaho DeMolay McClellan Champion Weybossett Towanda Colonel Bradley'),
     (None,'Rawlins wishes to know if the steamers named have started yet Jamestown Beckwith Sheldon'),
     (None,'Leary is just in leaves immediately for City Point Montauk we need her here Howell'),
     (None,'Montauk is there Bendford not here Ainsworth has copy Alliance hospital boat Sheldon O\'Brien'),
     ('papersofulyssess0013gran','Fort Monroe January 3 1865 Beckwith Sheldon steamers Howell'),
     ('papersofulyssess0013gran','Berrien launches large boats Webster Fortress Monroe'),
     ('privateofficialc05butl','Sheldon Fort Monroe January 1865 transports Beckwith')]
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
