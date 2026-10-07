#!/usr/bin/env python3
"""Gate G1 for Pietro de Pusterla's 1447 cipher (SFZ-P, 7 Oct 2026; gate pre-registered in
.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md, unchanged from SFZ-1's amidani/g1.py).

Leave-one-letter-out known-plaintext test over Pusterla's glossed units (cipher slip + later-hand clear copy, BnF italien
1584): learn sign -> letter from the other unit(s), decode the held-out slip, score letter accuracy against its own copy
with amidani/g1.py's `score` (imported, not copied). Control: 200 shuffles of the training key's sign -> value map.
PASS = mean held-out accuracy >= 0.60 AND every unit above its shuffle p95.

Deviation from g1.py, stated: the learner. tools/stream_align.learn (g1.py's) did not lock on to f.81/f.80 at all
(within-letter half/half hold-out 0.36-0.40 vs shuffle p95 0.38-0.43). Pusterla writes "che" as one sign (g÷; 17 of its
18 occurrences fall within 0.03 relative position of a "che" of the copy), so here "che" (also inside perche, siche,
qualche) is one clear-side letter 'k', the g÷ / che pairs are anchors, and the same banded DP (stream_align.band_dp,
emissions) runs hard EM between consecutive anchors. --stock reruns the gate with g1.py's own learner for comparison.

Also writes key.tsv (pooled), key_<unit>.tsv, align_<unit>.tsv. Readings are SFZ-P's single-reader transcriptions in
working mnemonics (pusterla_labels.md).
    python3 ciphers/sforza-italien1584-1447/pusterla/g1p.py [--check] [--stock]
"""
import os, re, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
sys.path.insert(0, os.path.join(HERE, '..', 'amidani'))
import stream_align as sa  # noqa: E402
import g1  # noqa: E402  (SFZ-1's gate; its score() is the statistic)

UNITS = [('f81', 'ciphertext_f81.tsv', 'clear_f80.txt'), ('f42', 'ciphertext_f42.tsv', 'clear_f41.txt')]
CHE_SIGN, CHE = 'g÷', 10  # 'k'
SEED, NSHUF = 1447, 200


def syms(f):
    t = [x for l in open(os.path.join(HERE, f)) if l.strip() and not l.startswith('#')
         for x in l.rstrip('\n').split('\t')[1].split()]
    o, i = [], 0
    while i < len(t):  # "g ÷" written apart in some lines is the one che sign
        if i + 1 < len(t) and t[i] == 'g' and t[i + 1] == '÷':
            o.append(CHE_SIGN); i += 2
        else:
            o.append(t[i]); i += 1
    return o


def text(f):
    s = ' '.join(l.strip() for l in open(os.path.join(HERE, f)) if not l.startswith('#')).replace('[ ]', ' ').lower()
    return sa.letters(re.sub(r'[^a-z]+', ' ', s).replace('che', 'k'))


def anchors(s, let):
    a = [i for i, x in enumerate(s) if x == CHE_SIGN]; b = [j for j, x in enumerate(let) if x == CHE]
    ra = [x / len(s) for x in a]; rb = [x / len(let) for x in b]
    n, m = len(a), len(b); D = np.zeros((n + 1, m + 1)); bk = {}
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j], bk[i, j] = min((D[i - 1][j - 1] + abs(ra[i - 1] - rb[j - 1]) - 0.05, 'm'), (D[i - 1][j], 'a'), (D[i][j - 1], 'b'))
    i, j, pairs = n, m, []
    while i > 0 and j > 0:
        k = bk[i, j]
        if k == 'm': pairs.append((a[i - 1], b[j - 1])); i -= 1; j -= 1
        elif k == 'a': i -= 1
        else: j -= 1
    pairs = pairs[::-1]; out = []; pi = pj = 0
    for x, y in pairs + [(len(s), len(let))]:
        out.append((pi, x, pj, y)); pi, pj = x, y
    return out


def learn(units, nsym, iters=8, band=12):
    counts = np.zeros((nsym, sa.A)); u = np.ones(sa.A)
    for S, let, sg in units:
        for i0, i1, j0, j1 in sg:
            for i in range(i0, i1):
                c = j0 + (i - i0) * (j1 - j0) / max(1, i1 - i0)
                for j in range(max(j0, int(c) - 3), min(j1, int(c) + 4)):
                    counts[S[i], let[j]] += 1 / 7
    for _ in range(iters):
        E = sa.emissions(counts, u, 0.5); new = np.zeros_like(counts); paths = []
        for S, let, sg in units:
            path = []
            for i0, i1, j0, j1 in sg:
                if i1 <= i0 or j1 <= j0: continue
                N, M = i1 - i0, j1 - j0
                p, _, _ = sa.band_dp(S[i0:i1], let[j0:j1], E, np.arange(N + 1) * (M / N), max(band, abs(M - N) + band), 1.5, 1.5)
                path += [(i + i0, j + j0) for i, j in p]
            for i, j in path: new[S[i], let[j]] += 1
            paths.append(path)
        counts = new
    return counts, paths


