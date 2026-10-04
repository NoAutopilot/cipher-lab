#!/usr/bin/env python3
"""NOX-OWNERSORT (account 3 worker, 4 Oct 2026): does the owner's quick sort of the Noailles c510-516 sorter hold up
against the two RUN2 machine readers, and where would deeper sorting pay?  Pre-registered in PREREG.md (same folder).

  python3 nox_ownersort.py            # run from this folder; writes merges.tsv, impurity.tsv, next_targets.tsv, results.json
  python3 nox_ownersort.py --check    # exit 1 if the committed outputs differ from a fresh run (rule 7)

Reads only committed files: ../settled_labels.tsv, ../summary.json, run2/nxatl/sequences.tsv, run2/nxatl/
cluster_provisional_names.tsv, run2/nxta/passA|B.tsv, run2/nxtb/passA|B.tsv, run2/nxtb/c515/passA|B.tsv, key.tsv.
No decode, no reading: key.tsv is used only to ask whether two reader labels stand for different plaintext letters.
"""
import csv, json, math, os, random, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '../../..'))
R = f'{T}/run2'
MIN_SUP, NNEAR, CTRL_SETS = 8, 8, 200


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


# ---- atlas tiles and owner piles
seq = [r for r in tsv(f'{R}/nxatl/sequences.tsv') if r['leaf'] != 'c262']
lines = defaultdict(list)
clus, knn1 = {}, {}
for r in seq:
    lines[(r['leaf'], r['line'])].append((int(r['pos']), r['tile']))
    clus[r['tile']] = r['cluster']
    knn1[r['tile']] = (r['k1'], float(r['s1']))
for k in lines:
    lines[k] = [t for _, t in sorted(lines[k])]
settled = {r['sid']: r for r in tsv(f'{HERE}/../settled_labels.tsv')}
summ = json.load(open(f'{HERE}/../summary.json'))
merges = summ['merges']
owner = {}
for t in clus:
    s = settled.get(t)
    owner[t] = (s['new_sign'] or 'BAD-CUT') if s else clus[t]
size = Counter(clus.values())


# ---- reader passes: (group, pass) -> {reader line: [labels]}
def norm(l):
    return l.rstrip('?') or l


def load_long(p):
    d = defaultdict(list)
    for r in tsv(p):
        d[r['line']].append((int(r['pos']), norm(r['sign'])))
    return {k: [s for _, s in sorted(v)] for k, v in d.items()}


def load_wide(p):
    d = {}
    for l in open(p):
        if '\t' in l:
            a, b = l.rstrip('\n').split('\t', 1)
            d[a] = [norm(x) for x in b.split()]
    return d


passes = {('nxta', 'A'): load_long(f'{R}/nxta/passA.tsv'), ('nxta', 'B'): load_long(f'{R}/nxta/passB.tsv'),
          ('nxtb', 'A'): {**load_wide(f'{R}/nxtb/passA.tsv'), **load_wide(f'{R}/nxtb/c515/passA.tsv')},
          ('nxtb', 'B'): {**load_wide(f'{R}/nxtb/passB.tsv'), **load_wide(f'{R}/nxtb/c515/passB.tsv')}}


def atlas_line(rl):
    m = re.match(r'(c51\d)(a|b)?_L(\d+)', rl)
    leaf, half, n = m.group(1), m.group(2), int(m.group(3))
    if leaf == 'c510':
        return ('c510', f'L{n + 5:02d}')
    if leaf == 'c515':
        return ('c515', f'L{n:02d}')
    if half == 'a':
        return ('c516', f'L{n:02d}')
    if n in (4, 5):
        return None                          # blot: both land on atlas L09, dropped (PREREG)
    return ('c516', f'L{n + 5 if n <= 3 else n + 4:02d}')


# ---- placement P1 (same fraction) and P2 (NW with hard-EM label|cluster scores)
def place_p1(labels, tiles):
    out = {}
    for i, l in enumerate(labels):
        j = min(len(tiles) - 1, max(0, round((i + 0.5) / len(labels) * len(tiles) - 0.5)))
        out.setdefault(tiles[j], l)
    return out


