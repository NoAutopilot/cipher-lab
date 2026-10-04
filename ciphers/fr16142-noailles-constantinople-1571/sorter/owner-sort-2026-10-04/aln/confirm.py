"""NOX-CONFIRM (account 3 worker, 4 Oct 2026): pre-registered confirmation of NOX-ALN's exploratory k014->k077 lock-on.
Pre-registered in PREREG-CONFIRM.md (same folder). Same pipeline as full_pair.py (nxaln.run_pipeline unchanged).
    python3 confirm.py list              print the 20 pre-registered alternative single merges -> results/confirm_alts.json
    python3 confirm.py target SEED       owner labels + k014->k077, nulls a/c 200, b 40 (max), rng SEED -> results/confirm_target_sSEED.json
    python3 confirm.py alt I             alternative I (0-19): owner labels + that merge, nulls a/c 200, b 10 (max), rng 20261004
"""
import json, random, sys
from collections import Counter
import nox_aln as n
sa, nx = n.sa, n.nx
X0, Y0 = 'k014', 'k077'


def stream_counts():
    tr, he = n.streams()
    return Counter(tr + he)


def alternatives(k=10):
    """10 merges k014->q (q: the 10 owner piles nearest k077 in tile count) and 10 merges p->k077 (p: the 10 nearest k014),
    ties broken by pile name, excluding k014/k077 themselves; piles as they exist after the owner's sort."""
    c = stream_counts()
    def near(p):
        cand = [q for q in c if q not in (X0, Y0)]
        return sorted(cand, key=lambda q: (abs(c[q] - c[p]), q))[:k]
    return [(X0, q) for q in near(Y0)] + [(p, Y0) for p in near(X0)]


def run(extra, seed, bdraws, label):
    f = lambda s: extra.get(s, s)
    tr_s, he_s = n.streams()
    ids, tr, he = n.ids_of([f(s) for s in tr_s], [f(s) for s in he_s])
    res, counts, path, key = nx.run_pipeline(tr, he, nx.dupuy_stream(), len(ids), 200, random.Random(seed),
                                             sa.letters(nx.fr16_text()), label, bdraws)
    res.update(extra=extra, seed=seed, n_symbols=len(ids))
    return res


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'list':
        alts = alternatives(); c = stream_counts()
        json.dump([dict(i=i, x=x, y=y, nx=c[x], ny=c[y]) for i, (x, y) in enumerate(alts)], open('results/confirm_alts.json', 'w'), indent=1)
        for i, (x, y) in enumerate(alts):
            print(i, x, c[x], '->', y, c[y])
    elif a[0] == 'target':
        s = int(a[1]); r = run({X0: Y0}, s, 40, f'confirm k014->k077 seed {s}')
        json.dump(r, open(f'results/confirm_target_s{s}.json', 'w'), indent=1); print(nx.summary(r))
    elif a[0] == 'alt':
        i = int(a[1]); x, y = alternatives()[i]
        r = run({x: y}, 20261004, 10, f'alt {i} {x}->{y}')
        r['i'] = i
        json.dump(r, open(f'results/confirm_alt_{i:02d}.json', 'w'), indent=1); print(i, nx.summary(r))
