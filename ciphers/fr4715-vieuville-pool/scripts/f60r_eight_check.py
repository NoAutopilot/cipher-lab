#!/usr/bin/env python3
"""GAPS-5 (2 Oct 2026): does a blind reader's '8' land where the inventory-only 8 rule (f60r_blocks.dp) puts one?

Lower block, pass A never writes the flicked open c as 8, pass B does (its own note). Segment pass A's digit stream
per line with the GAPS-4 segmenter, label each A zero P (first digit of an '8<' token: the rule says 8), F (second
digit of a key code x0: a true 0) or O (other), align A to B per line (difflib on bare digits), and cross-tabulate
the B reading at each A zero. Control (rule 3): the same table with the P/F labels shuffled among the A zeros, 10,000
times; the statistic is the share of B-8s among P minus among F.

    python3 scripts/f60r_eight_check.py
"""
import csv, difflib, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f60r_blocks as fb

W = fb.W


def stream(p):
    by = {}
    for r in csv.DictReader(open(os.path.join(W, 'f60r_lower_pass%s_long.tsv' % p), encoding='utf-8'), delimiter='\t'):
        by.setdefault(r['line'], []).append(r['token'])
    return by


def main():
    codes = fb.key_codes()
    A, B = stream('A'), stream('B')
    rows = []
    for L in fb.LOWER_LINES:
        ua, ub = A.get(L, []), B.get(L, [])
        toks = fb.segment_units(ua, codes)
        cls, ui = ['O'] * len(ua), 0
        for t in toks:
            width = 1 if (t.startswith('w:') or t in ('?', '♀', '▽')) else len(t.replace('8<', '8').lstrip('.'))
            if '8<' in t:
                cls[ui] = 'P'
            elif width == 2 and not t.startswith('.') and t[-1] == '0' and ua[ui + 1].lstrip('.=') == '0':
                cls[ui + 1] = 'F'
            ui += width
        sa = [u.lstrip('.=') for u in ua]; sb = [u.lstrip('.=') for u in ub]
        sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
        amap = {}
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op in ('equal', 'replace') and i2 - i1 == j2 - j1:
                for k in range(i2 - i1):
                    amap[i1 + k] = sb[j1 + k]
        for i, u in enumerate(sa):
            if u == '0' and i in amap:
                rows.append((L, i + 1, cls[i], amap[i]))
    tab = {}
    for _, _, c, b in rows:
        tab[(c, b)] = tab.get((c, b), 0) + 1
    def share(rs, c):
        n = [b for _, _, cc, b in rs if cc == c]
        return (sum(b == '8' for b in n) / len(n)) if n else 0.0, len(n)
    sp, nP = share(rows, 'P'); sf, nF = share(rows, 'F'); so, nO = share(rows, 'O')
    obs = sp - sf
    pf = [r for r in rows if r[2] in 'PF']; labels = [r[2] for r in pf]
    rng = random.Random(20261002); null = []
    for _ in range(10000):
        rng.shuffle(labels)
        sh = [(a, b_, l, d) for (a, b_, _, d), l in zip(pf, labels)]
        null.append(share(sh, 'P')[0] - share(sh, 'F')[0])
    null.sort()
    p = sum(x >= obs for x in null) / len(null)
    print('A zeros aligned to B: %d (P %d, F %d, other %d)' % (len(rows), nP, nF, nO))
    print('B reads 8 at: P %.3f (%d/%d), F %.3f (%d/%d), other %.3f (%d/%d)' % (
        sp, round(sp * nP), nP, sf, round(sf * nF), nF, so, round(so * nO), nO))
    print('table (class, B reading): ' + ', '.join('%s/%s %d' % (k[0], k[1], v) for k, v in sorted(tab.items())))
    print('statistic P-share minus F-share %.3f; shuffled P/F labels x10000: mean %.3f p95 %.3f max %.3f; p(>=obs) %.4f' % (
        obs, sum(null) / len(null), null[9500], null[-1], p))


if __name__ == '__main__':
    main()
