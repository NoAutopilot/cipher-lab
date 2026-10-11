#!/usr/bin/env python3
"""AUD2-FM16e (11 Oct 2026, for LANE DEFAULT-A1-0540): Google Books API (keyed, country=US) fresh phrase queries for E443 E445 E446 E448
(none of fv_l16e_gb.py's), Grant Papers vols. 10-12 and Butler's correspondence III-IV by title word; positive control = FV-L16e's E468 phrase.
Prints every snippet; flags titles naming Grant's or Butler's papers. >= 1.6 s apart; never prints the key. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = [('CTRL', '"meet you and the admiral there" Butler Grant'),
     ('E443', '"prevailing to considerable extent" "yellow fever" 1864'), ('E443', '"thought best to notify you at once" yellow fever'),
     ('E443', 'McDougall "medical director" "yellow fever" "New Berne" October 1864'),
     ('E445', '"have him sent here with his instruments"'), ('E445', 'Baird Porter Butler instruments torpedo December 1864 "Fort Monroe"'),
     ('E446', '"formerly employed in the American" telegraph Baltimore Dunn'), ('E446', '"Dunn" Cherrystone Butler March 1864 operator Titan'),
     ('E446', 'intitle:"Private and Official Correspondence" Butler Cherrystone Dunn'),
     ('E448', '"be at the wharf when the Manhattan"'), ('E448', 'Stanton Manhattan "City Point" "October 15, 1864" Eckert'),
     ('E448', 'intitle:"Papers of Ulysses S. Grant" Stanton Manhattan "City Point" October 1864')]
n = 0
for e, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); n += 1
        its = d.get('items', [])
        print(e, '|', q, '| total', d.get('totalItems'))
        for it in its[:8]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            t = v.get('title', ''); flag = ' <<GRANT/BUTLER' if ('Grant' in t and 'Papers' in t) or 'Official Correspondence' in t else ''
            print('    ', it['id'], t[:70], v.get('publishedDate'), flag, '|', s[:260])
    except Exception as ex: n += 1; print(e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.7)
print('requests', n)
