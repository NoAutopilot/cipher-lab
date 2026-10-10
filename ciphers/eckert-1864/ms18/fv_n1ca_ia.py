"""FV-N1C-a (10 Oct 2026): IA leaf lookup for E382 E388 E390 E391 and N2-IE IF II IJ; copied from fv_ms18p_ia.py.
Pages narrowed from the djvu text layer (running heads before each item), then confirmed on the page image.
Fetches <id>_page_numbers.json (to scratch) and the leaf's page image at 1400 px for eye-reading.
Usage: python3 ms18/fv_n1ca_ia.py SCRATCHDIR  (network; 1.6 s apart)."""
import json, sys, time, urllib.request
OUT = sys.argv[1]
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
WANT = [('E382', 'warofrebellion492unit', ['647']), ('E388', 'warofrebellion323unit', ['247']),
        ('E390', 'warofrebellion414unit', ['343']), ('N2-IJ', 'warofrebellion414unit', ['337']),
        ('E391', 'warofrebellion372unit', ['18', '19', '32']), ('N2-II', 'warofrebellion372unit', ['135']),
        ('N2-II', 'warofrebellion403unit', ['93']), ('N2-IE', 'warofrebellion013404rootrich', ['331']),
        ('N2-IF', 'warofrebellion33unit', ['663', '664'])]
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
