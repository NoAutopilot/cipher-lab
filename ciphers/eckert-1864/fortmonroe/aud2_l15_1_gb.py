#!/usr/bin/env python3
"""AUD2-LEDGER15-1 (10 Oct 2026): Google Books (keyed, country=US, never prints the key) on Grant Papers 13/14 for the second audit of
E555 and E541 (vol. 13, not on IA) and E568 (vol. 14 also searched in full text on IA, aud2_l15_1_beapi*.out): phrases, names and numbers
FV-L15a did not query; a hit = a snippet from one of FIX-FM65's four volume ids. 1.6 s apart. Writes aud2_l15_1_gb.out. A miss is a
search result, not a novelty verdict (rule 10)."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l15_1_gb.out')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
Q = [('ctl', '"six vessels" Oriental intitle:Grant'), ('E555', '"Blodget" Annapolis ice intitle:Grant'),
     ('E555', '"Meagher\'s division" intitle:Grant'), ('E555', 'Rucker "Schofield\'s corps" intitle:Grant'),
     ('E555', '"Twenty-third Corps" Rucker Annapolis intitle:Grant'), ('E555', '"2,500" Rucker "to-morrow morning" intitle:Grant'),
     ('E555', '"staff officers" "mule teams" intitle:Grant'), ('E555', 'Halleck "Fort Monroe" "Feb. 9" Rucker intitle:Grant'),
     ('E541', 'Stromboli intitle:Grant'), ('E541', 'Lynch torpedoes "St. Lawrence" intitle:Grant'),
     ('E541', '"Nevada" Rucker recruits intitle:Grant'), ('E568', '"O\'Brien" telegraph Wilmington Goldsboro intitle:Grant'),
     ('E568', '"construction parties" telegraph Schofield intitle:Grant')]
with open(OUT, 'w') as f:
    for e, q in Q:
        url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60)); its = d.get('items', []) or []
            g = [(GP[i['id']], re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))) for i in its if i.get('id') in GP]
            f.write(f'GB {e} | {q} | total {d.get("totalItems")} | grant-papers {len(g)}\n')
            for v, s in g: f.write(f'      vol {v} :: {s[:400]}\n')
        except Exception as ex: f.write(f'GB {e} | {q} | ERR {type(ex).__name__} {str(ex)[:60]}\n')
        f.flush(); time.sleep(1.6)
    f.write(f'requests {len(Q)}\n')
print(open(OUT).read())
