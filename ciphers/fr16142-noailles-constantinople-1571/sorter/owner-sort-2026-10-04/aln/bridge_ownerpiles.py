"""D07-NOXT (LANE DEFAULT-account-1-20261007-0042 worker, account 1, 7 Oct 2026): c262 tiles placed under the owner's piles, widening
the atlas-pile -> key.tsv bridge. Pre-registered in PREREG-D07NOXT.md (same folder). The EM is run2/nxatl/c262_align.py's, copied
verbatim in effect (asserted: on the raw atlas clusters it reproduces run2/nxatl/cluster_provisional_names.tsv exactly).
    python3 bridge_ownerpiles.py score   -> results/d07noxt_summary.json, results/d07noxt_provisional_owner.tsv, results/d07noxt_c262_tiles.tsv
    python3 bridge_ownerpiles.py check   rule 7: recompute and compare with the committed files
"""
import collections, csv, itertools, json, math, os, random, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results')
OS = os.path.dirname(HERE)
T = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
import keytie  # noqa: E402  (consensus, H, L_IDX, NL_IDX, SEEDS)

GAP, ITERS = 2.0, 15
SPLIT = ('k006', 'k072', 'k087')


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def load():
    tiles = collections.defaultdict(list)
    for r in tsv(os.path.join(T, 'run2', 'nxatl', 'sequences.tsv')):
        if r['leaf'] == 'c262':
            tiles[r['line']].append(dict(tile=r['tile'], cluster=r['cluster']))
    rec = {}
    for ln in open(os.path.join(T, 'witness', 'c262rc_recon.tsv')):
        if ln.startswith('#') or not ln.strip():
            continue
        L, toks = ln.rstrip('\n').split('\t', 1)
        rec[L] = toks.split()
    return tiles, rec


def nw(cs, ts, sc):
    n, m = len(cs), len(ts); D = [[0.0] * (m + 1) for _ in range(n + 1)]; B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): D[i][0] = -GAP * i; B[i][0] = 1
    for j in range(1, m + 1): D[0][j] = -GAP * j; B[0][j] = 2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            opts = (D[i - 1][j - 1] + sc(cs[i - 1], ts[j - 1]), D[i - 1][j] - GAP, D[i][j - 1] - GAP)
            k = max(range(3), key=lambda q: opts[q]); D[i][j] = opts[k]; B[i][j] = k
    i, j, pairs = n, m, []
    while i or j:
        k = B[i][j] if i and j else (1 if i else 2)
        if k == 0: pairs.append((i - 1, j - 1)); i, j = i - 1, j - 1
        elif k == 1: pairs.append((i - 1, None)); i -= 1
        else: pairs.append((None, j - 1)); j -= 1
    return pairs[::-1]


def em(tiles, rec, cl):
    """cl: {line: [cluster per tile]}. Returns (by: cluster -> Counter(label), align)."""
    lines = sorted(rec)
    align = {L: [(i, min(len(rec[L]) - 1, round(i * len(rec[L]) / len(cl[L])))) for i in range(len(cl[L]))] for L in lines}
    for it in range(ITERS):
        cnt = collections.Counter(); cc = collections.Counter(); tc = collections.Counter()
        for L in lines:
            for i, j in align[L]:
                if i is not None and j is not None:
                    cnt[(cl[L][i], rec[L][j])] += 1; cc[cl[L][i]] += 1; tc[rec[L][j]] += 1
        V = len(tc) or 1; N = sum(tc.values())
        sc = lambda c, t: math.log((cnt[(c, t)] + 0.2) / (cc[c] + 0.2 * V)) - math.log((tc[t] + 0.2) / (N + 0.2 * V))
        new = {L: nw(cl[L], rec[L], sc) for L in lines}
        if new == align:
            break
        align = new
    by = collections.defaultdict(collections.Counter)
    for L in lines:
        for i, j in align[L]:
            if i is not None and j is not None:
                by[cl[L][i]][rec[L][j]] += 1
    return by, align


