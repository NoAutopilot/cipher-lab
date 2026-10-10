#!/usr/bin/env python3
"""FV-L15a (10 Oct 2026): second Google Books pass (keyed, country=US, never prints the key) on Grant Papers 13/14 for E555 (Grant was at Fort
Monroe on 9 Feb 1865: Rucker's dispatch may sit in a note) and E541/E576; a hit = a snippet from one of FIX-FM65's four volume ids. 1.6 s apart."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
Q = [('E555', 'Rucker "difficulty with ice" intitle:Grant'), ('E555', '"mule teams and wagons" intitle:Grant'), ('E555', '"staff officers" batteries ambulances Annapolis intitle:Grant'), ('E555', 'Schofield Meagher "shipped from" Annapolis intitle:Grant'), ('E555', '"Meagher" Rucker "ambulances" intitle:Grant'),
     ('E555', '"10,000 men" Schofield Rucker February intitle:Grant'), ('E555', '"will sail from here" Rucker intitle:Grant'),
     ('E541', '"Nevada" Webster "City Point" recruits intitle:Grant'), ('E576', 'Ord Blackwater "cannot be forded" Sumner intitle:Grant'),
     ('E576', 'Gordon Boyle fords Blackwater intitle:Grant'), ('E568', 'O\'Brien "Morehead City" Goldsboro line intitle:Grant')]
import sys
if len(sys.argv) > 1: Q = [x for x in Q if x[1] in sys.argv[1:]]
for e, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); its = d.get('items', []) or []
        g = [(GP[i['id']], re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))) for i in its if i.get('id') in GP]
        print('GB', e, '|', q, '| total', d.get('totalItems'), '| grant-papers', len(g))
        for v, s in g: print('      vol', v, '::', s[:300])
    except Exception as ex: print('GB', e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.6)
