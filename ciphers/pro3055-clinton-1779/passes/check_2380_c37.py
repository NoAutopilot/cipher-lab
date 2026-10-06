#!/usr/bin/env python3
"""Item 2380: B.147 p.120 (H-1649 Image 758) cipher columns 3-7 checked against the period decipherment on pp.134-135
on the 1778 title-page key (R11-CLIN2380, 6 Oct 2026; pre-registered in ../PREREG_R11-CLIN2380.md).

Inputs: p120_c37_reconciled.tsv (col, idx, passA, entry, note: one blind Sonnet pass over ten column-half crops, re-read
by the worker on zoomed crops where a cell failed the key; "|" = underlined cell, a word end; "-P" repeats the previous
line figure), p120_cells.tsv (columns 1-2, GAPS9), p134_reading.txt (decipherment), title1778_reading.txt (key page).

Alignment (lengths only, never letters): the decipherment words after the 25 that GAPS9 aligned against columns 1-2 are
aligned to the cipher words of columns 3-7 by Needleman-Wunsch (+1 when the word's cell count equals the decipherment
word with doubled letters written once, 0 otherwise, gap -1). Equal-count pairs are compared cell by cell.

Statistic: compared cells whose page letter equals the decipherment letter, (a) printed page, (b) line 1 read as the GAPS9
variant "BY PERMISION of the RIGHT HONORABLE". Control: decipherment body letters shuffled (1000 seeds, seed 2380) at the
same positions, under (b). Gate: (b) share >= 0.80 and count > control max.
Output: check_2380_c37.json; --check exits 1 when stale (rule 7).
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)


def rows(path):
    out, hdr = [], None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if hdr is None:
            hdr = parts
            continue
        out.append(dict(zip(hdr, parts + [''] * (len(hdr) - len(parts)))))
    return out


chars = lambda s: re.sub(r'[^a-z&]', '', s.lower())
collapse = lambda w: re.sub(r'(.)\1+', r'\1', w)


def words(cells, line=None):
    out, cur = [], []
    for c in cells:
        e = c['entry'].strip().rstrip('?')
        end = e.endswith('|')
        e = e.rstrip('|').rstrip('?')
        if 'July' in e:
            out.append('JULY'); continue
        a, b = e.split('-')
        if a:
            line = int(a)
        cur.append((line, int(b), c['col'] + ':' + c['idx']))
        if end:
            out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out, line


def nw(cw, dw):
    n, m = len(cw), len(dw)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i
    for j in range(1, m + 1): S[0][j] = 0 if True else -j  # free leading/trailing decipherment words (text may run past the page)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s = 1 if len(cw[i - 1]) == len(collapse(dw[j - 1])) else 0
            S[i][j] = max(S[i - 1][j - 1] + s, S[i - 1][j] - 1, S[i][j - 1] - 1)
    j = max(range(m + 1), key=lambda k: S[n][k])
    i, pairs = n, []
    while i > 0 and j > 0:
        s = 1 if len(cw[i - 1]) == len(collapse(dw[j - 1])) else 0
        if S[i][j] == S[i - 1][j - 1] + s:
            pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif S[i][j] == S[i - 1][j] - 1:
            pairs.append((i - 1, None)); i -= 1
        else:
            pairs.append((None, j - 1)); j -= 1
    while i > 0:
        pairs.append((i - 1, None)); i -= 1
    return pairs[::-1]


def build():
    body = [l.rstrip('\n') for l in open(P('p134_reading.txt'), encoding='utf-8') if not l.startswith('#')]
    body = body[:body.index('')]
    dw = [w for w in (chars(x) for x in ' '.join(body).replace('19th July', ' JULYMARK ').split()) if w]
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    var = list(title); var[0] = chars('BY PERMISION of the RIGHT HONORABLE')
    w12, line = words(rows(P('p120_cells.tsv')))
    post = w12[w12.index('JULY') + 1:]
    start = dw.index('julymark') + 1 + len(post)
    rest = dw[start:]
    cells = rows(P('p120_c37_reconciled.tsv'))
    cw, _ = words(cells, line)
    pairs = nw(cw, rest)
    compared, apart, gaps = [], [], []
    for i, j in pairs:
        if i is None:
            gaps.append({'decipherment_word_without_cipher': rest[j]}); continue
        c = cw[i]
        pl = lambda T: ''.join(T[l - 1][p - 1] if p <= len(T[l - 1]) else '?' for l, p, _ in c)
        if j is None:
            gaps.append({'cipher_word_without_decipherment': [f'{l}-{p}' for l, p, _ in c], 'page_letters_variant': pl(var)}); continue
        w = rest[j]
        if len(c) != len(collapse(w)):
            apart.append({'decipherment_word': w, 'cells': [f'{l}-{p}' for l, p, _ in c], 'page_letters_variant': pl(var)}); continue
        for (l, p, ix), ch in zip(c, collapse(w)):
            compared.append((l, p, ch, w, ix))

    def score(T, letters):
        return sum(1 for (l, p, *_), ch in zip(compared, letters) if p <= len(T[l - 1]) and T[l - 1][p - 1] == ch)
    a = score(title, [x[2] for x in compared]); b = score(var, [x[2] for x in compared])
    pool = list(chars(' '.join(body))); rng = random.Random(2380); ctl = []
    for _ in range(1000):
        rng.shuffle(pool); ctl.append(score(var, pool[:len(compared)]))
    ctl.sort()
    mism = [{'cell': f'{l}-{p}', 'at': ix, 'want': ch, 'page_variant': var[l - 1][p - 1] if p <= len(var[l - 1]) else '?', 'word': w,
             'found_at_offset': [k for k in (-2, -1, 1, 2) if 0 <= p - 1 + k < len(var[l - 1]) and var[l - 1][p - 1 + k] == ch]}
            for l, p, ch, w, ix in compared if not (p <= len(var[l - 1]) and var[l - 1][p - 1] == ch)]
    n = len(compared)
    # reported apart from the gate (not pre-registered): cells L-PP whose two digits repeat and exceed the line, read as
    # the letter at P written twice (GAPS9's excluded 2-99, 2-44, 6-77 sit in "letters", "matross", "artillery")
    dbl = [{'cell': f'{l}-{p}', 'at': ix, 'want': ch, 'letter_at_single_P': var[l - 1][int(str(p)[0]) - 1], 'word': w}
           for l, p, ch, w, ix in compared if p > len(var[l - 1]) and len(str(p)) == 2 and str(p)[0] == str(p)[1]]
    var9 = list(var); var9[8] = chars('OFICERS in the several REGIMENTS')
    out = {'posthoc_not_gated_line9_OFICERS': score(var9, [x[2] for x in compared]), 'source': 'H-1649 Image 758 (B.147 p.120) full/max, columns 3-7 cut by PIL box (NOTES.md R11-CLIN2380)',
           'cells_read': sum(len(x) for x in cw), 'cipher_words': len(cw),
           'decipherment_words_from': start, 'decipherment_words_available': len(rest),
           'aligned_pairs_equal_count': sum(1 for i, j in pairs if i is not None and j is not None) - len(apart),
           'compared_cells': n, 'exact_printed_page': a, 'exact_line1_variant': b,
           'share_variant': round(b / n, 3) if n else 0,
           'control_variant': {'seeds': 1000, 'mean': round(sum(ctl) / 1000, 2), 'p95': ctl[949], 'max': ctl[-1]},
           'gate': 'PASS' if n and b / n >= 0.80 and b > ctl[-1] else 'FAIL',
           'doubled_figure_cells_not_in_gate': dbl,
           'mismatches': mism, 'pairs_apart_count_differs': apart, 'unpaired': gaps,
           'alignment': [[(' '.join(f'{l}-{p}' for l, p, _ in cw[i]) if i is not None else None), (rest[j] if j is not None else None)] for i, j in pairs]}
    return json.dumps(out, indent=1) + '\n'


def main():
    js = build(); path = P('check_2380_c37.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_2380_c37: ' + ('OK' if ok else 'FAIL (STALE check_2380_c37.json)')); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(js)
    d = json.loads(js); print({k: d[k] for k in list(d)[:12]}); print(len(d['mismatches']), 'mismatches;', len(d['pairs_apart_count_differs']), 'apart;', len(d['unpaired']), 'unpaired')


if __name__ == '__main__':
    main()