def prov_rows(by):
    out = []
    for c in sorted(by, key=lambda c: -sum(by[c].values())):
        (lab, n), tot = by[c].most_common(1)[0], sum(by[c].values())
        out.append(dict(cluster=c, label=lab, support=tot, purity=f'{n / tot:.2f}',
                        other=' '.join(f'{a}:{b}' for a, b in by[c].most_common()[1:])))
    return out


def lets(lab):
    return {x[0] for x in lab.split('/') if x and x[0].islower()}


def bridged(rows, L):
    merged_away = set()
    for r in L:
        merged_away |= set(r['extra']) | set(r['extra'].values())
    out = {}
    for r in rows:
        lab = r['label']
        if lab.startswith(('W:', 'N', 'D')) or float(r['purity']) < 0.40 or int(r['support']) < 3:
            continue
        s = lets(lab)
        if not s or r['cluster'] in merged_away or not all(r['cluster'] in k['key'] for k in L):
            continue
        out[r['cluster']] = {ord(c) - 97 for c in s}
    return out


def keytie_block(K, L, NL, sc):
    cL = keytie.consensus(L, sc); hL = keytie.H(cL, sc)
    rng = random.Random(20261004); ps, sets = list(sc), list(sc.values()); perm = []
    for _ in range(10000):
        s2 = sets[:]; rng.shuffle(s2)
        perm.append(sum(cL.get(p, -9) in s2[i] for i, p in enumerate(ps)))
    nl, novote = [], []
    for sub in itertools.combinations(NL, 6):
        c = keytie.consensus(list(sub), sc); nl.append(keytie.H(c, sc)); novote.append(len(sc) - len(c))
    degenerate = len(set(nl)) < 3 or np.mean([x > 3 for x in novote]) > 0.10
    sh = [keytie.H(keytie.consensus([K[f'shuf{s:02d}_alt{i:02d}'] for i in keytie.L_IDX], sc), sc) for s in keytie.SEEDS]
    res = dict(n=len(sc), H=hL, consensus={p: chr(97 + v) for p, v in sorted(cL.items())},
               agree=sorted(p for p in sc if cL.get(p, -9) in sc[p]),
               a_perm=dict(mean=round(float(np.mean(perm)), 3), p99=float(np.percentile(perm, 99)), max=max(perm)),
               b_nonlocking=dict(mean=round(float(np.mean(nl)), 3), p99=float(np.percentile(nl, 99)), max=max(nl),
                                 distinct=sorted(set(nl)), degenerate=bool(degenerate)),
               c_shuffled_dupuy=dict(values=sh, max=max(sh)))
    res['verdict'] = 'NON-TEST' if degenerate else (
        'PASS' if hL > res['a_perm']['p99'] and hL > res['b_nonlocking']['p99'] and hL > max(sh) else 'FAIL')
    return res


