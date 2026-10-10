"""FV-N1C-b (LANE LEDGER-12, 10 Oct 2026): IA leaf lookup and page images for the printed rows; copied from fv_ms18p_ia.py.
Pages narrowed from the djvu text layer (fv_n1cb_locate.out), then read on the page image (1400 px, scratch, not committed).
Usage: python3 ms18/fv_n1cb_ia.py SCRATCHDIR  (network; 1.6 s apart)."""
import json, sys, time, urllib.request
OUT = sys.argv[1]
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
WANT = [('N2-JA', 'warofrebellion322unit', ['432']), ('N2-JB', 'warofrebellion013404rootrich', ['304']),
        ('N2-JC', 'warofrebellion013403rootrich', ['306', '307']), ('N2-JF', 'warofrebellion013403rootrich', ['357']),
        ('N2-JD', 'warofrebellion372unit', ['15']), ('N2-JE', 'warofrebellion372unit', ['523']),
        ('N2-KD', 'warofrebellion372unit', ['384', '385']), ('N2-JJ', 'warofrebellion371unit', ['670']),
        ('N2-KE', 'officialrecordso0010unse', ['418'])]
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
