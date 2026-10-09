#!/usr/bin/env python3
"""FV-FM9d (9 Oct 2026): IA be-api full-text search (snippets only, no page numbers; CLAUDE.md access item 3) for E307 E308 E309 phrases,
across IA (no identifier) and inside named volumes. >= 2 s apart. A miss is a search result (rule 10). Positive control: '"Herman Frank Waterhouse"'
inside militarytelegraph02plumrich (known present in its djvu text)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None, '"Emory Round"'), (None, '"Chaplain White" "Providence Conference"'), (None, '"terrific naval engagement" Albemarle'),
     ('papersofulyssess0012gran', 'Webster Rucker steamers'), ('privateofficialc05butl', '"no spare boats"'),
     (None, '"J. R. Gilmore" Chambersburg'), ('militarytelegraph02plumrich', '"Herman Frank Waterhouse"')]
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:4]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('  id', h.get('_id') or src.get('identifier'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', ' '.join(s.split())[:260])
    except Exception as e: print(ident, '|', q, '| ERROR', e)
    time.sleep(2)
print('be-api requests', len(Q))