def compute():
    tiles, rec = load()
    lines = sorted(rec)
    raw = {L: [t['cluster'] for t in tiles[L]] for L in lines}
    # sanity: the copied EM reproduces RUN2-NXATL's committed table on the raw clusters
    old = tsv(os.path.join(T, 'run2', 'nxatl', 'cluster_provisional_names.tsv'))
    by0, _ = em(tiles, rec, raw)
    assert [(r['cluster'], r['label'], int(r['support']), r['purity']) for r in old] == \
           [(r['cluster'], r['label'], r['support'], r['purity']) for r in prov_rows(by0)], 'EM copy differs from c262_align.py'
    merges = json.load(open(os.path.join(OS, 'summary.json')))['merges']
    own = {L: [merges.get(c, c) for c in raw[L]] for L in lines}
    split_tiles = [t['tile'] for L in lines for t in tiles[L] if t['cluster'] in SPLIT]
    by, align = em(tiles, rec, own)
    rows = prov_rows(by)
    K = json.load(open(os.path.join(HERE, 'results', 'basin_keys.json')))
    L = [K[f'alt{i:02d}'] for i in keytie.L_IDX]
    NL = [K[f'alt{i:02d}'] for i in keytie.NL_IDX]
    before = keytie.scored_piles(L)
    after = bridged(rows, L)
    # null: owner-pile ids permuted among c262 tiles, counts kept
    nulls = []
    for s in range(1, 21):
        allc = [c for L_ in lines for c in own[L_]]; random.Random(s).shuffle(allc); k = 0; sh = {}
        for L_ in lines:
            sh[L_] = allc[k:k + len(own[L_])]; k += len(own[L_])
        nulls.append(len(bridged(prov_rows(em(tiles, rec, sh)[0]), L)))
    primary_pass = len(after) > max(nulls) and len(after) > len(before)
    # conflicts
    oldlab = {r['cluster']: r['label'] for r in old}
    members = collections.defaultdict(list)
    for c in set(oldlab):
        members[merges.get(c, c)].append(c)
    conf_merge = []
    for p, ms in sorted(members.items()):
        ls = {m: oldlab[m] for m in sorted(ms)}
        if len(ms) > 1 and len({frozenset(lets(v)) or v for v in ls.values()}) > 1:
            conf_merge.append(dict(pile=p, members=ls))
    conf_runner = []
    for r in rows:
        if r['cluster'] not in after:
            continue
        for o in r['other'].split():
            lab, n = o.rsplit(':', 1)
            if int(n) * 3 >= r['support'] and lets(lab) and not (lets(lab) & lets(r['label'])):
                conf_runner.append(dict(pile=r['cluster'], label=r['label'], support=r['support'], runner_up=lab, n=int(n)))
    res = dict(c262_tiles=sum(len(v) for v in raw.values()), tiles_moved_by_merge=sum(a != b for L_ in lines for a, b in zip(raw[L_], own[L_])),
               split_parent_tiles=len(split_tiles), split_parent_tile_ids=split_tiles,
               B_before=len(before), B_after=len(after), B_null=nulls, B_null_max=max(nulls),
               primary='PASS' if primary_pass else 'FAIL',
               bridged_after={p: ''.join(sorted(chr(97 + x) for x in s)) for p, s in sorted(after.items())},
               new_piles=sorted(set(after) - set(before)), lost_piles=sorted(set(before) - set(after)),
               conflicts_merge=conf_merge, conflicts_runner_up=conf_runner)
    if primary_pass:
        res['secondary_widened'] = keytie_block(K, L, NL, after)
        res['secondary_old17'] = dict(H=keytie.H(keytie.consensus(L, before), before), n=len(before))
    return res, rows, tiles, align, own


def write(res, rows, tiles, align, own):
    json.dump(res, open(os.path.join(OUT, 'd07noxt_summary.json'), 'w'), indent=1)
    with open(os.path.join(OUT, 'd07noxt_provisional_owner.tsv'), 'w') as f:
        f.write('# owner pile -> provisional label from c262 tile position (D07-NOXT, grade M; EM of run2/nxatl/c262_align.py on owner piles)\n')
        f.write('pile\tlabel\tsupport\tpurity\tother_labels\n')
        for r in rows:
            f.write(f"{r['cluster']}\t{r['label']}\t{r['support']}\t{r['purity']}\t{r['other']}\n")
    _, rec = load()
    with open(os.path.join(OUT, 'd07noxt_c262_tiles.tsv'), 'w') as f:
        f.write('line\ttile\towner_pile\trecon_pos\trecon_label\n')
        for L in sorted(rec):
            for i, j in align[L]:
                f.write(f"{L}\t{tiles[L][i]['tile'] if i is not None else '-'}\t{own[L][i] if i is not None else '-'}\t"
                        f"{j + 1 if j is not None else '-'}\t{rec[L][j] if j is not None else '-'}\n")


def main(a):
    if a[:1] == ['score']:
        out = compute(); write(*out)
        print(json.dumps({k: v for k, v in out[0].items() if k != 'split_parent_tile_ids'}, indent=1))
    elif a[:1] == ['check']:
        res = compute()[0]
        if res != json.load(open(os.path.join(OUT, 'd07noxt_summary.json'))):
            sys.exit('d07noxt_summary.json stale')
        print('d07noxt_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
