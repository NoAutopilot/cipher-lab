#!/usr/bin/env python3
"""FM65-D (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM65-D rows (Jan 1865): OR I/46-47 pts 1-3 (not in the local
cache), Butler Corr. V, Grant Papers 13 and whole-collection queries (no identifier). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
OR = ['warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion463unit', 'warofrebellion471unit', 'warofrebellion014702rootrich', 'warofrebellion014703rootrich']
Q = [(None, '"Fort Fisher is ours" Tribune correspondent Vanderbilt powder magazine explosion'),
     (None, '"Fort Fisher is ours" "New Inlet" assault Terry prisoners Vanderbilt'),
     (None, 'Varina Blair "passed through the lines" Ord Grant Mulford'),
     (None, 'torpedoes "900 pounds" insulating wire Parker Lynch Wise Bureau Ordnance'),
     (None, 'Nevada recruits Rucker Monroe City Point torpedoes Lynch Lawrence'),
     (None, 'Saugus left Monroe Grant needs her Secretary Navy Sheldon'),
     (None, 'Grant "absent several days" Ord "take charge" Army of the James Sheldon'),
     (None, 'Schofield "one battery with each division" Willards Washington Kentucky mules'),
     (None, 'Ship ordered Portsmouth "New Hampshire" "executive officer" detached Parker Sheldon Eckert'),
     (None, 'Stager Schofield cipher operator construction corps North Carolina Sheldon'),
     (None, 'Eckert Bates "President" left Annapolis boat Point Lookout cipher Sheldon'),
     (None, 'Anderson Blodget Schofield Sherman despatches Annapolis Sheldon')]
for ident in OR: Q.append((ident, 'Sheldon Eckert Schofield torpedoes Fort Fisher Terry Vanderbilt'))
Q += [('papersofulyssess0013gran', 'Ord Blair Varina Schofield Kentucky mules'), ('privateofficialc05butl', 'Sheldon Butler Beckwith Monroe')]
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
