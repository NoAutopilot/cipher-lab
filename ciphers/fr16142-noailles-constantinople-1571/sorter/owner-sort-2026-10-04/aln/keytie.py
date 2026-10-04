"""N8-NOX2 (LANE-NEAR8 worker, account 2, 4 Oct 2026): count-based key tie of the basin consensus to key.tsv via the c262 bridge.
Pre-registered in PREREG-KEYTIE.md (same folder, commit 4c5d72d9). Reads results/basin_keys.json (N8-NOX) unchanged; no re-learning.
    python3 keytie.py score   -> results/keytie_summary.json
    python3 keytie.py check   rule 7: recompute and compare with results/keytie_summary.json
"""
import csv, itertools, json, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results')
T = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
L_IDX = [4, 5, 6, 8, 12, 14]
NL_IDX = [1, 2, 3, 7, 9, 10, 11, 13, 15, 17, 18, 19]
SEEDS = range(1, 11)


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def scored_piles(L):
    # basin.py step 2's filter, verbatim in effect (checked against basin_summary.json's 'provisional' below)
    prov = tsv(os.path.join(T, 'run2', 'nxatl', 'cluster_provisional_names.tsv'))
    merged_away = set()
    for r in L:
        merged_away |= set(r['extra']) | set(r['extra'].values())
    out = {}
    for r in prov:
        lab = r['label']
        if lab.startswith(('W:', 'N', 'D')) or float(r['purity']) < 0.40 or int(r['support']) < 3:
            continue
        lets = {x[0] for x in lab.split('/') if x and x[0].islower()}
        if not lets or r['cluster'] in merged_away or not all(r['cluster'] in k['key'] for k in L):
            continue
        out[r['cluster']] = {ord(c) - 97 for c in lets}
    return out


def consensus(runs, piles):
    out = {}
    for p in piles:
        w = {}
        for r in runs:
            if p in r['extra'] or p in r['extra'].values() or p not in r['key']:
                continue
            v, c = r['key'][p]
            if v >= 0:
                w[v] = w.get(v, 0) + c
        if w:
            out[p] = max(w.items(), key=lambda t: (t[1], -t[0]))[0]
    return out


def H(cons, scored):
    return sum(cons.get(p, -9) in s for p, s in scored.items())


def compute():
    K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
    L = [K[f'alt{i:02d}'] for i in L_IDX]
    NL = [K[f'alt{i:02d}'] for i in NL_IDX]
    sc = scored_piles(L)
    prev = json.load(open(os.path.join(OUT, 'basin_summary.json')))['step2']['provisional']
    assert {p: ''.join(sorted(chr(97 + x) for x in s)) for p, s in sc.items()} == prev, 'bridge differs from N8-NOX'
    cL = consensus(L, sc)
    hL = H(cL, sc)
    h7 = H(consensus(L + [K['target']], sc), sc)
    single = {f'alt{i:02d}': H(consensus([K[f'alt{i:02d}']], sc), sc) for i in L_IDX}
    # (a) permutation of provisional letter sets across piles
    rng = random.Random(20261004)
    ps, sets = list(sc), list(sc.values())
    perm = []
    for _ in range(10000):
        s2 = sets[:]; rng.shuffle(s2)
        perm.append(sum(cL.get(p, -9) in s2[i] for i, p in enumerate(ps)))
    # (b) non-locking 6-subsets
    nl, novote = [], []
    for sub in itertools.combinations(NL, 6):
        c = consensus(list(sub), sc)
        nl.append(H(c, sc)); novote.append(len(sc) - len(c))
    degenerate = len(set(nl)) < 3 or np.mean([x > 3 for x in novote]) > 0.10
    # (c) shuffled Dupuy, same six merges
    sh = [H(consensus([K[f'shuf{s:02d}_alt{i:02d}'] for i in L_IDX], sc), sc) for s in SEEDS]
    res = dict(n_scored=len(sc), H_L=hL, H_L_plus_target=h7, H_single_L=single,
               consensus_L={p: chr(97 + v) for p, v in sorted(cL.items())},
               provisional=prev,
               a_perm=dict(n=10000, mean=round(float(np.mean(perm)), 3), p99=float(np.percentile(perm, 99)), max=max(perm)),
               b_nonlocking=dict(n=len(nl), mean=round(float(np.mean(nl)), 3), p99=float(np.percentile(nl, 99)), max=max(nl),
                                 distinct=sorted(set(nl)), share_subsets_over3_novote=round(float(np.mean([x > 3 for x in novote])), 4),
                                 degenerate=bool(degenerate)),
               c_shuffled_dupuy=dict(n=len(sh), values=sh, max=max(sh)))
    if degenerate:
        res['verdict'] = 'NON-TEST'
    else:
        ok = hL > res['a_perm']['p99'] and hL > res['b_nonlocking']['p99'] and hL > res['c_shuffled_dupuy']['max']
        res['verdict'] = 'PASS' if ok else 'FAIL'
    return res


def main(a):
    if a[:1] == ['score']:
        res = compute()
        json.dump(res, open(os.path.join(OUT, 'keytie_summary.json'), 'w'), indent=1)
        print(json.dumps({k: v for k, v in res.items() if k not in ('provisional',)}, indent=1))
    elif a[:1] == ['check']:
        if compute() != json.load(open(os.path.join(OUT, 'keytie_summary.json'))):
            sys.exit('keytie_summary.json stale')
        print('keytie_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
