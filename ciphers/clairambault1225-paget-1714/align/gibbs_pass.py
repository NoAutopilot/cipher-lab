#!/usr/bin/env python3
"""RUN1-PAG (4 Oct 2026): a different segmentation instrument (tools/gibbs_align.py, a collapsed Gibbs sampler) on the
56 gloss pairs, exactly as pre-registered in PREREG_seg2.md.

Step 1 matched known-answer control (synthetic gloss on the real code runs, 10 seeds; gate mean held-out >= 0.50 both
directions, else CONTROL BELOW GATE and stop). Step 2: per-letter gloss shuffle null (200 seeds), then the target.
Writes gibbs_pass.txt and gibbs_codes.tsv. Deterministic (fixed seeds); --check exits 1 if the committed outputs are stale.
    python3 gibbs_pass.py [--seeds 200] [--check]
"""
import collections, multiprocessing as mp, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import gibbs_align as ga
import interlinear_align as ia

L1 = {'f60R', 'f61L', 'f61R', 'f65L'}
p95 = lambda xs: sorted(xs)[min(len(xs) - 1, int(round(0.95 * (len(xs) - 1))))]


def key_of(pairs, seed):
    prep, keep = ga.sample(pairs, seed=seed)
    modes = ga.token_modes(prep, keep)
    return ga.code_key(modes), modes


def heldout(ka, modes_b):
    g = n = 0
    for _, _, c, ch, _ in modes_b:
        if ch and c in ka:
            n += 1
            g += ch == ka[c][0]
    return g, n


def one(let, seed):
    k1, m1 = key_of(let[1], seed)
    k2, m2 = key_of(let[2], seed)
    a, b = heldout(k1, m2), heldout(k2, m1)
    both = {c: (k1[c][0], k1[c][1], k1[c][2], k2[c][1], k2[c][2]) for c in k1 if c in k2 and k1[c][0] == k2[c][0]}
    return a, b, both


def shuf(ps, rng):
    g = [p['plain_raw'] for p in ps]
    rng.shuffle(g)
    return [dict(p, plain_raw=x) for p, x in zip(ps, g)]


