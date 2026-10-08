#!/usr/bin/env python3
"""B.148 p.123 (H-1649 Image 1205), the cipher copy of Carleton to Haldimand, New York, 25 Sept 1782: all six columns checked
against the period decipherment (p.102, p102_reading.txt) on the 1778 title-page key (D4-CLIN, 8 Oct 2026; pre-registered in
../PREREG_D4-CLIN.md before this script was run). GAPS7 checked only the 32 opening pairs of column 1 (check_p102.py).

Input: p123_full_reconciled.tsv (col, idx, kind, entry, underline, gloss, grade, passA, passB, note): two blind Sonnet passes
on the column crops of cut_2380_p121_122.py (Image 1205, SHEAR=0.012 PAD=0), reconciled by the worker on zoomed crops.
kind (read from the page, never from the decipherment): letter (x/+ L-P or -P), word (a full pair without x: a 1782 word-code
element), head (column 1's 3-4), clear (a plain-text word on the page). An underline ends a word; a word code is a word alone.
Rows graded M are dropped from the compared set (their word is reported apart).

Alignment (lengths only): "Each column is continued on the page following", so each column is aligned on its own to the whole
decipherment word list by check_2380_c37.py's Needleman-Wunsch shape with free leading/trailing words: +1 when a letter word's
cell count equals the decipherment word's length written out or with doubled letters once, 0 for a word code or a mismatch,
gap -1. Best and runner-up end positions are reported per column. Equal-count pairs are compared cell by cell.

Statistics: (a) printed page; (b) line 1 = "BY PERMISION of the RIGHT HONORABLE" -- GATED; (c) (b) + line 9 "OFICERS in the
several REGIMENTS"; (d) (c) + doubled-figure cells. Control: body letters shuffled, 1000 seeds, seed 123, same positions.
Gate: (b) share >= 0.80 and (b) count > control max. Word codes: aligned word per code, repeats, glosses. Output
check_p123_full.json; --check exits 1 when stale (rule 7).
"""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
chars = lambda s: re.sub(r'[^a-z&0-9]', '', s.lower())
collapse = lambda w: re.sub(r'(.)\1+', r'\1', w)


def rows(path):
    out, hdr = [], None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t')
        if hdr is None:
            hdr = parts; continue
        out.append(dict(zip(hdr, parts + [''] * (len(hdr) - len(parts)))))
    return out


def page_letter(T, l, p, dbl=False):
    if l < 1 or l > len(T):
        return '?'
    t = T[l - 1]
    if p <= len(t):
        return t[p - 1]
    s = str(p)
    if dbl and len(set(s)) == 1 and len(s) > 1 and int(s[0]) <= len(t):
        return t[int(s[0]) - 1]
    return '?'


def tokens(cells):
    """Per column: list of ('L', [(line, pos, ref, grade)]) letter words and ('W', code, gloss, ref) word codes."""
    out, cur, line = [], [], None
    for c in cells:
        k = c['kind']
        if k in ('head', 'clear', 'skip'):
            continue
        ref = f"{c['col']}:{c['idx']}"
        if k == 'word':
            if cur: out.append(('L', cur)); cur = []
            out.append(('W', c['entry'], c['gloss'], ref)); continue
        a, b = c['entry'].lstrip('x+').split('-')
        if a:
            line = int(a)
        cur.append((line, int(b), ref, c['grade']))
        if c['underline'] == 'y':
            out.append(('L', cur)); cur = []
    if cur:
        out.append(('L', cur))
    return out


def fits(n, w):
    return n == len(w) or n == len(collapse(w))


def nw(tk, dw):
    n, m = len(tk), len(dw)
    sc = lambda t, w: 1 if t[0] == 'L' and fits(len(t[1]), w) else 0
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + sc(tk[i - 1], dw[j - 1]), S[i - 1][j] - 1, S[i][j - 1] - 1)
    ends = sorted(range(m + 1), key=lambda k: -S[n][k])
    j = ends[0]
    runner = max((S[n][k] for k in range(m + 1) if abs(k - j) >= 3), default=None)
    best = S[n][j]
    i, pairs = n, []
    while i > 0 and j > 0:
        if S[i][j] == S[i - 1][j - 1] + sc(tk[i - 1], dw[j - 1]):
            pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif S[i][j] == S[i - 1][j] - 1:
            pairs.append((i - 1, None)); i -= 1
        else:
            pairs.append((None, j - 1)); j -= 1
    while i > 0:
        pairs.append((i - 1, None)); i -= 1
    return pairs[::-1], best, runner


