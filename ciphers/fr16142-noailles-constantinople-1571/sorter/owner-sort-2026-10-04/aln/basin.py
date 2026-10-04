"""N8-NOX (LANE-NEAR8 worker, account 2, 4 Oct 2026): pre-registered basin test of NOX-CONFIRM's locked-on runs.
Pre-registered in PREREG-BASIN.md (same folder, commit 29a256ef). Imports nox_aln / confirm / nxaln / stream_align unchanged.
    python3 basin.py run      learn every key (L, NL, target, shuffled-Dupuy L x 10 seeds) -> results/basin_keys.json
    python3 basin.py score    step 1 (and step 2 only on a step-1 PASS) -> results/basin_summary.json
    python3 basin.py check    rule 7: re-learn the six L keys and compare with results/basin_keys.json
"""
import csv, itertools, json, os, random, sys
from multiprocessing import Pool
import numpy as np
import nox_aln as n
import confirm as cf
sa, nx = n.sa, n.nx
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results')
L_IDX = [4, 5, 6, 8, 12, 14]
NL_IDX = [1, 2, 3, 7, 9, 10, 11, 13, 15, 17, 18, 19]
SEEDS = range(1, 11)


def learn(extra, text):
    f = lambda s: extra.get(s, s)
    tr_s, he_s = n.streams()
    ids, tr, he = n.ids_of([f(s) for s in tr_s], [f(s) for s in he_s])
    counts, path = sa.learn(np.array(tr), sa.letters(text), len(ids))
    key = sa.decode(counts)
    inv = {v: k for k, v in ids.items()}
    w = counts.sum(1)
    return {inv[i]: [int(key[i]), int(w[i])] for i in range(len(ids))}


def shuffled_dupuy(seed):
    w = nx.dupuy_stream().split()
    random.Random(seed).shuffle(w)
    return ' '.join(w)


def job(spec):
    name, extra, seed = spec
    text = nx.dupuy_stream() if seed is None else shuffled_dupuy(seed)
    return name, dict(extra=extra, seed=seed, key=learn(extra, text))


def specs():
    alts = cf.alternatives()
    out = [(f'alt{i:02d}', {alts[i][0]: alts[i][1]}, None) for i in L_IDX + NL_IDX]
    out.append(('target', {cf.X0: cf.Y0}, None))
    out += [(f'shuf{s:02d}_alt{i:02d}', {alts[i][0]: alts[i][1]}, s) for s in SEEDS for i in L_IDX]
    return out


def agree(a, b, weighted=False):
    excl = set(a['extra']) | set(a['extra'].values()) | set(b['extra']) | set(b['extra'].values())
    num = den = 0
    for p, (va, wa) in a['key'].items():
        if p in excl or p not in b['key']:
            continue
        vb, wb = b['key'][p]
        if va < 0 or vb < 0:
            continue
        w = (wa + wb) / 2 if weighted else 1
        num += w * (va == vb); den += w
    return num / den if den else float('nan'), den


def S(runs, weighted=False):
    return float(np.mean([agree(a, b, weighted)[0] for a, b in itertools.combinations(runs, 2)]))


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def step2(K, L, NL_all):
    prov = tsv(os.path.join(n.T, 'run2', 'nxatl', 'cluster_provisional_names.tsv'))
    merged_away = set()
    for r in L:
        merged_away |= set(r['extra']) | set(r['extra'].values())
    scored = {}
    for r in prov:
        lab = r['label']
        if lab.startswith(('W:', 'N', 'D')) or float(r['purity']) < 0.40 or int(r['support']) < 3:
            continue
        lets = {x[0] for x in lab.split('/') if x and x[0].islower()}
        if not lets or r['cluster'] in merged_away or not all(r['cluster'] in k['key'] for k in L):
            continue
        scored[r['cluster']] = {ord(c) - 97 for c in lets}

    def consensus(runs):
        out = {}
        for p in scored:
            vals = [k['key'][p][0] for k in runs if p in k['key'] and k['key'][p][0] >= 0]
            if vals:
                v, c = max(((v, vals.count(v)) for v in set(vals)), key=lambda t: (t[1], -t[0]))
                if c >= 4:
                    out[p] = v
        return out

    def kscore(cons):
        return sum(cons[p] in scored[p] for p in cons) / len(cons) if cons else float('nan'), len(cons)
    cons = consensus(L)
    k, nk = kscore(cons)
    rng = random.Random(20261004)
    ps, vs, perm = list(cons), list(cons.values()), []
    for _ in range(10000):
        v2 = vs[:]; rng.shuffle(v2)
        perm.append(sum(v2[i] in scored[p] for i, p in enumerate(ps)) / len(ps))
    nl = [kscore(consensus(sub))[0] for sub in itertools.combinations(NL_all, 6)]
    nl = [x for x in nl if x == x]
    res = dict(n_scored_piles=len(scored), n_consensus=nk, K=round(k, 4),
               null_perm=dict(n=10000, mean=round(float(np.mean(perm)), 4), p99=round(float(np.percentile(perm, 99)), 4)),
               null_nl=dict(n=len(nl), mean=round(float(np.mean(nl)), 4), p99=round(float(np.percentile(nl, 99)), 4)),
               consensus={p: chr(97 + v) for p, v in sorted(cons.items())},
               provisional={p: ''.join(sorted(chr(97 + x) for x in s)) for p, s in sorted(scored.items())})
    res['pass'] = bool(k > res['null_perm']['p99'] and k > res['null_nl']['p99'])
    return res