def nw(labels, tiles, score, gap=-1.5):
    n, m = len(labels), len(tiles)
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0], B[i][0] = i * gap, 1
    for j in range(1, m + 1):
        D[0][j], B[0][j] = j * gap * 0.5, 2          # extra tiles (split signs) cost less than missing ones
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            band = abs(i / n - j / m) > 0.25
            c = [D[i - 1][j - 1] + score(labels[i - 1], tiles[j - 1]) - (5 if band else 0),
                 D[i - 1][j] + gap, D[i][j - 1] + gap * 0.5]
            k = max(range(3), key=lambda x: c[x])
            D[i][j], B[i][j] = c[k], k
    out, i, j = {}, n, m
    while i > 0 and j > 0:
        k = B[i][j]
        if k == 0:
            out[tiles[j - 1]] = labels[i - 1]; i -= 1; j -= 1
        elif k == 1:
            i -= 1
        else:
            j -= 1
    return out


def placements():
    jobs = []
    for gp, d in passes.items():
        for rl, labels in d.items():
            al = atlas_line(rl)
            if al and al in lines and labels:
                jobs.append((gp, labels, lines[al]))
    p1 = defaultdict(dict)
    for gp, labels, tiles in jobs:
        p1[gp].update(place_p1(labels, tiles))
    cur = p1
    for _ in range(5):                                   # hard EM over P(label|cluster)
        cnt, tot = defaultdict(Counter), Counter()
        for gp in cur:
            for t, l in cur[gp].items():
                cnt[clus[t]][l] += 1; tot[clus[t]] += 1
        V = len({l for c in cnt.values() for l in c}) + 1

        def score(l, t):
            c = clus[t]
            return math.log((cnt[c][l] + 0.5) / (tot[c] + 0.5 * V)) + math.log(V) * 0.6
        nxt = defaultdict(dict)
        for gp, labels, tiles in jobs:
            nxt[gp].update(nw(labels, tiles, score))
        cur = nxt
    return p1, cur


# ---- statistics
def dists(place, pile_of):
    """pile -> {(group,pass): Counter(label)}"""
    d = defaultdict(lambda: defaultdict(Counter))
    for gp, m in place.items():
        for t, l in m.items():
            d[pile_of[t]][gp][l] += 1
    return d


def S(d, a, b):
    vals = []
    for gp in passes:
        ca, cb = d[a].get(gp), d[b].get(gp)
        if not ca or not cb:
            continue
        na, nb = sum(ca.values()), sum(cb.values())
        vals.append(sum(ca[l] * cb[l] for l in ca) / (na * nb))
    return sum(vals) / len(vals) if vals else None


def support(d, a):
    return sum(sum(c.values()) for c in d[a].values()) / 2.0      # mean per reader-pass pair (2 groups x 2 passes / 2)


def nearest(p, excl, k=NNEAR):
    c = [q for q in size if q not in excl]
    return sorted(c, key=lambda q: (abs(size[q] - size[p]), q))[:k]


