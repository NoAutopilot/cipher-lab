#!/usr/bin/env python3
"""DEB-SWARM-G front end (29 Sept 2026): Portuguese / Spanish / Latin homophonic letter substitution.

  python3 gg.py model LANG            build models/LANG.bin (conditional interpolated quadgram, 26 letters, a-z)
  python3 gg.py real TEXT             print N, K of c1 / c2 as loaded (X and punctuation dropped by default)
  python3 gg.py control LANG --n N --k K [--noise F] [--zipf] [--seeds S] [--restarts R] [--iters I] [--klw W]
                                      hand-planted control: a LANG window of N letters from the held-out file,
                                      enciphered homophonically with K signs (variants allotted by frequency,
                                      Zipf-weighted choice when --zipf), F share of tokens replaced by a random
                                      sign (transcription noise); solved blind; prints recovery pct per seed.
  python3 gg.py solve LANG TEXT [--restarts R] [--iters I] [--klw W] [--out key.tsv]
                                      anneal on c1 or c2 (or c12) and write the key TSV (sign, value).
Plaintext of a control is never written to disk; only recovery numbers are.
The annealer core is hsa.c (built to $HSA or /tmp/claude-0/hsa).
"""
import argparse, collections, csv, gzip, json, math, os, random, re, struct, subprocess, sys, tempfile, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..'))
HSA = os.environ.get('HSA', '/tmp/claude-0/hsa')
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
A = 'abcdefghijklmnopqrstuvwxyz'
# training files and the held-out file each control draws from (never the same file)
LANGS = {
    'pt': dict(train=['corpus/pg70664.txt.gz', 'corpus/pg68986.txt.gz', 'corpus/pg71330.txt.gz'],
               held=['corpus/pg68905.txt.gz']),
    'ptv': dict(train=['corpus/pg70664.txt.gz', 'corpus/pg68905.txt.gz', 'corpus/pg68986.txt.gz'],
                held=['corpus/pg71330.txt.gz']),   # held-out = Garrett's verse (Debosnys's texts are verse)
    'es': dict(train=['corpus/pg69089.txt.gz'], held=['corpus/pg66979.txt.gz']),
    # *all: every file of the language, for scoring the real texts (no held-out file needed there)
    'ptall': dict(train=['corpus/pg70664.txt.gz', 'corpus/pg68905.txt.gz', 'corpus/pg68986.txt.gz', 'corpus/pg71330.txt.gz'], held=[]),
    'esall': dict(train=['corpus/pg69089.txt.gz', 'corpus/pg66979.txt.gz'], held=[]),
    'la': dict(train=[os.path.join(REPO, 'tools/data/la18/zaluski_epistolae_t1.txt.gz'),
                      os.path.join(REPO, 'tools/data/la18/zaluski_epistolae_t2.txt.gz')],
               held=[os.path.join(REPO, 'tools/data/la18/zaluski_epistolae_t3.txt.gz')]),
}
LANGS['laall'] = dict(train=LANGS['la']['train'] + LANGS['la']['held'], held=[])

def read(p):
    p = p if os.path.isabs(p) else os.path.join(HERE, p)
    t = gzip.open(p, 'rt', encoding='utf-8', errors='replace').read()
    m = re.search(r'\*\*\* START OF.*?\*\*\*', t); e = re.search(r'\*\*\* END OF', t)
    if m: t = t[m.end():e.start() if e else None]
    return t

def fold(t):
    t = unicodedata.normalize('NFKD', t.lower())
    t = ''.join(ch for ch in t if not unicodedata.combining(ch))
    return re.sub(r'[^a-z]', '', t)

def build_model(lang, floor=None):
    s = ''.join(fold(read(p)) for p in LANGS[lang]['train'])
    idx = [A.index(ch) for ch in s]
    c1 = [0] * 26; c2 = [0] * 676; c3 = [0] * 17576; c4 = [0] * 456976
    for i, x in enumerate(idx):
        c1[x] += 1
        if i >= 1: c2[idx[i-1]*26+x] += 1
        if i >= 2: c3[(idx[i-2]*26+idx[i-1])*26+x] += 1
        if i >= 3: c4[((idx[i-3]*26+idx[i-2])*26+idx[i-1])*26+x] += 1
    n = len(idx); B = 2.0
    p1 = [(c + 0.5) / (n + 13) for c in c1]
    h1 = [sum(c2[a*26:(a+1)*26]) for a in range(26)]
    p2 = [(c2[a*26+b] + B*p1[b]) / (h1[a] + B) for a in range(26) for b in range(26)]
    h2 = [sum(c3[ab*26:(ab+1)*26]) for ab in range(676)]
    p3 = [(c3[ab*26+x] + B*p2[(ab % 26)*26+x]) / (h2[ab] + B) for ab in range(676) for x in range(26)]
    h3 = [sum(c4[abc*26:(abc+1)*26]) for abc in range(17576)]
    out = []
    for abc in range(17576):
        base = (abc % 676) * 26; hh = h3[abc] + B
        for x in range(26):
            v = math.log((c4[abc*26+x] + B*p3[base+x]) / hh); out.append(max(v, floor) if floor is not None else v)
    os.makedirs(os.path.join(HERE, 'models'), exist_ok=True)
    name = lang + ('_f%g' % -floor if floor is not None else '')
    with open(os.path.join(HERE, 'models', name + '.bin'), 'wb') as f:
        f.write(struct.pack('26f', *[math.log(p) for p in p1])); f.write(struct.pack('%df' % len(out), *out))
    print(lang, 'train letters', n, 'files', LANGS[lang]['train'])

