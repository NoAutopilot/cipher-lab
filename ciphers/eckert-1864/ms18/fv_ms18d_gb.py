#!/usr/bin/env python3
"""FV-MS18d (9 Oct 2026): Google Books API (country=US, key from env, never printed) and loc.gov (Chronicling America) phrase queries for
E333, E335, E340. A miss is a search result, not a verdict (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GB = ['"Monthny"', '"de Lasalle" Havana spies 1864', '"Portuguese passport" Havana 1864 steamer', '"plot to seize" steamer Havana Dix 1864',
      '"Berrien" Pittsburgh powder Pennock 1864', '"retain it at Pittsburgh"', '"Alberger" Lynchburg 1865 Baker', '"Alberger" "safe key"']
LOC = ['Lasalle Havana spies', 'Monthny', 'plot seize steamer Havana spies', 'Alberger Lynchburg']
for q in GB:
    u = 'https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&maxResults=10&country=US' + ('&key=' + K if K else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        print('GB', q, '|', d.get('totalItems'), '|', ' || '.join(f"{i['id']} {i['volumeInfo'].get('title','')[:50]} {i['volumeInfo'].get('publishedDate','')}: {i.get('searchInfo',{}).get('textSnippet','')[:160]}" for i in d.get('items', [])[:6]), flush=True)
    except Exception as e:
        print('GB', q, '| ERROR', str(e)[:80], flush=True)
    time.sleep(1.6)
for q in LOC:
    u = 'https://www.loc.gov/collections/chronicling-america/?fo=json&dates=1864/1865&q=' + urllib.parse.quote(q)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        r = d.get('results', [])
        print('LOC', q, '|', d.get('pagination', {}).get('of'), '|', ' || '.join(f"{x.get('date')} {str(x.get('title'))[:60]}" for x in r[:6]), flush=True)
    except Exception as e:
        print('LOC', q, '| ERROR', str(e)[:80], flush=True)
    time.sleep(2)
