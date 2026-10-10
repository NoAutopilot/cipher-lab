#!/usr/bin/env python3
"""FV-L16e (10 Oct 2026, for LANE LEDGER-16; copied from fv_l15d_gb.py): Google Books API (keyed, country=US) G3 phrase queries for the 1864 entries
E447 E471 E474 E470 E443 E445 E446 E448 (and E468 as the positive control, printed OR I/42 pt 3 p.735) -- Grant Papers ids flagged as before: vols. 13-14 (ids mnRjmhe3QLoC, ij8fAQAAMAAJ = vol. 13; DVLPEPsH1_oC, 1D8fAQAAMAAJ = vol. 14), two more per entry beyond FIX-FM65's two, names and
numbers included, plus one positive control (E531, FIX-FM65's hit). A hit = a snippet from one of the four ids. Other volumes' snippets are printed
too (ORN/OR/press). >= 1.6 s apart; never prints the key. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
IDS = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ', 'DVLPEPsH1_oC', '1D8fAQAAMAAJ'}
Q = [('CTRL', '"meet you and the admiral there" Butler Grant'),
     ('E447', 'Saugus Colhoun "start down" December 1864 "City Point"'), ('E447', '"above City Point" Saugus Colhoun Porter telegram'),
     ('E471', '"cable is repaired" Kilpatrick Sheldon 1864'), ('E471', '"send no ciphers" Kilpatrick March 1864'),
     ('E474', '"Butler\'s fleet" left Ingalls Webster December 1864'),
     ('E470', '"Mahopac, Canonicus, and Saugus" "ready for service"'),
     ('E443', '"yellow fever is prevailing" Newbern McDougall 1864'), ('E443', '"yellow fever" Newbern October 1864 McDougall Horner'),
     ('E445', 'Baird instruments "City of Hudson" Porter December 1864'), ('E445', '"Mr. Baird" instruments Butler Porter 1864 telegraph'),
     ('E446', '"W. A. Dunn" Cherrystone operator Baltimore'), ('E446', 'Dunn operator Cherrystone "American office" Butler'),
     ('E448', 'Manhattan Stanton "City Point" October 1864 Dealy'), ('E448', '"don\'t mention his coming" Stanton')]
for e, q in Q:
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
    time.sleep(1.6)
