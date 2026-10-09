#!/usr/bin/env python3
"""AUD2-LEDGER-18 (9 Oct 2026, account 4): page-by-page print greps for the second audit of E254, E272, E275, E277.

Usage: aud2_ledger18_print.py OR423_DJVU OR403_DJVU BUTLERSBOOK_DJVU > aud2_ledger18_print.out
  OR423 = archive.org warofrebellion423unit_djvu.txt (OR ser. I vol. 42 pt 3), fetched once to scratch;
  OR403 = sources/ia-fulltext/print-check/warofrebellion403unit_djvu.txt.gz (OR I/40 pt 3, cached);
  BUTLERSBOOK = archive.org autobiographyan00butlgoog_djvu.txt (Butler's Book, 1892), fetched once to scratch.
Pages are split on the djvu text's bare running-head numbers (an increasing run, gaps <= 12), so a page
label can be off by one where a head was mis-OCR'd; every cited page was read in context, not from the label alone.
"""
import gzip, json, re, sys

def load(p):
    return (gzip.open(p, 'rt', encoding='utf-8', errors='replace') if p.endswith('.gz') else open(p, encoding='utf-8', errors='replace')).read()

def pages(text):
    lines = text.split('\n')
    cand = [(i, int(l.strip())) for i, l in enumerate(lines) if re.fullmatch(r'\s*\d{1,4}\s*', l)]
    cuts, last = [], 0
    for i, n in cand:
        if last < n <= last + 12:
            cuts.append((i, n)); last = n
    out = {}
    for k, (i, n) in enumerate(cuts):
        j = cuts[k + 1][0] if k + 1 < len(cuts) else len(lines)
        out[n] = re.sub(r'\s+', ' ', ' '.join(lines[i:j]))
    return out

def grep(P, lo, hi, terms, width=200):
    for n in range(lo, hi + 1):
        v = P.get(n)
        if v is None:
            continue
        for t in terms:
            for m in re.finditer(t, v, re.I):
                print(f'  p{n} [{t}] ...{v[max(0, m.start() - width):m.end() + width]}...')

def main():
    o423, o403, bb = (load(p) for p in sys.argv[1:4])
    P = pages(o423)
    print('== OR I/42 pt 3: pages carrying each date')
    for d in ['November 2, 1864', 'December 9, 1864', 'December 12, 1864']:
        rx = re.compile(d.replace(' ', r'\s*').replace(',', r'\s*[,.]'), re.I)
        print(' ', d, sorted(k for k, v in P.items() if rx.search(v)))
    print('== E254 (12 Dec): whole volume, raw text counts')
    for t in ['Brice', 'Binney', 'paymaster']:
        print(f'  {t}: {len(re.findall(t, o423, re.I))}')
    print('== E254 (12 Dec): pp.969-990'); grep(P, 969, 990, ['Brice', 'Binney', 'paymaster', r"month.s pay", 'make you whole', 'outlay'])
    print('== E275 (9 Dec): pp.886-925'); grep(P, 886, 925, ['boats', 'transportation', 'Allen', 'Captain James', 'Webster', 'to spare'])
    print('== E275 context (Fort Monroe, 10 Dec)'); grep(P, 936, 940, [r'Fort Monroe, December 10'], 300)
    print('== E277 (2 Nov): pp.480-505'); grep(P, 480, 505, ['Howard', 'Napoleon', 'Martin', 'chief of artillery', r'The batteries are'])
    Q = pages(o403)
    print('== E272 (10 July): OR I/40 pt 3')
    for pat in ['sent immediately forward to Washington', 'advance of the Nineteenth Army Corps', 'None have arrived yet', 'How many vessels with the Nineteenth']:
        ks = [k for k, v in Q.items() if re.search(pat.replace(' ', r'\s*'), v, re.I)]
        print(f'  {pat!r}: pp.{ks}')
        for k in ks[:1]:
            v = Q[k]; m = re.search(pat.replace(' ', r'\s*'), v, re.I)
            print(f'    ...{v[max(0, m.start() - 300):m.end() + 200]}...')
    b = re.sub(r'\s+', ' ', bb)
    print("== Butler's Book (1892): counts")
    for t in ['Brice', 'Binney', 'Fred Martin', 'Colonel Howard', 'New Orleans troops', 'boats of any kind', 'two batteries of Napoleon']:
        print(f'  {t}: {len(re.findall(t, b, re.I))}')

if __name__ == '__main__':
    main()
