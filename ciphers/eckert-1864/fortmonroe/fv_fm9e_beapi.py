#!/usr/bin/env python3
"""FV-FM9e (9 Oct 2026; copy of fv_fm9d_beapi.py): IA be-api full-text search (snippets only, no page numbers; CLAUDE.md access item 3) for E310-E313 phrases,
across IA (no identifier) and inside named volumes. >= 2 s apart. A miss is a search result (rule 10). Positive control: '"Chief Operator Fortress Monroe"'
inside militarytelegraph02plumrich (known present in its djvu text, fv_fm9e_print.out)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None, '"W. W. Shore" World'), (None, '"Shore" "aid and comfort" Butler Wallace'), (None, '"Bowers Hill" Suffolk evacuated 1864'),
     (None, '"careful in punctuation" cipher'), (None, '"arbitrary words should be used"'), (None, '"building party" Jamestown "White House" 1864'),
     ('militarytelegraph02plumrich', '"Chief Operator Fortress Monroe"')]
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
