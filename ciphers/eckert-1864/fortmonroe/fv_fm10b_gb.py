#!/usr/bin/env python3
"""FV-FM10b (9 Oct 2026): Google Books API phrase queries (G3) on E319-E321's decoded phrases; key from GOOGLE_BOOKS_KEY, country=US,
>= 2 s apart, stop on 429. Prints hit counts and titles only. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
Q = ['"navigation must remain open for vessels"', '"some of which have high masts"', '"string wire across"  Mattapony',
     '"regret having ordered" OBrien', '"Caldwell will attend to all cipher work"', '"dragged up by anchors" cable',
     '"nearest the south shore" cable Caldwell']
k = os.environ.get('GOOGLE_BOOKS_KEY', ''); n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10}) + ('&key=' + k if k else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60)); n += 1
    except Exception as e:
        n += 1; print(q, '| ERROR', str(e)[:60]); 
        if '429' in str(e): break
        continue
    items = d.get('items', [])
    print(q, '|', d.get('totalItems'), '|', '; '.join((i['volumeInfo'].get('title', '')[:50] + ' ' + str(i['volumeInfo'].get('publishedDate', ''))) for i in items[:5]))
    time.sleep(2)
print('requests', n)
