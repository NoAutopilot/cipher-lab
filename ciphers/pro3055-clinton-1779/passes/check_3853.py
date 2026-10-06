#!/usr/bin/env python3
"""Item 3853 (Robertson to Haldimand, 31 Oct 1781): the B.147 p.406 cipher (H-1649 Image 1056) checked against the f.381
decipherment as printed in 1920 vol. III doc. (260) p.214 (p381_print1920.txt), on the 1778 Army List title-page key
(R15-CLIN3853, 6 Oct 2026; pre-registered in ../PREREG_R15-CLIN3853.md).

Alignment (pre-registered, letters never used): units = cipher words (cells split at the copyist's rules) and glosses
(their own words); Needleman-Wunsch of units against printed words, gloss word +2 on an equal printed word, cipher word +1
on a printed word of equal letter count, gaps -1, free leading/trailing printed words. Equal-count pairs compared cell by
cell; cipher words on a gap are reported with their letters (text beyond the extract), printed words on a gap likewise.
Variants: (a) printed page, (b) line 1 BY PERMISION ... HONORABLE (GATED), (c) (b) + line 9 OFICERS. Control: printed
letters of the aligned span shuffled, 1000 seeds, seed 3853, scored under (b). Gate: (b) share >= 0.80 and > control max.
p.407 (Image 1058) is scored the same way from p407_*.tsv (R15-CLIN407, ../PREREG_R15-CLIN407.md).
Usage: check_3853.py [--check]   (writes check_3853.json; --check exits 1 when it is stale, rule 7)."""
import json, os, random, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
sys.path.insert(0, ROOT)
from check_2380_c37 import rows, chars  # noqa: E402

OCR = {'(Sir': 'Sir', 'will1': 'will', 'youj': 'your', '1': 'I'}
GLOSS_NORM = {'&': 'and'}


def print_words():
    lines = [l for l in open(P('p381_print1920.txt'), encoding='utf-8') if not l.startswith('#')]
    txt = ' '.join(lines[lines.index(next(l for l in lines if l.startswith('Sir'))):])
    txt = txt.split('Ever')[0].replace('—', ' ')
    return [w for w in (chars(OCR.get(t, t)) if not re.fullmatch(r'\d+(th)?\W*', t) else re.sub(r'\W', '', t)
                        for t in txt.split()) if w]


def units(path):
    out, cur, line = [], [], None
    for r in rows(path):
        e = r['entry'].replace('[?]', '').strip()
        bar = e.endswith('|')
        e = e.rstrip('|').strip()
        if e.startswith('"'):
            if cur:
                out.append(('c', cur)); cur = []
            for w in e.strip('"').split():
                out.append(('g', GLOSS_NORM.get(w, re.sub(r'[^a-z0-9]', '', w.lower()))))
            continue
        a, b = e.split('-')
        line = int(a) if a else line
        cur.append((line, int(b), r['col'] + ':' + r['idx']))
        if bar:
            out.append(('c', cur)); cur = []
    if cur:
        out.append(('c', cur))
    return out


def sc(u, w):
    if u[0] == 'g':
        return 2 if u[1] == w else 0
    return 1 if len(u[1]) == len(w) else 0


def nw(us, ws):
    n, m = len(us), len(ws)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0] = -i
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + sc(us[i - 1], ws[j - 1]), S[i - 1][j] - 1, S[i][j - 1] - 1)
    j = max(range(m + 1), key=lambda k: S[n][k])
    jend, i, pairs = j, n, []
    while i > 0:
        if j > 0 and S[i][j] == S[i - 1][j - 1] + sc(us[i - 1], ws[j - 1]):
            pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif S[i][j] == S[i - 1][j] - 1:
            pairs.append((i - 1, None)); i -= 1
        else:
            pairs.append((None, j - 1)); j -= 1
    return pairs[::-1], j, jend


