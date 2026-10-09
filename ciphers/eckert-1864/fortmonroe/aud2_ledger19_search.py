#!/usr/bin/env python3
"""AUD2-LEDGER-19 (9 Oct 2026, second audit of E280 E281 E283 E284 E285): (1) IA be-api full-text search, snippet only, of the
Grant Papers vols. 10 and 12 on E281/E284/E280 words the first audit (FV-FM8b, fv_fm8b_beapi.py) did not query; (2) Google Books
API (GOOGLE_BOOKS_KEY, country=US; key never printed) on the distinctive words of each safe sentence. >= 1.6 s apart per host;
a host that fails twice is stopped. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
BE = [('papersofulyssess0012gran', 'Lizzie'), ('papersofulyssess0012gran', '"only boat"'),
      ('papersofulyssess0012gran', '"forty-eight hours" Babcock'), ('papersofulyssess0012gran', '"48 hours" Fort Monroe'),
      ('papersofulyssess0012gran', '"authority to take"'), ('papersofulyssess0012gran', 'Craney Island'),
      ('papersofulyssess0012gran', '"yellow fever" New Berne'), ('papersofulyssess0012gran', 'Beckwith Babcock'),
      ('papersofulyssess0010gran', 'Eckert Sheldon'), ('papersofulyssess0010gran', '"cut poles"'),
      ('papersofulyssess0010gran', 'Gloucester telegraph line')]
GB = [('E280', '"Newport Barracks" "yellow fever" Waterhouse telegraph'), ('E280', 'Vanderhoef "yellow fever" Newbern 1864'),
      ('E280', '"close the offices" Gilmore telegraph Newbern'),
      ('E281', 'Bickford "Port Royal" "West Point" telegraph 1864 Eckert'), ('E281', '"cut poles" Gloucester "West Point" telegraph'),
      ('E283', '"White Shoal" "Point of Shoals" Porter 1864'), ('E283', '"hold the persons in them as prisoners"'),
      ('E284', '"Lizzie Baker" Babcock 1864'), ('E284', '"Mulford\'s boats"'), ('E284', '"Lizzie Baker" steamer Fort Monroe'),
      ('E285', 'Tallapoosa "Montauk Point" 1864'), ('E285', '"steering for Halifax"'), ('E285', 'Maumee Yantic Tallapoosa Tallahassee Halifax telegram Porter')]

def get(url, headers=UA):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60))

def run(items, mk, show, tag):
    n = fails = 0
    for it in items:
        for attempt in (1, 2):
            try:
                d = get(mk(it)); n += 1; show(it, d); break
            except Exception as e:
                n += 1; print(tag, it, 'ERR', str(e)[:80])
                if attempt == 1: time.sleep(20)
                else: fails += 1
        if fails: print(tag, 'failed twice: host stopped'); break
        time.sleep(1.6)
    print(tag, 'requests', n)

def be_show(it, d):
    hits = d.get('hits', {}).get('hits', [])
    print('BE', it[0], it[1], len(hits))
    for h in hits[:4]:
        for s in (h.get('highlight', {}) or {}).get('text', [])[:6]: print('   ', s.replace('\n', ' ')[:320])

def gb_show(it, d):
    items = d.get('items', []) or []
    print('GB', it[0], it[1], 'total', d.get('totalItems'))
    for v in items[:8]:
        vi = v.get('volumeInfo', {}); si = (v.get('searchInfo', {}) or {}).get('textSnippet', '')
        print('   ', vi.get('title', '')[:80], '|', vi.get('publishedDate'), '|', v.get('accessInfo', {}).get('viewability'), '|', si.replace('\n', ' ')[:240])

if __name__ == '__main__':
    run(BE, lambda it: 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': it[1], 'identifier': it[0]}), be_show, 'BE')
    key = os.environ.get('GOOGLE_BOOKS_KEY', '')
    if not key: print('GB: GOOGLE_BOOKS_KEY absent, not run'); sys.exit(0)
    run(GB, lambda it: 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': it[1], 'maxResults': 10, 'country': 'US', 'key': key}), gb_show, 'GB')
