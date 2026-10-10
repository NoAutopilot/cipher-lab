"""AUD2-LEDGER16-4 (10 Oct 2026): date-window read of cached OR / ORN djvu texts for E441 E472 E442 E473 E469 E466.
For each dated message heading in the window, print the heading context if its body (next ~1800 chars) carries a keyword.
Usage: python3 aud2_l16_4_or.py  (reads sources/ia-fulltext/print-check, prints to stdout; the committed .out keeps only the window index lines)"""
import gzip, re, sys
P = 'sources/ia-fulltext/print-check/'
JOBS = [
 ('warofrebellion363unit', r'May (2[6-9]|3[01]), 1864', r'telegraph|Eckert|Sheldon|O.Brien|cable|wire|operator|Mattapon|firing|cannonad|Yorktown|Gloucester|Jamestown|Homan|Collings|Collins|Williamsburg'),
 ('warofrebellion363unit', r'May 20, 1864', r'Biggs|Sheridan|forage|Meigs|Quartermaster'),
 ('warofrebellion33unit', r'April (2[4-9]|30), 1864', r'telegraph|Eckert|Sheldon|O.Brien|Dunn|New Regime|Regime|Edgar|Clark|newspaper|exchanges|operator'),
 ('officialrecordso0010unse', r'May (29|30|31), 1864', r'firing|cannonad|heard|Bermuda|Grant'),
 ('officialrecordso0009unse', r'April (2[4-9]|30), 1864', r'Regime|newspaper|Edgar|Dunn|Clark|telegraph'),
]
for vol, date, kw in JOBS:
    t = gzip.open(P + vol + '_djvu.txt.gz', 'rt', errors='replace').read()
    print('=' * 20, vol, date, len(t))
    n = 0
    for m in re.finditer(date.replace(' ', r'\s+'), t):
        body = t[m.start(): m.start() + 1800]
        ks = sorted(set(k.lower() for k in re.findall(kw, body, re.I)))
        if not ks:
            continue
        # page from the nearest preceding running head number line
        pre = t[max(0, m.start() - 6000): m.start()]
        heads = re.findall(r'\n\s*(\d{1,4})\s+[A-Z][A-Z .,\-]{8,}\s*\n|\n\s*[A-Z][A-Z .,\-]{8,}\s+(\d{1,4})\s*\n', pre)
        pg = (heads[-1][0] or heads[-1][1]) if heads else '?'
        n += 1
        print('--- p~%s off %d kw %s' % (pg, m.start(), ','.join(ks)))
        print(re.sub(r'\s+', ' ', t[max(0, m.start() - 250): m.start() + 900]))
    print('windows with keywords:', n)
