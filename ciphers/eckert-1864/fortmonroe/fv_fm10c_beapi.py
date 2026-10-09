#!/usr/bin/env python3
"""FV-FM10c (9 Oct 2026; copy of fv_fm9e_beapi.py): IA be-api full-text search (snippets only, no page numbers; CLAUDE.md access item 3) for O9-BD, O9-CA..CD phrases,
across IA (no identifier) and inside named volumes. >= 2 s apart. A miss is a search result (rule 10). Positive control: '"Chief Operator Fortress Monroe"'
inside militarytelegraph02plumrich (known present in its djvu text, fv_fm9e_print.out)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellionco0006unit', 'Brengle'), ('warofrebellionco0006unit', 'Brengle Mulford February'), (None, 'Brengle "flag of truce" Mulford 1864'),
     (None, '"Brengle" Frederick Butler Davenport'), (None, '"William Lee" detective Horner 1864'), (None, '"painful rumors" Havre de Grace 1864'),
     (None, 'Buell "New Castle" July 1864 telegraph steamers "Havre de Grace"'), ('privateoffice03butlrich', 'Brengle'),
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
