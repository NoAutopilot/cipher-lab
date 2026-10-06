#!/usr/bin/env python3
"""R9-SEURE2 key-fit test (PREREG-R9B.md): Bourdeau's La Guiche 1551 key under a fixed label map vs the f81R reads.
Unigram fit U, shuffled-key null, La Guiche own-text power control first (exit 3 if below gate).
Usage: python3 guiche_fit.py OUT.json [--check]   (--check: recompute and compare to OUT.json)."""
import sys, gzip, glob, json, math, random, re, os
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, '..', '..', '..'))
MAP = {'#':'#','#/':'X','3':'3','4':'4','oo':'8','+':'+','t':'t','t/':'t','ff':'F','ff/':'F','f':'f','f/':'f','p':'p',
       'W':'W','P':'P','A':'A','A/':'A','e/':'e','d':'d','g':'g','r':'r'}
CODES = sorted(set(MAP.values()))
ERRS = [0.0, 0.095, 0.242]; DRAWS = 1000
def norm(s): return re.sub('[^a-z]', '', s.lower().replace('j','i').replace('v','u').replace('w','u'))
def load_key():
    k = {}
    for l in open(os.path.join(H, 'guiche_key.tsv')):
        if l.startswith('# ') or l.startswith('code\t'): continue
        f = l.rstrip('\n').split('\t'); k[f[0]] = f[1]
    return k
def unigram():
    c = Counter()
    for p in sorted(glob.glob(os.path.join(R, 'tools/data/fr16/*.gz'))):
        c.update(norm(gzip.open(p, 'rt', errors='ignore').read()))
    tot = sum(c.values()) + 0.5 * 26
    return {ch: math.log10((c[ch] + 0.5) / tot) for ch in 'abcdefghijklmnopqrstuvwxyz'}
def U(codes, val, lp):
    xs = [lp[ch] for c in codes if c in val for ch in norm(val[c])]
    return sum(xs) / len(xs) if xs else float('nan'), len(xs)
def null(codes, val, lp, rng):
    vs = [val[c] for c in CODES]; out = []
    for _ in range(DRAWS):
        rng.shuffle(vs); out.append(U(codes, dict(zip(CODES, vs)), lp)[0])
    out.sort(); return out
def summ(codes, val, lp, rng):
    u, n = U(codes, val, lp); nl = null(codes, val, lp, rng)
    p95 = nl[int(0.95 * DRAWS) - 1]
    return {'U': round(u, 4), 'n': n, 'null_mean': round(sum(nl) / len(nl), 4), 'null_p95': round(p95, 4),
            'null_max': round(nl[-1], 4), 'pass': u > p95}
def main():
    out_path = sys.argv[1]; check = '--check' in sys.argv
    key = load_key(); lp = unigram(); val = {c: key[c] for c in CODES}
    own = [s for l in open(os.path.join(H, 'guiche_ct.txt')) if l.startswith('L') for s in l.split()[1:] if s != ':']
    allc = sorted(set(own)); res = {'own_len': len(own), 'control': []}
    for e in ERRS:
        for seed in (1, 2, 3):
            rng = random.Random(1000 * seed + int(e * 1000)); t = own[:]
            for i in range(len(t)):
                if rng.random() < e: t[i] = rng.choice([c for c in allc if c != t[i]])
            r = summ(t, val, lp, rng); r.update(err=e, seed=seed); res['control'].append(r)
    ok = lambda e: sum(r['pass'] for r in res['control'] if r['err'] == e) >= 2
    res['power'] = ok(0.095) and ok(0.242)
    if res['power']:
        for name in ('R1', 'R2'):
            labs = [s for l in open(os.path.join(H, '..', 'kp', f'f81R_recon_{name}.tsv'))
                    if l.startswith('L') for s in l.rstrip('\n').split('\t')[-1].split()]
            codes = [MAP.get(s) for s in labs]
            r = summ(codes, val, lp, random.Random(7)); r.update(signs=len(labs), mapped=sum(c is not None for c in codes))
            r['decode_sample'] = ''.join(val[c] if c else '.' for c in codes)[:200]; res[name] = r
    if check:
        old = json.load(open(out_path))
        if old != json.loads(json.dumps(res)): print('STALE'); sys.exit(1)
        print('check OK'); return
    json.dump(res, open(out_path, 'w'), indent=1); print(json.dumps(res, indent=1))
    if not res['power']: print('CONTROL BELOW GATE: NON-TEST'); sys.exit(3)
main()
