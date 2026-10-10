"""FV-MS18m (10 Oct 2026): IA leaf lookup for the seven printed MS18-R6 rows (E361-E365, E367, E368).
Pages narrowed from the djvu text layer (running heads before each item), then confirmed on the page image.
Fetches <id>_page_numbers.json (to scratch) and the leaf's page image at 1400 px for eye-reading.
Usage: python3 ms18/fv_ms18m_ia.py SCRATCHDIR  (network; 1.6 s apart)."""
import json, sys, time, urllib.request
OUT = sys.argv[1]
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
WANT = [('E361', 'warofrebellion322unit', ['361']), ('E365', 'warofrebellion322unit', ['369']),
        ('E363', 'warofrebellion322unit', ['389']), ('E362', 'warofrebellion414unit', ['418']),
        ('E364', 'warofrebellion013404rootrich', ['586']), ('E367', 'warofrebellion372unit', ['429']),
        ('E368', 'warofrebellion482unit', ['730'])]
n = 0; pn = {}
def get(url):
    global n
    n += 1; r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read(); time.sleep(1.6); return r
for e, ia, pages in WANT:
    if ia not in pn:
        pn[ia] = json.loads(get(f'https://archive.org/download/{ia}/{ia}_page_numbers.json'))
    for p in pages:
        leaves = [x['leafNum'] for x in pn[ia]['pages'] if x.get('pageNumber') == p]
        print(e, ia, 'page', p, 'leaf', leaves, flush=True)
        for lf in leaves[:1]:
            img = get(f'https://archive.org/download/{ia}/page/n{lf - 1}_w1400.jpg')
            fn = f'{OUT}/{e}_{ia}_p{p}_leaf{lf}.jpg'; open(fn, 'wb').write(img); print('  ->', fn, len(img))
print('requests', n)
