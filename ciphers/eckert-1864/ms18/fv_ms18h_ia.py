"""FV-MS18h (9 Oct 2026): IA leaf lookup for the four printed MS18-R4 rows (E341, E342, E344, E348).
Fetches <id>_page_numbers.json (to scratch) and prints the leaf for each printed page; then fetches that leaf's page image
at 1400 px to scratch for eye-reading. Usage: python3 ms18/fv_ms18h_ia.py SCRATCHDIR  (network; 1.6 s apart)."""
import json, sys, time, urllib.request
OUT = sys.argv[1]
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
WANT = [('E341', 'warofrebellion393unit', ['703', '704']), ('E342', 'warofrebellion392unit', ['343']),
        ('E344', 'warofrebellion393unit', ['274']), ('E348', 'warofrebellion372unit', ['133', '134'])]
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
