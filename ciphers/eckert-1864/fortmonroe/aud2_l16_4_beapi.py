"""AUD2-LEDGER16-4 (10 Oct 2026): IA be-api full-text queries (whole collection, or one identifier), 1.8 s apart, one retry after 25 s on 5xx.
Usage: python3 aud2_l16_4_beapi.py > aud2_l16_4_beapi.out"""
import json, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
Q = [
 ('"Suwo Nada"', None),                               # control (OR I/46 pt 2)
 ('Eckert', 'papersofulyssess0010gran'),              # does Grant Papers vol. 10 exist on IA with fts
 ('"heavy and continuous firing"', 'papersofulyssess0010gran'),
 ('"how wide is the Mattapony"', None),
 ('"dread the necessity"', None),
 ('"office at Gillmore"', None),
 ('"one at Bermuda landing"', None),
 ('"stop your exchanges"', None),
 ('"know of none and do not believe"', None),
 ('"it may be that Grant has reached"', None),
 ('"New Regime" Norfolk 1864 Edgar', None),
]
def get(q, ident):
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)
n = 0
for q, ident in Q:
    for attempt in (1, 2):
        n += 1
        try:
            d = get(q, ident); break
        except Exception as e:
            print('ERR', q, ident, e)
            d = None
            if attempt == 1: time.sleep(25)
    time.sleep(1.8)
    if d is None: continue
    hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
    tot = d.get('hits', {}).get('total') if isinstance(d.get('hits'), dict) else len(hits)
    print('== %s | %s | total %s' % (q, ident, tot))
    for h in hits[:8]:
        f = h.get('fields', h.get('_source', {}))
        hl = h.get('highlight', {})
        print('  ', f.get('identifier'), '|', str(f.get('title'))[:70], '|', str(f.get('year') or f.get('date'))[:10], '|', ' ... '.join(sum(hl.values(), []))[:300].replace('\n', ' '))
print('requests', n)
