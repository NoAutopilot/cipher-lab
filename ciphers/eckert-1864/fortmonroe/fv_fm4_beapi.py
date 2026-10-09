#!/usr/bin/env python3
"""FV-FM4 (9 Oct 2026): IA be-api full-text search (snippet only) of named volumes for E193/E194 phrases, >= 1.6 s apart, and one
Google Books probe per entry (country=US, key from the environment, never printed). A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('papersofulyssess0012gran', '"sick prisoners"'), ('papersofulyssess0012gran', '"5,700"'), ('papersofulyssess0012gran', 'Langdon'),
     ('papersofulyssess0012gran', '"letter of instructions"'), ('warofrebellion422unit', '"sick prisoners"'), ('warofrebellion422unit', '"5,700"'),
     ('warofrebellion432unit', '"letters of instructions"'), ('warofrebellion432unit', '"letter of instructions"')]
n = 0
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, q, len(hits))
        for h in hits[:6]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:4]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, q, 'ERR', e)
    n += 1; time.sleep(1.6)
k = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in ['"sick prisoners to be exchanged at some point"', '"open your own letter of instructions"']:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'key': k})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        print('GB', q, d.get('totalItems'), [i['volumeInfo'].get('title') for i in d.get('items', [])[:5]])
    except Exception as e: print('GB', q, 'ERR', str(e)[:80]); break
    time.sleep(1.6)
print('be-api requests', n)
