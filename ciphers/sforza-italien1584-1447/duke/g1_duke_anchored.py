#!/usr/bin/env python3
"""Gate G1 for the Duke's 1447 key with pusterla/g1p.py's segment-anchored hard-EM learner (SFZ-DUKE, 8 Oct 2026;
pre-registered in PREREG-SFZ-DUKE.md as a SECONDARY test on reader A: the primary AB test could not run, see NOTES.md).
Gate unchanged: leave-one-letter-out over f8/f5, 200 shuffles, seed 1447, amidani/g1.py score; PASS = mean >= 0.60 and
every unit > shuffle p95. The Duke has no che sign (no sign sits near the copies' "che" above chance), so the anchors are
(slip start, copy start) and (start of the shared final run, the copy's "data" = dateline), fixed by hand below.
    python3 ciphers/sforza-italien1584-1447/duke/g1_duke_anchored.py [--check]
Writes gate_g1_anchored.tsv only.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'pusterla'))
sys.path.insert(0, os.path.join(HERE, '..', 'amidani'))
import g1p  # noqa: E402
import g1  # noqa: E402
g1p.HERE = HERE
# (unit, slip, copy, line holding the shared final run's first sign, index in that line)
UNITS = [('f8', 'ciphertext_f8.tsv', 'clear_f10.txt', 'f8_L15', 0), ('f5', 'ciphertext_f5.tsv', 'clear_f7.txt', 'f5_L14', 0)]
RUN = ['b', '3', 'd', 't']  # the run's opening, identical in both slips' reader-A reads (f8 L15, f5 L14)


def load(ct, cl, line, k):
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, ct)) if l.strip() and not l.startswith('#')]
    s = [x for _, r in rows for x in r.split()]
    off = sum(len(r.split()) for n, r in rows[:[n for n, _ in rows].index(line)]) + k
    assert s[off:off + len(RUN)] == RUN, (ct, s[off:off + len(RUN)])
    raw = ' '.join(l.strip() for l in open(os.path.join(HERE, cl)) if not l.startswith('#')).lower()
    pre = raw[:raw.rindex('data abiate')]
    import re
    jd = len(g1p.sa.letters(re.sub(r'[^a-z]+', ' ', pre).replace('che', 'k')))
    let = g1p.text(cl)
    return s, let, [(0, off, 0, jd), (off, len(s), jd, len(let))]


def main(check):
    U = [(n,) + load(ct, cl, ln, k) for n, ct, cl, ln, k in UNITS]
    allsyms = sorted({x for _, s, _, _ in U for x in s}); ids = {x: i for i, x in enumerate(allsyms)}
    data = {n: (np.array([ids[x] for x in s]), let, sg) for n, s, let, sg in U}
    nulls = {}
    for n, s, let, sg in U:
        _, (path,) = g1p.learn([data[n]], len(ids)); nulls[n] = set(range(len(s))) - {i for i, _ in path}
    rng = np.random.default_rng(g1p.SEED)
    rows = ['held_out\tn_signs\tn_null\ttrain_signs\tunseen\treal\tshuffle_mean\tshuffle_p95\tabove_p95']
    reals, allabove = [], True
    for n, s, let, sg in U:
        c, _ = g1p.learn([data[m] for m, *_ in U if m != n], len(ids))
        key = g1p.sa.decode(c); tr = np.where(key >= 0)[0]
        real = g1.score(key, s, let, ids, nulls[n]); sh = []
        for _ in range(g1p.NSHUF):
            k2 = key.copy(); k2[tr] = key[rng.permutation(tr)]; sh.append(g1.score(k2, s, let, ids, nulls[n]))
        sh = np.array(sh); p95 = float(np.quantile(sh, 0.95)); above = real > p95; allabove &= above; reals.append(real)
        unseen = sum(1 for x in s if key[ids[x]] < 0)
        rows.append(f'{n}\t{len(s)}\t{len(nulls[n])}\t{len(tr)}\t{unseen}\t{real:.3f}\t{sh.mean():.3f}\t{p95:.3f}\t{above}')
    mean = float(np.mean(reals)); v = 'PASS' if mean >= 0.60 and allabove else 'FAIL'
    rows.append(f'# learner: dateline-anchored segment EM (pusterla/g1p.learn), reader A; mean held-out accuracy {mean:.3f}; gate >= 0.60 and every unit > shuffle p95: {v}')
    txt = '\n'.join(rows) + '\n'; f = os.path.join(HERE, 'gate_g1_anchored.tsv')
    if check:
        ok = os.path.exists(f) and open(f).read() == txt; print('ok: gate_g1_anchored.tsv reproduces' if ok else 'stale: gate_g1_anchored.tsv'); return 0 if ok else 1
    open(f, 'w').write(txt); print(txt, end=''); return 0


if __name__ == '__main__':
    sys.exit(main('--check' in sys.argv))
