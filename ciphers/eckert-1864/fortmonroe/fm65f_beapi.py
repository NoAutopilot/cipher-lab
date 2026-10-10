#!/usr/bin/env python3
"""FM65-F (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM65-F rows (Jan 1865): OR I/46-47 pts 1-3 (not in the local
cache), Butler Corr. V, Grant Papers 13 and whole-collection queries (no identifier). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
OR = []
Q = [(None, '"I have joined the" Sumner "mounted rifles" Emerick Sheldon'),
     (None, '"flat cars sent here at once" Wright commence work Beckwith'),
     (None, '"double line from Morehead City to Goldsboro" Eckert Sheldon'),
     (None, '"very essential objection" "moving office" Eckert Sheldon'),
     (None, '"Captain Glisson" "Convoy is now ready" Rawlins Beckwith'),
     (None, '"Champion arrived" Wilmington Fayetteville Sherman scouts Eckert Sheldon'),
     (None, '"no news of the Montauk" Eckert Hurlbut Kinston'),
     (None, '"name of boat is" Sheldon Eckert Dealy Windsor'),
     (None, '"how much water can your" gunboats Gordon Emerick Beckwith'),
     (None, '"Broad Ford is the best place" Boyle guide Blackwater Gordon Emerick'),
     (None, '"you will therefore not be relieved" Gordon Emerick Hartsuff'),
     (None, '"relative to barges" Morehead City "no exertions will be spared" Eckert James'),
     (None, '"Sherman occupied Goldsboro" Sinclair Tribune Elias Smith'),
     ('privateofficialc05butl', 'Sheldon Emerick Gordon Boyle Blackwater Suffolk'),
     ('papersofulyssess0014gran', 'Sheldon Beckwith Emerick Gordon Blackwater'),
     ('warofrebellion014702rootrich', 'Gordon Emerick Boyle Blackwater Suffolk guide')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:4]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('   id', src.get('identifier') or h.get('_id'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
