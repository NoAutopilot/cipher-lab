#!/usr/bin/env python3
"""N6-VIV63B gates exactly as PREREG-N6VIV63B.md: b2 (vs letter-order-shuffle null p99) with positive controls C1 (f.103r) and
C2 (ink 54) first, on (i) the new pages alone and (ii) the whole piece; then the registered specificity check (200 wrong keys,
key.tsv values permuted across codes, each scored through b2 on the whole piece; PASS iff real margin > wrong-key margin p99).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63b_test.py [--draws 200] [--wrong 200]

Same run() as tx/viv63_test.py (imported; its b1 arm is computed there and simply not used as a gate here). The specificity loop
uses a cached 4-gram log table that returns the same floats as NgramModel.score (same expression, same summation order).
Writes tx/viv63b_result.json and piece63_decode.txt (whole piece, candidate letters, unread codes dropped).
"""
import json, math, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t, viv63_decode as v63, viv54_decode as vd, vivk_test as vt, judge_plaintext as jp  # noqa: E402


def fast(model):
    cache = {}
    n, k, V = model.n, model.k, model.V

    def score(s):
        s = jp.fold(s)
        if len(s) < n:
            return -9.9
        tot = 0.0
        for i in range(n - 1, len(s)):
            g = s[i - n + 1:i + 1]
            v = cache.get(g)
            if v is None:
                v = cache[g] = math.log10((model.c.get(g, 0) + k) / (model.ctx.get(g[:-1], 0) + V * k))
            tot += v
        return tot / (len(s) - n + 1)
    return score


def b2_only(score, km, seq, draws, tag):
    real = ''.join(km.get(c, '') for c in seq); s = score(real)
    rng = random.Random(f'{t.SEED}-{tag}'); no = []
    for _ in range(draws):
        L = list(real); rng.shuffle(L); no.append(score(''.join(L)))
    no.sort()
    return s, jp.pct(no, 0.99)


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    res = {'seed': t.SEED, 'draws': draws, 'pages_new': list(v63.PAGES_B), 'pages_whole': list(v63.PAGES)}
    res['C1_f103r'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_ink54'], _ = t.run(model, k, c2, draws, 'C2')
    new = [c for _, _, seq in v63.lines(v63.PAGES_B) for c, _ in seq]
    whole = [c for _, _, seq in v63.lines(v63.PAGES) for c, _ in seq]
    res['target_new'], _ = t.run(model, k, new, draws, 'T-new')
    res['target_whole'], cand = t.run(model, k, whole, draws, 'T-whole')
    res['per_page_new'] = {p: t.run(model, k, [c for _, _, seq in v63.lines((p,)) for c, _ in seq], draws, p)[0] for p in v63.PAGES_B}
    gate = all(res[c]['b2']['pass'] and res[c]['b2']['headroom_ok'] for c in ('C1_f103r', 'C2_ink54'))
    for arm in ('target_new', 'target_whole'):
        res[f'verdict_b2_{arm}'] = ('PASS' if res[arm]['b2']['pass'] else 'FAIL') if gate else 'not a gate (positive control fails or no headroom)'
    # specificity (registered): wrong keys through b2 on the whole piece
    score = fast(model)
    s_chk, p_chk = b2_only(score, k, whole, draws, 'T-whole-b2chk')
    assert abs(s_chk - res['target_whole']['s']) < 1e-4, 'fast scorer disagrees with NgramModel.score'
    real_margin = res['target_whole']['s'] - res['target_whole']['b2']['null_p99']
    codes = sorted(k); rng = random.Random(f'{t.SEED}-spec'); rows = []
    for i in range(nwrong):
        v = [k[c] for c in codes]; rng.shuffle(v); km = dict(zip(codes, v))
        s, p99 = b2_only(score, km, whole, draws, f'spec-{i}')
        rows.append(round(s - p99, 4))
    ms = sorted(rows)
    spec = {'wrong_keys': nwrong, 'b2_pass_share': round(sum(m > 0 for m in rows) / nwrong, 3),
            'margin_median': jp.pct(ms, 0.5), 'margin_p95': jp.pct(ms, 0.95), 'margin_p99': jp.pct(ms, 0.99), 'margin_max': ms[-1],
            'real_margin': round(real_margin, 4)}
    spec['verdict'] = 'PASS' if real_margin > spec['margin_p99'] else 'FAIL'
    res['specificity'] = spec; res['specificity_margins'] = rows
    open(os.path.join(T, 'piece63_decode.txt'), 'w').write(cand + '\n')
    json.dump(res, open(os.path.join(HERE, 'viv63b_result.json'), 'w'), indent=1)
    print(json.dumps({x: y for x, y in res.items() if x != 'specificity_margins'}, indent=1))


if __name__ == '__main__':
    main()
