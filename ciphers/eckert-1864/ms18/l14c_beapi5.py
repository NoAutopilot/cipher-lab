#!/usr/bin/env python3
"""L14-C be-api round 5: snippet of the 9811/0 phrase inside papersofulyssess0011gran and henryhalleckswar0000ande (round 4 hit ids). >= 2.2 s apart."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for ident in ['papersofulyssess0011gran', 'henryhalleckswar0000ande']:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': '"beg to be excused from deciding"', 'identifier': ident})
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
    print(ident, len(hits))
    for h in hits[:2]:
        for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('   ', ' '.join(s.split())[:500])
    time.sleep(2.2)
