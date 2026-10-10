#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026): follow-up Google Books API queries (keyed, country=US; never prints the key; 1.6 s apart) after fv_l15b_gb.out:
E567's hit in Grant Papers vol. 14 (header, source line), E545's near-miss in vol. 13 (whose telegram, what date), E572 press wording."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"None have arrived at this place" intitle:Grant', '"Col Wright can commence work" intitle:Grant', '"flat cars sent here at once" intitle:Grant',
     '"Wright can commence work" Newbern intitle:Grant', '"two engines and some flat cars" Schofield telegram received',
     '"be left behind" Schofield batteries intitle:Grant', '"to be fitted up here if necessary" intitle:Grant', '"Mitten Collection" Schofield batteries intitle:Grant',
     '"one battery" Schofield division intitle:Grant', '"let the others follow" intitle:Grant', '"mules" "from Kentucky" Schofield intitle:Grant',
     '"the Champion" Wilmington Sherman Fayetteville scouts 1865 newspaper', '"reached Fayetteville" Champion "Fortress Monroe"']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 6, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        print(q, '| total', d.get('totalItems'))
        for it in d.get('items', [])[:6]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('   ', it.get('id'), (v.get('title') or '')[:50], v.get('publishedDate'), it.get('accessInfo', {}).get('viewability'), '|', s[:500])
    except Exception as ex: print(q, '| ERR', str(ex)[:80])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
