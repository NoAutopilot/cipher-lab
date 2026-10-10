#!/usr/bin/env python3
"""FV-L16a (10 Oct 2026): Google Books API (keyed, country=US, key from the environment, never printed) phrase queries for E509 E511 E514 E506
E508 E521 with intitle:Grant, a hit being a snippet from a Grant Papers vol. 13/14 volume id (FIX-FM65's four ids); positive control E531 first;
three fresh queries per entry (names, vessels, numbers; not CLEAR-SWEEP's). >= 1.6 s apart. A miss is a search result, not a novelty verdict."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
GB = [('CTRL-E531', '"six vessels" Oriental intitle:Grant'),
 ('E509', '"Ben De Ford" Webster Dodge intitle:Grant'), ('E509', '"Western Metropolis" Alliance intitle:Grant'), ('E509', 'Ainsworth Montauk Bradley Leary intitle:Grant'),
 ('E511', '"light draft" "Eliza Hancox" intitle:Grant'), ('E511', 'Winants Hancox Rawlins Howell intitle:Grant'), ('E511', '"not over five feet" intitle:Grant'),
 ('E514', '"river steamer" "sea-going" Ingalls Blackstone intitle:Grant'), ('E514', '"medical department" Blackstone Leary intitle:Grant'), ('E514', '"three hundred and fifty" troops transportation Ingalls intitle:Grant'),
 ('E506', 'Rawlins steamers "reported from Jamestown" intitle:Grant'), ('E506', 'Rawlins Howell "named in your dispatch" intitle:Grant'), ('E506', 'steamers Jamestown Beckwith Sheldon January intitle:Grant'),
 ('E508', '"C. C. Leary" Montauk intitle:Grant'), ('E508', '"ten days\' coal" Leary intitle:Grant'), ('E508', 'Leary "City Point" Webster Howell Montauk intitle:Grant'),
 ('E521', 'Beckwith "Butler has left" Monroe intitle:Grant'), ('E521', '"don\'t mention that I" Beckwith intitle:Grant'), ('E521', 'Butler "Fort Monroe" January 6 1865 Beckwith Sheldon intitle:Grant')]
for e, q in GB:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90)); its = d.get('items', []) or []
        g = [(GP[i['id']], re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))) for i in its if i.get('id') in GP]
        print('GB', e, '|', q, '| total', d.get('totalItems'), '| grant-papers', len(g))
        for v, s in g: print('      vol', v, '::', s[:300])
        for i in its[:3]:
            vi = i.get('volumeInfo', {}); print('      top:', (vi.get('title') or '')[:60], vi.get('publishedDate'), '::', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', ''))[:160])
    except Exception as ex: print('GB', e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.6)
