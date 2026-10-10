#!/usr/bin/env python3
"""FV-L16a (10 Oct 2026): second, shorter Google Books pass (fv_l16a_gb.py's long ANDed queries returned 0): one or two rare words per entry with
intitle:Grant; keyed, country=US, key never printed; >= 1.6 s apart. A miss is a search result, not a novelty verdict."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
GB = [('E509', '"Ben De Ford" intitle:Grant'), ('E509', '"Western Metropolis" intitle:Grant'), ('E511', '"Eliza Hancox" intitle:Grant'),
      ('E511', 'Winants intitle:Grant'), ('E514', 'Blackstone "medical department" intitle:Grant'), ('E508', '"C. C. Leary" intitle:Grant'),
      ('E506', 'Jamestown steamers Rawlins intitle:Grant'), ('E521', '"has left Fort Monroe" intitle:Grant')]
for e, q in GB:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90)); its = d.get('items', []) or []
        g = [(GP[i['id']], re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))) for i in its if i.get('id') in GP]
        print('GB', e, '|', q, '| total', d.get('totalItems'), '| grant-papers', len(g))
        for v, s in g: print('      vol', v, '::', s[:400])
    except Exception as ex: print('GB', e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.6)
