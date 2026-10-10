#!/usr/bin/env python3
"""AUD2-LEDGER17-3 (10 Oct 2026, owner account; copied from fv_l17c_beapi.py): IA be-api full-text snippet search, second audit of E622 E623:
Grant Papers vol. 10 (Jan-May 1864) and the DLI copies of OR ser. III vol. 4 by identifier, plus whole-collection queries (Lew Wallace's
Autobiography, Butler's Book, press histories). >= 1.8 s apart; one retry after 25 s on an error, then stop. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G10 = 'papersofulyssess0010gran'
Q = [(G10, 'Fort Monroe'),                      # control (vol. 10 is Jan-May 1864: Grant at Fort Monroe 1-2 Apr 1864)
 (G10, 'Van Vliet'), (G10, 'Chesapeake City'), (G10, 'Captain Wise'), (G10, 'Biggs'), (G10, 'canal barges'),
 ('in.ernet.dli.2015.165578', 'Van Vliet'), ('in.ernet.dli.2015.155283', 'Van Vliet'), ('in.ernet.dli.2015.171703', 'Van Vliet'),
 (None, 'Van Vliet chartered vessels expedition Fort Monroe April 1864 Wise Meigs'),
 (None, 'Shore correspondent World Butler arrested Baltimore Wallace'),
 (None, 'Davenport Bureau of Information Butler Shore'),
 (None, '"W. W. Shore"'),
 (None, 'Butler ordered out of the department correspondent World 1864 Shore')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    for attempt in (1, 2):
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
            hits = d.get('hits', {}).get('hits', [])
            print(ident or '(all)', '|', q, '|', len(hits))
            for h in hits[:6]:
                f = h.get('fields', {}) or {}
                print('   ', f.get('identifier'), (f.get('title', '') or '')[:70] if isinstance(f.get('title', ''), str) else '')
                for s in (h.get('highlight', {}) or {}).get('text', [])[:4]: print('      ', s.replace('\n', ' ')[:300])
            break
        except Exception as e:
            n += 1; print(ident or '(all)', '|', q, '| ERR', attempt, str(e)[:100])
            if attempt == 1: time.sleep(25)
    time.sleep(1.8)
print('be-api requests', n)
