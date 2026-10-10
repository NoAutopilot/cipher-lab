#!/usr/bin/env python3
"""CLEAR-SWEEP (10 Oct 2026, for LANE LEDGER-15): IA be-api full-text phrase query per entry (whole collection, no identifier), then for the Feb-Mar 1865 entries the
same phrase restricted to papersofulyssess0014gran (Grant Papers 14). Positive control first: '"Suwo Nada"' (OR I/46 pt 2). >= 1.8 s apart, <= 60 requests.
A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
P = {'E509': 'hospital boat Metropolis', 'E511': 'Eliza Hancox', 'E514': 'Blackstone can be dispensed with', 'E518': 'Elias Smith', 'E526': 'no other vessels of forage',
 'E527': 'I think I will resign', 'E542': 'Saugus left this morning', 'E543': 'return to your headquarters in the field', 'E546': 'Ship ordered to Portsmouth',
 'E548': 'boat passes Point Lookout', 'E550': 'important despatches for him from General Sherman', 'E553': 'General Vogdes', 'E554': 'investigation can progress',
 'E558': 'office at Yorktown', 'E562': 'greatest rascal should escape', 'E564': 'entirely out of pilots', 'E566': 'First Mounted Rifles', 'E569': 'want the room',
 'E571': 'Glisson says he will send', 'E574': 'go on board the boat on arrival', 'E577': 'General Hartsuff', 'E506': 'steamers named in your dispatch',
 'E508': 'ten days coal', 'E521': 'don\'t mention that I enquired', 'E441': 'dread the necessity of cables', 'E472': 'forage him by the other line',
 'E465': 'none of the New Orleans troops', 'E447': 'six miles above City Point', 'E442': 'one mile of cable', 'E474': 'General Butler\'s fleet left',
 'E471': 'send no ciphers till the cable is repaired', 'E470': 'Mahopac, Canonicus and Saugus', 'E468': 'meet you at Monroe tomorrow',
 'E443': 'yellow fever is prevailing', 'E473': 'stop your exchanges', 'E445': 'City of Hendron', 'E469': 'heavy and continuous firing',
 'E466': 'believe a word against him', 'E446': 'operator at Cherrystone', 'E448': 'wharf when the Manhattan arrives'}
G14 = ['E548', 'E550', 'E553', 'E554', 'E558', 'E562', 'E564', 'E566', 'E569', 'E571', 'E574', 'E577']
jobs = [('CTRL', '', 'Suwo Nada')] + [(e, '', p) for e, p in P.items()] + [(e, 'papersofulyssess0014gran', P[e]) for e in G14]
n = 0
for e, ident, ph in jobs:
    u = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': '"' + ph + '"', **({'identifier': ident} if ident else {})})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90)); n += 1
        h = d.get('hits', {}); hits = h.get('hits', []) if isinstance(h, dict) else h
        tot = h.get('total') if isinstance(h, dict) else len(hits)
        print(f'## {e} | {ident or "ALL"} | "{ph}" | total {tot}')
        for x in hits[:6]:
            f = x.get('fields', {}); hl = x.get('highlight', {})
            print('    ', f.get('identifier'), '|', str(f.get('title'))[:60], '|', ' '.join(' '.join(v) if isinstance(v, list) else str(v) for v in hl.values())[:240].replace('\n', ' '))
    except Exception as ex:
        print(f'## {e} | {ident or "ALL"} | "{ph}" | ERROR {ex}'); n += 1
    sys.stdout.flush(); time.sleep(1.9)
print('# requests', n)
