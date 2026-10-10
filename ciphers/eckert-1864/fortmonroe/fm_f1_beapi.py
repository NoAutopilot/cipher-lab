#!/usr/bin/env python3
"""FM-F1 (10 Oct 2026): one IA be-api full-text phrase query WITHOUT identifier (whole collection) per row, on the readable clause, >= 1.9 s apart.
A miss is a search result, not a statement about print (rule 10). Hits are printed with identifier and snippet for hand review."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('5752/0','"Hancock is not near enough to render" Smith any aid'), ('5699/1','"how wide is" Yorktown "West Point" cable poles Eckert Sheldon 1864'),
     ('5707/0','"one mile of cable" City Point Gillmore Williamsburg Jamestown island O\'Brien'), ('5785/1','"yellow fever is prevailing to considerable extent"'),
     ('5799/0','"copy of all dispatches sent north from your office"'), ('5816/2','"Baird will arrive" "with his instruments" Hendron Porter'),
     ('5583/2','"W. A. Dunn" "American office" Baltimore Cherrystone operator Butler'), ('5827/0','Saugus "above City Point" Porter "will start down" Beckwith'),
     ('5793/1','"Manhattan" "Secretary of War" wharf Dealy Eckert Fort Monroe October 1864'), ('5822/2','"Demolay" "leave here at daylight" Sheldon O\'Brien'),
     ('5638/0','"do not believe a word against him" Dunn Butler Eckert'), ('5632/2','"ready to put up at a moment\'s notice" Butler telegraph miles'),
     ('5810/1','"meet you at Monroe tomorrow" Beckwith Butler Grant November 1864'), ('5720/0','"heavy and continuous firing" "fifteen miles" Grant battery O\'Brien May 1864'),
     ('5814/0','Mahopac Canonicus Saugus "ready for service" Porter Butler monitors')]
n = 0
for lab, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(lab, '|', q, '|', len(hits), flush=True)
        for h in hits[:5]:
            print('   ', (h.get('fields', {}) or {}).get('identifier'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', s.replace('\n', ' ')[:260])
    except Exception as e: print(lab, '|', q, '| ERR', str(e)[:100], flush=True)
    n += 1; time.sleep(1.9)
print('be-api requests', n)