def main(check=False, stock=False):
    U = []
    for name, ct, cl in UNITS:
        s = syms(ct); let = text(cl); U.append((name, s, let))
    allsyms = sorted({x for _, s, _ in U for x in s}); ids = {x: i for i, x in enumerate(allsyms)}
    data = {n: (np.array([ids[x] for x in s]), let, anchors(s, let)) for n, s, let in U}
    selfk, nulls = {}, {}
    for name, s, let in U:
        S, _, sg = data[name]
        if stock:
            c, path = sa.learn(S, let, len(ids), band=40, step=60)
        else:
            c, (path,) = learn([data[name]], len(ids))
        selfk[name] = c; pj = dict(path)
        nulls[name] = set(range(len(s))) - set(pj)
        if not stock:
            with open(os.path.join(HERE, f'align_{name}.tsv'), 'w') as f:
                f.write('pos\tsign\tletter\n')
                for i, x in enumerate(s):
                    f.write(f'{i}\t{x}\t{("che" if let[pj[i]] == CHE else chr(97 + let[pj[i]])) if i in pj else "-"}\n')
    def val(v): return 'che' if v == CHE else chr(97 + v)
    pooled = sum(selfk.values())
    out = ['sign\tvalue\tcount\tshare\tunits\tgrade']
    for x in allsyms:
        r = pooled[ids[x]]
        if r.sum() == 0: continue
        us = ','.join(n for n in selfk if selfk[n][ids[x]].sum() > 0)
        out.append(f'{x}\t{val(int(r.argmax()))}\t{int(round(r.max()))}\t{r.max() / r.sum():.2f}\t{us}\t'
                   f'{"C" if r.max() >= 2 and r.max() / r.sum() >= 0.6 else "M"}')
    keytxt = '\n'.join(out) + '\n'
    rng = np.random.default_rng(SEED)
    rows = ['held_out\tn_signs\tn_null\ttrain_signs\tunseen\treal\tshuffle_mean\tshuffle_p95\tabove_p95']
    reals, allabove = [], True
    for name, s, let in U:
        train = [data[n] for n, _, _ in U if n != name]
        if stock:
            c = sum(sa.learn(S, l2, len(ids), band=40, step=60)[0] for S, l2, _ in train)
        else:
            c, _ = learn(train, len(ids))
        key = sa.decode(c); tr = np.where(key >= 0)[0]
        real = g1.score(key, s, let, ids, nulls[name]); sh = []
        for _ in range(NSHUF):
            k2 = key.copy(); k2[tr] = key[rng.permutation(tr)]; sh.append(g1.score(k2, s, let, ids, nulls[name]))
        sh = np.array(sh); p95 = float(np.quantile(sh, 0.95)); above = real > p95; allabove &= above; reals.append(real)
        unseen = sum(1 for x in s if key[ids[x]] < 0)
        rows.append(f'{name}\t{len(s)}\t{len(nulls[name])}\t{len(tr)}\t{unseen}\t{real:.3f}\t{sh.mean():.3f}\t{p95:.3f}\t{above}')
    mean = float(np.mean(reals)); verdict = 'PASS' if mean >= 0.60 and allabove else 'FAIL'
    rows.append(f'# learner: {"stream_align.learn (g1.py stock)" if stock else "che-anchored segment EM"}; mean held-out accuracy {mean:.3f}; gate >= 0.60 and every unit > shuffle p95: {verdict}')
    gtxt = '\n'.join(rows) + '\n'
    gfile = 'gate_g1_stock.tsv' if stock else 'gate_g1.tsv'
    if check:
        files = ((gfile, gtxt),) + ((('key.tsv', keytxt),) if not stock else ())
        bad = [f for f, t in files if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != t]
        print('stale: ' + ', '.join(bad) if bad else f'ok: {", ".join(f for f, _ in files)} reproduce')
        return 1 if bad else 0
    open(os.path.join(HERE, gfile), 'w').write(gtxt)
    if not stock:
        open(os.path.join(HERE, 'key.tsv'), 'w').write(keytxt)
    print(gtxt, end='')
    return 0


if __name__ == '__main__':
    sys.exit(main('--check' in sys.argv, '--stock' in sys.argv))
