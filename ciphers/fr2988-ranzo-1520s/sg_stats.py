#!/usr/bin/env python3
"""Summarise sg_results.tsv against the A1B-RANZO-SG pre-registration (NOTES.md).

  python3 sg_stats.py --vasto <clone>/targets/vasto1527

Controls: mean/SD token accuracy per arm, C0-C1 and C0-C2 with 2xSE. Target: stable skeleton (types given the same word on
>=5 of 6 seeds, keys in the clone's n20/key_<arm>_<seed>.json) for T0 seeds 1-6, T0 seeds 7-12, T1, T2, and the movement
rule. Also counts how many of T1's relabelled tokens change type after solve2.py's own g->s / b->h merge (norm()).
"""
import argparse, collections, csv, json, math, os, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__))


def norm_types(toks):
    cnt = collections.Counter(toks)
    def n(t):
        if t == '|' or '?' in t or not t[1:].isdigit(): return None
        L, k = t[0], t[1:]
        if L == 'g' and cnt['s' + k] >= cnt[t]: L = 's'
        if L == 'b' and cnt['h' + k] >= cnt[t]: L = 'h'
        return L + k
    return [n(t) for t in toks]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--vasto', required=True); a = ap.parse_args()
    R = list(csv.DictReader(open(os.path.join(HERE, 'sg_results.tsv')), delimiter='\t'))
    acc = collections.defaultdict(list)
    for r in R:
        if r['token_acc']: acc[r['arm']].append(float(r['token_acc']))
    for arm in ('C0', 'C1', 'C2'):
        v = acc[arm]; print(f'{arm}: n {len(v)} token acc mean {st.mean(v):.4f} sd {st.stdev(v):.4f}')
    for arm in ('C1', 'C2'):
        d = st.mean(acc['C0']) - st.mean(acc[arm])
        se = math.sqrt(st.variance(acc['C0']) / len(acc['C0']) + st.variance(acc[arm]) / len(acc[arm]))
        print(f'C0-{arm}: {d:+.4f}, 2xSE {2 * se:.4f} -> {"matters" if d > 2 * se else "within noise"}')
    def stable(arm, seeds):
        keys = [json.load(open(os.path.join(a.vasto, 'n20', f'key_{arm}_{s}.json'))) for s in seeds]
        out = set()
        for t in keys[0]:
            c = collections.Counter(k.get(t) for k in keys).most_common(1)[0]
            if c[1] >= 5 and c[0] != '<null>': out.add((t, c[0]))
        return out
    S = {'T0a': stable('T0', range(1, 7)), 'T0b': stable('T0', range(7, 13)), 'T1': stable('T1', range(1, 7)),
         'T2': stable('T2', range(1, 7))}
    for k, v in S.items(): print(f'stable skeleton {k}: {len(v)} types')
    noise = abs(len(S['T0a']) - len(S['T0b']))
    for k in ('T1', 'T2'):
        d = abs(len(S[k]) - len(S['T0a']))
        print(f'{k}: |stable-T0| {d} vs noise {noise}+2 -> {"MOVEMENT" if d > noise + 2 else "no movement"}; '
              f'gained {sorted(S[k] - S["T0a"])[:12]} lost {sorted(S["T0a"] - S[k])[:12]}')
    print(f'overlap T0a/T0b {len(S["T0a"] & S["T0b"])}, T0a/T1 {len(S["T0a"] & S["T1"])}')
    t0 = open(os.path.join(HERE, 'bourdeau_relabelled', 'pooled_T0.txt')).read().split()
    t1 = open(os.path.join(HERE, 'bourdeau_relabelled', 'pooled_T1.txt')).read().split()
    n0, n1 = norm_types(t0), norm_types(t1)
    ch = [(x, y, p, q) for x, y, p, q in zip(t0, t1, n0, n1) if x != y]
    print(f'T1 relabelled tokens {len(ch)}; type unchanged after solve2 norm(): {sum(p == q for _, _, p, q in ch)}')


if __name__ == '__main__':
    main()