def synth_let(let, real_gloss, seed):
    """Planted homophonic syllabary with nulls and inserted words on the real code runs (PREREG_seg2.md step 1)."""
    rng = random.Random(1000 + seed)
    uc = collections.Counter(real_gloss)
    letters, w = zip(*sorted(uc.items()))
    lw = [0.3, 0.4, 0.18]
    inv = set()
    while len(inv) < 60:
        L = rng.choices([1, 2, 3], weights=lw)[0]
        inv.add(''.join(rng.choices(letters, weights=w, k=L)))
    inv = sorted(inv)
    zw = [1.0 / (1 + i) for i in range(len(inv))]
    codes = sorted({ia.classify_token(t)[1] for k in (1, 2) for p in let[k] for t in p['cipher_raw'].split()
                    if ia.classify_token(t)[0] == 'num'})
    key = {c: rng.choices(inv, weights=zw)[0] for c in codes}
    for c in rng.sample(codes, max(1, len(codes) // 10)):
        key[c] = ''
    out = {}
    for k in (1, 2):
        out[k] = []
        for p in let[k]:
            g = ''
            for t in p['cipher_raw'].split():
                kind, v = ia.classify_token(t)
                if kind == 'num':
                    g += key[v]
            if rng.random() < 0.15:
                q = rng.randint(0, len(g))
                g = g[:q] + ''.join(rng.choices(letters, weights=w, k=rng.randint(3, 6))) + g[q:]
            out[k].append(dict(p, plain_raw=g))
    return out, key


def _synth_job(args):
    let, real_gloss, s = args
    sl, key = synth_let(let, real_gloss, s)
    (a, b), (c, d), _ = one(sl, s)
    kall, _ = key_of(sl[1] + sl[2], s)
    n = collections.Counter(ia.classify_token(t)[1] for k in (1, 2) for p in sl[k] for t in p['cipher_raw'].split())
    test = [x for x in key if key[x] and n[x] >= 2]
    rec = sum(kall.get(x, ('',))[0] == key[x] for x in test) / len(test)
    return a / b if b else 0.0, c / d if d else 0.0, rec


def _shuf_job(args):
    let, s = args
    rng = random.Random(s)
    sl = {1: shuf(let[1], rng), 2: shuf(let[2], rng)}
    (a, b), (c, d), bd = one(sl, s)
    return a / b if b else 0.0, c / d if d else 0.0, len(bd)


def compute(seeds):
    pairs = ia.load_pairs(os.path.join(HERE, 'pairs.tsv'))
    let = {1: [p for p in pairs if p['page'] in L1], 2: [p for p in pairs if p['page'] not in L1]}
    real_gloss = ''.join(ga.fold(ia.plain_letters(p['plain_raw'])[0]) for p in pairs)
    out = ['RUN1-PAG Gibbs segmentation pass (PREREG_seg2.md); tools/gibbs_align.py defaults %s' % ga.DEFAULTS]
    rows = ['code\tvalue\tL1_top\tL1_n\tL2_top\tL2_n']
    with mp.Pool(4) as pool:
        sy = pool.map(_synth_job, [(let, real_gloss, s) for s in range(10)])
        m12 = sum(x[0] for x in sy) / len(sy)
        m21 = sum(x[1] for x in sy) / len(sy)
        rec = sum(x[2] for x in sy) / len(sy)
        cok = m12 >= 0.5 and m21 >= 0.5
        out.append('step 1 matched known-answer control (10 synthetic seeds on the real code runs): held-out L1->L2 mean %.3f '
                   '(min %.3f), L2->L1 mean %.3f (min %.3f); planted-value recovery (pooled, codes n>=2) mean %.3f -> %s'
                   % (m12, min(x[0] for x in sy), m21, min(x[1] for x in sy), rec,
                      'CONTROL PASS' if cok else 'CONTROL BELOW GATE'))
        if not cok:
            return out, rows
        sh = pool.map(_shuf_job, [(let, s) for s in range(seeds)])
    (g12, n12), (g21, n21), bd = one(let, 0)
    s12, s21, sc = [x[0] for x in sh], [x[1] for x in sh], [x[2] for x in sh]
    r12, r21 = g12 / n12, g21 / n21
    ok = r12 > p95(s12) and r21 > p95(s21)
    cnt_ok = len(bd) > p95(sc)
    out.append('step 2 target: L1->L2 %d/%d = %.3f vs shuffle mean %.3f p95 %.3f; L2->L1 %d/%d = %.3f vs shuffle mean %.3f '
               'p95 %.3f -> %s; codes supported both directions %d vs shuffle mean %.1f p95 %d -> %s'
               % (g12, n12, r12, sum(s12) / seeds, p95(s12), g21, n21, r21, sum(s21) / seeds, p95(s21),
                  'PASS' if ok else 'FAIL', len(bd), sum(sc) / seeds, p95(sc), 'above' if cnt_ok else 'not above'))
    for c, (v, a1, n1, a2, n2) in sorted(bd.items()):
        rows.append('%s\t%s\t%d\t%d\t%d\t%d' % (c, v, a1, n1, a2, n2))
    vals = collections.Counter(x[0] for x in bd.values())
    out.append('homophony read-off: %d codes -> %d distinct values; values with >1 code: %s'
               % (len(bd), len(vals), ', '.join('%s:%s' % (k, '/'.join(str(c) for c in sorted(bd) if bd[c][0] == k))
                                               for k, n in sorted(vals.items()) if n > 1) or 'none'))
    return out, rows


def main():
    a = sys.argv[1:]
    seeds = int(a[a.index('--seeds') + 1]) if '--seeds' in a else 200
    out, rows = compute(seeds)
    txt, tsv = '\n'.join(out) + '\n', '\n'.join(rows) + '\n'
    pt, pc = os.path.join(HERE, 'gibbs_pass.txt'), os.path.join(HERE, 'gibbs_codes.tsv')
    if '--check' in a:
        same = open(pt).read() == txt and open(pc).read() == tsv
        print('gibbs_pass up to date' if same else 'gibbs_pass STALE')
        sys.exit(0 if same else 1)
    open(pt, 'w').write(txt)
    open(pc, 'w').write(tsv)
    print(txt)


if __name__ == '__main__':
    main()
