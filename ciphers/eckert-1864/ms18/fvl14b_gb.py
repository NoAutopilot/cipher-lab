#!/usr/bin/env python3
"""FV-L14b: Google Books API (keyed, country=US; CLAUDE.md access item 3) exact-phrase queries on the plain clauses of the four not-located entries.
1.6 s apart. Prints title/date/snippet only; a miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
Q = [('E611', '"daily shipments of forage"'), ('E611b', '"barely sufficient for daily wants" forage'),
     ('E612', '"not satisfied with your conduct" Ferry Allen'), ('E612b', '"Captain Ferry" Memphis Allen'),
     ('E620', '"Beverly Tucker will cross"'), ('E620b', '"officer of sufficient discretion" Odell'),
     ('E621', '"arms were sent from here to Harper"'), ('E621b', '"have been delayed on the railroad" Garrett')]
k = os.environ['GOOGLE_BOOKS_KEY']; n = 0
for lab, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': k})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60)); n += 1
        it = d.get('items', [])
        print(lab, '|', q, '|', d.get('totalItems'), flush=True)
        for i in it[:6]:
            v = i['volumeInfo']; print('   ', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', (i.get('searchInfo', {}) or {}).get('textSnippet', '')[:220])
    except Exception as e: n += 1; print(lab, '| ERROR', str(e)[:80])
    time.sleep(1.6)
print('googleapis requests', n)
