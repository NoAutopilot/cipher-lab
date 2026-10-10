"""AUD2-LEDGER13-2 (10 Oct 2026): IA be-api full-text queries: ORN ser. I vol. 12 (officialrecordso0012unse, whose _djvu.txt answered 500 to
FV-FM65b) with a positive control first, then the ship names of E507 E512 E520; and two whole-collection phrase variants not run by FV-FM65b.
>= 2 s apart. Writes aud2_l13_2_beapi.out beside this file. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l13_2_beapi.out')
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('officialrecordso0012unse', 'Wilmington'), ('officialrecordso0012unse', 'Malvern'),
     ('officialrecordso0012unse', 'Winants'), ('officialrecordso0012unse', 'Hancox'), ('officialrecordso0012unse', '"steamer Russia"'),
     ('officialrecordso0012unse', 'Webster quartermaster Monroe'),
     (None, '"Russia is disabled"'), (None, '"Winants is hardly"'), (None, '"Baltic which was at Baltimore"'),
     (None, '"fifty six-mule teams"'), (None, '"transportation for 4,000 men"')]
with open(OUT, 'w') as f:
    for ident, q in Q:
        p = {'q': q}
        if ident: p['identifier'] = ident
        url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
            hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
            tot = d.get('hits', {}).get('total') if isinstance(d.get('hits'), dict) else len(hits)
            f.write(f'{ident}\t{q}\ttotal {tot}\n')
            for h in hits[:6]:
                s = h.get('_source', h); hl = h.get('highlight', {})
                f.write(f'    {s.get("identifier")} | {" ".join(str(hl)[:300].split())}\n')
        except Exception as e:
            f.write(f'{ident}\t{q}\tERROR {type(e).__name__} {str(e)[:80]}\n')
        time.sleep(2)
print(open(OUT).read())
