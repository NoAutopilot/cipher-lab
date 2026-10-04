#!/usr/bin/env python3
"""N7-VIV54L: PREREG-N7VIV54L (ii) -- longest repair-free stretches of a decode, with a letter-order-shuffle control.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_stretch.py [--tsv reading.tsv] [--draws 200] [--top 10] [--strict]

--strict is a POST-HOC variant added after the registered vocabulary proved non-discriminating (its own shuffle control
equals the real value); descriptive only.

Vocabulary: words of length >= 2 seen >= 3 times in tools/data/fr16 (PREREG-N6VIV63's files), plus a, y, o; lowercase, accents
folded, u/v and i/j folded to u and i. A stretch = maximal substring of a page's line-joined decode ('_' = U breaks it) that a DP
splits entirely into vocabulary words, at least 3 words; per page, greedy longest-first, non-overlapping. Word division is the only
liberty applied; M letters inside are counted. Control: the same longest-stretch statistic on letter-order shuffles of each page's
decode (seed "20261054L-stretch"). Lists, never judges: whether a stretch is a clause is the auditor's call (rule 4a).
"""
import os, random, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t  # noqa: E402  (FR16 file list)

MAXW = 14


def fold(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('v', 'u').replace('j', 'i')


def vocab():
    from collections import Counter
    c = Counter()
    for p in t.FR16:
        c.update(w for w in re.findall(r'[a-z]+', fold(open(p, encoding='utf-8', errors='ignore').read())) if len(w) >= 2)
    if '--strict' in sys.argv:   # POST-HOC variant (not in the PREREG): words >= 3 letters + listed 1-2 letter French words only
        return {w for w, n in c.items() if n >= 3 and 3 <= len(w) <= MAXW} | STRICT_SHORT
    return {w for w, n in c.items() if n >= 3 and len(w) <= MAXW} | {'a', 'y', 'o'}


STRICT_SHORT = {'a', 'y', 'o', 'de', 'le', 'la', 'et', 'en', 'il', 'ne', 'se', 'ce', 'si', 'au', 'un', 'on', 'ou', 'du', 'me', 'te',
                'ma', 'sa', 'ta', 'qu', 'or', 'ia', 'es', 'est'}


def best_cover(s, V):
    """For every start i: longest end j such that s[i:j] splits into >= 3 vocab words; returns (i, j, words)."""
    n, best = len(s), None
    for i in range(n):
        # reach[j] = min/max word count partition of s[i:j]; keep max words to prefer reaching >= 3
        reach = {i: []}
        for j in range(i, n):
            if j not in reach:
                continue
            for L in range(1, MAXW + 1):
                if j + L > n:
                    break
                w = s[j:j + L]
                if w in V and (j + L not in reach or len(reach[j + L]) < len(reach[j]) + 1):
                    reach[j + L] = reach[j] + [w]
        cands = [(e, ws) for e, ws in reach.items() if len(ws) >= 3]
        if cands:
            e, ws = max(cands, key=lambda x: (x[0], -len(x[1])))
            if best is None or e - i > best[1] - best[0]:
                best = (i, e, ws)
    return best


def stretches(s, V, top):
    """Greedy longest-first non-overlapping stretches over a string with '_' breaks."""
    out, segs = [], [(m.start(), m.group()) for m in re.finditer(r'[^_]+', s)]
    pool = [(off, seg) for off, seg in segs]
    while pool and len(out) < top:
        found = []
        for off, seg in pool:
            b = best_cover(seg, V)
            if b:
                found.append((b[1] - b[0], off, seg, b))
        if not found:
            break
        L, off, seg, (i, e, ws) = max(found, key=lambda x: x[0])
        out.append((off + i, off + e, ws))
        pool.remove((off, seg))
        pool += [(off, seg[:i]), (off + e, seg[e:])]
        pool = [(o, x) for o, x in pool if len(x) >= 3]
    return out


def pages(tsv):
    P = {}
    for ln in open(tsv, encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'page':
            continue
        d, g = P.setdefault(f[0], ['', ''])
        P[f[0]] = [d + f[3], g + f[4]]
    return P


def main():
    tsv = sys.argv[sys.argv.index('--tsv') + 1] if '--tsv' in sys.argv else os.path.join(T, 'reading_piece54_L.tsv')
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    top = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 10
    V = vocab()
    rows = []
    for page, (dec, gr) in pages(tsv).items():
        for a, b, ws in stretches(dec, V, top):
            rows.append((b - a, page, a, ' '.join(ws), len(ws), gr[a:b].count('M'), sum(len(w) <= 2 for w in ws)))
    rows.sort(reverse=True)
    print(f'{os.path.basename(tsv)}: vocabulary {len(V)} words')
    print('letters\tpage\toffset\twords\tn_words\tM_inside\tshort_words(<=2)')
    for r in rows[:top]:
        print('\t'.join(map(str, r)))
    rng = random.Random('20261054L-stretch'); null = []
    for _ in range(draws):
        m = 0
        for page, (dec, gr) in pages(tsv).items():
            L = [c for c in dec if c != '_']; rng.shuffle(L); it = iter(L)
            sh = ''.join(c if c == '_' else next(it) for c in dec)
            b = stretches(sh, V, 1)
            m = max(m, (b[0][1] - b[0][0]) if b else 0)
        null.append(m)
    null.sort()
    print(f'control (letter-order shuffles, {draws}): longest-stretch median {null[len(null)//2]}, '
          f'p99 {null[min(len(null)-1, int(0.99*len(null)))]}, max {null[-1]}; real longest {rows[0][0] if rows else 0}')


if __name__ == '__main__':
    main()
