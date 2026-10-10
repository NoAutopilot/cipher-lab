"""AUD2-LEDGER15-1 (10 Oct 2026): IA be-api full-text queries for the second audit of E555 E568 E541 E576 E575: inside The Papers of
Ulysses S. Grant vol. 14 (papersofulyssess0014gran, lending-only, fts works without a loan) with a positive control first, then
whole-collection phrase variants FV-L15a did not run. >= 2 s apart. Writes aud2_l15_1_beapi.out beside this file.
A miss is a search result, not a novelty verdict (rule 10). Usage: aud2_l15_1_beapi.py"""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l15_1_beapi.out')
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess0014gran'
Q = [(G, '"organize a force of cavalry"'), (G, '"Sumner\'s cavalry"'),
     (G, 'Nansemond'), (G, 'Boyle'), (G, '"Broad Ford"'), (G, 'Blackwater'), (G, 'Nottoway'), (G, '"carry pontoons"'),
     (G, 'Emerick'), (G, '"O\'Brien"'), (G, '"construction parties"'), (G, '"double line"'), (G, 'Morehead'),
     (G, 'Meagher'), (G, '"mule teams"'), (G, 'ambulances Schofield'), (G, 'Stromboli'), (G, 'Nevada'),
     (None, '"double line from Morehead"'), (None, '"construction parties" Goldsboro Wilmington operators'),
     (None, '"difficulty of getting operators"'), (None, '"torpedoes of the kind"'), (None, '"Stromboli" torpedoes Lynch'),
     (None, '"Broad Ford" Blackwater'), (None, '"guide Boyle"'), (None, '"102 horse ambulances"'),
     (None, '"Meagher\'s division" "Annapolis" Rucker'), (None, '"steamer Nevada" recruits')]
with open(OUT, 'w') as f:
    n = 0
    for ident, q in Q:
        p = {'q': q}
        if ident: p['identifier'] = ident
        url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
        for attempt in (1, 2):
            n += 1
            try:
                d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
                hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
                tot = d.get('hits', {}).get('total') if isinstance(d.get('hits'), dict) else len(hits)
                f.write(f'{ident}\t{q}\ttotal {tot}\n')
                for h in hits[:8]:
                    s = h.get('_source', h); hl = h.get('highlight', {})
                    f.write(f'    {s.get("identifier")} | {" ".join(str(hl)[:700].split())}\n')
                break
            except Exception as e:
                f.write(f'{ident}\t{q}\tERROR {type(e).__name__} {str(e)[:80]} (attempt {attempt})\n')
                if attempt == 1: time.sleep(25)
        f.flush(); time.sleep(2)
    f.write(f'requests {n}\n')
print(open(OUT).read())