def b2(cells, title_b, dw_letters, seed=123, seeds=1000):
    """Addendum B (PREREG_D4-CLIN.md): decode H letter cells on the key, runs split at underlines and word codes; a run of >= 3
    cells is a hit when its decoded string is a substring of the decipherment letters. Control: page characters permuted."""
    runs, cur, line = [], [], None
    for c in cells:
        k = c['kind']
        if k in ('head', 'clear', 'skip'):
            continue
        if k == 'word':
            if cur: runs.append(cur); cur = []
            continue
        a, b = c['entry'].lstrip('x+').split('-')
        if a:
            line = int(a)
        cur.append((line, int(b), c['grade'], f"{c['col']}:{c['idx']}"))
        if c['underline'] == 'y':
            runs.append(cur); cur = []
    if cur:
        runs.append(cur)
    runs = [r for r in runs if len(r) >= 3 and all(g == 'H' for _, _, g, _ in r)]
    dec = lambda T, r: ''.join(page_letter(T, l, p) for l, p, *_ in r)
    hits = lambda T: sum(1 for r in runs if '?' not in dec(T, r) and dec(T, r) in dw_letters)
    h = hits(title_b)
    lens = [len(t) for t in title_b]; flat = list(''.join(title_b)); rng = random.Random(seed); ctl = []
    for _ in range(seeds):
        rng.shuffle(flat); T, o = [], 0
        for n in lens:
            T.append(''.join(flat[o:o + n])); o += n
        ctl.append(hits(T))
    ctl.sort()
    return {'runs_ge3': len(runs), 'hits': h, 'share': round(h / len(runs), 3) if runs else 0,
            'control_page_permuted': {'seeds': seeds, 'mean': round(sum(ctl) / seeds, 2), 'p95': ctl[int(seeds * .95) - 1], 'max': ctl[-1]},
            'gate': 'PASS' if runs and h / len(runs) >= 0.60 and h > ctl[-1] else 'FAIL',
            'decoded_runs': [{'start': r[0][3], 'cells': ' '.join(f'{l}-{p}' for l, p, *_ in r), 'decoded': dec(title_b, r),
                              'hit': '?' not in dec(title_b, r) and dec(title_b, r) in dw_letters} for r in runs]}


