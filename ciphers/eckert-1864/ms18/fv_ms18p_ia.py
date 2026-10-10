"""FV-MS18p (10 Oct 2026): IA leaf lookup for the printed MS18-R7 rows (E372, E373, E376, E377, E380) and E379's quoted dispatch; copied from fv_ms18m_ia.py.
Pages narrowed from the djvu text layer (running heads before each item), then confirmed on the page image.
Fetches <id>_page_numbers.json (to scratch) and the leaf's page image at 1400 px for eye-reading.
Usage: python3 ms18/fv_ms18m_ia.py SCRATCHDIR  (network; 1.6 s apart)."""
import json, sys, time, urllib.request
OUT = sys.argv[1]
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
WANT = [('E372', 'warofrebellion452unit', ['82']), ('E373', 'warofrebellion393unit', ['482']),
        ('E376', 'warofrebellion482unit', ['505']), ('E377', 'warofrebellion372unit', ['63']),
        ('E380', 'warofrebellion013403rootrich', ['480']), ('E379', 'warofrebellion391unit', ['20'])]
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
