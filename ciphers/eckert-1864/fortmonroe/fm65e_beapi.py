#!/usr/bin/env python3
"""FM65-E (10 Oct 2026, account 1): IA be-api full-text snippet queries (no identifier = whole collection; plus ORN I/11-12, Grant Papers 13-14, Butler Corr. V),
short quoted phrases from the readable clause of each filed candidate; control 'Fort Fisher'. >= 1.8 s apart. A miss is a search result, not print status (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None,'"Fort Fisher" Beckwith')]
Q += [(None, q) for q in [
 '"exclusive of the Rhode Island"',                      # 5898/1
 '"Dumbarton" "Cambridge" available Tuesday next',       # 5899/0
 '"Vogdes" "Eastern District" Gordon Commission investigation',  # 5902/1, 5902/2
 '"investigation can progress quietly"',                 # 5902/2
 '"Meagher" Schofield Rucker Annapolis "mule teams" ambulances',  # 5904/1
 '"torpedoes" Lynch "Bureau" "ultimo" "immediate use"',  # 5907/1
 '"anxious inquiry" office Yorktown operators',          # 5912/1
 '"station be established at Yorktown"',                 # 5915/0
 '"I sent for Johnson" "turn State evidence"',           # 5917/1
 '"greatest rascal should escape"',                      # 5917/1
 '"Wilder" "Plato" "moneys" negroes "public property"',  # 5918/0
 '"out of pilots" monitors James River',                 # 5918/1
 '"Roberts" "139th New York" Bowers scout',              # 5919/1
]]
for ident in ['officialrecordso0011unse','officialrecordso0012unse','papersofulyssess0013gran','papersofulyssess0014gran','privateofficialc05butl']:
    for q in ['Dumbarton Cambridge', 'Vogdes Gordon commission', 'Lynch torpedoes', 'pilots monitors', 'Wilder Plato']:
        Q.append((ident, q))
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:5]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('   id', src.get('identifier') or h.get('_id'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
