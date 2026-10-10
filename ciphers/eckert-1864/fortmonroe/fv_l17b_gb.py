#!/usr/bin/env python3
"""FV-L17b (10 Oct 2026; after fm_s65b_gb.py): Google Books API (keyed, country=US, intitle:Grant) snippet search of The Papers of Ulysses S. Grant
vols. 13 (mnRjmhe3QLoC, ij8fAQAAMAAJ; Nov 1864-20 Feb 1865) and 14 (DVLPEPsH1_oC, 1D8fAQAAMAAJ) on short fresh phrases for E589-E594. Control first
(E531 'six vessels' Oriental, vol. 13 hit for FM-S65B). Stops the whole run at the first HTTP 429 or 503 (one retry after 25 s); 1.6 s apart; never
prints the key. A miss is a search result, not a statement about print (rule 10)."""
import json, os, re, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}; V14 = {'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
P = [('CTRL-E531', '"six vessels" Oriental'),
     ('E590', '"retained no copy"'), ('E590', '"hands of a staff officer" Seward'), ('E590', 'Seward "staff officer" letter February 2'),
     ('E589', 'Monohansett'), ('E589', 'Monohansett Eckert Beckwith'),
     ('E591', 'Radford torpedoes Lynch'), ('E591', '"New Ironsides" torpedoes'),
     ('E592', 'Camman gold'), ('E592', 'Cooper "naval officer" gold'),
     ('E593', 'ponchos Ingalls'), ('E593', 'ponchos Sheridan'),
     ('E594', '"John Sherman" "Old Point"'), ('E594', 'Sherman Goldsboro Newbern Wednesday'), ('E594', '"Senator Sherman" "City Point" March 27')]
out = open('fv_l17b_gb.out', 'w'); n = 0
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
for e, q in P:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q + ' intitle:Grant', 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        try: d = get(url); n += 1
        except Exception as ex:
            n += 1
            if '429' in str(ex) or '503' in str(ex):
                time.sleep(25)
                try: d = get(url); n += 1
                except Exception as ex2: out.write(f'{e}\t{q}\tERR {str(ex2)[:50]} after one retry: STOP\n'); n += 1; break
            else: raise
        hits = []
        for it in d.get('items', []):
            vid = it.get('id')
            if vid not in V13 | V14: continue
            s = (it.get('searchInfo') or {}).get('textSnippet', '')
            hits.append((('v13' if vid in V13 else 'v14'), vid, s))
        if not hits: out.write(f'{e}\t{q}\tNO HIT in vols 13/14 (total {d.get("totalItems")})\n')
        for v, vid, s in hits: out.write(f'{e}\t{q}\t{v} {vid}\t{re.sub(chr(10), " ", s)[:500]}\n')
    except Exception as ex: out.write(f'{e}\t{q}\tERR {str(ex)[:60]}\n')
    out.flush(); time.sleep(1.6)
out.write(f'# requests {n}\n'); out.close()