def build(src='p406_reconciled.tsv'):
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    vb = list(title); vb[0] = chars('BY PERMISION of the RIGHT HONORABLE')
    vc = list(vb); vc[8] = chars('OFICERS in the several REGIMENTS')
    let = lambda T, c: T[c[0] - 1][c[1] - 1] if c[0] <= len(T) and c[1] <= len(T[c[0] - 1]) else '?'
    ws = print_words()
    us = units(P(src))
    pairs, j0, j1 = nw(us, ws)
    comp, apart, beyond, extract_more, gloss = [], [], [], [], []
    for i, j in pairs:
        u = us[i] if i is not None else None
        w = ws[j] if j is not None else None
        if u is None:
            extract_more.append(w); continue
        if u[0] == 'g':
            gloss.append({'gloss': u[1], 'print': w, 'equal': u[1] == w}); continue
        rd = ''.join(let(vb, c) for c in u[1])
        if w is None:
            beyond.append({'cells': ' '.join(f'{c[2]}={c[0]}-{c[1]}' for c in u[1]), 'letters_b': rd}); continue
        if len(u[1]) == len(w):
            comp += list(zip(u[1], w))
        else:
            apart.append({'print': w, 'letters_b': rd, 'cells': ' '.join(f'{c[0]}-{c[1]}' for c in u[1])})
    span = [c for w in ws[j0:j1] for c in w if c.isalpha()]
    def count(T):
        return sum(1 for c, x in comp if let(T, c) == x or (x == 'j' and let(T, c) == 'i'))
    b = count(vb)
    rng = random.Random(3853)
    null = []
    for _ in range(1000):
        sh = span[:]
        rng.shuffle(sh)
        null.append(sum(1 for (c, _), y in zip(comp, sh) if let(vb, c) == y))
    null.sort()
    res = {'source': src, 'units': len(us), 'cells': sum(len(u[1]) for u in us if u[0] == 'c'),
           'print_span': ' '.join(ws[j0:j1]), 'print_words_after_span': ' '.join(ws[j1:]),
           'compared_cells': len(comp), 'a_printed_page': count(title), 'b_gated': b,
           'b_share': round(b / len(comp), 3) if comp else 0, 'c_secondary': count(vc),
           'control_b': {'seeds': 1000, 'mean': round(sum(null) / 1000, 2), 'p95': null[949], 'max': null[-1]},
           'gate_pass': bool(comp) and b / len(comp) >= 0.80 and b > null[-1],
           'mismatches_b': [f"{c[2]} {c[0]}-{c[1]} key {let(vb, c)} / print {x}" for c, x in comp
                            if not (let(vb, c) == x or (x == 'j' and let(vb, c) == 'i'))],
           'apart': apart, 'cipher_words_on_gap': beyond, 'print_words_on_gap_inside_span': extract_more,
           'glosses': gloss,
           'reading_b': ' '.join((''.join(let(vb, c) for c in u[1]) if u[0] == 'c' else u[1].upper()) for u in us)}
    return res


def main():
    out = {'pass_A': build('p406_passA.tsv')}
    if os.path.exists(P('p406_reconciled.tsv')):
        out['reconciled'] = build()
    # p.407 (H-1649 Image 1058), the cipher continued (R15-CLIN407, 6 Oct 2026; PREREG_R15-CLIN407.md), scored apart
    for k, f in (('p407_pass_A', 'p407_passA.tsv'), ('p407_reconciled', 'p407_reconciled.tsv')):
        if os.path.exists(P(f)):
            out[k] = build(f)
    js = json.dumps(out, indent=1) + '\n'
    p = P('check_3853.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p, encoding='utf-8').read() == js
        print('check_3853: ' + ('OK' if ok else 'FAIL (STALE check_3853.json)'))
        sys.exit(0 if ok else 1)
    open(p, 'w', encoding='utf-8').write(js)
    print(js)


if __name__ == '__main__':
    main()
