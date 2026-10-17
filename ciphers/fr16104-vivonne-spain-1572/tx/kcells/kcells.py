#!/usr/bin/env python3
"""VIV-KCELLS (17 Oct 2026): p/m/f key cells by whole-stream alignment, PREREG-VIV-KCELLS.md.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/kcells/kcells.py --control   # LOO known-answer gate + shuffled control
    python3 ciphers/fr16104-vivonne-spain-1572/tx/kcells/kcells.py --target    # refuses unless control_result.json PASSed

Instrument: tools/stream_align.py emissions/band_dp, emissions seeded from key.tsv C rows (10 pseudo-counts), hard EM per window.
Writes tx/kcells/control_result.json, target_result.json, <letter>_positions.tsv.
"""
import json, os, re, sys
from collections import Counter, defaultdict
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
TX = os.path.dirname(HERE)
T = os.path.dirname(TX)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import stream_align as sa  # noqa: E402

A = 26
PRIOR = 10.0
C_LETTERS = 'acdegilnoqrstu'
TARGETS = 'pmfkxybhz'
PAIRS = {
    'P40': (('f102r', 'f102v', 'f103r'), ('dec_norm.txt',)),
    'P67': (('f201r', 'f201v'), ('dec67_norm.txt', 'dec67b_norm.txt')),
    'P70': (('f211r', 'f211v'), ('dec70_norm.txt',)),
}


def row_tokens(s):
    s = re.sub(r'\[PLAIN:[^\]]*\]', ' ', s)
    s = re.sub(r'\[\.\.\.\]|\[[^\]]*\]', ' ', s)
    toks = [t.rstrip('?') for t in s.split() if t.rstrip('?')]
    out, i = [], 0
    while i < len(toks):
        if toks[i] == 'o' and i + 1 < len(toks) and toks[i + 1] == 'o':
            out.append('oo'); i += 2
        else:
            out.append(toks[i]); i += 1
    return out


def stream(pages):
    toks, pos = [], []
    for p in pages:
        for ln in open(os.path.join(TX, f'{p}_rec.tsv'), encoding='utf-8'):
            if ln.startswith('row\t') or not ln.strip():
                continue
            parts = ln.rstrip('\n').split('\t', 1)
            if len(parts) < 2 or parts[1].strip() == 'DUP':
                continue
            for i, t in enumerate(row_tokens(parts[1])):
                if re.fullmatch(r'\{.*\}', t):
                    continue
                toks.append(t); pos.append((p, parts[0], i))
    return toks, pos


