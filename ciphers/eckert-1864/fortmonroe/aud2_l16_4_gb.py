"""AUD2-LEDGER16-4 (10 Oct 2026): Google Books API phrase queries (keyed via GOOGLE_BOOKS_KEY, country=US, never printed), 1.6 s apart.
Usage: python3 aud2_l16_4_gb.py > aud2_l16_4_gb.out"""
import json, os, time, urllib.parse, urllib.request
K = os.environ['GOOGLE_BOOKS_KEY']
Q = ['"Butler favors crossing at Yorktown"',            # control (OR I/36 pt 3 p.322)
     '"New Regime" "Captain Clark" Butler Norfolk',
     '"H. C. Clark" "New Regime"',
     '"Captain Edgar" Armstrong Norfolk 1864',
     '"New Regime" Edgar Armstrong Butler',
     '"heavy and continuous firing" Butler 1864 Grant',
     '"Mattapony" Eckert telegraph Sheldon 1864',
     'Dunn Cherrystone operator disloyal',
     '"Bermuda landing" "City Point" cable telegraph 1864']
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
    except Exception as e:
        print('==', q, 'ERR', type(e).__name__); time.sleep(1.6); continue
    print('== %s | total %s' % (q, d.get('totalItems')))
    for it in d.get('items', [])[:10]:
        v = it['volumeInfo']
        print('   %s | %s | %s | %s' % (it['id'], v.get('title', '')[:70], v.get('publishedDate'), (it.get('searchInfo', {}).get('textSnippet') or '')[:220].replace('\n', ' ')))
    time.sleep(1.6)
