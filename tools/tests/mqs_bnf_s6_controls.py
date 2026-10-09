#!/usr/bin/env python3
"""PREREG-MQS-BNF-S6 controls for bnf_findingaid.section_known / tomo_item_lines (disk only; reads sources/cryptiana/web).
K1 GL.htm 'Achievements in 2023' item lines outside the fr.3029/fr.3092 section, no own-line negation: share known.
N1 the same population WITH own-line negation: count known (gate 0).  N2 unsolved.htm + unsolved-2026-09-24.htm item
pairs on lines with no POSITIVE word: share known by the section rule (gate <= 0.10).  N3 fr.3029 survivors' folios
+37: count known (gate 0).  Run: python3 tools/tests/mqs_bnf_s6_controls.py"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as b  # noqa: E402

PAIR = re.compile(r'\bBnF\s+((?:fr|es)\.\s?\d+|(?:Dupuy|Baluze|Clair\.?)\s?\d+),?\s+ff?\.\s?(\d+)', re.I)


def gl_items():
    L = b.tomo_lines(ROOT, 'sources/cryptiana/web/GL.htm')
    start = next(i for i, l in enumerate(L) if l.startswith('## Achievements in 2023'))
    stop = next(i for i, l in enumerate(L) if i > start and re.match(r'##\s', l))
    cur, out = None, []
    for i in range(start, stop):
        l = L[i]
        if 'fr.3029' in l and l.startswith('###'):
            cur = 'SKIP'
        vols = b.VOL_LINE.findall(l)
        if vols and not b.ITEM_LINE.match(l):
            if cur == 'SKIP' and not l.startswith('###') and ('fr.3029' in l or 'fr.3092' in l):
                continue
            cur = vols[0] if len(set(map(b._vkey, vols))) == 1 else (None if not l.startswith('###') or 'fr.3029' not in l else 'SKIP')
            continue
        if cur and cur != 'SKIP' and b.ITEM_LINE.match(l):
            for f in sorted({int(x) for x in re.findall(r'(?i)\bff?\.\s?(\d+)', l.split(' no.')[0])}):
                out.append((cur, f, bool(b.NEGATION.search(l)), i + 1))
    return out


def main():
    k1, n1 = [], []
    for cote, f, neg, ln in gl_items():
        st, ev = b.portal_status(cote, f, ROOT)
        (n1 if neg else k1).append((cote, f, st, ln, ev[:90]))
    kk = sum(1 for x in k1 if x[2] == 'known')
    print('K1 %d/%d = %.3f known (gate >= 0.90)' % (kk, len(k1), kk / max(1, len(k1))))
    for x in k1:
        if x[2] != 'known':
            print('   K1 miss', x[:4])
    nn = [x for x in n1 if x[2] == 'known']
    print('N1 %d/%d known (gate 0)' % (len(nn), len(n1)))
    for x in nn:
        print('   N1 false', x)
    pairs = set()
    for fn in ('unsolved.htm', 'unsolved-2026-09-24.htm'):
        for l in b.tomo_lines(ROOT, 'sources/cryptiana/web/' + fn):
            if b.POSITIVE.search(l):
                continue
            for v, f in PAIR.findall(l):
                pairs.add((v.replace(' ', ''), int(f)))
    sec = tot = 0
    for v, f in sorted(pairs):
        st, ev = b.portal_status(v, f, ROOT)
        tot += st == 'known'
        if st == 'known' and ' section (text line' in ev:
            sec += 1
            print('   N2 section-known', v, f, ev[:110])
    print('N2 %d/%d = %.3f known by the section rule (gate <= 0.10); %d known in all' %
          (sec, len(pairs), sec / max(1, len(pairs)), tot))
    n3 = [(f + 37, b.portal_status('fr.3029', f + 37, ROOT)[0]) for f in (67, 100, 134, 162, 172, 182, 186)]
    print('N3 %d/7 known (gate 0): %s' % (sum(1 for _, s in n3 if s == 'known'), n3))


if __name__ == '__main__':
    main()