def ckey():
    k = defaultdict(list)
    for ln in open(os.path.join(T, 'key.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'code' or len(f) < 3 or f[2] != 'C':
            continue
        v = {'j': 'i', 'v': 'u'}.get(f[1], f[1])
        k[v].append(f[0])
    return k


def anchor(dec, let):
    best = (-1, 0)
    d80 = dec[:80]
    for j in range(0, max(1, len(let) - 120), 5):
        s = sa.nw_score(d80, let[j:j + 120], band=200)
        if s > best[0]:
            best = (s, j)
    for j in range(max(0, best[1] - 5), min(len(let) - 1, best[1] + 6)):
        s = sa.nw_score(d80, let[j:j + 120], band=200)
        if s > best[0]:
            best = (s, j)
    return best


def align(toks, let, seed, j0, band=150, step=300, iters=3, first=300):
    """Key-seeded growing-window hard EM. seed: {label: letter index}. Returns path [(i, j)] on let[j0:]."""
    labels = sorted(set(toks))
    ids = {c: n for n, c in enumerate(labels)}
    sym = np.array([ids[c] for c in toks])
    L = let[j0:]
    u = np.bincount(L, minlength=A).astype(float) + 1.0
    u /= u.sum()
    prior = np.zeros((len(labels), A))
    for c, v in seed.items():
        if c in ids:
            prior[ids[c], v] = PRIOR
    counts = prior.copy()
    N = len(sym)
    n = min(N, first)
    path = []
    while True:
        ref = sa.ref_from(path, n)
        for _ in range(iters):
            E = sa.emissions(counts, u, 0.5)
            path, _, _ = sa.band_dp(sym[:n], L, E, ref, band, 1.5, 1.5)
            counts = prior.copy()
            for i, j in path:
                counts[sym[i], L[j]] += 1
            ref = sa.ref_from(path, n)
        if n >= N:
            break
        n = min(N, n + step)
    return [(i, j + j0) for i, j in path]


def load(shuffle_seed=None):
    out = {}
    for name, (pages, decs) in PAIRS.items():
        toks, pos = stream(pages)
        text = ''.join(open(os.path.join(TX, d), encoding='utf-8').read() for d in decs)
        let = sa.letters(text)
        if shuffle_seed is not None:
            rng = np.random.default_rng(1000 * shuffle_seed + sum(map(ord, name)))
            chunks = [let[k:k + 60] for k in range(0, len(let), 60)]
            order = rng.permutation(len(chunks))
            let = np.concatenate([chunks[o] for o in order])
        out[name] = (toks, pos, let)
    return out


_ANCH = {}


def run(data, seed_key, tag=None, full_key=None):
    """Returns {pair: list of (label, letter, pos)} at matched pairs. The start offset is located once per stream with the
    full C key (full_key), so the 14 held-out runs on one stream share it."""
    res = {}
    for name, (toks, pos, let) in data.items():
        if (tag, name) not in _ANCH:
            fk = full_key or seed_key
            _ANCH[(tag, name)] = anchor(np.array([fk.get(t, -1) for t in toks]), let)
        sc, j0 = _ANCH[(tag, name)]
        path = align(toks, let, seed_key, j0)
        res[name] = ([(toks[i], chr(97 + let[j]), pos[i]) for i, j in path], round(float(sc), 3), int(j0))
    return res


def seedmap(ck, drop=''):
    return {c: ord(v) - 97 for v, cs in ck.items() if v not in drop for c in cs}


def one(args):
    s, X = args
    ck = ckey()
    r = run(load(s), seedmap(ck, X), tag=s, full_key=seedmap(ck))
    return s, X, Counter(lab for name in r for lab, l, _ in r[name][0] if l == X)


def loo(tallies, ck):
    rec, detail = 0, {}
    for X in C_LETTERS:
        tally = tallies[X]
        n = sum(tally.values())
        top = tally.most_common(1)[0][0] if n else None
        own = sum(tally[c] for c in ck[X])
        share = own / n if n else 0.0
        ok = top in ck[X] and share >= 2 / 3
        rec += ok
        detail[X] = {'n': n, 'top': top, 'own_share': round(share, 3), 'recovered': bool(ok),
                     'top5': tally.most_common(5)}
    return rec, detail


def control():
    from multiprocessing import Pool
    ck = ckey()
    seeds = [None] + list(range(20))
    tasks = [(s, X) for s in seeds for X in C_LETTERS]
    got = defaultdict(dict)
    with Pool(4) as pool:
        for s, X, t in pool.imap_unordered(one, tasks):
            got[s][X] = t
    real, detail = loo(got[None], ck)
    print(f'LOO real: {real}/14', flush=True)
    sh = [loo(got[s], ck)[0] for s in range(20)]
    print('shuffles:', sh, flush=True)
    res = {'real_recovered': real, 'shuffle': sh, 'shuffle_mean': float(np.mean(sh)), 'shuffle_max': int(max(sh)),
           'gate': 'PASS' if real >= 10 and np.mean(sh) < 4 else 'FAIL', 'detail': detail}
    json.dump(res, open(os.path.join(HERE, 'control_result.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != 'detail'}))
    return res


def target():
    c = json.load(open(os.path.join(HERE, 'control_result.json')))
    if c['gate'] != 'PASS':
        sys.exit('control gate not passed: NON-TEST, target not run')
    ck = ckey()
    r = run(load(), seedmap(ck))
    purity = defaultdict(Counter)
    for name in r:
        for lab, l, _ in r[name][0]:
            purity[lab][l] += 1
    out = {'anchors': {k: {'score': v[1], 'j0': v[2], 'matched': len(v[0])} for k, v in r.items()}, 'letters': {}}
    for X in TARGETS:
        per = {name: Counter(lab for lab, l, _ in r[name][0] if l == X) for name in r}
        pooled = sum(per.values(), Counter())
        n = sum(pooled.values())
        rows = []
        for lab, k in pooled.most_common():
            pair_sh = {name: (round(per[name][lab] / sum(per[name].values()), 3), sum(per[name].values()))
                       for name in r if sum(per[name].values())}
            tot = sum(purity[lab].values())
            ok = (k / n >= 2 / 3 and k >= 10 and
                  all(sh >= 0.5 for sh, m in pair_sh.values() if m >= 5))
            rows.append({'label': lab, 'count': k, 'share': round(k / n, 3), 'per_pair': pair_sh,
                         'purity': [(l2, c2, round(c2 / tot, 3)) for l2, c2 in purity[lab].most_common(4)],
                         'cell': bool(ok)})
        out['letters'][X] = {'n': n, 'labels': rows}
        with open(os.path.join(HERE, f'{X}_positions.tsv'), 'w', encoding='utf-8') as f:
            f.write('pair\tpage\tline\tpos\tlabel\n')
            for name in r:
                for lab, l, (pg, ln, i) in r[name][0]:
                    if l == X:
                        f.write(f'{name}\t{pg}\t{ln}\t{i}\t{lab}\n')
    json.dump(out, open(os.path.join(HERE, 'target_result.json'), 'w'), indent=1)
    for X in TARGETS:
        d = out['letters'][X]
        print(X, d['n'], [(x['label'], x['count'], x['share'], x['cell']) for x in d['labels'][:5]])
    print(out['anchors'])


if __name__ == '__main__':
    if '--control' in sys.argv:
        control()
    elif '--target' in sys.argv:
        target()
    else:
        sys.exit(__doc__)
