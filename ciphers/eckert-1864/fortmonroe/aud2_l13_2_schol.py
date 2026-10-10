"""AUD2-LEDGER13-2 (10 Oct 2026): open-index scholarship pass (OpenAlex, Semantic Scholar, CrossRef) for the Fort Monroe
January 1865 telegrams E502 E507 E512 E520 E532. Keys from OPENALEX_KEY / S2_KEY (headers), never printed. Writes .out beside."""
import json, os, time, urllib.parse, urllib.request
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aud2_l13_2_schol.out')
QS = ['Fort Monroe telegrams cipher 1865', 'Eckert telegraph cipher ledger Huntington', 'Fort Fisher expedition transports quartermaster Webster 1865',
      'Winants Eliza Hancox steamer', 'military telegraph cipher books Civil War decipherment', 'Ingalls quartermaster transports Baltimore January 1865']
UA = 'cipher-lab research script (contact via repository)'
def get(url, hdr):
    hdr = dict(hdr, **{'User-Agent': UA})
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=60))
with open(OUT, 'w') as f:
    for q in QS:
        for name, url, hdr, pick in [
            ('openalex', 'https://api.openalex.org/works?per-page=8&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + os.environ.get('OPENALEX_KEY', '')},
             lambda d: [(w.get('publication_year'), w.get('display_name')) for w in d.get('results', [])]),
            ('s2', 'https://api.semanticscholar.org/graph/v1/paper/search?limit=8&fields=title,year&query=' + urllib.parse.quote(q), {'x-api-key': os.environ.get('S2_KEY', '')},
             lambda d: [(w.get('year'), w.get('title')) for w in d.get('data', []) or []]),
            ('crossref', 'https://api.crossref.org/works?rows=8&query.bibliographic=' + urllib.parse.quote(q), {},
             lambda d: [((w.get('issued', {}).get('date-parts') or [[None]])[0][0], (w.get('title') or [''])[0]) for w in d.get('message', {}).get('items', [])])]:
            try:
                rows = pick(get(url, hdr)); f.write(f'{name}\t{q}\t{len(rows)} shown\n')
                for y, t in rows: f.write(f'    {y} {str(t)[:140]}\n')
            except Exception as e:
                f.write(f'{name}\t{q}\tERROR {type(e).__name__} {str(e)[:80]}\n')
            time.sleep(1.6)
print(open(OUT).read())
