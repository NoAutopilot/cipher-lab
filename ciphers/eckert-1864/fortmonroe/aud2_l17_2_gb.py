#!/usr/bin/env python3
"""AUD2-LEDGER17-2 (10 Oct 2026): Google Books API queries for E591 (Grant Papers 13) and E594 (Sherman memoirs, John Sherman's
Recollections, Grant Papers 14). Keyed (GOOGLE_BOOKS_KEY, never printed), country=US, 2 s apart, stops at the first 429/503 after one
retry after 25 s. A miss is a search result, not a novelty verdict (rule 10). Usage: aud2_l17_2_gb.py > aud2_l17_2_gb.out"""
import json, os, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = [
 ('control', '"six vessels" Oriental', ''),
 ('E591 GP13', '"torpedoes" Radford Lynch', 'mnRjmhe3QLoC'),
 ('E591 GP13', '"Radford" "New Ironsides" February 1865', 'mnRjmhe3QLoC'),
 ('E591 GP13', '"submarine torpedoes"', 'mnRjmhe3QLoC'),
 ('E591 GP13 alt', '"torpedoes" Radford', 'ij8fAQAAMAAJ'),
 ('E591 all', '"no torpedoes on hand"', ''),
 ('E591 all', '"twenty submarine torpedoes"', ''),
 ('E594 all', '"going to see General Grant at City Point"', ''),
 ('E594 all', '"from Old Point on Wednesday"', ''),
 ('E594 all', '"by way of Newbern" Sherman Goldsboro 1865 "Old Point"', ''),
 ('E594 all', '"John Sherman" telegram brother "City Point" "March 27" 1865', ''),
 ('E594 all', '"Senator Sherman" "City Point" "Goldsboro" brother telegram Fortress Monroe', ''),
 ('E594 all', 'John Sherman Recollections "City Point" "my brother" Goldsboro 1865', ''),
]
def get(u):
    r = urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'})
    with urllib.request.urlopen(r, timeout=40) as f: return json.load(f)
for lab, q, vid in Q:
    qq = q
    u = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': qq, 'country': 'US', 'maxResults': 10, 'key': K})
    if vid: u = f'https://www.googleapis.com/books/v1/volumes/{vid}?country=US&key={K}'.replace('?','?')  # placeholder, replaced below
    if vid:
        # search inside one volume: q with the volume id filter is not supported; use the volumes endpoint q + filter by id
        u = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': qq, 'country': 'US', 'maxResults': 40, 'key': K})
    for attempt in (1, 2):
        try:
            d = get(u); break
        except Exception as e:
            code = getattr(e, 'code', str(e))
            print(lab, '|', q, '| HTTP', code, '(attempt', attempt, ')'); sys.stdout.flush()
            if attempt == 1: time.sleep(25); continue
            print('STOP at first unrecovered error'); sys.exit(0)
    items = d.get('items', [])
    if vid: items = [i for i in items if i.get('id') == vid]
    print(lab, '|', q, '| total', d.get('totalItems'), '| shown', len(items))
    for i in items[:10]:
        vi = i.get('volumeInfo', {}); s = i.get('searchInfo', {}).get('textSnippet', '')
        print('   ', i.get('id'), '|', vi.get('title', '')[:70], '|', vi.get('publishedDate'), '|', ' '.join(s.split())[:300])
    sys.stdout.flush(); time.sleep(2)
