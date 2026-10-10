#!/usr/bin/env python3
"""AUD2-LEDGER16-5 (10 Oct 2026, for LANE LEDGER-16; copied from fv_l16e_gb.py, fresh queries for E447 E471 E474). Original header: FV-L16e: Google Books API (keyed, country=US) G3 phrase queries for the 1864 entries
E447 E471 E474 E470 E443 E445 E446 E448 (and E468 as the positive control, printed OR I/42 pt 3 p.735) -- Grant Papers ids flagged as before: vols. 13-14 (ids mnRjmhe3QLoC, ij8fAQAAMAAJ = vol. 13; DVLPEPsH1_oC, 1D8fAQAAMAAJ = vol. 14), two more per entry beyond FIX-FM65's two, names and
numbers included, plus one positive control (E531, FIX-FM65's hit). A hit = a snippet from one of the four ids. Other volumes' snippets are printed
too (ORN/OR/press). >= 1.6 s apart; never prints the key. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
IDS = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ', 'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
Q = [('CTRL', '"meet you and the admiral there" Butler Grant'),
     ('E474', '"fleet left yet" Ingalls'), ('E474', 'Ingalls "Colonel Webster" "December 13, 1864"'), ('E474', '"most of the fleet left during last night"'),
     ('E447', '"early daylight" Saugus Colhoun'), ('E447', 'Saugus aground James River December 1864 Colhoun "Hampton Roads"'), ('E447', '"Colhoun" "six miles above City Point"'),
     ('E471', '"number one cipher" Sheldon 1864'), ('E471', '"cable" Cherrystone broken March 1864 telegraph Fort Monroe'), ('E471', '"nothing heard from Kilpatrick"'),
     ('E471', 'Sheldon Eckert "March 3, 1864" cipher')]
import sys
RETRY = set(open(sys.argv[1]).read().splitlines()) if len(sys.argv) > 1 else None
if RETRY: time.sleep(30)
for e, q in Q:
    if RETRY is not None and q not in RETRY: continue
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
        its = d.get('items', [])
        hit = [it['id'] for it in its if it['id'] in IDS]
        print(e, '|', q, '| total', d.get('totalItems'), '| GRANT HIT ' + ','.join(hit) if hit else '| no Grant 13/14 hit')
        for it in its[:6]:
            v = it.get('volumeInfo', {}); s = (it.get('searchInfo', {}) or {}).get('textSnippet', '')
            print('    ', it['id'], v.get('title', '')[:70], v.get('publishedDate'), '|', s[:260])
    except Exception as ex: print(e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(3.0 if RETRY else 1.6)
