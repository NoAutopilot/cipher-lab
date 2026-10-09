#!/usr/bin/env python3
"""FV-FM6b (9 Oct 2026): IA be-api full-text search (snippet only) of named volumes for E228/E229/E240/E241 phrases, >= 1.6 s apart, and one
Google Books probe per entry (country=US, key from the environment, never printed; stop on 429). A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0010gran', 'Hicksford'), ('papersofulyssess0010gran', '"Fulton and Craig"'),
     ('papersofulyssess0012gran', '"yellow fever"'), ('papersofulyssess0013gran', 'Pocotaligo'), ('papersofulyssess0013gran', 'Sherman'),
     ('privateofficialc05butl', '"yellow fever"'), ('privateofficialc05butl', 'torpedoes')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, q, len(hits))
        for h in hits[:4]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, q, 'ERR', e)
    n += 1; time.sleep(1.6)
k = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in ['"torpedoes" "invented by Mr. Woods"', '"Pocotaligo bridge" "Herald" Foster 1864 wrong', '"Surgeon D. W. Hand" "yellow fever"', '"Fulton and Craig" 1864']:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'key': k})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        print('GB', q, d.get('totalItems'), [i['volumeInfo'].get('title') for i in d.get('items', [])[:5]])
    except Exception as e: print('GB', q, 'ERR', str(e)[:80]); break
    time.sleep(1.6)
print('be-api requests', n)
