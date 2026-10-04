#!/usr/bin/env python3
"""N6-VIV53 gates exactly as PREREG-N6VIV53.md (derived from tx/viv54_test.py; only the piece inputs differ): (a) gloss check, (b) fr16 judge with f.103r positive control.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53_test.py [--draws 200]

Writes tx/viv53_result.json and piece53_decode.txt (candidate letters); asserts f103r_control_decode.txt unchanged.
"""
import json, math, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, 'tools'))
import viv54_decode as vd
import viv53_decode as v53  # noqa: E402
import vivk_test as vt  # noqa: E402
import judge_plaintext as jp  # noqa: E402

FR16 = [os.path.join(ROOT, 'tools/data/fr16', f) for f in
        ('lettresdecatheri01cathuoft_djvu.txt.gz', 'lettresdecatheri02cathuoft_djvu.txt.gz', 'lettresindites00marg_djvu.txt.gz')]
SPEC = {'judge': {'corpora': FR16, 'min_word_cover': 0.5}}
fold = lambda s: s.replace('j', 'i').replace('v', 'u')


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def main():
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    k = {c: v for c, (v, g) in vd.key().items()}
    codes = sorted(k)
    lines = []
    for page in v53.PAGES_N6VIV53:
        for line, seq in sorted(vd.page_tokens(page).items()):
            lines.append((page, line, [c for c, _ in seq]))
    gl = [ln.rstrip('\n').split('\t') for ln in open(os.path.join(HERE, 'glosses53.tsv'), encoding='utf-8')][1:]
    gl = [g for g in gl if g[6] == 'yes']
    bykey = {(p, l): s for p, l, s in lines}

    def s_a(km):
        sc = []
        for p, l, x0, x1, _, g, *_ in gl:
            seq = bykey[(p, l)]; n = len(seq)
            a, b = max(0, math.floor((float(x0) - 0.08) * n)), min(n, math.ceil((float(x1) + 0.08) * n))
            w = fold(''.join(km.get(c, '') for c in seq[a:b]))
            sc.append(lcs(fold(g), w) / len(g))
        return sum(sc) / len(sc), sc

    def letters(km, seqs):
        return ''.join(km.get(c, '') for s in seqs for c in s)

    rng = random.Random(20260957)
    shuf = []
    for _ in range(draws):
        v = [k[c] for c in codes]; rng.shuffle(v); shuf.append(dict(zip(codes, v)))
    # (a)
    real_a, per = s_a(k)
    null_a = sorted(s_a(km)[0] for km in shuf)
    p95a, meda = jp.pct(null_a, 0.95), jp.pct(null_a, 0.5)
    pass_a = real_a > p95a and real_a >= 0.60 and meda < 0.95
    # (b)
    cand = letters(k, [s for _, _, s in lines])
    ctrl = ''.join(k.get(c, '') for c in vt.tokens(os.path.join(HERE, 'f103r_rec.tsv')))
    open(os.path.join(T, 'piece53_decode.txt'), 'w').write(cand + '\n')
    assert open(os.path.join(HERE, 'f103r_control_decode.txt')).read() == ctrl + '\n'
    jc, jt = jp.judge(SPEC, ctrl), jp.judge(SPEC, cand)
    model = jp.NgramModel([jp.read_corpus(p) for p in FR16])
    N = len(cand)
    real, null, cov = model.controls(N, samples=200)
    null99, real05 = jp.pct(null, 0.99), jp.pct(real, 0.05)
    sh_scores, sh_pass = [], 0
    for km in shuf:
        s = letters(km, [x for _, _, x in lines]); sc = model.score(s)
        sh_scores.append(sc)
        if sc > null99 and sc > real05 and model.cover(s) >= 0.5:
            sh_pass += 1
    sh_scores.sort()
    sh99 = jp.pct(sh_scores, 0.99)
    cand_sc = jt['checks']['language']['score']
    if not jc['pass']:
        verdict_b = 'judge not a gate (positive control FAILs)'
    elif sh_pass > 10:
        verdict_b = f'judge void ({sh_pass}/200 shuffled-key decodes PASS)'
    else:
        verdict_b = 'PASS' if (jt['pass'] and cand_sc > sh99) else 'FAIL'
    res = {'a': {'S_a': round(real_a, 3), 'per_gloss': [round(x, 3) for x in per], 'null_median': round(meda, 3),
                 'null_p95': round(p95a, 3), 'pass': pass_a},
           'b': {'candidate': jt, 'positive_control_f103r': jc, 'shuffled_key_score_median': round(jp.pct(sh_scores, 0.5), 3),
                 'shuffled_key_score_p99': round(sh99, 3), 'shuffled_key_judge_passes': sh_pass, 'verdict': verdict_b},
           'letters': {'candidate': len(cand), 'control': len(ctrl)}, 'draws': draws, 'seed': 20260957}
    json.dump(res, open(os.path.join(HERE, 'viv53_result.json'), 'w'), indent=1, default=str)
    print(json.dumps({'a': res['a'], 'b_verdict': verdict_b, 'cand': jt['checks'], 'ctrl': jc['checks'],
                      'shuf_med': res['b']['shuffled_key_score_median'], 'shuf_p99': res['b']['shuffled_key_score_p99'],
                      'shuf_judge_pass': sh_pass, 'letters': res['letters']}, indent=1, default=str))


if __name__ == '__main__':
    main()
