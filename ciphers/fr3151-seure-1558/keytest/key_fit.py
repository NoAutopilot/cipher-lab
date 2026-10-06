#!/usr/bin/env python3
"""R9-SEURE key-fit test (PREREG-R9.md): Danzay 1557 key under a fixed label map vs f81R reads, shuffled-key null,
Danzay-own positive control. Usage: python3 key_fit.py OUT.json [--check]   (--check: recompute and compare to OUT.json)."""
import sys, gzip, glob, json, math, random, re, os
from collections import Counter
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(H, '..', '..', '..'))
MAP = {'2':'r2','4':'q4','6':'b6','7':'g7','8':'g8','9':'h9','3':'le','=':'eq','=/':'eq','*':'st','x':'x','x/':'x','y':'ven',
       'm':'sha','p':'hp','t':'pd','t/':'pd','#':'pp','#/':'pp','s':'ls','f':'fd','f/':'fd','o':'O','oo':'xinf'}
CODES = sorted(set(MAP.values()))
def norm(s):
    s = s.lower().replace('j','i').replace('v','u').replace('w','u')
    return re.sub('[^a-z]', '', s)
def load_key():
    k = {}
    for l in open(os.path.join(R, 'ciphers/fr20140-danzay-1557/key.tsv')):
        if l.startswith('#') or l.startswith('sign\t'): continue
        f = l.rstrip('\n').split('\t')
        v = f[2].split('|')[0]
        k[f[0]] = '' if v == 'null' else norm(v)
    return k
def train():
    c3, c2 = Counter(), Counter()
    for p in sorted(glob.glob(os.path.join(R, 'tools/data/fr16/*.gz'))):
        t = norm(gzip.open(p, 'rt', errors='ignore').read())
        for i in range(len(t) - 2): c3[t[i:i+3]] += 1; c2[t[i:i+2]] += 1
    return c3, c2
def F(runs, c3, c2):
    tot, n = 0.0, 0
    for r in runs:
        for i in range(len(r) - 2):
            tot += math.log10((c3[r[i:i+3]] + 0.5) / (c2[r[i:i+2]] + 13.0)); n += 1
    return tot / n if n else float('nan'), n
def decode(codes, val):
    """codes: list of glyph codes or None (gap). Returns letter runs."""
    runs, cur = [], ''
    for c in codes:
        if c is None or c not in val:
            if cur: runs.append(cur)
            cur = ''
        else: cur += val[c]
    if cur: runs.append(cur)
    return runs
def null(codes, val, c3, c2, draws, rng):
    ks = sorted(val); vs = [val[k] for k in ks]; out = []
    for _ in range(draws):
        rng.shuffle(vs); out.append(F(decode(codes, dict(zip(ks, vs))), c3, c2)[0])
    out.sort(); return out
def main():
    out = sys.argv[1]; check = '--check' in sys.argv
    key = load_key(); val = {c: key[c] for c in CODES}; c3, c2 = train(); res = {'map': MAP, 'values': val}
    # positive control on Danzay's own ciphertext
    toks = []
    for l in open(os.path.join(R, 'ciphers/fr20140-danzay-1557/ciphertext.txt')):
        if l.startswith('#') or l.startswith('line\t'): continue
        s = l.split('\t')[2]
        if s.startswith('w:') or 'g' in l.split('\t')[0][-1:]: continue
        toks.append(s)
    toks = toks[:461]; inv = sorted(set(toks)); res['control'] = {}
    res['control']['coverage'] = sum(t in val for t in toks) / len(toks)
    for err in (0, 0.095, 0.242):
        rows = []
        for seed in (1, 2, 3):
            rng = random.Random(seed * 1000 + int(err * 1000))
            t2 = [rng.choice([x for x in inv if x != t]) if rng.random() < err else t for t in toks]
            codes = [t if t in val else None for t in t2]
            f, n = F(decode(codes, val), c3, c2); nl = null(codes, val, c3, c2, 1000, random.Random(seed))
            rows.append({'seed': seed, 'F': round(f, 4), 'trigrams': n, 'null_p95': round(nl[949], 4), 'null_max': round(nl[-1], 4), 'pass': f > nl[949]})
        res['control'][str(err)] = rows
    power = all(sum(r['pass'] for r in res['control'][e]) >= 2 for e in ('0.095', '0.242')); res['power'] = power
    for rd in ('R1', 'R2'):
        codes = []
        for l in open(os.path.join(H, '..', 'kp', f'f81R_recon_{rd}.tsv')).read().splitlines()[1:]:
            for s in l.split('\t')[1].split(): codes.append(MAP.get(s))
        f, n = F(decode(codes, val), c3, c2); nl = null(codes, val, c3, c2, 1000, random.Random(7))
        res[rd] = {'signs': len(codes), 'mapped': sum(c is not None for c in codes), 'F': round(f, 4), 'trigrams': n,
                   'null_mean': round(sum(nl) / len(nl), 4), 'null_p95': round(nl[949], 4), 'null_max': round(nl[-1], 4),
                   'pass': f > nl[949], 'decode_runs': decode(codes, val)}
    if check:
        old = json.load(open(out)); ok = json.dumps(old, sort_keys=True) == json.dumps(json.loads(json.dumps(res)), sort_keys=True)
        print('check', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    json.dump(res, open(out, 'w'), indent=1, ensure_ascii=False)
    print(json.dumps({k: v for k, v in res.items() if k not in ('map', 'values')}, default=str)[:3000])
main()
