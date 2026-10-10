#!/usr/bin/env python3
"""L14-B: IA be-api full-text, whole collection (no identifier), one or two exact-phrase queries per row not located in the cached OR set. 1.6 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('E611 9733/1','"daily shipments of forage to Monroe"'),('E611 9733/1','"consign this forage to Colonel Biggs"'),
     ('E612 9883/0','"not satisfied with your conduct" "Captain Ferry" Memphis'),('E612 9883/0','"Captain Ferry to Memphis" "Robert Allen"'),
     ('E613 9802/1','"find a place for an officer of so high rank"'),('E613 9802/1','"Carl Schurz" Gillem Johnson Nashville 1864 telegram'),
     ('E614 9874/2','"suspended by my telegraphic dispatch" supplies "Hilton Head"'),('E614 9874/2','"held afloat for instant transfer"'),
     ('E617 9686/2','"will exercise authority over any troops not within the limits of your department"'),('E617 9686/2','"assuming command of troops outside of such boundaries"')]
for row, q in Q:
    u = 'https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&size=10'
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
    except Exception as e: print(row, q, 'ERR', str(e)[:100], flush=True); time.sleep(25); continue
    h = d.get('hits', {}); hs = h.get('hits', []) if isinstance(h, dict) else h
    print(row, q, '| total', h.get('total') if isinstance(h, dict) else len(hs), '|', ' || '.join(f"{(x.get('fields') or x.get('_source') or {}).get('identifier')}: " + ' / '.join(t.replace(chr(10),' ')[:160] for t in x.get('highlight', {}).get('text', [])[:1]) for x in hs[:5]), flush=True)
    time.sleep(1.6)
