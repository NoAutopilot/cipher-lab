#!/usr/bin/env python3
"""THUR-BAMF gate (PREREG-THUR-BAMF.md): can a Bamfylde 1655 letter table (Birch vol 4 printed gloss) give an
English-like string on the 24 letter codes of vol 6 p.160 (l.19092), against value-shuffled tables and two other
correspondents' keys, with a matched leave-page-out control on the vol 4 pool first.

  python3 gate_bamf.py --djvu V6_DJVU.txt   # (re)build trigram_v6.json.gz from the vol 6 djvu, then run
  python3 gate_bamf.py                      # run from the committed model; writes gate_bamf.json
  python3 gate_bamf.py --check              # exit 1 if gate_bamf.json is stale
"""
import argparse, collections, gzip, json, math, random, re, sys
from pathlib import Path

H = Path(__file__).resolve().parent
TP = H.parent
SEED, NSHUF, N = 1657, 1000, 24
A = 'abcdefghijklmnopqrstuvwxyz'


def build_model(djvu):
    lines = Path(djvu).read_text(encoding='utf-8', errors='replace').splitlines()
    keep = [l for i, l in enumerate(lines, 1) if not (19050 <= i <= 19200)]
    t = re.sub(r'[^a-z]', '', ' '.join(keep).replace('ſ', 's').lower())
    uni, bi, tri = collections.Counter(t), collections.Counter(), collections.Counter()
    for i in range(len(t) - 1):
        bi[t[i:i + 2]] += 1
    for i in range(len(t) - 2):
        tri[t[i:i + 3]] += 1
    m = {'n': len(t), 'uni': dict(uni), 'bi': dict(bi), 'tri': dict(tri)}
    with gzip.open(H / 'trigram_v6.json.gz', 'wt') as f:
        json.dump(m, f, sort_keys=True)


def load_model():
    with gzip.open(H / 'trigram_v6.json.gz', 'rt') as f:
        m = json.load(f)
    uni, bi, tri, n = m['uni'], m['bi'], m['tri'], m['n']
    def p(c, ctx):
        pu = (uni.get(c, 0) + .5) / (n + 13)
        if len(ctx) >= 1:
            a = ctx[-1]; da = uni.get(a, 0)
            pb = (bi.get(a + c, 0) + .5) / (da + 13)
        else:
            pb = pu
        if len(ctx) >= 2:
            ab = ctx[-2:]; dab = bi.get(ab, 0)
            pt = (tri.get(ab + c, 0) + .5) / (dab + 13)
        else:
            pt = pb
        return .6 * pt + .3 * pb + .1 * pu
    return p


def table_from(rows):
    votes = collections.defaultdict(collections.Counter)
    for r in rows:
        c, g = r['code'], r['gloss'].lower()
        if c.isdigit() and int(c) < 100 and len(g) == 1 and g in A:
            votes[int(c)][g] += 1
    T = {}
    for c, v in votes.items():
        top = v.most_common()
        if len(top) == 1 or top[0][1] > top[1][1]:
            T[c] = (top[0][0], top[0][1], sum(v.values()))
    return T  # code -> (letter, n_agree, n_total)


def score(runs, key, p):
    tot = 0.0; npos = 0
    for run in runs:
        ctx = ''
        for c in run:
            npos += 1
            if c in key:
                tot += math.log10(p(key[c], ctx)); ctx += key[c]
            else:
                tot += math.log10(1 / 26); ctx = ''
    return tot / npos


def shuffled(key, rng):
    codes = sorted(key); letters = [key[c] for c in codes]; rng.shuffle(letters)
    return dict(zip(codes, letters))