def model_path(lang):
    p = os.path.join(HERE, 'models', lang + '.bin')
    if not os.path.exists(p):
        base, _, fl = lang.partition('_f'); build_model(base, -float(fl) if fl else None)
    return p

def ctl_tokens(text):
    # harness control ciphertext: swarm/controls/<ID>.tsv, parts <ID>.c1 / <ID>.c2 / <ID> (pooled); X is not special here
    cid, _, part = text.partition('.')
    rows = list(csv.DictReader(open(os.path.join(HERE, '..', 'controls', cid + '.tsv')), delimiter='\t'))
    return [r['sign'] for r in rows if not part or r['line'].startswith(part + '_')]

def scorer_tokens(text):
    # the frozen scorer's own loader (read-only import): the exact token stream score.py scores, X kept
    import importlib.util
    spec = importlib.util.spec_from_file_location('deb_score', os.path.join(HERE, '..', 'score.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.flat(m.load_text(text))

def real_tokens(text, keep_x=False):
    if text.startswith('S:'):
        toks = scorer_tokens(text[2:])
        return toks if keep_x else [t for t in toks if t != 'X']
    if text not in ('c1', 'c2', 'c12'): return ctl_tokens(text)
    sys.path.insert(0, os.path.join(ROOT, 'scripts')); from settled_lines import settled_lines
    pres = {'c1': ['c1'], 'c2': ['c2'], 'c12': ['c1', 'c2']}[text]
    toks = []
    for pre in pres:
        for v in settled_lines(ROOT, pre, drop_clear=True).values():
            toks += [s for s in v if s not in PUNCT and (keep_x or s != 'X')]
    return toks

def anneal(lang, seq, K, restarts, iters, seed, klw, fixed=None):
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f:
        f.write('%d %d\n' % (len(seq), K) + ' '.join(map(str, seq)) + '\n'); cp = f.name
    args = [HSA, model_path(lang), cp, str(restarts), str(iters), str(seed), str(klw)]
    if fixed:
        with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as g:
            for s, l in fixed.items(): g.write('%d %s\n' % (s, l))
        args.append(g.name)
    o = subprocess.run(args, capture_output=True, text=True, check=True).stdout.split('\n')
    os.unlink(cp)
    bi = [i for i, l in enumerate(o) if l.startswith('BEST')][0]
    return float(o[bi].split()[1]), o[bi+1].strip()

def make_control(lang, n, k, noise, zipf, rng):
    s = fold(''.join(read(p) for p in LANGS[lang]['held']))
    st = rng.randrange(len(s) - n - 1); pt = s[st:st+n]
    freq = collections.Counter(pt); letters = [l for l, _ in freq.most_common()]
    # homophones: one per letter present, the rest allotted by largest remaining freq/variants
    nv = {l: 1 for l in letters}
    for _ in range(max(0, k - len(letters))):
        l = max(letters, key=lambda x: freq[x] / nv[x]); nv[l] += 1
    signs = {}; sid = 0
    for l in letters:
        signs[l] = list(range(sid, sid + nv[l])); sid += nv[l]
    ct = []
    for ch in pt:
        vs = signs[ch]
        w = [1.0 / (i + 1) for i in range(len(vs))] if zipf else [1.0] * len(vs)
        ct.append(rng.choices(vs, w)[0])
    for i in range(len(ct)):
        if rng.random() < noise: ct[i] = rng.randrange(sid)
    return pt, ct, sid

def curve_control(lang, noise, rng):
    # the real pooled sign-count curve (scorer tokens c1+c2, X kept: N 790, K 136) put on a LANG plaintext window:
    # signs, largest count first, go to the letter with the largest remaining deficit; each occurrence then draws a
    # homophone in proportion to its remaining quota, so every sign ends at its real count; then noise replaces a share
    # of tokens by a sign drawn from the curve (the harness's -N15 style). Parts: first 132 = c1 shape, rest = c2 shape.
    real = scorer_tokens('c1') + scorer_tokens('c2')
    cnt = sorted(collections.Counter(real).values(), reverse=True); n = len(real)
    s = fold(''.join(read(p) for p in LANGS[lang]['held']))
    st = rng.randrange(len(s) - n - 1); pt = s[st:st+n]
    need = collections.Counter(pt); owner = []; quota = collections.defaultdict(list)
    for sid, c in enumerate(cnt):
        l = max(need, key=lambda x: need[x]) if any(v > 0 for v in need.values()) else rng.choice(list(need))
        owner.append(l); quota[l].append([sid, c]); need[l] -= c
    ct = []
    for ch in pt:
        q = quota.get(ch)
        if not q: ct.append(rng.randrange(len(cnt))); continue
        w = [max(x[1], 0) + 1e-9 for x in q]; i = rng.choices(range(len(q)), w)[0]; q[i][1] -= 1; ct.append(q[i][0])
    pool = [sid for sid, c in enumerate(cnt) for _ in range(c)]
    for i in range(len(ct)):
        if rng.random() < noise: ct[i] = rng.choice(pool)
    return pt, ct

def cmd_hcontrol(a):
    res = []
    for seed in range(a.seeds):
        rng = random.Random(5000 + seed)
        pt, ct = curve_control(a.lang, a.noise, rng)
        fit, test = (ct[132:], ct[:132]) if a.dir == 'c2c1' else (ct[:132], ct[132:])
        ptt = pt[:132] if a.dir == 'c2c1' else pt[132:]
        used = sorted(set(fit)); ix = {s: i for i, s in enumerate(used)}
        sc, key = anneal(a.model, [ix[t] for t in fit], len(used), a.restarts, a.iters, seed + 1, a.klw)
        ok = sum(1 for t, p in zip(test, ptt) if t in ix and key[ix[t]] == p)
        res.append(ok / len(test)); print('seed', seed, 'recovery_test %.3f' % res[-1], flush=True)
    print(json.dumps(dict(cmd='hcontrol', lang=a.lang, model=a.model, noise=a.noise, dir=a.dir, restarts=a.restarts, iters=a.iters,
                          perturb=os.environ.get('HSA_PERTURB'), recovery_test=[round(r, 3) for r in res], mean=round(sum(res) / len(res), 3))))

def cmd_control(a):
    res = []
    for seed in range(a.seeds):
        rng = random.Random(1000 + seed)
        pt, ct, K = make_control(a.lang, a.n, a.k, a.noise, a.zipf, rng)
        used = sorted(set(ct)); remap = {s: i for i, s in enumerate(used)}
        seq = [remap[s] for s in ct]
        sc, key = anneal(a.model or a.lang, seq, len(used), a.restarts, a.iters, seed + 1, a.klw)
        dec = ''.join(key[x] for x in seq)
        rec = sum(1 for x, y in zip(dec, pt) if x == y) / len(pt)
        res.append(rec); print('seed', seed, 'N', len(pt), 'K', len(used), 'recovery %.3f' % rec, 'score %.1f' % sc, flush=True)
    print(json.dumps(dict(lang=a.lang, model=a.model or a.lang, n=a.n, k=a.k, noise=a.noise, zipf=a.zipf, restarts=a.restarts,
                          iters=a.iters, klw=a.klw, recovery=[round(r, 3) for r in res], mean=round(sum(res) / len(res), 3))))

def cmd_solve(a):
    toks = real_tokens(a.text, a.keep_x)
    signs = sorted(set(toks)); ix = {s: i for i, s in enumerate(signs)}
    sc, key = anneal(a.lang, [ix[t] for t in toks], len(signs), a.restarts, a.iters, a.seed, a.klw)
    print('score %.2f per-char %.3f N %d K %d' % (sc, sc / len(toks), len(toks), len(signs)))
    if a.out:
        with open(a.out, 'w') as f:
            f.write('sign\tvalue\n')
            for s in signs: f.write('%s\t%s\n' % (s, key[ix[s]]))
            if not a.keep_x: f.write('X\t\n')
    if a.show: print(''.join(key[ix[t]] for t in toks))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest='cmd', required=True)
    m = sp.add_parser('model'); m.add_argument('lang'); m.add_argument('--floor', type=float)
    r = sp.add_parser('real'); r.add_argument('text'); r.add_argument('--keep-x', action='store_true')
    c = sp.add_parser('control'); c.add_argument('lang'); c.add_argument('--model')
    for p in (c,):
        p.add_argument('--n', type=int, required=True); p.add_argument('--k', type=int, required=True)
        p.add_argument('--noise', type=float, default=0.0); p.add_argument('--zipf', action='store_true')
        p.add_argument('--seeds', type=int, default=3)
    h = sp.add_parser('hcontrol'); h.add_argument('lang'); h.add_argument('--model', required=True)
    h.add_argument('--noise', type=float, default=0.15); h.add_argument('--seeds', type=int, default=4); h.add_argument('--dir', default='c2c1')
    s = sp.add_parser('solve'); s.add_argument('lang'); s.add_argument('text'); s.add_argument('--keep-x', action='store_true')
    s.add_argument('--out'); s.add_argument('--show', action='store_true'); s.add_argument('--seed', type=int, default=1)
    for p in (c, s, h):
        p.add_argument('--restarts', type=int, default=8); p.add_argument('--iters', type=int, default=300000)
        p.add_argument('--klw', type=float, default=1.0)
    a = ap.parse_args()
    if a.cmd == 'model': build_model(a.lang, a.floor)
    elif a.cmd == 'real':
        t = real_tokens(a.text, a.keep_x); print(a.text, 'N', len(t), 'K', len(set(t)))
    elif a.cmd == 'control': cmd_control(a)
    elif a.cmd == 'hcontrol': cmd_hcontrol(a)
    else: cmd_solve(a)
