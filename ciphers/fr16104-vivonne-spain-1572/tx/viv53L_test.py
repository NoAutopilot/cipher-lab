#!/usr/bin/env python3
"""N7-VIV53L gates exactly as PREREG-N7VIV53L.md (iv) = PREREG-N6VIV53B's (b-ii) and (c), rule unchanged, on the look-alike re-decode.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53L_test.py [--draws 200] [--wrong 200]

b2 = tx/viv63_test.run unchanged (fr16 4-gram score per letter vs 200 letter-order shuffles; pass = s > null p99); controls C1 f.103r and
C2 ink 54 at full length first ("not a gate" if either fails or lacks headroom). (c) 200 wrong keys (key.tsv values permuted, unread set
unchanged) through b2 on the whole piece; pass iff real margin > wrong-key margin p99. Seed string "20261053L". Target = the code
sequence of tx/viv53L_decode.py (': :' joined, look-alike fold-in). Writes tx/viv53L_result.json.
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t  # noqa: E402
import viv54_decode as vd  # noqa: E402
import viv53L_decode as vl  # noqa: E402
import viv53b_test as vb  # noqa: E402
import vivk_test as vt  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SEED = '20261053L'


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    t.SEED = SEED
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    pages = {p: [c for _, seq in sorted(vl.page_tokens(p).items()) for c, _, _ in seq] for p in vl.PAGES}
    whole = [c for p in vl.PAGES for c in pages[p]]
    res = {'seed': SEED, 'draws': draws}
    res['C1_full'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_full'], _ = t.run(model, k, c2, draws, 'C2')
    res['whole'], cand = t.run(model, k, whole, draws, 'whole')
    res['verdict_b_ii'] = vb.gate(res, ('C1_full', 'C2_full'), 'whole')
    res['per_page'] = {p: t.run(model, k, pages[p], draws, p)[0] for p in vl.PAGES}
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
    json.dump(res, open(os.path.join(HERE, 'viv53L_result.json'), 'w'), indent=1)
    print(json.dumps({x: res[x] for x in ('verdict_b_ii', 'c', 'audit_ready')}, indent=1))
    for x in ('C1_full', 'C2_full', 'whole'):
        print(x, res[x]['letters'], res[x]['s'], 'b2 p99', res[x]['b2']['null_p99'], res[x]['b2']['pass'], res[x]['b2']['headroom_ok'])


if __name__ == '__main__':
    main()
