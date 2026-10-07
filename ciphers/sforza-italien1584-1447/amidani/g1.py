#!/usr/bin/env python3
"""Gate G1 (SFZ-1, 7 Oct 2026; pre-registered in .claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md).

Leave-one-letter-out known-plaintext test for Vincenzo Amidani's 1447 cipher (BnF italien 1584):
for each unit, learn a sign -> letter key from the OTHER units' slip/clear-copy pairs (tools/stream_align.py hard-EM),
decode the held-out slip's signs with it, and score letter accuracy against the held-out unit's own clear copy
(stream_align.nw_score: identical aligned pairs; signs absent from the training key count as wrong; the denominator
excludes the held-out signs that its own slip/copy alignment leaves unmatched, i.e. nulls / undeciphered names).
Control: 200 shuffles of the training key's sign -> value map (values permuted among the trained signs), same statistic.
PASS = mean held-out accuracy >= 0.60 AND every held-out unit above its own shuffle p95.

Also writes key.tsv (pooled over all units), key_<unit>.tsv and align_<unit>.tsv (per-sign alignment), and counts
shared-sign conflicts between unit keys.

    python3 ciphers/sforza-italien1584-1447/amidani/g1.py [--check]
--check: recompute and exit 1 if gate_g1.tsv or key.tsv on disk differ from the recomputation.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import stream_align as sa  # noqa: E402

# unit: (ciphertext tsv, clear copy, text that starts the cipher part of the copy or None)
UNITS = [
    ('f366', 'ciphertext_f366.tsv', 'clear_f365.txt', 'fundamentalmente'),  # slip opens in clear up to this word
    ('f367', 'ciphertext_f367.tsv', 'clear_f368.txt', None),
]
OPTS = dict(band=40, step=60)
SEED = 1447
NSHUF = 200


def load(u):
    name, ct, cl, start = u
    syms = [t for l in open(os.path.join(HERE, ct)) if l.strip() and not l.startswith('#')
            for t in l.rstrip('\n').split('\t')[1].split()]
    txt = ' '.join(l.strip() for l in open(os.path.join(HERE, cl)) if not l.startswith('#')).replace('[ ]', ' ')
    if start:
        txt = txt[txt.index(start) + len(start):]
    return name, syms, sa.letters(txt)


def learn(units, ids):
    """Pool the per-unit learned counts (each unit aligned against its own copy)."""
    counts = np.zeros((len(ids), sa.A))
    paths = {}
    for name, syms, let in units:
        c, path = sa.learn(np.array([ids[s] for s in syms]), let, len(ids), **OPTS)
        counts += c
        paths[name] = path
    return counts, paths


def score(key, syms, let, ids, nulls):
    dec = np.array([key[ids[s]] if s in ids else -1 for s in syms])
    keep = np.array([i not in nulls for i in range(len(syms))])
    # align the full decode (positions matter), count hits at non-null positions only
    d2 = np.where(dec < 0, sa.A, dec)
    E = np.full((sa.A + 1, sa.A), -1.0)
    E[np.arange(sa.A), np.arange(sa.A)] = 2.0
    N, M = len(dec), len(let)
    ref = np.arange(N + 1) * (M / N)
    path, _, _ = sa.band_dp(d2, let, E, ref, max(200, abs(M - N) + 200), 1.0, 1.0, free_start=True)
    hits = sum(1 for i, j in path if keep[i] and d2[i] == let[j])
    return hits / max(1, keep.sum())


def main(check=False):
    units = [load(u) for u in UNITS]
    allsyms = sorted({s for _, syms, _ in units for s in syms})
    ids = {s: n for n, s in enumerate(allsyms)}
    # self-alignment per unit: keys, nulls, alignments
    selfk, nulls = {}, {}
    for name, syms, let in units:
        c, path = sa.learn(np.array([ids[s] for s in syms]), let, len(ids), **OPTS)
        selfk[name] = c
        matched = {i for i, j in path}
        nulls[name] = {i for i in range(len(syms)) if i not in matched}
        with open(os.path.join(HERE, f'align_{name}.tsv'), 'w') as f:
            f.write('pos\tsign\tletter\n')
            pj = dict(path)
            for i, s in enumerate(syms):
                f.write(f'{i}\t{s}\t{chr(97 + let[pj[i]]) if i in pj else "-"}\n')
        k = sa.decode(c)
        with open(os.path.join(HERE, f'key_{name}.tsv'), 'w') as f:
            f.write('sign\tvalue\tcount\tshare\n')
            for s in allsyms:
                r = c[ids[s]]
                if r.sum() > 0:
                    f.write(f'{s}\t{chr(97 + int(r.argmax()))}\t{int(round(r.max()))}\t{r.max() / r.sum():.2f}\n')
    # pooled key (grade C: every value comes from the later-hand clear copies)
    pooled = sum(selfk.values())
    out = ['sign\tvalue\tcount\tshare\tunits\tgrade']
    for s in allsyms:
        r = pooled[ids[s]]
        if r.sum() == 0:
            continue
        us = ','.join(n for n in selfk if selfk[n][ids[s]].sum() > 0)
        out.append(f'{s}\t{chr(97 + int(r.argmax()))}\t{int(round(r.max()))}\t{r.max() / r.sum():.2f}\t{us}\t'
                   f'{"C" if r.max() >= 2 and r.max() / r.sum() >= 0.6 else "M"}')
    keytxt = '\n'.join(out) + '\n'
    # conflicts on shared signs (both units give >=2 counts)
    conf = []
    a, b = [selfk[n] for n in ('f366', 'f367')]
    for s in allsyms:
        ra, rb = a[ids[s]], b[ids[s]]
        if ra.max() >= 2 and rb.max() >= 2:
            conf.append((s, chr(97 + int(ra.argmax())), chr(97 + int(rb.argmax()))))
    # leave-one-out
    rng = np.random.default_rng(SEED)
    rows = ['held_out\tn_signs\tn_null\ttrain_signs\tunseen\treal\tshuffle_mean\tshuffle_p95\tabove_p95']
    reals = []
    allabove = True
    for k, (name, syms, let) in enumerate(units):
        train = [x for x in units if x[0] != name]
        c, _ = learn(train, ids)
        key = sa.decode(c)
        trained = np.where(key >= 0)[0]
        real = score(key, syms, let, ids, nulls[name])
        sh = []
        for _ in range(NSHUF):
            k2 = key.copy()
            k2[trained] = key[rng.permutation(trained)]
            sh.append(score(k2, syms, let, ids, nulls[name]))
        sh = np.array(sh)
        p95 = float(np.quantile(sh, 0.95))
        unseen = sum(1 for s in syms if key[ids[s]] < 0)
        above = real > p95
        allabove &= above
        reals.append(real)
        rows.append(f'{name}\t{len(syms)}\t{len(nulls[name])}\t{len(trained)}\t{unseen}\t{real:.3f}\t{sh.mean():.3f}\t'
                    f'{p95:.3f}\t{above}')
    mean = float(np.mean(reals))
    verdict = 'PASS' if mean >= 0.60 and allabove else 'FAIL'
    rows.append(f'# mean held-out accuracy {mean:.3f}; gate >= 0.60 and every unit > shuffle p95: {verdict}')
    agree = sum(1 for _, x, y in conf if x == y)
    rows.append(f'# shared signs with >=2 counts in both unit keys: {len(conf)}; same value {agree}; conflicts '
                + ', '.join(f'{s}:{x}/{y}' for s, x, y in conf if x != y))
    gtxt = '\n'.join(rows) + '\n'
    if check:
        bad = [f for f, t in (('gate_g1.tsv', gtxt), ('key.tsv', keytxt))
               if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != t]
        print('stale: ' + ', '.join(bad) if bad else 'ok: gate_g1.tsv and key.tsv reproduce')
        return 1 if bad else 0
    open(os.path.join(HERE, 'gate_g1.tsv'), 'w').write(gtxt)
    open(os.path.join(HERE, 'key.tsv'), 'w').write(keytxt)
    print(gtxt, end='')
    return 0


if __name__ == '__main__':
    sys.exit(main('--check' in sys.argv))