def build():
    body = [l.rstrip('\n') for l in open(P('p102_reading.txt'), encoding='utf-8') if not l.startswith('#')]
    text = ' '.join(body).replace('con. tributed', 'contributed').replace('Ver. plank', 'Verplank').replace('^', '')
    text = text.replace('(Signed)', '')
    dw = [w for w in (chars(x) for x in text.split()) if w]
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    vb = list(title); vb[0] = chars('BY PERMISION of the RIGHT HONORABLE')
    vc = list(vb); vc[8] = chars('OFICERS in the several REGIMENTS')
    T = {'a': (title, False), 'b': (vb, False), 'c': (vc, False), 'd': (vc, True)}
    cells = rows(P('p123_full_reconciled.tsv'))
    cols = sorted({c['col'] for c in cells})
    compared, apart, unpaired, codes, spans = [], [], [], [], {}
    for col in cols:
        tk = tokens([c for c in cells if c['col'] == col])
        pairs, best, runner = nw(tk, dw)
        js = [j for i, j in pairs if i is not None and j is not None]
        spans[col] = {'tokens': len(tk), 'letter_cells': sum(len(t[1]) for t in tk if t[0] == 'L'),
                      'word_codes': sum(1 for t in tk if t[0] == 'W'), 'score': best, 'runner_up_score': runner,
                      'decipherment_span': [min(js), max(js)] if js else None,
                      'span_words': ' '.join(dw[min(js):max(js) + 1]) if js else ''}
        for i, j in pairs:
            if i is None:
                if spans[col]['decipherment_span'] and spans[col]['decipherment_span'][0] <= j <= spans[col]['decipherment_span'][1]:
                    unpaired.append({'col': col, 'decipherment_word_without_cipher': dw[j]})
                continue
            t = tk[i]
            if t[0] == 'W':
                codes.append({'col': col, 'code': t[1], 'gloss': t[2], 'ref': t[3], 'aligned_word': dw[j] if j is not None else None})
                continue
            c = t[1]
            pl = ''.join(page_letter(vc, l, p, True) for l, p, *_ in c)
            if j is None:
                unpaired.append({'col': col, 'cipher_word_without_decipherment': [f'{l}-{p}' for l, p, *_ in c], 'page_letters_d': pl}); continue
            w = dw[j]
            if not fits(len(c), w):
                apart.append({'col': col, 'decipherment_word': w, 'cells': [f'{l}-{p}' for l, p, *_ in c], 'page_letters_d': pl}); continue
            ww = w if len(c) == len(w) else collapse(w)
            for (l, p, ref, g), ch in zip(c, ww):
                if g == 'M':
                    continue
                compared.append((l, p, ch, w, ref))
    score = lambda k, letters: sum(1 for (l, p, *_), ch in zip(compared, letters) if page_letter(T[k][0], l, p, T[k][1]) == ch)
    want = [x[2] for x in compared]
    S = {k: score(k, want) for k in T}
    pool = [ch for ch in chars(' '.join(body)) if ch.isalpha() or ch == '&']
    rng = random.Random(123); ctl = {k: [] for k in 'bcd'}
    for _ in range(1000):
        rng.shuffle(pool)
        for k in 'bcd':
            ctl[k].append(score(k, pool[:len(compared)]))
    for k in ctl: ctl[k].sort()
    n = len(compared)
    mism = [{'cell': f'{l}-{p}', 'at': ref, 'want': ch, 'page_d': page_letter(vc, l, p, True), 'word': w,
             'found_at_offset_c': [k for k in (-2, -1, 1, 2) if 1 <= l <= len(vc) and 0 <= p - 1 + k < len(vc[l - 1]) and vc[l - 1][p - 1 + k] == ch]}
            for l, p, ch, w, ref in compared if page_letter(vc, l, p, True) != ch]
    bycode = {}
    for c in codes:
        bycode.setdefault(c['code'], []).append(c['aligned_word'])
    grades = {}
    for c in cells:
        if c['kind'] in ('letter', 'word'):
            grades[c['grade']] = grades.get(c['grade'], 0) + 1
    out = {'source': 'H-1649 Image 1205 (B.148 p.123) full/max, columns cut by cut_2380_p121_122.py (SHEAR=0.012 PAD=0)',
           'cells_letter_and_word': sum(grades.values()), 'cell_grades': grades,
           'compared_cells': n, 'a_printed_page': S['a'], 'b_line1_variant_GATED': S['b'], 'c_plus_line9_OFICERS': S['c'],
           'd_plus_doubled_figures': S['d'], 'share_b': round(S['b'] / n, 3) if n else 0,
           'share_c': round(S['c'] / n, 3) if n else 0, 'share_d': round(S['d'] / n, 3) if n else 0,
           'control': {k: {'seeds': 1000, 'mean': round(sum(v) / 1000, 2), 'p95': v[949], 'max': v[-1]} for k, v in ctl.items()},
           'gate': 'PASS' if n and S['b'] / n >= 0.80 and S['b'] > ctl['b'][-1] else 'FAIL',
           'addendum_B2_decode_shuffled_key': b2(cells, vb, ''.join(c for c in ''.join(dw) if c.isalpha() or c == '&')),
           'columns': spans, 'word_codes': codes, 'word_codes_by_code': bycode,
           'mismatches_under_d': mism, 'pairs_apart_count_differs': apart, 'unpaired_inside_span': unpaired}
    return json.dumps(out, indent=1) + '\n'


def main():
    js = build(); path = P('check_p123_full.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_p123_full: ' + ('OK' if ok else 'FAIL (STALE check_p123_full.json)')); sys.exit(0 if ok else 1)
    if '--dry' not in sys.argv:
        open(path, 'w', encoding='utf-8').write(js)
    d = json.loads(js)
    print({k: d[k] for k in list(d)[:12]}); B = d['addendum_B2_decode_shuffled_key']; print({k: B[k] for k in list(B)[:5]})
    for r in B['decoded_runs']: print(r['start'], r['decoded'], r['hit'])
    for col, s in d['columns'].items(): print(col, s)
    print(len(d['mismatches_under_d']), 'mismatches;', len(d['pairs_apart_count_differs']), 'apart;', len(d['unpaired_inside_span']), 'unpaired')


if __name__ == '__main__':
    main()
