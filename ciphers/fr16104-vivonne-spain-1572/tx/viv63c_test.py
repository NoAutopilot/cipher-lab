#!/usr/bin/env python3
"""N6-VIV63C gates exactly as PREREG-N6VIV63C.md: b2 (vs letter-order-shuffle null p99) on (i) the new pages ff.193v-194r alone, with
positive controls C1 (f.103r) and C2 (ink 54) SUBSAMPLED to the new pages' decoded letter count (contiguous window from token 0), and
(ii) the whole piece ff.190r-194r with the controls at full length; then the registered specificity check (200 wrong keys, key.tsv values
permuted across codes, seed '20260967-spec-C', each scored through b2 on the whole piece; PASS iff real margin > wrong-key margin p99).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63c_test.py [--draws 200] [--wrong 200]

run() from tx/viv63_test.py, fast()/b2_only() from tx/viv63b_test.py (imported, unchanged). Writes tx/viv63c_result.json and
piece63_decode.txt (whole piece, candidate letters, unread codes dropped).
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t, viv63b_test as tb, viv63_decode as v63, viv54_decode as vd, vivk_test as vt, judge_plaintext as jp  # noqa: E402


def window(k, seq, n):
    """Contiguous window of seq from token 0 whose key.tsv decode has exactly (or first reaches) n letters."""
    out, L = [], 0
    for c in seq:
        if L >= n:
            break
        out.append(c); L += len(k.get(c, ''))
    return out


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    new = [c for _, _, seq in v63.lines(v63.PAGES_C) for c, _ in seq]
    whole = [c for _, _, seq in v63.lines(v63.PAGES) for c, _ in seq]
    n_new = len(''.join(k.get(c, '') for c in new))
    res = {'seed': t.SEED, 'draws': draws, 'pages_new': list(v63.PAGES_C), 'pages_whole': list(v63.PAGES), 'new_letters': n_new}
    res['C1_f103r'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_ink54'], _ = t.run(model, k, c2, draws, 'C2')
    res['C1_sub'], _ = t.run(model, k, window(k, c1, n_new), draws, 'C1-sub-C')
    res['C2_sub'], _ = t.run(model, k, window(k, c2, n_new), draws, 'C2-sub-C')
    res['target_new'], _ = t.run(model, k, new, draws, 'T-new-C')
    res['target_whole'], cand = t.run(model, k, whole, draws, 'T-whole-C')
    res['per_page_new'] = {p: t.run(model, k, [c for _, _, seq in v63.lines((p,)) for c, _ in seq], draws, p)[0] for p in v63.PAGES_C}
    ok = lambda arms: all(res[c]['b2']['pass'] and res[c]['b2']['headroom_ok'] for c in arms)
    res['verdict_b2_target_new'] = (('PASS' if res['target_new']['b2']['pass'] else 'FAIL') if ok(('C1_sub', 'C2_sub'))
                                    else 'not a gate (subsampled positive control fails or no headroom)')
    res['verdict_b2_target_whole'] = (('PASS' if res['target_whole']['b2']['pass'] else 'FAIL') if ok(('C1_f103r', 'C2_ink54'))
                                      else 'not a gate (positive control fails or no headroom)')
    score = tb.fast(model)
    s_chk, _ = tb.b2_only(score, k, whole, draws, 'T-whole-C-b2chk')
    assert abs(s_chk - res['target_whole']['s']) < 1e-4, 'fast scorer disagrees with NgramModel.score'
    real_margin = res['target_whole']['s'] - res['target_whole']['b2']['null_p99']
    codes = sorted(k); rng = random.Random(f'{t.SEED}-spec-C'); rows = []
    for i in range(nwrong):
        v = [k[c] for c in codes]; rng.shuffle(v); km = dict(zip(codes, v))
        s, p99 = tb.b2_only(score, km, whole, draws, f'spec-C-{i}')
        rows.append(round(s - p99, 4))
    ms = sorted(rows)
    spec = {'wrong_keys': nwrong, 'b2_pass_share': round(sum(m > 0 for m in rows) / nwrong, 3),
            'margin_median': jp.pct(ms, 0.5), 'margin_p95': jp.pct(ms, 0.95), 'margin_p99': jp.pct(ms, 0.99), 'margin_max': ms[-1],
            'real_margin': round(real_margin, 4)}
    spec['verdict'] = 'PASS' if real_margin > spec['margin_p99'] else 'FAIL'
    res['specificity'] = spec; res['specificity_margins'] = rows
    open(os.path.join(T, 'piece63_decode.txt'), 'w').write(cand + '\n')
    json.dump(res, open(os.path.join(HERE, 'viv63c_result.json'), 'w'), indent=1)
    print(json.dumps({x: y for x, y in res.items() if x != 'specificity_margins'}, indent=1))


if __name__ == '__main__':
    main()
