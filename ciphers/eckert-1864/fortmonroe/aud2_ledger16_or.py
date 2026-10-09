#!/usr/bin/env python3
"""AUD2-LEDGER-16 (9 Oct 2026, account 4): date-window read of the Official Records djvu texts for E260 (OR I/42 pt 3, Union
correspondence 4-6 Oct 1864), E263 (OR I/42 pt 3, 28-30 Nov 1864) and E262 (OR I/36 pt 3, 11-12 June 1864; I/40 pt 2 starts 13 June).
Usage: aud2_ledger16_or.py DIR  (DIR holds warofrebellion423unit.txt and warofrebellion363unit.txt, the archive.org _djvu.txt files,
fetched once to scratch). Prints every occurrence of the entries' names/terms inside each window with 250 chars of context, so a
reader can check each letter in the window that touches quartermaster, steamer, telegraph or cable business. Offsets are the
first/last date-line positions of the Union correspondence for each window. A miss is a search result (rule 10)."""
import re, sys
D = sys.argv[1]
W = [('E260 OR I/42 pt 3, 4-6 Oct 1864', 'warofrebellion423unit.txt', 160000, 262000),
     ('E263 OR I/42 pt 3, 28-30 Nov 1864', 'warofrebellion423unit.txt', 1965000, 2092000),
     ('E262 OR I/36 pt 3, 11-12 June 1864', 'warofrebellion363unit.txt', 1938000, 2364000)]
RX = r'[IL1][nu]gall|Webster|Hudson|Bradley|Howell|steamers?\b|transportation|buildings|Sixth Corps|quartermaster|\bcable\b|O.Brien|telegraph|Homan|arriving'
for name, f, a, b in W:
    t = open(f'{D}/{f}', encoding='utf-8', errors='replace').read()
    seg = re.sub(r'\s+', ' ', t[a:b])
    print('#####', name)
    for m in re.finditer(RX, seg, re.I):
        print('--', m.group(0), '|', seg[max(0, m.start()-250):m.end()+200])
