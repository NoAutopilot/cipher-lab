#!/usr/bin/env python3
"""FV-FM10a (9 Oct 2026): IA be-api full-text search inside named identifiers (snippets only, no page numbers; CLAUDE.md access item 3)
for E314 E315 E318 phrases, plus a positive control. >= 2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion363unit', '"Gloucester route"'), ('warofrebellion363unit', 'Gloucester Mackintosh'), ('warofrebellion363unit', 'Gloucester Yorktown telegraph'),
     ('militarytelegraph02plumrich', '"porous cups"'), ('militarytelegraph02plumrich', 'Gloucester'), ('militarytelegraph02plumrich', 'Mackintosh'),
     ('militarytelegraph02plumrich', '"O\'Brien"'), ('papersofulyssess0011gran', 'Gloucester route'),
     ('warofrebellion363unit', '"Fort Monroe"')]  # last = positive control
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:2]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:8]: print('   ', ' '.join(s.split())[:300])
    except Exception as e: print(ident, '|', q, '| ERROR', e)
    time.sleep(2)
print('be-api requests', len(Q))
