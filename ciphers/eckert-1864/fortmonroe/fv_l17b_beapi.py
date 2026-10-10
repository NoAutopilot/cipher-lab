#!/usr/bin/env python3
"""FV-L17b (10 Oct 2026): IA be-api full-text search, short fresh phrases (not FM-S65B's long ANDed queries), whole collection and Grant Papers 14
(papersofulyssess0014gran). Control first. 2 s apart; one retry after 25 s on 502, then stop. A miss is a search result, not a statement about print."""
import json, time, urllib.parse, urllib.request, sys
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G14 = 'papersofulyssess0014gran'
Q = [(None, '"Wait at Fort Monroe until I get there"'),            # control: OR I/46 pt 2 p.198 (E587)
     (G14, '"Wait at Fort Monroe"'),                                 # G14 control candidate (Jan 1865: likely vol 13, may miss)
     (G14, '"Cashier of the National Bank"'),                        # G14 positive control (FM-S65B snippet, 5914/2)
     (None, '"retained no copy"'), (G14, '"retained no copy"'), (G14, '"staff officer to be delivered"'),
     (None, '"Camman"  gold Norfolk'), (None, '"sell gold" Norfolk 1865'),
     (None, '"ponchos are not on hand"'), (G14, 'ponchos'), (None, '"ponchos" Ingalls'),
     (None, '"Monohansett will leave"'), (G14, 'Monohansett'),
     (None, '"no torpedoes on hand"'), (None, '"forward immediately on receipt"'),
     (None, '"from Old Point on Wednesday"'), (None, '"back to Goldsboro by way of"'), (None, '"I am going to see General Grant"'),
     (G14, '"Old Point" Sherman Goldsboro'), (G14, 'Seward "staff officer"')]
Q = Q[int(sys.argv[1]) if len(sys.argv) > 1 else 0:]
n = 0
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        try: d = get(url); n += 1
        except Exception as e:
            n += 1
            if '502' in str(e) or '503' in str(e): time.sleep(25); d = get(url); n += 1
            else: raise
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:6]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('   id', src.get('identifier') or h.get('_id'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:400])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    time.sleep(2)
print('be-api requests', n)
