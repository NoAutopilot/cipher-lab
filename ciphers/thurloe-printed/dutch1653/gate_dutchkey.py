#!/usr/bin/env python3
"""DUTCH-KEY gate, supporting folds and the p.435 controls, exactly as PREREG-DUTCHKEY.md (pushed 6f9dbc5f7 before any score).

  python3 gate_dutchkey.py            compute and write gate_dutchkey.json (numbers only; prints no p.435 text)
  python3 gate_dutchkey.py --check    recompute and exit 1 if gate_dutchkey.json differs
  python3 gate_dutchkey.py --no-435   stop after the gate and the folds (used when the gate FAILs)
"""
import csv, glob, gzip, json, math, os, random, re, sys, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(H, '..', '..', '..'))
SEED, DRAWS = 20261010, 1000
REFS = {1: 'princessedouariere', 2: 'graefwillem', 3: 'haerehoocheyt', 4: 'grave', 5: 'haerehoocheyt',
        7: 'designeren', 8: 'haerehoocheyt', 9: 'haerehoocheyt', 10: 'haerhoff', 11: 'haerehoocheyt'}
TRAIN_PAGES = ['071', '072', '073'] + [f'{i:03d}' for i in range(91, 99)] + [f'{i:03d}' for i in range(102, 108)] + \
              [f'{i:03d}' for i in range(109, 113)]

def norm(s):
    s = unicodedata.normalize('NFKD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.replace('v', 'u').replace('j', 'i')

def html_text(p):
    return re.sub(r'<[^>]+>', ' ', open(p, encoding='utf-8', errors='ignore').read())

def keylist():
    rows = list(csv.DictReader(open(os.path.join(H, 'key_dewitt_1653.tsv')), delimiter='\t'))
    return [int(r['code']) for r in rows], [norm(r['letter']) for r in rows]

def runs(name):
    out = {}
    for r in csv.DictReader(open(os.path.join(H, f'ct_{name}.tsv')), delimiter='\t'):
        out.setdefault((r['page'], int(r['run'])), []).append(int(r['token']))
    return out

def dec(tokens, K):
    return ''.join(K[t] for t in tokens if t in K)

def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]

def gate_stat(R, K):
    L = n = 0
    for (p, run), toks in R.items():
        if run not in REFS: continue
        d = dec(toks, K); L += lcs(d, REFS[run]); n += len(d)
    return L / n if n else 0.0

class Quad:
    def __init__(self, text):
        self.A = sorted(set(text)); self.c4, self.c3 = {}, {}
        for i in range(3, len(text)):
            g = text[i - 3:i + 1]; self.c4[g] = self.c4.get(g, 0) + 1; self.c3[g[:3]] = self.c3.get(g[:3], 0) + 1
        self.V = 25
    def lp(self, ctx, c):
        return math.log10((self.c4.get(ctx + c, 0) + 1) / (self.c3.get(ctx, 0) + self.V))
    def score(self, strings):
        tot = n = 0
        for s in strings:
            for i in range(3, len(s)):
                tot += self.lp(s[i - 3:i], s[i]); n += 1
        return tot / n if n else float('nan')

def model():
    parts = [html_text(os.path.join(H, 'edition', f'VAN_DEWITT_01_{p}.html')) for p in TRAIN_PAGES]
    for f in sorted(glob.glob(os.path.join(ROOT, 'tools', 'data', 'nl16', '*.txt.gz'))):
        parts.append(gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read())
    return Quad(norm(' '.join(parts)))

def perms(letters):
    rng = random.Random(SEED); out = []
    for _ in range(DRAWS):
        l = letters[:]; rng.shuffle(l); out.append(l)
    return out

def summ(real, ctrl):
    s = sorted(ctrl)
    return {'decode': round(real, 4), 'ctrl_p95': round(s[int(0.95 * len(s)) - 1], 4), 'ctrl_max': round(s[-1], 4),
            'ctrl_mean': round(sum(s) / len(s), 4), 'frac_ctrl_ge_decode': round(sum(1 for x in s if x >= real) / len(s), 4)}

def fold(R, Q, codes, letters, P):
    strs = lambda K: [dec(t, K) for t in R.values()]
    real = Q.score(strs(dict(zip(codes, letters))))
    return summ(real, [Q.score(strs(dict(zip(codes, l)))) for l in P]), sum(len(x) for x in strs(dict(zip(codes, letters))))

def main():
    codes, letters = keylist(); K = dict(zip(codes, letters)); P = perms(letters)
    out = {'prereg': '6f9dbc5f7', 'seed': SEED, 'draws': DRAWS}
    R = runs('p351'); toks = [t for v in R.values() for t in v]
    g = summ(gate_stat(R, K), [gate_stat(R, dict(zip(codes, l))) for l in P])
    g['coverage'] = round(sum(1 for t in toks if t <= 66) / len(toks), 4); g['tokens'] = len(toks)
    g['per_run'] = {str(r): [lcs(dec(t, K), REFS[r]), len(dec(t, K))] for (p, r), t in R.items() if r in REFS}
    g['PASS'] = bool(g['decode'] >= 0.80 and g['decode'] > g['ctrl_p95'])
    out['gate_p351'] = g
    Q = model()
    for n in ('p339', 'p308', 'p351'):
        R = runs(n); f, nl = fold(R, Q, codes, letters, P)
        toks = [t for v in R.values() for t in v]
        f.update({'letters': nl, 'coverage': round(sum(1 for t in toks if t <= 66) / len(toks), 4),
                  'supports': f['decode'] > f['ctrl_max']})
        out['fold_' + n] = f
    if g['PASS'] and '--no-435' not in sys.argv:
        R = runs('p435'); f, nl = fold(R, Q, codes, letters, P)
        toks = [t for v in R.values() for t in v]
        f.update({'letters': nl, 'coverage': round(sum(1 for t in toks if t <= 66) / len(toks), 4),
                  'beats_max': f['decode'] > f['ctrl_max']})
        out['p435'] = f
        # matched control: p.108's first quoted passage, 128 letters, random homophones, 8 codes at p.435's relative positions
        t108 = html_text(os.path.join(H, 'edition', 'VAN_DEWITT_01_108.html'))
        src = norm(t108[t108.index('"') + 1:])[:128]
        rng = random.Random(SEED + 1); inv = {}
        for c, l in zip(codes, letters): inv.setdefault(l, []).append(c)
        ct = [rng.choice(inv[ch]) for ch in src]
        flat = [t for v in R.values() for t in v]; codepos = [i for i, t in enumerate(flat) if t > 66]
        syn = ct[:]
        for i in codepos: syn.insert(min(i, len(syn)), flat[i])
        Rs = {('syn', 1): syn}
        fs, nls = fold(Rs, Q, codes, letters, P)
        fs.update({'letters': nls, 'tokens': len(syn), 'codes': len(codepos), 'separates': fs['decode'] > fs['ctrl_max'],
                   'source_first20': src[:20]})
        out['matched_control_p108'] = fs
    js = json.dumps(out, indent=1, sort_keys=True) + '\n'
    p = os.path.join(H, 'gate_dutchkey.json')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == js
        print('OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(js); print(js)

if __name__ == '__main__':
    main()
