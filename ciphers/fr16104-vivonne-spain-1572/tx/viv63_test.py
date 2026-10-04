#!/usr/bin/env python3
"""N6-VIV63 gate (b) exactly as PREREG-N6VIV63.md: b1 (vs shuffled-key null) and b2 (vs letter-order-shuffle null),
positive controls C1 (f.103r, N5-VIVK) and C2 (ink 54, N5-VIV54) first, then the target whole and per page.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63_test.py [--draws 200]

Writes tx/viv63_result.json and piece63_decode.txt (candidate letters, unread codes dropped).
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, 'tools'))
import viv54_decode as vd  # noqa: E402
import viv63_decode as v63  # noqa: E402
import vivk_test as vt  # noqa: E402
import judge_plaintext as jp  # noqa: E402

FR16 = [os.path.join(ROOT, 'tools/data/fr16', f) for f in
        ('lettresdecatheri01cathuoft_djvu.txt.gz', 'lettresdecatheri02cathuoft_djvu.txt.gz', 'lettresindites00marg_djvu.txt.gz')]
SEED = 20260967


def run(model, k, seqs, draws, tag):
    codes = sorted(k)
    dec = lambda km: ''.join(km.get(c, '') for c in seqs)
    real = dec(k); s = model.score(real)
    rng = random.Random(f'{SEED}-{tag}')
    nk, no = [], []
    for _ in range(draws):
        v = [k[c] for c in codes]; rng.shuffle(v); nk.append(model.score(dec(dict(zip(codes, v)))))
        L = list(real); rng.shuffle(L); no.append(model.score(''.join(L)))
    nk.sort(); no.sort()
    r = {'letters': len(real), 's': round(s, 4), 'cover': round(model.cover(real), 3)}
    for name, nl in (('b1', nk), ('b2', no)):
        p99, med = jp.pct(nl, 0.99), jp.pct(nl, 0.5)
        r[name] = {'null_median': round(med, 4), 'null_p99': round(p99, 4), 'pass': s > p99,
                   'headroom_ok': (s - p99) > 0.01 and med < s}
    return r, real


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in FR16])
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c2 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    res = {'seed': SEED, 'draws': draws}
    res['C1_f103r'], _ = run(model, k, c1, draws, 'C1')
    res['C2_ink54'], _ = run(model, k, c2, draws, 'C2')
    L = v63.lines()
    tgt = [c for _, _, seq in L for c, _ in seq]
    res['target'], cand = run(model, k, tgt, draws, 'T')
    res['per_page'] = {}
    for page in v63.PAGES:
        res['per_page'][page], _ = run(model, k, [c for p, _, seq in L if p == page for c, _ in seq], draws, page)
    for b in ('b1', 'b2'):
        gate = all(res[c][b]['pass'] and res[c][b]['headroom_ok'] for c in ('C1_f103r', 'C2_ink54'))
        res[f'verdict_{b}'] = ('PASS' if res['target'][b]['pass'] else 'FAIL') if gate else 'not a gate (positive control fails or no headroom)'
    open(os.path.join(T, 'piece63_decode.txt'), 'w').write(cand + '\n')
    json.dump(res, open(os.path.join(HERE, 'viv63_result.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
