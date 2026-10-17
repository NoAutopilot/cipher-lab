#!/usr/bin/env python3
"""VIV-KCELLS2 (PREREG-VIV-KCELLS2.md): trial cells c=p, 2=m on inks 63/53/54 against value-shuffled and swapped nulls.

    python3 tx/kcells2/kcells2.py [--out tx/kcells2/result.json]

Order as registered: K0 before, K1 20 value-shuffles, K2 swapped (c=m, 2=p), then K3 real (c=p, 2=m). No key.tsv edit.
"""
import csv, json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); TX = os.path.dirname(H); T = os.path.dirname(TX); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, TX); sys.path.insert(0, os.path.join(ROOT, 'tools'))
sv = sys.argv; sys.argv = [sv[0], '--strict']
import viv54L_stretch as vs  # noqa: E402
import viv63_decode as v63  # noqa: E402
import judge_plaintext as jp  # noqa: E402
V = vs.vocab(); sys.argv = sv
FR16 = [os.path.join(ROOT, 'tools/data/fr16', f) for f in
        ('lettresdecatheri01cathuoft_djvu.txt.gz', 'lettresdecatheri02cathuoft_djvu.txt.gz', 'lettresindites00marg_djvu.txt.gz')]
ALPHA = 'abcdefghiklnoqrstuxyz'


def streams():
    """Per ink: list of (page, code, flag)."""
    out = {'63': [(p, c, f) for p, _, seq in v63.lines() for c, f in seq]}
    for ink in ('53', '54'):
        out[ink] = [(r['page'], c, False) for r in csv.DictReader(open(os.path.join(T, f'reading_piece{ink}.tsv')), delimiter='\t')
                    for c in r['codes'].split()]
    return out


def tsv_grades(ink):
    return ''.join(r['grades'] for r in csv.DictReader(open(os.path.join(T, f'reading_piece{ink}.tsv')), delimiter='\t'))


def decode(stream, k, trial, ink):
    letters, grades = [], []
    tg = tsv_grades(ink) if ink != '63' else None
    for i, (pg, c, f) in enumerate(stream):
        if c in trial:
            letters.append(trial[c]); grades.append('M' if f else 'H')
        elif c in k:
            letters.append(k[c][0]); grades.append(tg[i] if tg else ('M' if (f or k[c][1] == 'M') else 'H'))
        else:
            letters.append('_'); grades.append('U')
    return letters, grades


def hrun(grades):
    b = cur = 0
    for g in grades:
        cur = cur + 1 if g == 'H' else 0; b = max(b, cur)
    return b


def vstr(stream, letters, grades, mask):
    pages = {}
    for (pg, _, _), l, g in zip(stream, letters, grades):
        pages[pg] = pages.get(pg, '') + (l if (g == 'H' or not mask) else '_')
    best, where = 0, None
    for pg, s in pages.items():
        st = vs.stretches(s, V, 1)
        if st and st[0][1] - st[0][0] > best:
            best, where = st[0][1] - st[0][0], (pg, st[0][0], st[0][1], s[st[0][0]:st[0][1]], st[0][2])
    return best, where


def measure(stream, k, trial, ink, model, b2=False):
    L, G = decode(stream, k, trial, ink)
    txt = ''.join(l for l in L if l != '_')
    hv, wh = vstr(stream, L, G, True)
    r = {'trial': trial, 'hrun': hrun(G), 'hrunV': hv, 'hrunV_where': wh, 'v_strict': vstr(stream, L, G, False)[0],
         's': round(model.score(txt), 4), 'H': G.count('H'), 'tokens': len(G)}
    if b2:
        rng = random.Random(f'VIV-KCELLS2-b2-{ink}-{trial}'); nl = []
        for _ in range(200):
            x = list(txt); rng.shuffle(x); nl.append(model.score(''.join(x)))
        nl.sort(); r['b2_order_p99'] = round(jp.pct(nl, 0.99), 4)
    return r


def main():
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(H, 'result.json')
    k = {c: (v, g) for c, (v, g) in v63.vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in FR16])
    S = streams(); res = {}
    # before-check: the route reproduces reading_piece63.tsv grades
    L, G = decode(S['63'], k, {}, '63')
    assert ''.join(G) == tsv_grades('63'), 'ink 63 route does not reproduce reading_piece63.tsv'
    for ink in ('63', '53', '54'):
        st = S[ink]; r = {'K0_before': measure(st, k, {}, ink, model, True)}
        sh = []
        for i in range(20):
            rng = random.Random(f'VIV-KCELLS2-shuf-{i}')
            sh.append(measure(st, k, {'c': rng.choice(ALPHA), '2': rng.choice(ALPHA)}, ink, model))
        r['K1_shuffle'] = sh
        for stat in ('hrunV', 's', 'v_strict', 'hrun'):
            r[f'K1_p99_{stat}'] = round(jp.pct(sorted(x[stat] for x in sh), 0.99), 4)
        r['K2_swap'] = measure(st, k, {'c': 'm', '2': 'p'}, ink, model)
        r['K3_real'] = measure(st, k, {'c': 'p', '2': 'm'}, ink, model, True)
        K3, K2 = r['K3_real'], r['K2_swap']
        r['pass'] = (K3['hrunV'] > r['K1_p99_hrunV'] and K3['s'] > r['K1_p99_s'] and K3['hrunV'] > K2['hrunV'] and K3['s'] > K2['s'])
        res[ink] = r
        print(ink, json.dumps({x: r[x] for x in r if x != 'K1_shuffle'}, default=str), flush=True)
    json.dump(res, open(out, 'w'), indent=1, default=str)


if __name__ == '__main__':
    main()
