#!/usr/bin/env python3
"""DEB-SWARM-A driver: fit a homophonic key on FIT, score it held-out on TEST, and rank that held-out score against
NNULL keys fitted the same way on FIT with its token order shuffled (the order-shuffled-fit null: it keeps every
sign-frequency/letter-frequency match and destroys only sequence, so it is the null the value-shuffled one is not).
usage: pipeline.py FIT.cip TEST.cip OUTPREFIX [--alpha 26|27] [--R 8] [--it 5000000] [--nnull 10] [--seed 7]
Prints JSON: fit key file, held-out line (coverage, real, shuf_mean, value-shuffle percentile), null held-out reals, rank."""
import sys, os, subprocess, random, json, argparse, re
H = os.path.dirname(os.path.abspath(__file__)); W = os.path.join(H, 'work'); B = os.path.join(W, 'hsolve')
ap = argparse.ArgumentParser(); ap.add_argument('fit'); ap.add_argument('test'); ap.add_argument('out')
ap.add_argument('--alpha', type=int, default=26); ap.add_argument('--R', type=int, default=8); ap.add_argument('--it', type=int, default=5000000)
ap.add_argument('--nnull', type=int, default=10); ap.add_argument('--seed', type=int, default=7); ap.add_argument('--floor', default='-4')
a = ap.parse_args()
train = os.path.join(W, 'train_sp.txt' if a.alpha == 27 else 'train.txt')
env = dict(os.environ, ALPHA=str(a.alpha), FLOOR=a.floor)
def fit(cipfile, seed):
    o = subprocess.run([B, train, cipfile, str(a.R), str(a.it), str(seed), '0.3', '5'], capture_output=True, text=True, env=env).stdout
    seen = set(open(cipfile).read().split())
    key = [l for l in o.split('\n') if re.fullmatch(r'\d+ [a-z{]', l) and l.split()[0] in seen]
    return o, key
def held(keylines, tag):
    kf = f'{a.out}_{tag}.key'; open(kf, 'w').write('\n'.join(keylines) + '\n')
    e = dict(env, HELDOUT=kf)
    o = subprocess.run([B, train, a.test, '1', '1', '1', '0.3', '5'], capture_output=True, text=True, env=e).stdout.strip()
    d = dict(zip(o.split()[1::2], o.split()[2::2])); return {k: float(v) for k, v in d.items()}
o, key = fit(a.fit, a.seed); open(a.out + '_fit.txt', 'w').write(o)
res = {'fit_score': o.split('\n')[0], 'heldout': held(key, 'real')}
toks = open(a.fit).read().split(); rng = random.Random(a.seed); nulls = []
for j in range(a.nnull):
    t = toks[:]; rng.shuffle(t); nf = f'{a.out}_null{j}.cip'; open(nf, 'w').write(' '.join(t) + '\n')
    _, k2 = fit(nf, a.seed + 100 + j); nulls.append(held(k2, f'null{j}')['real'])
res['null_reals'] = nulls
res['rank_vs_orderfit_null'] = f"{sum(x >= res['heldout']['real'] for x in nulls)} of {len(nulls)} null fits score >= real"
print(json.dumps(res))
