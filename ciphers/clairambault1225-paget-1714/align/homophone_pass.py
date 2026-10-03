#!/usr/bin/env python3
"""READ2-PAG (3 Oct 2026): open-codes homophone/null pass, exactly as pre-registered in PREREG_homophone.md.

Each letter aligned alone (tools/interlinear_align.py via evaluate.run, NEXT-PAG settings); key_A = unique top folded
chunk per code; held-out agreement A->B = share of B's aligned code tokens (code in key_A) whose chunk equals key_A.
C1 null-cost -3 (empty chunks excluded), C2 null-cost 0 (empty chunk = value ''). Control: plain_raw permuted within
each letter, 200 seeds. Writes homophone_pass.txt and homophone_codes.tsv.
    python3 homophone_pass.py [--seeds 200]
"""
import collections, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import evaluate as ev
ia = ev.ia
L1 = {'f60R', 'f61L', 'f61R', 'f65L'}
CONF = {'C1': -3.0, 'C2': 0.0}


def chunks(pairs, nc, nulls):
    """per-code list of folded chunks, one per aligned code token."""
    prep, res, _, _ = ev.run(pairs, nc)
    out = collections.defaultdict(list)
    for (p, raw, toks, letters, *_), cs in zip(prep, res):
        for (kind, val), c in zip(toks, cs):
            if kind != 'num':
                continue
            ch = ia.fold(letters[c[0]:c[1]]) if c and c[1] > c[0] else ''
            if ch or nulls:
                out[val].append(ch)
    return out


def key(ch):
    k = {}
    for v, xs in ch.items():
        mc = collections.Counter(xs).most_common()
        if len(mc) == 1 or mc[0][1] > mc[1][1]:
            k[v] = (mc[0][0], mc[0][1], len(xs))
    return k


def heldout(ka, chb):
    g = n = 0
    for v, xs in chb.items():
        if v in ka:
            n += len(xs)
            g += sum(x == ka[v][0] for x in xs)
    return g, n


def both(k1, k2):
    return {v: k1[v] + k2[v][1:] for v in k1 if v in k2 and k1[v][0] == k2[v][0] and k1[v][0]}


def one(let, nc, nulls):
    c1, c2 = chunks(let[1], nc, nulls), chunks(let[2], nc, nulls)
    k1, k2 = key(c1), key(c2)
    a, b = heldout(k1, c2), heldout(k2, c1)
    return a, b, both(k1, k2)


def shuf(ps, rng):
    g = [p['plain_raw'] for p in ps]
    rng.shuffle(g)
    return [dict(p, plain_raw=x) for p, x in zip(ps, g)]


def main():
    a = sys.argv[1:]
    seeds = int(a[a.index('--seeds') + 1]) if '--seeds' in a else 200
    ev.OPTS.update(max_chunk=4, seg_bonus=0.5, len_prior=0.5)
    pairs = ia.load_pairs(os.path.join(HERE, 'pairs.tsv'))
    let = {1: [p for p in pairs if p['page'] in L1], 2: [p for p in pairs if p['page'] not in L1]}
    p95 = lambda xs: sorted(xs)[min(len(xs) - 1, int(round(0.95 * (len(xs) - 1))))]
    out = ['READ2-PAG homophone/null pass (PREREG_homophone.md); settings %s; per-letter gloss shuffle, %d seeds' % (ev.OPTS, seeds)]
    rows = ['config\tcode\tvalue\tL1_agree\tL1_n\tL2_agree\tL2_n']
    res = {}
    for name, nc in CONF.items():
        nulls = name == 'C2'
        (g12, n12), (g21, n21), bd = one(let, nc, nulls)
        r12, r21 = g12 / n12, g21 / n21
        s12, s21, sc = [], [], []
        for s in range(seeds):
            rng = random.Random(s)
            sl = {1: shuf(let[1], rng), 2: shuf(let[2], rng)}
            (a_, b_), (c_, d_), sbd = one(sl, nc, nulls)
            s12.append(a_ / b_ if b_ else 0.0)
            s21.append(c_ / d_ if d_ else 0.0)
            sc.append(len(sbd))
        ok = r12 > p95(s12) and r21 > p95(s21)
        cok = len(bd) > p95(sc)
        res[name] = (ok, cok, bd)
        out.append('%s null-cost %g: L1->L2 %d/%d = %.3f vs shuffle mean %.3f p95 %.3f; L2->L1 %d/%d = %.3f vs shuffle mean %.3f '
                   'p95 %.3f -> %s; codes supported both directions %d vs shuffle mean %.1f p95 %d -> %s'
                   % (name, nc, g12, n12, r12, sum(s12) / seeds, p95(s12), g21, n21, r21, sum(s21) / seeds, p95(s21),
                      'PASS' if ok else 'FAIL', len(bd), sum(sc) / seeds, p95(sc), 'above' if cok else 'not above'))
        if nulls:
            c1, c2 = chunks(let[1], nc, True), chunks(let[2], nc, True)
            k1, k2 = key(c1), key(c2)
            nl = sorted(v for v in k1 if v in k2 and k1[v][0] == '' and k2[v][0] == '')
            out.append('%s null codes (empty top chunk in both letters): %s' % (name, ' '.join(map(str, nl)) or 'none'))
        for v, (val, a1, n1, a2, n2) in sorted(bd.items()):
            rows.append('%s\t%s\t%s\t%d\t%d\t%d\t%d' % (name, v, val, a1, n1, a2, n2))
        vals = collections.Counter(x[0] for x in bd.values())
        out.append('%s homophony read-off: %d codes -> %d distinct values; values with >1 code: %s'
                   % (name, len(bd), len(vals), ', '.join('%s:%s' % (k, '/'.join(str(v) for v in sorted(bd) if bd[v][0] == k))
                                                        for k, n in sorted(vals.items()) if n > 1) or 'none'))
    open(os.path.join(HERE, 'homophone_pass.txt'), 'w').write('\n'.join(out) + '\n')
    open(os.path.join(HERE, 'homophone_codes.tsv'), 'w').write('\n'.join(rows) + '\n')
    print('\n'.join(out))


if __name__ == '__main__':
    main()
