#!/usr/bin/env python3
"""FV-FM65b (10 Oct 2026, account 1; copy of fm65a_beapi.py): IA be-api full-text snippet search, whole collection (no identifier, which
covers Grant Papers vols 13-14 and the digitised press where IA holds them), quoted decoded phrases of E502 E507 E512 E520 E530 E532 plus one
positive control (a sentence printed in OR I/46 pt 2). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None,'"Steamers all ready coaled and loaded with proper rations"'),
     (None,'"turn them over to Colonel Morgan"'),
     (None,'"what number of troops each steamer"'),
     (None,'"all the steamers named had left"'),
     (None,'"if the steamer Russia is at"'),
     (None,'"in time for a flag ship"'),
     (None,'"Eliza Hancox has already been sent"'),
     (None,'"Winants is hardly capable"'),
     (None,'"have the Winants in order"'),
     (None,'"were all ordered to Baltimore"'),
     (None,'"except the Baltic which was at Baltimore"'),
     (None,'"have sailed in perfect order" Ashland'),
     (None,'"what time can this transportation"'),
     (None,'"mule teams complete" Bradley')]
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
