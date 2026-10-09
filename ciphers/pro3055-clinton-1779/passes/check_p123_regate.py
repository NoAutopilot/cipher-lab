#!/usr/bin/env python3
"""B.148 p.123 re-gate (CLIN-RG, 9 Oct 2026; pre-registered in ../PREREG-CLIN-RG.md, pushed ab6288fc before this was run).
Second attempt of the whole-page key check after D4-CLIN (check_p123_full.py): class rule fixed (a full pair inside an open,
un-underlined letter word is a letter cell) and an anchored per-column alignment (start at the column's first decoded word).
Inputs as check_p123_full.py. Gate: compared >= 40, share (b) >= 0.80, count (b) > K max (page-permuted key) and > S max
(shuffled-column) when S passes its pre-scoring can-differ check (>= 0.95 of seeds). Output check_p123_regate.json;
--check exits 1 when stale (rule 7); --precheck prints only the S can-differ check (no score).
"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_p123_full import P, rows, page_letter, chars, collapse, fits

SEED, SEEDS = 123, 1000


def inputs():
    body = [l.rstrip('\n') for l in open(P('p102_reading.txt'), encoding='utf-8') if not l.startswith('#')]
    text = ' '.join(body).replace('con. tributed', 'contributed').replace('Ver. plank', 'Verplank').replace('^', '').replace('(Signed)', '')
    dw = [w for w in (chars(x) for x in text.split()) if w]
    title = [chars(l) for l in open(P('title1778_reading.txt'), encoding='utf-8') if not l.startswith('#') and l.strip()]
    vb = list(title); vb[0] = chars('BY PERMISION of the RIGHT HONORABLE')
    vc = list(vb); vc[8] = chars('OFICERS in the several REGIMENTS')
    return dw, {'a': (title, False), 'b': (vb, False), 'c': (vc, False), 'd': (vc, True)}, rows(P('p123_full_reconciled.tsv'))


def tokens(cells):
    """Step 1: class rule, resolve to (line, pos), split. Token = ('L', [(l, p, ref, grade)]) or ('W', code, ref)."""
    out, cur, line, prev, reclassed = [], [], None, None, []
    for c in cells:
        k = c['kind']
        if k in ('head', 'clear', 'skip'):
            continue
        ref = f"{c['col']}:{c['idx']}"
        if k == 'word' and prev is not None and prev['kind2'] == 'letter' and prev['underline'] == 'n':
            k = 'letter'; reclassed.append(ref + ' ' + c['entry'])
        c = dict(c, kind2=k); prev = c
        if k == 'word':
            if cur: out.append(('L', cur)); cur = []
            out.append(('W', c['entry'], ref)); continue
        e = c['entry'].lstrip('x+')
        a, b = e.split('-') if not e.startswith('-') else ('', e[1:])
        if a:
            line = int(a)
        cur.append((line, int(b), ref, c['grade']))
        if c['underline'] == 'y':
            out.append(('L', cur)); cur = []
    if cur:
        out.append(('L', cur))
    return out, reclassed


def dec(T, cells):
    return ''.join(page_letter(T[0], l, p, T[1]) for l, p, *_ in cells)


def anchors(cols_tk, dw, T):
    """Step 2: per column the first all-H letter token >= 3 cells decoding to a dw word; earliest occurrence after prior anchor."""
    out, last = {}, -1
    for col, tk in cols_tk:
        for i, t in enumerate(tk):
            if t[0] != 'L' or len(t[1]) < 3 or any(g != 'H' for *_, g in t[1]):
                continue
            s = dec(T, t[1])
            occ = [j for j, w in enumerate(dw) if s == w or s == collapse(w)]
            after = [j for j in occ if j > last]
            if after:
                out[col] = (i, after[0], s, len(occ)); last = after[0]; break
    return out


def sc(t, w):
    return 1 if t[0] == 'L' and fits(len(t[1]), w) else 0


def nw_fixed_start(tk, dw):
    """Align tk to dw with both starts fixed at index 0, trailing dw free. Returns [(i, j|None)] for tokens."""
    n, m = len(tk), len(dw)
    S = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i
    for j in range(1, m + 1): S[0][j] = -j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = max(S[i - 1][j - 1] + sc(tk[i - 1], dw[j - 1]), S[i - 1][j] - 1, S[i][j - 1] - 1)
    j = max(range(m + 1), key=lambda k: (S[n][k], -k)); i = n; pairs = []
    while i > 0:
        if j > 0 and S[i][j] == S[i - 1][j - 1] + sc(tk[i - 1], dw[j - 1]):
            pairs.append((i - 1, j - 1)); i -= 1; j -= 1
        elif S[i][j] == S[i - 1][j] - 1:
            pairs.append((i - 1, None)); i -= 1
        else:
            j -= 1
    return pairs[::-1]


def align_col(tk, ai, aj, dw):
    """Step 3: forward from the anchor, backward before it. Returns {token index: dw index}."""
    m = {}
    for i, j in nw_fixed_start(tk[ai + 1:], dw[aj + 1:]):
        if j is not None: m[ai + 1 + i] = aj + 1 + j
    pre, dpre = tk[:ai][::-1], dw[:aj][::-1]
    for i, j in nw_fixed_start(pre, dpre):
        if j is not None: m[ai - 1 - i] = aj - 1 - j
    return m


def compared_set(cols_tk, anc, dw):
    out = []
    for col, tk in cols_tk:
        if col not in anc:
            continue
        ai, aj = anc[col][0], anc[col][1]
        for i, j in sorted(align_col(tk, ai, aj, dw).items()):
            t = tk[i]
            if t[0] != 'L' or not fits(len(t[1]), dw[j]):
                continue
            w = dw[j]; ww = w if len(t[1]) == len(w) else collapse(w)
            out += [(l, p, ch, w, ref) for (l, p, ref, g), ch in zip(t[1], ww) if g == 'H']
    return out


def score(T, comp):
    return sum(1 for l, p, ch, *_ in comp if page_letter(T[0], l, p, T[1]) == ch)


def permuted_keys(vb):
    lens = [len(t) for t in vb]; flat = list(''.join(vb)); rng = random.Random(SEED)
    for _ in range(SEEDS):
        rng.shuffle(flat); T, o = [], 0
        for n in lens:
            T.append(''.join(flat[o:o + n])); o += n
        yield (T, False)


def shuffled_cols(cols_tk, anc):
    rng = random.Random(SEED)
    for _ in range(SEEDS):
        out = []
        for col, tk in cols_tk:
            if col not in anc:
                out.append((col, tk)); continue
            ai = anc[col][0]; rest = tk[:ai] + tk[ai + 1:]; rng.shuffle(rest)
            out.append((col, rest[:ai] + [tk[ai]] + rest[ai:]))
        yield out


def build(precheck=False):
    dw, T, cells = inputs()
    cols = sorted({c['col'] for c in cells})
    cols_tk, reclassed = [], []
    for col in cols:
        tk, rc = tokens([c for c in cells if c['col'] == col]); cols_tk.append((col, tk)); reclassed += rc
    anc = anchors(cols_tk, dw, T['b'])
    comp = compared_set(cols_tk, anc, dw)
    key = lambda cs: sorted((ref, ch) for l, p, ch, w, ref in cs)
    target_key = key(comp)
    S_sets = [compared_set(ct, anc, dw) for ct in shuffled_cols(cols_tk, anc)]
    differ = sum(1 for s in S_sets if key(s) != target_key) / SEEDS
    s_is_test = differ >= 0.95
    pre = {'reclassed_word_to_letter': reclassed,
           'anchors': {c: {'token_index': a[0], 'dw_index': a[1], 'word': a[2], 'occurrences_in_dw': a[3]} for c, a in anc.items()},
           'columns_without_anchor': [c for c in cols if c not in anc], 'compared_cells': len(comp),
           'S_can_differ_share': round(differ, 3), 'S_is_test': s_is_test}
    if precheck:
        return json.dumps(pre, indent=1) + '\n'
    n = len(comp); sb = score(T['b'], comp)
    K = sorted(score(Tk, comp) for Tk in permuted_keys(T['b'][0]))
    Kfull = []
    for Tk in permuted_keys(T['b'][0]):
        a2 = anchors(cols_tk, dw, Tk); c2 = compared_set(cols_tk, a2, dw); Kfull.append(score(Tk, c2))
    Kfull.sort()
    Ssc = sorted(score(T['b'], s) for s in S_sets)
    summ = lambda v: {'seeds': SEEDS, 'mean': round(sum(v) / SEEDS, 2), 'p95': v[int(SEEDS * .95) - 1], 'max': v[-1]}
    ok = n >= 40 and sb / n >= 0.80 and sb > K[-1] and (not s_is_test or sb > Ssc[-1])
    gate = 'NON-TEST (compared < 40)' if n < 40 else ('PASS' if ok else 'FAIL')
    mism = [{'at': ref, 'cell': f'{l}-{p}', 'want': ch, 'word': w, 'page_b': page_letter(T['b'][0], l, p)}
            for l, p, ch, w, ref in comp if page_letter(T['b'][0], l, p) != ch]
    per_col = {}
    for l, p, ch, w, ref in comp:
        c = ref.split(':')[0]; d = per_col.setdefault(c, [0, 0]); d[0] += 1; d[1] += page_letter(T['b'][0], l, p) == ch
    out = dict(pre, **{'a_printed_page': score(T['a'], comp), 'b_line1_variant_GATED': sb, 'c_plus_line9': score(T['c'], comp),
               'd_plus_doubled_figures': score(T['d'], comp), 'share_b': round(sb / n, 3) if n else 0,
               'per_column_b_compared_matched': per_col,
               'control_K_page_permuted_key': summ(K), 'control_K_full_pipeline_reanchored_not_gated': summ(Kfull),
               'control_S_shuffled_column': summ(Ssc), 'gate': gate, 'mismatches_b': mism})
    return json.dumps(out, indent=1) + '\n'


def main():
    if '--precheck' in sys.argv:
        print(build(precheck=True)); return
    js = build(); path = P('check_p123_regate.json')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == js
        print('check_p123_regate: ' + ('OK' if ok else 'FAIL (STALE check_p123_regate.json)')); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(js)
    d = json.loads(js); print(json.dumps({k: v for k, v in d.items() if k != 'mismatches_b'}, indent=1)); print(len(d['mismatches_b']), 'mismatches')


if __name__ == '__main__':
    main()
