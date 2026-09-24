#!/usr/bin/env python3
"""Build key_tomokiyo.tsv from the hand alignment of the La Luzerne 8 Jan 1781 passage.

Source: Tomokiyo, Cryptiana blog, 23 Sept 2021 (sources/cryptiana/blog/2021_09_decoded-but-not-identified-code-of.html),
Beinecke Rochambeau Papers item 4528532. alignment_yale_8jan1781.tsv holds one row per code group
(figures re-extracted from the snapshot and checked here) with the plaintext unit it was aligned to and a grade:
C aligned from the printed decoded text, M alignment uncertain, I repaired against the printed text, U unaligned.

  python3 build_key_tomokiyo.py          # rewrite key_tomokiyo.tsv, print counts and the ordering test
  python3 build_key_tomokiyo.py --check  # exit 1 if the figures differ from the snapshot or the key is stale
"""
import argparse, collections, html, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, '..', '..', 'sources', 'cryptiana', 'blog', '2021_09_decoded-but-not-identified-code-of.html')
ALIGN = os.path.join(HERE, 'alignment_yale_8jan1781.tsv')
KEY = os.path.join(HERE, 'key_tomokiyo.tsv')
SRC = 'Tomokiyo 2021 (Cryptiana blog), Beinecke 4528532, 8 Jan 1781'


def snapshot_figures():
    t = html.unescape(re.sub(r'<[^>]+>', ' ', open(SNAP, encoding='utf-8').read()))
    a, b = t.index('445 538 819'), t.index('Decoding on a separate')
    return re.findall(r'\d+', re.sub(r'p\.\d+', ' ', t[a:b]))


def build():
    rows = [l.rstrip('\n').split('\t') for l in open(ALIGN, encoding='utf-8')][1:]
    figs = snapshot_figures()
    if [r[2] for r in rows] != figs:
        sys.exit('alignment figures differ from the Tomokiyo snapshot')
    by = collections.OrderedDict()
    for idx, _line, fig, _mark, unit, grade in rows:
        by.setdefault(int(fig), []).append((int(idx), unit, grade))
    out = ['figure\tplaintext\tgrade\tn\tpositions\tsource']
    for fig in sorted(by):
        occ = by[fig]
        units = list(collections.OrderedDict.fromkeys(u for _, u, _ in occ))
        grades = [g for _, _, g in occ]
        grade = 'C' if 'C' in grades else ('M' if 'M' in grades else grades[0])
        out.append(f"{fig}\t{' / '.join(units)}\t{grade}\t{len(occ)}\t{','.join(str(i) for i, _, _ in occ)}\t{SRC}")
    return rows, '\n'.join(out) + '\n'


def ordering_test(rows):
    """One-part codes number their entries alphabetically: figure rank tracks plaintext rank. Spearman rho on the
    C-graded single-meaning pairs, against 10,000 shuffles."""
    pairs = {}
    for _i, _l, fig, _m, unit, g in rows:
        if g == 'C' and '|' not in unit and not unit.startswith('['):
            pairs[int(fig)] = unit.replace("'", '').replace('(', '').replace(')', '')
    figs = sorted(pairs)
    units = [pairs[f] for f in figs]
    rank = {u: i for i, u in enumerate(sorted(set(units)))}
    x = list(range(len(figs)))
    y = [rank[u] for u in units]

    def rho(yy):
        n = len(yy); mx = (n - 1) / 2; my = sum(yy) / n
        num = sum((a - mx) * (b - my) for a, b in zip(x, yy))
        den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in yy)) ** 0.5
        return num / den
    r = rho(y)
    rnd = random.Random(1781); ge = 0
    for _ in range(10000):
        z = y[:]; rnd.shuffle(z)
        ge += abs(rho(z)) >= abs(r)
    return len(figs), r, ge / 10000


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    rows, text = build()
    if a.check:
        if not os.path.exists(KEY) or open(KEY, encoding='utf-8').read() != text:
            sys.exit('key_tomokiyo.tsv is stale; rerun build_key_tomokiyo.py')
        print('ok'); return
    open(KEY, 'w', encoding='utf-8').write(text)
    tok = collections.Counter(r[5] for r in rows)
    keyg = collections.Counter(l.split('\t')[2] for l in text.splitlines()[1:])
    print('tokens', dict(tok), 'distinct figures', dict(keyg))
    n, r, p = ordering_test(rows)
    print(f'ordering test: {n} C pairs, Spearman rho {r:+.3f}, shuffle p(|rho|>=obs) {p:.3f}')


if __name__ == '__main__':
    main()
