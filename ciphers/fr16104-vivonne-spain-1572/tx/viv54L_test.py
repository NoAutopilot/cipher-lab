#!/usr/bin/env python3
"""N7-VIV54L gate (iv) exactly as PREREG-N7VIV54L.md: b2 (tx/viv63_test.run unchanged) on the ink 54 re-decode with positive controls
C1 = f.103r and C2 = ink 53 whole piece run first; (c) 200 wrong keys through b2 on the re-decode (pass iff real margin > wrong-key
margin p99). The same b2 + (c) on the committed N5-VIV54 sequence, descriptive ("before").

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_test.py [--draws 200] [--wrong 200]

Writes tx/viv54L_result.json and piece54_decode_L.txt (re-decode letters, unread codes dropped).
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t  # noqa: E402
import viv54_decode as vd  # noqa: E402
import viv54L_decode as vl  # noqa: E402
import viv53_decode as v53  # noqa: E402
import vivk_test as vt  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SEED = '20261054L'


def spec(model, k, seq, draws, nwrong, tag):
    res, _ = t.run(model, k, seq, draws, tag)
    codes = sorted(k); rng = random.Random(SEED + '-wrong-' + tag); margins, passes = [], 0
    for i in range(nwrong):
        v = [k[c] for c in codes]; rng.shuffle(v)
        r, _ = t.run(model, dict(zip(codes, v)), seq, draws, f'{tag}wrong{i}')
        margins.append(r['s'] - r['b2']['null_p99']); passes += r['b2']['pass']
    margins.sort(); real_m = res['s'] - res['b2']['null_p99']; p99 = jp.pct(margins, 0.99)
    res['c'] = {'wrong_keys': nwrong, 'b2_passes': passes, 'share': round(passes / nwrong, 3),
                'margin_median': round(jp.pct(margins, 0.5), 4), 'margin_p95': round(jp.pct(margins, 0.95), 4),
                'margin_p99': round(p99, 4), 'margin_max': round(margins[-1], 4), 'real_margin': round(real_m, 4),
                'pass': real_m > p99}
    return res


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    t.SEED = SEED
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for p in v53.PAGES for _, seq in sorted(vd.page_tokens(p).items()) for c, _ in seq]
    after = [c for p in vl.PAGES for _, seq in sorted(vl.page_seqs(p).items()) for c, _, _ in seq]
    before = [c for p in vl.PAGES for _, seq in sorted(vd.page_tokens(p).items()) for c, _ in seq]
    res = {'seed': SEED, 'draws': draws}
    res['C1_f103r'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_ink53'], _ = t.run(model, k, c2, draws, 'C2')
    ctrl_ok = all(res[c]['b2']['pass'] and res[c]['b2']['headroom_ok'] for c in ('C1_f103r', 'C2_ink53'))
    res['after'] = spec(model, k, after, draws, nwrong, 'A')
    res['before'] = spec(model, k, before, draws, nwrong, 'B')
    res['verdict_b2'] = ('PASS' if res['after']['b2']['pass'] else 'FAIL') if ctrl_ok else 'not a gate (positive control fails or no headroom)'
    res['verdict_c'] = 'PASS' if res['after']['c']['pass'] else 'FAIL'
    res['audit_ready'] = res['verdict_b2'] == 'PASS' and res['after']['c']['pass']
    open(os.path.join(T, 'piece54_decode_L.txt'), 'w').write(''.join(k.get(c, '') for c in after) + '\n')
    json.dump(res, open(os.path.join(HERE, 'viv54L_result.json'), 'w'), indent=1)
    for x in ('C1_f103r', 'C2_ink53', 'after', 'before'):
        r = res[x]; print(x, r['letters'], r['s'], 'b2 p99', r['b2']['null_p99'], r['b2']['pass'], r['b2']['headroom_ok'], r.get('c', ''))
    print('verdict b2', res['verdict_b2'], '| c', res['verdict_c'], '| audit_ready', res['audit_ready'])


if __name__ == '__main__':
    main()