def main(a):
    if a[0] == 'run':
        with Pool(4) as pool:
            keys = dict(pool.map(job, specs()))
        json.dump(keys, open(os.path.join(OUT, 'basin_keys.json'), 'w'))
        print(len(keys), 'keys learned')
    elif a[0] == 'score':
        K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
        L = [K[f'alt{i:02d}'] for i in L_IDX]; NL = [K[f'alt{i:02d}'] for i in NL_IDX]
        sL, sLw, s7 = S(L), S(L, True), S(L + [K['target']])
        n1 = [S(list(c)) for c in itertools.combinations(NL, 6)]
        n2 = [S([K[f'shuf{s:02d}_alt{i:02d}'] for i in L_IDX]) for s in SEEDS]
        n2w = [S([K[f'shuf{s:02d}_alt{i:02d}'] for i in L_IDX], True) for s in SEEDS]
        n1w = [S(list(c), True) for c in itertools.combinations(NL, 6)]
        pairs = {f'{x}-{y}': round(agree(K[f'alt{x:02d}'], K[f'alt{y:02d}'])[0], 4) for x, y in itertools.combinations(L_IDX, 2)}
        sh = [agree(K[f'alt{i:02d}'], K[f'alt{j:02d}'])[1] for i, j in itertools.combinations(L_IDX, 2)]
        res = dict(S_L=round(sL, 4), S_L_weighted=round(sLw, 4), S_L_plus_target=round(s7, 4), pairs_L=pairs,
                   shared_piles_min_max=[min(sh), max(sh)],
                   N1_nonlocking=dict(n=len(n1), mean=round(float(np.mean(n1)), 4), p99=round(float(np.percentile(n1, 99)), 4),
                                      max=round(max(n1), 4), weighted_p99=round(float(np.percentile(n1w, 99)), 4)),
                   N2_shuffled_dupuy=dict(n=len(n2), mean=round(float(np.mean(n2)), 4), max=round(max(n2), 4),
                                          values=[round(x, 4) for x in n2], weighted_max=round(max(n2w), 4)))
        res['step1_pass'] = bool(sL > res['N1_nonlocking']['p99'] and sL > res['N2_shuffled_dupuy']['max'])
        if res['step1_pass']:
            res['step2'] = step2(K, L, NL)
        json.dump(res, open(os.path.join(OUT, 'basin_summary.json'), 'w'), indent=1)
        print(json.dumps({k: v for k, v in res.items() if k != 'step2'}, indent=1))
        if 'step2' in res:
            print(json.dumps({k: v for k, v in res['step2'].items() if k not in ('consensus', 'provisional')}, indent=1))
    elif a[0] == 'check':
        K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
        alts = cf.alternatives()
        for i in L_IDX:
            k = learn({alts[i][0]: alts[i][1]}, nx.dupuy_stream())
            if k != K[f'alt{i:02d}']['key']:
                sys.exit(f'stale at alt{i:02d}')
        print('basin_keys.json up to date (six L keys)')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
