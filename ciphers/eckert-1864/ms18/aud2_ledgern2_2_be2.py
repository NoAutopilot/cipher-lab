"""AUD2-LEDGERN2-2 (10 Oct 2026): IA be-api follow-ups -- Fry 2020 context and notes around McCloskey (does Fry cite the War Department's 30 Oct telegram?),
positive controls for the Grant Papers misses. >= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('republicinranks0000zach', '"Tammany Hall operative"'), ('republicinranks0000zach', 'Dana Warren'), ('republicinranks0000zach', '"ballot-box"'),
     ('republicinranks0000zach', 'stuffer'), ('republicinranks0000zach', 'Seymour commissioners Fifth Corps'), ('republicinranks0000zach', '"Fifth Corps"'),
     ('papersofulyssess0012gran', 'Seymour'), ('papersofulyssess0013gran', '"Sixth Corps" Ingalls'), ('papersofulyssess0013gran', 'Wright Sixth Corps December')]
n = 0
for ident, q in Q:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident}), headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:2]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:8]: print('   ', s.replace('\n', ' ')[:400])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
