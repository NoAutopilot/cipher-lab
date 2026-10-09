#!/usr/bin/env python3
"""FM-R4a (9 Oct 2026): IA be-api full-text search (snippet only) of Grant Papers volumes (10 Jan-May 1864, 11 Jun-Aug, 12 Aug-Nov, 0000unse unnumbered)
for FM-R4a rows' rare words, >= 1.6 s apart, stop on a non-200 after one retry. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0011gran', 'Este'), ('papersofulyssess0011gran', '"Silver Spring" Ricketts'), ('papersofulyssess0011gran', 'Purviance'),
     ('papersofulyssess0011gran', 'Pettus'), ('papersofulyssess0011gran', '"Channing Clapp"'),
     ('papersofulyssess0010gran', 'Montauk'), ('papersofulyssess0010gran', 'Spaulding Hilton Head'),
     ('papersofulyssess0012gran', '"Van Duzer"'), ('papersofulyssess0012gran', 'Sheldon "Fort Monroe" fever'), ('papersofulyssess0012gran', 'Wilcox Hilton Head'),
     ('papersofulyssess0000unse', 'Barton Sheldon'), ('papersofulyssess0000unse', 'Binney Brice'), ('papersofulyssess0000unse', 'Beckwith "Fort Monroe" Barton')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:4]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:6]: print('   ', s.replace('\n', ' ')[:320])
    except Exception as e:
        print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