def merge_table(d, prov):
    rows = []
    for a, b in sorted(merges.items()):
        s = S(d, a, b)
        null = [x for x in (S(d, x, y) for x in nearest(a, {a, b}) for y in nearest(b, {a, b}) if x != y) if x is not None]
        null.sort()
        sa, sb = support(d, a), support(d, b)
        if s is None or min(sa, sb) < MIN_SUP:
            v = 'readers silent'
        else:
            p90, med = null[int(0.9 * (len(null) - 1))], null[len(null) // 2]
            v = 'corroborated' if s > p90 else ('not corroborated' if s <= med else 'weak')
        pct = sum(x < s for x in null) / len(null) if (s is not None and null) else None
        rows.append(dict(a=a, b=b, size_a=size[a], size_b=size[b], sup_a=sa, sup_b=sb, S=s,
                         null_med=null[len(null) // 2] if null else None, null_p90=null[int(0.9 * (len(null) - 1))] if null else None,
                         pct=pct, verdict=v, c262_S=prov(a, b)))
    return rows


provd = {}
for r in tsv(f'{R}/nxatl/cluster_provisional_names.tsv'):
    c = Counter({r['label']: round(float(r['purity']) * int(r['support']))})
    for x in r['other_labels'].split():
        l, n = x.rsplit(':', 1); c[l] += int(n)
    provd[r['cluster']] = c


def prov(a, b):
    ca, cb = provd.get(a), provd.get(b)
    if not ca or not cb or sum(ca.values()) < 3 or sum(cb.values()) < 3:
        return None
    return sum(ca[l] * cb[l] for l in ca) / (sum(ca.values()) * sum(cb.values()))


def agreed(place):
    """tile -> label where both passes of the same reader group put the same label on the tile"""
    out = {}
    for g in ('nxta', 'nxtb'):
        A, B = place.get((g, 'A'), {}), place.get((g, 'B'), {})
        for t in A:
            if B.get(t) == A[t]:
                out[t] = A[t]
    return out


def impurity(ag, pile_of):
    c = defaultdict(Counter)
    for t, l in ag.items():
        c[pile_of[t]][l] += 1
    N = sum(sum(x.values()) for x in c.values())
    imp = 1 - sum(max(x.values()) for x in c.values()) / N
    H = -sum(n / N * math.log2(n / sum(x.values())) for x in c.values() for n in x.values())
    return imp, H, N


# key letters for a reader label (only to ask: do two labels stand for different letters?)
def letters(l):
    if l.startswith('?{') or l in ('?', ''):
        return None
    if l.startswith('W:'):
        return {l}
    out = set()
    for p in l.split('/'):
        m = re.match(r'([a-zA-Z]+?)(\d+)$', p)
        out.add(('N' if m and m.group(1) == 'N' else m.group(1)) if m else p)
    return out


def differ(l1, l2):
    a, b = letters(l1), letters(l2)
    if a is None or b is None:
        return 0.5
    return 0.0 if a & b else 1.0


def run():
    p1, p2 = placements()
    res = {}
    for name, pl in (('P1', p1), ('P2', p2)):
        d = dists(pl, clus)
        res[name] = merge_table(d, prov)
    # step 2: impurity vs agreed reader labels, before / after, with random-merge control
    imp = {}
    rnd = random.Random(20261004)
    for name, pl in (('P1', p1), ('P2', p2)):
        ag = {t: l for t, l in agreed(pl).items() if owner[t] != 'BAD-CUT'}
        before = impurity(ag, clus)
        after = impurity(ag, owner)
        ctrl = []
        for _ in range(CTRL_SETS):
            mp, used = {}, set()
            for a, b in merges.items():
                x = rnd.choice(nearest(a, used | {a}))
                y = rnd.choice(nearest(b, used | {x, b}))
                used |= {x, y}; mp[x] = y
            pile = {t: mp.get(clus[t], clus[t]) for t in ag}
            ctrl.append(impurity(ag, pile)[0] - before[0])
        ctrl.sort()
        imp[name] = dict(n_agreed=before[2], before=before[0], after=after[0], H_before=before[1], H_after=after[1],
                         delta=after[0] - before[0], ctrl_mean=sum(ctrl) / len(ctrl), ctrl_p05=ctrl[int(0.05 * len(ctrl))],
                         ctrl_p50=ctrl[len(ctrl) // 2],
                         share_ctrl_le_owner=sum(c <= after[0] - before[0] for c in ctrl) / len(ctrl))
    # siblings: two source piles merged into the same target should match each other too
    sib = []
    tgt = defaultdict(list)
    for a, b in merges.items():
        tgt[b].append(a)
    for name, pl in (('P1', p1), ('P2', p2)):
        d = dists(pl, clus)
        for b, srcs in sorted(tgt.items()):
            for i in range(len(srcs)):
                for j in range(i + 1, len(srcs)):
                    a1, a2 = sorted((srcs[i], srcs[j]))
                    s = S(d, a1, a2)
                    null = [x for x in (S(d, x, y) for x in nearest(a1, {a1, a2}) for y in nearest(a2, {a1, a2}) if x != y) if x is not None]
                    sib.append(dict(placement=name, target=b, a=a1, b=a2, S=s, sup_a=support(d, a1), sup_b=support(d, a2),
                                    pct=(sum(x < s for x in null) / len(null)) if (s is not None and null) else None))
    res['siblings'] = sib
    # step 3, pre-registered rule on P1 (label-blind): mixed owner piles
    def mixed_piles(pl, rule_p1):
        ag = {t: l for t, l in agreed(pl).items() if owner[t] != 'BAD-CUT'}
        byp = defaultdict(Counter)
        for t, l in ag.items():
            byp[owner[t]][l] += 1
        out = []
        for p, c in byp.items():
            n = sum(c.values())
            if n < 15:
                continue
            (l1, n1), (l2, n2) = (c.most_common(2) + [(None, 0)])[:2]
            if not l2 or differ(l1, l2) == 0:
                continue
            if rule_p1 and not (n1 / n >= 0.25 and n2 / n >= 0.25):
                continue
            out.append(dict(pile=p, tiles=len(pile_tiles[p]), n_agreed=n, top1=f'{l1}:{n1}', top2=f'{l2}:{n2}',
                            second_share=n2 / n, knn_split=split[p], removable=(n - n1) / len(ag),
                            score=(n - n1) * differ(l1, l2)))
        out.sort(key=lambda r: (-r['score'], r['pile']))
        return out, ag, byp
    pile_tiles = defaultdict(list)
    for t, p in owner.items():
        pile_tiles[p].append(t)
    split = {p: sum(knn1[t][0] != clus[t] for t in ts) / len(ts) for p, ts in pile_tiles.items()}
    res['step3_prereg_P1'] = mixed_piles(p1, True)[0]
    # exploratory (deviation from PREREG, labelled): P1 found none, so rank on P2 (EM placement; sharper, partly circular)
    mixed, ag, byp = mixed_piles(p2, False)
    # merge whose sibling sources disagree on both placements -> its target pile is a re-check pile
    bad_sib = sorted({x['target'] for x in sib if x['S'] is not None and x['pct'] is not None and x['pct'] <= 0.1
                      and x['placement'] == 'P1'} & {x['target'] for x in sib if x['placement'] == 'P2' and x['S'] is not None
                                                     and x['pct'] is not None and x['pct'] <= 0.1})
    piles = [m for m in mixed if m['pile'] not in bad_sib][:2]
    for b in bad_sib[:1]:
        piles.append(dict(pile=b, tiles=len(pile_tiles[b]), sibling_check=True,
                          sources=[a for a, t in merges.items() if t == b]))
    piles = piles[:3]
    maj = {p: c.most_common(1)[0][0] for p, c in byp.items()}
    cand = {m['pile'] for m in mixed[:4]} | set(bad_sib) | {b for a, b in merges.items()}
    tiles = []
    for t, l in ag.items():
        p = owner[t]
        if p not in cand or p not in maj or l == maj[p] or differ(l, maj[p]) < 1:
            continue
        own_share = knn1[t][1] if knn1[t][0] == clus[t] else 0.0
        tiles.append(dict(sid=t, pile=p, pile_majority=maj[p], readers_agree=l, letters_differ=1.0,
                          knn_k1=knn1[t][0], own_knn_share=own_share, score=1 - own_share))
    tiles.sort(key=lambda r: (-r['score'], r['sid']))
    mixed = piles
    return res, imp, mixed, tiles


def fmt(v):
    return '' if v is None else (f'{v:.3f}' if isinstance(v, float) else str(v))


def write(res, imp, mixed, tiles, out):
    cols = ['a', 'b', 'size_a', 'size_b', 'sup_a', 'sup_b', 'S', 'null_med', 'null_p90', 'pct', 'verdict']
    with open(f'{out}/merges.tsv', 'w') as f:
        f.write('# NOX-OWNERSORT step 1: per owner merge a->b, reader-label overlap S vs 64 size-matched pile pairs (PREREG.md)\n')
        f.write('\t'.join(['merge'] + [f'P1_{c}' for c in cols[2:]] + ['P2_S', 'P2_pct', 'P2_verdict', 'c262_S']) + '\n')
        for r1, r2 in zip(res['P1'], res['P2']):
            f.write('\t'.join([f"{r1['a']}->{r1['b']}"] + [fmt(r1[c]) for c in cols[2:]] +
                              [fmt(r2['S']), fmt(r2['pct']), r2['verdict'], fmt(r1['c262_S'])]) + '\n')
    with open(f'{out}/impurity.tsv', 'w') as f:
        f.write('# NOX-OWNERSORT step 2: pile impurity vs signs both passes of one reader agree on; control = 200 random 18-merge sets\n')
        keys = list(imp['P1'].keys())
        f.write('placement\t' + '\t'.join(keys) + '\n')
        for k, v in imp.items():
            f.write(k + '\t' + '\t'.join(fmt(v[x]) for x in keys) + '\n')
    with open(f'{out}/next_targets.tsv', 'w') as f:
        f.write('# NOX-OWNERSORT step 3: what to sort next, ranked (at most 3 piles + 40 tiles). No reading is claimed.\n')
        f.write('kind\tid\tpile\twhy\n')
        for m in mixed[:3]:
            if m.get('sibling_check'):
                f.write(f"pile\t{m['pile']}\t{m['pile']}\tre-check the merge: sources {' and '.join(m['sources'])} were both merged into "
                        f"{m['pile']} but the two readers give the two sources different labels (S at or below the 10th percentile of "
                        f"size-matched pairs on both placements); undo one if the shapes differ\n")
                continue
            f.write(f"pile\t{m['pile']}\t{m['pile']}\tmixed on the readers: {m['n_agreed']} agreed signs split {m['top1']} / {m['top2']} "
                    f"(different letters, EM placement P2, exploratory); kNN puts {m['knn_split']:.0%} of its tiles nearer another cluster; split it into two piles\n")
        for t in tiles[:40]:
            f.write(f"tile\t{t['sid']}\t{t['pile']}\tboth passes read {t['readers_agree']}, pile majority {t['pile_majority']} "
                    f"(letters differ {t['letters_differ']:.1f}); atlas k1 {t['knn_k1']}, own-cluster vote {t['own_knn_share']:.2f}\n")
    json.dump(dict(merges=res, impurity=imp, mixed=mixed, n_tile_candidates=len(tiles)), open(f'{out}/results.json', 'w'),
              indent=1, sort_keys=True, default=lambda x: round(x, 6))


if __name__ == '__main__':
    res, imp, mixed, tiles = run()
    if '--check' in sys.argv:
        import tempfile, filecmp
        d = tempfile.mkdtemp()
        write(res, imp, mixed, tiles, d)
        bad = [f for f in ('merges.tsv', 'impurity.tsv', 'next_targets.tsv', 'results.json')
               if not filecmp.cmp(f'{d}/{f}', f'{HERE}/{f}', shallow=False)]
        print('CHECK', 'FAIL ' + ' '.join(bad) if bad else 'OK')
        sys.exit(1 if bad else 0)
    write(res, imp, mixed, tiles, HERE)
    for r in res['P1']:
        print(r['a'], r['b'], r['verdict'], fmt(r['S']), fmt(r['pct']), fmt(r['sup_a']), fmt(r['sup_b']))
    print(json.dumps(imp, indent=1, default=lambda x: round(x, 4)))
    print('piles', mixed, 'tiles', len(tiles))
    print('prereg P1 step3', res['step3_prereg_P1'])
    [print(x) for x in res['siblings']]
