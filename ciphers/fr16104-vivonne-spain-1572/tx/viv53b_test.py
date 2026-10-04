#!/usr/bin/env python3
"""N6-VIV53B gates exactly as PREREG-N6VIV53B.md: b2 (PREREG-N6VIV63's statistic, tx/viv63_test.run unchanged) on (b-i) f.171v alone
with both positive controls subsampled to its letter count, (b-ii) the whole piece 53 with full-length controls, and (c) 200 wrong
keys through b2 on the whole piece (pass iff real margin > wrong-key margin p99). Gate (a) does not apply (no glosses on f.171v).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53b_test.py [--draws 200] [--wrong 200]

Writes tx/viv53b_result.json and piece53_decode_all.txt (whole-piece letters, unread codes dropped).
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t  # noqa: E402  (run(), FR16; b1 is computed by run() too and reported, but not a gate here)
import viv54_decode as vd  # noqa: E402
import viv53_decode as v53  # noqa: E402
import vivk_test as vt  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SEED = '20261053'


def window(k, seq, n_letters):
    """Contiguous code window from token 0 whose decode has n_letters letters (PREREG (b-i))."""
    out, n = [], 0
    for c in seq:
        if n >= n_letters:
            break
        out.append(c); n += 1 if c in k else 0
    return out


def gate(res, ctrls, tgt):
    ok = all(res[c]['b2']['pass'] and res[c]['b2']['headroom_ok'] for c in ctrls)
    return ('PASS' if res[tgt]['b2']['pass'] else 'FAIL') if ok else 'not a gate (positive control fails or no headroom)'


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    t.SEED = SEED
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    pages = {p: [c for _, seq in sorted(vd.page_tokens(p).items()) for c, _ in seq] for p in v53.PAGES}
    whole = [c for p in v53.PAGES for c in pages[p]]
    new = pages['f171v']
    n_new = sum(c in k for c in new)
    res = {'seed': SEED, 'draws': draws}
    # (b-i)
    res['C1_sub'], _ = t.run(model, k, window(k, c1, n_new), draws, 'C1sub')
    res['C2_sub'], _ = t.run(model, k, window(k, c2, n_new), draws, 'C2sub')
    res['f171v'], _ = t.run(model, k, new, draws, 'f171v')
    res['verdict_b_i'] = gate(res, ('C1_sub', 'C2_sub'), 'f171v')
    # (b-ii)
    res['C1_full'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_full'], _ = t.run(model, k, c2, draws, 'C2')
    res['whole'], cand = t.run(model, k, whole, draws, 'whole')
    res['verdict_b_ii'] = gate(res, ('C1_full', 'C2_full'), 'whole')
    res['per_page'] = {p: t.run(model, k, pages[p], draws, p)[0] for p in v53.PAGES}
    # (c)
    codes = sorted(k); rng = random.Random(SEED + '-wrong'); margins, passes = [], 0
    for i in range(nwrong):
        v = [k[c] for c in codes]; rng.shuffle(v)
        r, _ = t.run(model, dict(zip(codes, v)), whole, draws, f'wrong{i}')
        margins.append(r['s'] - r['b2']['null_p99']); passes += r['b2']['pass']
    margins.sort()
    real_m = res['whole']['s'] - res['whole']['b2']['null_p99']
    p99 = jp.pct(margins, 0.99)
    res['c'] = {'wrong_keys': nwrong, 'b2_passes': passes, 'share': round(passes / nwrong, 3),
                'margin_median': round(jp.pct(margins, 0.5), 4), 'margin_p95': round(jp.pct(margins, 0.95), 4),
                'margin_p99': round(p99, 4), 'margin_max': round(margins[-1], 4), 'real_margin': round(real_m, 4),
                'pass': real_m > p99}
    res['audit_ready'] = res['verdict_b_ii'] == 'PASS' and res['c']['pass']
    open(os.path.join(T, 'piece53_decode_all.txt'), 'w').write(cand + '\n')
    json.dump(res, open(os.path.join(HERE, 'viv53b_result.json'), 'w'), indent=1)
    print(json.dumps({x: res[x] for x in ('verdict_b_i', 'verdict_b_ii', 'c', 'audit_ready')}, indent=1))
    for x in ('C1_sub', 'C2_sub', 'f171v', 'C1_full', 'C2_full', 'whole'):
        print(x, res[x]['letters'], res[x]['s'], 'b2 p99', res[x]['b2']['null_p99'], res[x]['b2']['pass'], res[x]['b2']['headroom_ok'])


if __name__ == '__main__':
    main()
