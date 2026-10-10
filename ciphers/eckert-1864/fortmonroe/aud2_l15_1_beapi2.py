"""AUD2-LEDGER15-1 (10 Oct 2026): follow-up be-api queries inside Grant Papers vol. 14 (papersofulyssess0014gran) on the 113n-114n
Blackwater note (E575/E576) and the Wilmington telegraph (E568). >= 2 s apart. Writes aud2_l15_1_beapi2.out. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l15_1_beapi2.out')
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
G = 'papersofulyssess0014gran'
Q = ['Gordon Norfolk', 'Suffolk', 'Chowan', 'pontoons', '"Gordon" Blackwater', 'forded', 'gunboats Suffolk', 'Eckert',
     'telegraph Goldsboro', 'operators', 'Wilmington telegraph']
with open(OUT, 'w') as f:
    n = 0
    for q in Q:
        url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': G})
        n += 1
        try:
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
            hits = d.get('hits', {}).get('hits', [])
            f.write(f'{G}\t{q}\ttotal {d.get("hits", {}).get("total")}\n')
            for h in hits[:3]:
                for t in h.get('highlight', {}).get('text', []): f.write('    :: ' + ' '.join(t.split()) + '\n')
        except Exception as e: f.write(f'{G}\t{q}\tERROR {type(e).__name__} {str(e)[:80]}\n')
        f.flush(); time.sleep(2)
    f.write(f'requests {n}\n')
print(open(OUT).read())
