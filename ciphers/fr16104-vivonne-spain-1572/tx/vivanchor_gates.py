#!/usr/bin/env python3
"""VIV-ANCHOR gates, PREREG-VIVANCHOR.md (v): b2 + 200 wrong keys on each ink with key.tsv after the VIV-ANCHOR row, NEW seeds; registered
V_strict stretch on ink 53; longest H run per ink (descriptive). Same code paths as tx/viv63g_test.py (whole piece), tx/viv53G_decode.gates()
and tx/viv54L_test.spec(); the registered result files are not touched.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/vivanchor_gates.py {63|53|54|runs} [--draws 200] [--wrong 200]

Writes tx/vivanchor_gates_<ink>.json.
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t, viv54_decode as vd, vivk_test as vt, judge_plaintext as jp  # noqa: E402


def wrong(model, k, seq, draws, nwrong, seed, tag):
    res, cand = t.run(model, k, seq, draws, tag)
    codes = sorted(k); rng = random.Random(seed + '-wrong'); margins, passes = [], 0
    import viv63b_test as tb
    score = tb.fast(model)
    for i in range(nwrong):
        v = [k[c] for c in codes]; rng.shuffle(v)
        s, p99 = tb.b2_only(score, dict(zip(codes, v)), seq, draws, f'{tag}wrong{i}')
        margins.append(s - p99); passes += s > p99
    margins.sort(); real_m = res['s'] - res['b2']['null_p99']; p99 = jp.pct(margins, 0.99)
    res['c'] = {'wrong_keys': nwrong, 'b2_passes': passes, 'margin_median': round(jp.pct(margins, 0.5), 4),
                'margin_p99': round(p99, 4), 'margin_max': round(margins[-1], 4), 'real_margin': round(real_m, 4), 'pass': real_m > p99}
    return res, cand


def runs():
    out = {}
    for ink, f in (('63', 'reading_piece63.tsv'), ('53', 'reading_piece53_G.tsv'), ('54', 'reading_piece54_L.tsv')):
        rows = list(csv.DictReader(open(os.path.join(T, f), encoding='utf-8'), delimiter='\t'))
        best = (0, None); cnt = {}
        for page in dict.fromkeys(r['page'] for r in rows):
            g = ''; d = ''; ln = []
            for r in rows:
                if r['page'] == page:
                    g += r['grades']; d += r['decode']; ln += [r['line']] * len(r['grades'])
                    for c in r['grades']:
                        cnt[c] = cnt.get(c, 0) + 1
            i = 0
            while i < len(g):
                if g[i] == 'H':
                    j = i
                    while j < len(g) and g[j] == 'H':
                        j += 1
                    if j - i > best[0]:
                        best = (j - i, f'{page} {ln[i]}-{ln[j - 1]}: {d[i:j]}')
                    i = j
                else:
                    i += 1
        out[ink] = {'grades': cnt, 'longest_H_run': best[0], 'where': best[1]}
    return out


def main():
    ink = sys.argv[1]
    draws = int(sys.argv[sys.argv.index('--draws') + 1]) if '--draws' in sys.argv else 200
    nwrong = int(sys.argv[sys.argv.index('--wrong') + 1]) if '--wrong' in sys.argv else 200
    if ink == 'runs':
        r = runs(); json.dump(r, open(os.path.join(HERE, 'vivanchor_gates_runs.json'), 'w'), indent=1, ensure_ascii=False)
        print(json.dumps(r, indent=1, ensure_ascii=False)); return
    seed = f'20261008VA-{ink}'
    t.SEED = seed
    k = {c: v for c, (v, g) in vd.key().items()}
    model = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
    c1 = vt.tokens(os.path.join(HERE, 'f103r_rec.tsv'))
    c54 = [c for page in ('f173r', 'f173v') for _, seq in sorted(vd.page_tokens(page).items()) for c, _ in seq]
    res = {'ink': ink, 'seed': seed, 'draws': draws}
    if ink == '63':
        import viv63_decode as v63
        target = [c for _, _, seq in v63.lines(v63.PAGES) for c, _ in seq]
        c2, c2n = c54, 'C2_ink54'
    elif ink == '53':
        import viv53G_decode as g
        fold = g.decoys()['pass_']
        target = [c for p in g.PAGES for _, seq in sorted(g.page_tokens(p, fold).items()) for c, _, _ in seq]
        c2, c2n = c54, 'C2_ink54'
    else:
        import viv54L_decode as vl, viv53_decode as v53
        target = [c for p in vl.PAGES for _, seq in sorted(vl.page_seqs(p).items()) for c, _, _ in seq]
        c2, c2n = [c for p in v53.PAGES for _, seq in sorted(vd.page_tokens(p).items()) for c, _ in seq], 'C2_ink53'
    res['C1_f103r'], _ = t.run(model, k, c1, draws, 'C1')
    res[c2n], _ = t.run(model, k, c2, draws, 'C2')
    ctrl_ok = all(res[c]['b2']['pass'] and res[c]['b2']['headroom_ok'] for c in ('C1_f103r', c2n))
    res['target'], cand = wrong(model, k, target, draws, nwrong, seed, 'T')
    res['verdict_b2'] = ('PASS' if res['target']['b2']['pass'] else 'FAIL') if ctrl_ok else 'not a gate (positive control fails or no headroom)'
    res['verdict_wrong_keys'] = 'PASS' if res['target']['c']['pass'] else 'FAIL'
    if ink == '53':
        V, form = g.strict_vocab()
        res['V_strict'] = len(V)
        res['stretch_after'] = g.stretches(lambda p: g.page_tokens(p, fold), V, form, 200, seed + '-stretch')
    json.dump(res, open(os.path.join(HERE, f'vivanchor_gates_{ink}.json'), 'w'), indent=1, ensure_ascii=False)
    for x in ('C1_f103r', c2n, 'target'):
        r = res[x]; print(ink, x, r['letters'], r['s'], 'b2 p99', r['b2']['null_p99'], r['b2']['pass'], r['b2']['headroom_ok'])
    print(ink, 'verdict b2', res['verdict_b2'], '| wrong keys', res['verdict_wrong_keys'], res['target']['c'])
    if ink == '53':
        r = res['stretch_after']
        print('53 stretch top1', r['real_top1'], 'top3', r['real_top3mean'], 'null med/p99', r['null_top1_median'], r['null_top1_p99'])
        for s in r['top'][:3]:
            print('  ', s['page'], s['lines'], s['letters'], s['words'])


if __name__ == '__main__':
    main()