def test(runs, key, p, rng):
    real = score(runs, key, p)
    null = sorted(score(runs, shuffled(key, rng), p) for _ in range(NSHUF))
    p95 = null[int(.95 * NSHUF) - 1]
    return {'S': round(real, 4), 'null_mean': round(sum(null) / NSHUF, 4), 'null_p95': round(p95, 4),
            'null_max': round(null[-1], 4), 'p_emp': round((1 + sum(x >= real for x in null)) / (NSHUF + 1), 4),
            'coverage': f"{sum(c in key for r in runs for c in r)}/{sum(len(r) for r in runs)}",
            'pass': real > p95}


def first_n_runs(rows, n):
    """Letter-code positions (< 100) in reading order, runs split at codes >= 100 and run boundaries; first n."""
    runs, cur, left, last = [], [], n, None
    for r in rows:
        if (r['page'], r['run']) != last and cur:
            runs.append(cur); cur = []
        last = (r['page'], r['run'])
        c = int(r['code'])
        if c >= 100:
            if cur: runs.append(cur); cur = []
            continue
        if left == 0: break
        cur.append(c); left -= 1
    if cur: runs.append(cur)
    return runs


def other_key(name):
    k = {}
    for line in (TP / name).read_text().splitlines()[1:]:
        f = line.split('\t')
        if f[0].isdigit() and int(f[0]) < 100 and len(f[1]) == 1 and f[1].isalpha():
            k[int(f[0])] = f[1].lower()
    return k


def run():
    p = load_model()
    rows = [dict(zip(['page', 'run', 'pos', 'code', 'gloss'], l.split('\t'))) for l in
            (H / 'pairs_vol4.tsv').read_text().splitlines()[1:]]
    rows = [r | {'gloss': r.get('gloss', '')} for r in rows]
    out = {'prereg': 'PREREG-THUR-BAMF.md', 'seed': SEED, 'nshuf': NSHUF}
    rng = random.Random(SEED)
    # matched control first
    p194 = [r for r in rows if r['page'] in ('p194', 'p195')]
    p232 = [r for r in rows if r['page'] == 'p232']
    ctl = {}
    for fold, train, held in (('A_train194-195_test232', p194, p232), ('B_train232_test194-195', p232, p194)):
        T = {c: v[0] for c, v in table_from(train).items()}
        ctl[fold] = test(first_n_runs(held, N), T, p, rng) | {'table_size': len(T)}
    out['control'] = ctl
    out['control_pass'] = all(v['pass'] for v in ctl.values())
    # target
    TT = table_from(rows)
    T = {c: v[0] for c, v in TT.items()}
    out['table'] = {str(c): {'letter': v[0], 'agree': v[1], 'n': v[2]} for c, v in sorted(TT.items())}
    ct = [l for l in (H / 'ct_p160.txt').read_text().splitlines() if l and not l.startswith('#')][0]
    runs = [[int(x) for x in seg.split() if int(x) < 100] for seg in ct.split('|')]
    runs = [r for r in runs if r]
    assert sum(map(len, runs)) == N, runs
    out['target'] = test(runs, T, p, rng) | {'table_size': len(T)}
    for name in ('key_downing.tsv', 'key_lockhart.tsv'):
        k = other_key(name)
        out['other_' + name] = {'S': round(score(runs, k, p), 4), 'table_size': len(k),
                                'coverage': f"{sum(c in k for r in runs for c in r)}/{N}"}
    S = out['target']['S']
    out['gate_pass'] = bool(out['control_pass'] and out['target']['pass'] and
                            S > out['other_key_downing.tsv']['S'] and S > out['other_key_lockhart.tsv']['S'])
    out['verdict'] = ('PASS' if out['gate_pass'] else
                      'NON-TEST (control failed)' if not out['control_pass'] else 'FAIL')
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--djvu'); ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.djvu:
        build_model(a.djvu)
    out = json.dumps(run(), indent=1, sort_keys=True) + '\n'
    f = H / 'gate_bamf.json'
    if a.check:
        ok = f.exists() and f.read_text() == out
        print('gate_bamf.json', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    f.write_text(out); print(out)


if __name__ == '__main__':
    main()
