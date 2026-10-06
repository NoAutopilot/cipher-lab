#!/usr/bin/env python3
"""Item 2380: B.147 p.121 (H-1649 Image 759) cipher cells checked against the period decipherment (pp.134-135) on the
1778 title-page key (R11-CLIN2380B, 6 Oct 2026; pre-registered in ../PREREG_R11-CLIN2380B.md, pushed 4aa284973).

Inputs: p121_reconciled.tsv (entry column), p120_cells.tsv + p120_c37_reconciled.tsv (to carry the line figure and find
where p.120's alignment stopped), p134_reading.txt, title1778_reading.txt. Alignment and helpers are check_2380_c37.py's
(lengths only, never letters). p.121's cipher words are aligned to the decipherment words after p.120's last aligned word.

Statistics: (a) printed page; (b) line 1 = "BY PERMISION of the RIGHT HONORABLE" (GATED: share >= 0.80 and count > control
max); (c) (b) + line 9 = "OFICERS in the several REGIMENTS"; (d) (c) + doubled-figure cells (L-PP, digits repeat, P beyond
the line) read as the letter at single P. Control: decipherment body letters shuffled, 1000 seeds, seed 2380, at the same
compared positions, scored under (b), (c), (d). Output check_2380_p121.json; --check exits 1 when stale (rule 7).
"""
import json, os, random, sys
import check_2380_c37 as C

P = C.P


def page_letter(T, l, p, dbl=False):
    t = T[l - 1]
    if p <= len(t):
        return t[p - 1]
    s = str(p)
    if dbl and len(set(s)) == 1 and len(s) > 1 and int(s[0]) <= len(t):
        return t[int(s[0]) - 1]
    return '?'


def build():
    body = [l.rstrip('\n') for l in open(P('p134_reading.txt'), encoding='utf-8') if not l.startswith('#')]
    body = body[:body.index('')]
    dw = [w for w in (C.chars(x) for x in ' '.join(body).replace('19th July', ' JULYMARK ').split()) if w]
    title = [C.chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    vb = list(title); vb[0] = C.chars('BY PERMISION of the RIGHT HONORABLE')
    vc = list(vb); vc[8] = C.chars('OFICERS in the several REGIMENTS')
    # where p.120 stopped: rerun check_2380_c37's alignment
    w12, line = C.words(C.rows(P('p120_cells.tsv')))
    start = dw.index('julymark') + 1 + len(w12[w12.index('JULY') + 1:])
    rest37 = dw[start:]
    cw37, line = C.words(C.rows(P('p120_c37_reconciled.tsv')), line)
    last_j = max(j for i, j in C.nw(cw37, rest37) if i is not None and j is not None)
    start121 = start + last_j + 1
    rest = dw[start121:]
    cw, _ = C.words(C.rows(P('p121_reconciled.tsv')), line)
    pairs = C.nw(cw, rest)
    compared, apart, gaps = [], [], []
    for i, j in pairs:
        if i is None:
            gaps.append({'decipherment_word_without_cipher': rest[j]}); continue
        c = cw[i]
        pl = ''.join(page_letter(vc, l, p, True) for l, p, _ in c)
        if j is None:
            gaps.append({'cipher_word_without_decipherment': [f'{l}-{p}' for l, p, _ in c], 'page_letters_d': pl}); continue
        w = rest[j]
        if len(c) != len(C.collapse(w)):
            apart.append({'decipherment_word': w, 'cells': [f'{l}-{p}' for l, p, _ in c], 'page_letters_d': pl}); continue
        for (l, p, ix), ch in zip(c, C.collapse(w)):
            compared.append((l, p, ch, w, ix))
    T = {'a': (title, False), 'b': (vb, False), 'c': (vc, False), 'd': (vc, True)}
    score = lambda k, letters: sum(1 for (l, p, *_), ch in zip(compared, letters) if page_letter(T[k][0], l, p, T[k][1]) == ch)
    want = [x[2] for x in compared]
    S = {k: score(k, want) for k in T}
    pool = list(C.chars(' '.join(body))); rng = random.Random(2380); ctl = {k: [] for k in 'bcd'}
    for _ in range(1000):
        rng.shuffle(pool)
        for k in 'bcd':
            ctl[k].append(score(k, pool[:len(compared)]))
    for k in ctl: ctl[k].sort()
    n = len(compared)
    mism = [{'cell': f'{l}-{p}', 'at': ix, 'want': ch, 'page_d': page_letter(vc, l, p, True), 'word': w,
             'found_at_offset_c': [k for k in (-2, -1, 1, 2) if 0 <= p - 1 + k < len(vc[l - 1]) and vc[l - 1][p - 1 + k] == ch]}
            for l, p, ch, w, ix in compared if page_letter(vc, l, p, True) != ch]
    out = {'source': 'H-1649 Image 759 (B.147 p.121) full/max, columns cut by cut_2380_p121_122.py (SHEAR 0.025, PAD 30)',
           'cells_read': sum(len(x) for x in cw), 'cipher_words': len(cw), 'decipherment_words_from': start121,
           'first_decipherment_words': rest[:4], 'decipherment_words_available': len(rest),
           'compared_cells': n, 'a_printed_page': S['a'], 'b_line1_variant_GATED': S['b'], 'c_plus_line9_OFICERS': S['c'],
           'd_plus_doubled_figures': S['d'], 'share_b': round(S['b'] / n, 3) if n else 0,
           'share_c': round(S['c'] / n, 3) if n else 0, 'share_d': round(S['d'] / n, 3) if n else 0,
           'control': {k: {'seeds': 1000, 'mean': round(sum(v) / 1000, 2), 'p95': v[949], 'max': v[-1]} for k, v in ctl.items()},
           'gate': 'PASS' if n and S['b'] / n >= 0.80 and S['b'] > ctl['b'][-1] else 'FAIL',
           'mismatches_under_d': mism, 'pairs_apart_count_differs': apart, 'unpaired': gaps,
           'alignment': [[(' '.join(f'{l}-{p}' for l, p, _ in cw[i]) if i is not None else None), (rest[j] if j is not None else None)] for i, j in pairs]}
    return json.dumps(out, indent=1) + '\n'


def main():
    js = build(); path = P('check_2380_p121.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_2380_p121: ' + ('OK' if ok else 'FAIL (STALE check_2380_p121.json)')); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(js)
    d = json.loads(js); print({k: d[k] for k in list(d)[:16]}); print(len(d['mismatches_under_d']), 'mismatches;', len(d['pairs_apart_count_differs']), 'apart;', len(d['unpaired']), 'unpaired')


if __name__ == '__main__':
    main()
