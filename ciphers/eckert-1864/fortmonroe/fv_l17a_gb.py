#!/usr/bin/env python3
"""FV-L17a (10 Oct 2026; copied from fv_l16a_gb.py): Google Books API (keyed, country=US, key from the environment, never printed) phrase queries for E581 E582 E583 E585
E586 E587 with intitle:Grant, a hit being a snippet from a Grant Papers vol. 13/14 volume id (FIX-FM65's four ids); positive control E531 first;
three fresh queries per entry (names, vessels, numbers; not CLEAR-SWEEP's). >= 1.6 s apart. A miss is a search result, not a novelty verdict."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
GB = [('CTRL-E531', '"six vessels" Oriental intitle:Grant'),
 ('E581', '"River Queen" Butler January Sheldon intitle:Grant'), ('E581', 'Butler "gone up the James" intitle:Grant'), ('E581', 'Beckwith Butler "River Queen" Monroe intitle:Grant'),
 ('E582', 'Foster Ord relieve Stanton "Fort Monroe" intitle:Grant'), ('E582', '"Mrs. Foster" leg relieve intitle:Grant'), ('E582', 'Foster Ord Steele "either" relieve intitle:Grant'),
 ('E583', 'Illinois "go to sea" Morgan Rawlins intitle:Grant'), ('E583', '"Illinois" Grover Newport Baltimore steamer intitle:Grant'), ('E583', '"1287" OR "1,287" men Illinois intitle:Grant'),
 ('E585', 'Grover "forty rounds" OR "40 rounds" ammunition intitle:Grant'), ('E585', 'Grover ammunition Rawlins "Fort Monroe" January intitle:Grant'), ('E585', 'Grover division Savannah ammunition rounds intitle:Grant'),
 ('E586', 'Grover rounds "will answer" Rawlins intitle:Grant'), ('E586', '"need not wait" ammunition Grover intitle:Grant'),
 ('E587', 'Palmer "wait at" Monroe Annapolis intitle:Grant'), ('E587', '"leave Annapolis" Palmer Grant January intitle:Grant'), ('E587', 'Palmer Newbern Monroe "until I get there" intitle:Grant')]
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

