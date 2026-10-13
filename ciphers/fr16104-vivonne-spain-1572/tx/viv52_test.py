#!/usr/bin/env python3
"""VIV52-O gates exactly as PREREG-VIV52O.md: positive controls C1 (f.103r) and C2 (ink 54) through b1/b2 first, then the target
(ink 52 f.164r+f.164v under key.tsv) b1/b2 whole and per page, the 200-wrong-key specificity gate (c), and the key_tomokiyo.tsv
decode (descriptive). Code paths: tx/viv63_test.run and tx/vivanchor_gates.wrong (unchanged).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv52_test.py [--draws 200] [--wrong 200]

Writes tx/viv52_result.json and piece52_decode.txt (candidate letters, unread codes dropped).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t, viv54_decode as vd, vivk_test as vt, judge_plaintext as jp  # noqa: E402
import vivanchor_gates as vg  # noqa: E402
import viv52_decode as v52  # noqa: E402

SEED = '20261013VIV52O'


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    t.SEED = SEED
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    res = {'seed': SEED, 'draws': draws}
    res['C1_f103r'], _ = t.run(model, k, c1, draws, 'C1')
    res['C2_ink54'], _ = t.run(model, k, c2, draws, 'C2')
    L = v52.lines()
    tgt = [c for _, _, seq in L for c, _ in seq]
    res['target'], cand = vg.wrong(model, k, tgt, draws, nwrong, SEED, 'T')
    res['per_page'] = {p: t.run(model, k, [c for pg, _, seq in L if pg == p for c, _ in seq], draws, p)[0] for p in v52.PAGES}
    kt = {c: v for c, (v, g) in v52.key('key_tomokiyo.tsv').items()}
    res['target_key_tomokiyo'], _ = t.run(model, kt, tgt, draws, 'TT')
    for b in ('b1', 'b2'):
        gate = all(res[c][b]['pass'] and res[c][b]['headroom_ok'] for c in ('C1_f103r', 'C2_ink54'))
        res[f'verdict_{b}'] = ('PASS' if res['target'][b]['pass'] else 'FAIL') if gate else 'not a gate (positive control fails or no headroom)'
    res['verdict_wrong_keys'] = 'PASS' if res['target']['c']['pass'] else 'FAIL'
    open(os.path.join(T, 'piece52_decode.txt'), 'w').write(cand + '\n')
    json.dump(res, open(os.path.join(HERE, 'viv52_result.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
