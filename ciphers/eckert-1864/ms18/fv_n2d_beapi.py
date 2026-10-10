"""FV-N2d (10 Oct 2026): IA be-api full-text search, short phrases, Papers of U. S. Grant vols. 11-12 (and one positive control per volume).
>= 1.8 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess00%02dgran'
Q = [(11, '"put in command of all the troops in the field"'), (11, '"single and separate command"'), (11, '"Grover\'s command"'),
     (11, '"flag of truce boats"'), (11, '"capacity of"  Rucker'), (11, 'Meigs steamboats "30,000 men"'),
     (12, '"Biggs or Bingham"'), (12, 'Bingham inspection "Little Rock"'), (12, '"Fort Smith" Gibson Leavenworth'), (12, '"cripple us"')]
n = 0
for vol, q in Q:
    ident = G % vol
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident, '|', q, '|', len(hits))
        for h in hits[:3]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:4]: print('   ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident, '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
