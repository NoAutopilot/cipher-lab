#!/usr/bin/env python3
"""FV-MS18j (10 Oct 2026): Google Books (country=US, key) and IA be-api full-text phrase queries on decoded phrases of E351 E355 E356.
A miss is a search result, not a verdict (rule 10). Usage: fv_ms18j_gb.py"""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
GB = ['"Stiner" "Herald" Fox "Fortress Monroe" 1864', '"of what use is it to the northern reader"', '"Goodman" "late Judge Advocate" Olcott',
      '"bring back any witness discharged"', '"habeas corpus in case of minors"', '"by whom the minors" "illegally enlisted"', 'Cluer witness discharged Boston navy yard Olcott 1864']
BE = ['"Stiner" "northern reader"', '"Goodman" "Olcott" "navy yard" 1864', '"habeas corpus" minors Hancock Baltimore 1865']
k = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in GB:
    u = 'https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&maxResults=8&country=US' + (('&key=' + k) if k else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        print(f'GB {q!r}: {d.get("totalItems")}')
        for it in d.get('items', [])[:8]:
            v = it['volumeInfo']; print('   ', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', (it.get('searchInfo') or {}).get('textSnippet', '')[:160].replace('\n', ' '))
    except Exception as e:
        print(f'GB {q!r}: ERROR {type(e).__name__}')
    time.sleep(1.6)
for q in BE:
    u = 'https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(f'BE {q!r}: {len(hits)}')
        for h in hits[:8]:
            s = h.get('_source', h); print('   ', s.get('identifier'), '|', str(s.get('title'))[:60], '|', str((h.get('highlight') or {}).get('text', ''))[:200].replace('\n', ' '))
    except Exception as e:
        print(f'BE {q!r}: ERROR {type(e).__name__}')
    time.sleep(1.6)
