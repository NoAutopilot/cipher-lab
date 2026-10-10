#!/usr/bin/env python3
"""FV-L15a (10 Oct 2026): non-holder network searches for E555 E536 E568 E541 E576 E575. (1) Google Books API (keyed, country=US, key from the
environment, never printed) phrase queries with intitle:Grant, a hit being a snippet from a Grant Papers vol. 13/14 volume id (FIX-FM65's four
ids), positive control E531 first; four queries per entry (FIX-FM65 ran two: these add names and numbers). (2) IA be-api whole-collection phrase
queries (no identifier), positive control '"Suwo Nada"' in OR I/46 pt 2 by identifier. (3) loc.gov Chronicling America JSON for E536 (the Tribune
dispatch) and E555. >= 1.6 s apart per host. A miss is a search result, not a novelty verdict (rule 10)."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GP = {'mnRjmhe3QLoC': 13, 'ij8fAQAAMAAJ': 13, 'DVLPEPsH1_oC': 14, '1D8fAQAAMAAJ': 14}
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
def get(url, ua=UA):
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=ua), timeout=90))
GB = [('CTRL-E531', '"six vessels" Oriental intitle:Grant'),
 ('E555', '"Meagher\'s division" Rucker Annapolis intitle:Grant'), ('E555', '"mule teams" ambulances "23d Corps" Rucker intitle:Grant'),
 ('E555', '"prepared and loaded" intitle:Grant'), ('E555', '"102" ambulances "306" intitle:Grant'),
 ('E536', '"Pennypacker" "Vanderbilt" Tribune intitle:Grant'), ('E536', '"stunning report" Fisher intitle:Grant'),
 ('E536', '"bright flash" Fisher magazine intitle:Grant'), ('E536', 'Tribune correspondent Dana "Fort Fisher" Hall intitle:Grant'),
 ('E568', '"double line" Goldsboro "Morehead City" intitle:Grant'), ('E568', 'O\'Brien telegraph "construction parties" intitle:Grant'),
 ('E568', '"difficulty of getting operators" intitle:Grant'), ('E568', 'O\'Brien Schofield telegraph line Wilmington "Fort Fisher" operators intitle:Grant'),
 ('E541', '"Nevada" recruits "City Point" Rucker Webster intitle:Grant'), ('E541', 'Stromboli torpedoes Lynch Wise intitle:Grant'),
 ('E541', '"sea-going steam vessels" Monroe intitle:Grant'), ('E541', '"next five or six days" Monroe intitle:Grant'),
 ('E576', 'Boyle guide Blackwater Gordon intitle:Grant'), ('E576', '"Broad Ford" Blackwater intitle:Grant'),
 ('E576', 'Blackwater "Army of the Potomac" bridging Nottoway intitle:Grant'), ('E576', '"twenty-two miles from Suffolk" intitle:Grant'),
 ('E575', 'Gordon gunboats Suffolk Nansemond cavalry pontoons Ord intitle:Grant'), ('E575', '"Sumner\'s cavalry" Norfolk Gordon Ord intitle:Grant'),
 ('E575', '"how much water" gunboats Suffolk intitle:Grant'), ('E575', 'Emerick Gordon Ord Nansemond intitle:Grant')]
for e, q in GB:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        d = get(url, {'User-Agent': 'Mozilla/5.0'}); its = d.get('items', []) or []
        g = [(GP[i['id']], re.sub(r'\s+', ' ', re.sub('<[^>]+>', '', (i.get('searchInfo') or {}).get('textSnippet', '')))) for i in its if i.get('id') in GP]
        print('GB', e, '|', q, '| total', d.get('totalItems'), '| grant-papers', len(g))
        for v, s in g: print('      vol', v, '::', s[:300])
    except Exception as ex: print('GB', e, '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.6)
BE = [('warofrebellion014602rootrich', '"Suwo Nada"'), (None, '"Fort Fisher is ours" "stunning report"'), (None, '"Bell and Pennypacker"'),
      (None, '"bright flash was seen to proceed"'), (None, '"well sustained assault of four hours"'), (None, '"Meagher\'s division" "mule teams" Rucker'),
      (None, '"double line from Morehead City"'), (None, '"vices and straps"'), (None, '"torpedoes of the kind you name"'),
      (None, '"those on board the Stromboli"'), (None, '"guide Boyle"'), (None, '"Broad Ford" Blackwater Suffolk'),
      (None, '"how much water can your gunboats"'), (None, '"leave word where they had better land"'),
      ('officialrecordso0012unse', 'Stromboli'), ('officialrecordso0012unse', 'Nansemond')]
for ident, q in BE:
    p = {'q': q}
    if ident: p['identifier'] = ident
    try:
        d = get('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)); hits = d.get('hits', {}).get('hits', [])
        print('BE', ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:5]:
            f = h.get('fields', {}) or {}; hl = h.get('highlight', {}) or {}
            print('      ', f.get('identifier'), '::', ' '.join(' '.join(x if isinstance(x, str) else str(x) for x in (hl.get('text') or [])).split())[:300])
    except Exception as ex: print('BE', ident or '(all)', '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.8)
for q, dr in [('"Pennypacker" Vanderbilt "bright flash"', '1865-01-17/1865-01-31'), ('"stunning report" Fisher magazine', '1865-01-17/1865-01-31'),
              ('Tribune "Fort Fisher is ours" Pennypacker Bell', '1865-01-17/1865-01-25'), ('"Meagher" "mule teams" ambulances Annapolis', '1865-02-08/1865-02-20')]:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode({'q': q, 'fo': 'json', 'dates': dr, 'c': 10})
    try:
        d = get(url); r = d.get('results', [])
        print('LOC', q, dr, '| results', d.get('pagination', {}).get('of'))
        for x in r[:8]: print('      ', x.get('date'), (x.get('title') or '')[:70], x.get('id'))
    except Exception as ex: print('LOC', q, '| ERR', str(ex)[:100])
    time.sleep(2)
