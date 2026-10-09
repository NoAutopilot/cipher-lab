#!/usr/bin/env python3
"""FV-FM10b (9 Oct 2026): IA be-api full-text search inside named identifiers (snippets only, no page numbers; CLAUDE.md access item 3)
for E319-E321 phrases (OR I/36 pt 3 searched here because its djvu download failed twice). >= 2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('warofrebellion363unit', '"high masts"'), ('warofrebellion363unit', '"string wire"'), ('warofrebellion363unit', 'Mattapony Sheldon'),
     ('warofrebellion363unit', '"regret having ordered"'), ('warofrebellion363unit', '"careful working"'), ('warofrebellion363unit', 'Mackintosh builders'),
     ('warofrebellion363unit', 'Sheldon'), ('papersofulyssess0011gran', '"high masts"'), ('papersofulyssess0011gran', 'Mattapony wire'),
     ('papersofulyssess0012gran', '"dragged up by anchors"'), ('papersofulyssess0012gran', 'cable anchors'), ('privateofficialc04butl', 'OBrien cipher')]
for ident, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:2]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:6]: print('   ', ' '.join(s.split())[:260])
    except Exception as e: print(ident, '|', q, '| ERROR', e)
    time.sleep(2)
print('be-api requests', len(Q))
