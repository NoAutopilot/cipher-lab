#!/usr/bin/env python3
"""DEB-SWARM-B driver: English plaintext, homophonic letter substitution (29 Sept 2026).

  python3 gb.py model                       build model_en.bin (quadgram log10 P + unigram) from the LM corpus
  python3 gb.py control --text c2 [--xnull] [--noise 0.15] [--seed 1] [--restarts 40] [--iters 3000000] [--beta B]
        hand-planted control (score.py not frozen yet): an English window of the target's own non-gap length,
        gaps at the target's own positions, signs allotted to letters so the sign-count multiset follows the
        target's (greedy), each occurrence drawing a homophone in proportion to remaining quota. --xnull makes
        the target's X a null inserted at X's own positions instead of a letter. --noise replaces that share of
        tokens with a random other sign (transcription noise, 14-18 pct measured on c1/c2).
        Prints recovery (share of plaintext letters read right) -- the answer never leaves this process.
  python3 gb.py target --text c2 [--xnull] ...   solve the real text; writes key_<text>_<tag>.tsv (sign<TAB>value)

LM corpus (public domain, tools/data): Moby-Dick 1851, Huckleberry Finn 1884, Pride and Prejudice 1813, Gatsby 1925
(held out of the control plaintext); control plaintext: Holmes 1892 (tools/data/pg1661_holmes.txt), never in the LM.
"""
import argparse, os, random, re, struct, subprocess, sys, json, math
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DEB = os.path.abspath(os.path.join(HERE, '..', '..'))
ROOT = os.path.abspath(os.path.join(DEB, '..', '..'))
sys.path.insert(0, os.path.join(DEB, 'scripts'))
from settled_lines import settled_lines  # noqa

LM_FILES = ['tools/data/pg2701_mobydick.txt', 'tools/data/en/pg76_huckfinn.txt', 'tools/data/en/pg1342_pride.txt',
            'tools/data/en/pg64317_gatsby.txt'] + sorted(
    'ciphers/debosnys-1883/swarm/G-B/corpus/' + f for f in (os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'corpus'))
    if os.path.isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'corpus')) else []) if f.endswith('.txt'))
CTRL_FILE = 'tools/data/pg1661_holmes.txt'
CTRL_FOLD = False
REVERSE = False  # read every line right to left
DROP_PICT = False  # H31 pictogram class (PICT-*, SUN, STAR, HEART, RAM) read as gaps (capitals/determinatives)
GAP = {'_', 'MULTI'}
ROBUST = 0.0
MODELS = {4: 'model_en.bin', 5: 'model5_en.bin', 's': 'model5s_en.bin'}
SPACE = False
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H'}


def body(path):
    p = os.path.join(ROOT, path)
    if p.endswith('.gz'):
        import gzip; t = gzip.open(p, 'rt', encoding='utf-8', errors='ignore').read()
    else: t = open(p, encoding='utf-8', errors='ignore').read()
    if CTRL_FOLD:
        import unicodedata; t = ''.join(c for c in unicodedata.normalize('NFKD', t) if not unicodedata.combining(c))
    a = t.find('*** START'); b = t.find('*** END')
    if a >= 0: t = t[t.find('\n', a) + 1:]
    if b >= 0: t = t[:t.find('*** END')]
    return t


def letters(t):
    return re.sub(r'[^a-z]', '', t.lower())


def build_model(out):
    s = ''.join(letters(body(p)) for p in LM_FILES)
    q = Counter(s[i:i + 4] for i in range(len(s) - 3)); u = Counter(s)
    tot = sum(q.values()); floor = math.log10(0.01 / tot)
    arr = [floor] * 456976
    for g, c in q.items():
        a, b, cc, d = (ord(x) - 97 for x in g); arr[((a * 26 + b) * 26 + cc) * 26 + d] = math.log10(c / tot)
    ut = sum(u.values())
    with open(out, 'wb') as f:
        f.write(struct.pack('456976f', *arr)); f.write(struct.pack('26f', *[(u[chr(97 + i)] + 1) / (ut + 26) for i in range(26)]))
    print('model', out, 'chars', len(s), 'quadgram types', len(q))


def target_stream(text, xnull=False, keep_punct=False):
    if '+' in text:  # pooled texts, e.g. c2+c3+c4, joined by a 5-gap break
        out = []
        for t in text.split('+'): out += target_stream(t, xnull, keep_punct) + [None] * 5
        return out
    """tokens of the settled draft for c1/c2 (clear spans dropped); gaps as None; lines concatenated."""
    L = settled_lines(DEB, text, drop_clear=True)
    out = []
    for toks in L.values():
        if REVERSE: toks = toks[::-1]
        for s in toks:
            if DROP_PICT and (s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')):
                out.append(None); continue
            if s in GAP: out.append(None)
            elif s in PUNCT and not keep_punct: continue
            elif xnull and s == 'X': continue
            else: out.append(s)
    return out


def encode(stream):
    signs = sorted({s for s in stream if s is not None})
    idx = {s: i for i, s in enumerate(signs)}
    return signs, [idx[s] if s is not None else -1 for s in stream]


def run_solver(seq, K, restarts, iters, seed, beta, t0=1.5, fix=None, model='model_en.bin'):
    cf = os.path.join(HERE, f'_cipher_{os.getpid()}_{seed}.txt')
    with open(cf, 'w') as f: f.write(f'{K} {len(seq)}\n' + ' '.join(map(str, seq)) + '\n')
    args = [os.path.join(HERE, 'hsolve5s' if '5s' in model else 'hsolve5b' if '5' in model else 'hsolve'), os.path.join(HERE, model), cf, str(restarts), str(iters), str(seed), str(beta), str(t0)]
    if fix:
        ff = cf + '.fix'
        with open(ff, 'w') as f: f.write(''.join(f'{s} {l}\n' for s, l in fix.items()))
        args.append(ff)
    o = subprocess.run(args, capture_output=True, text=True, env=dict(os.environ, HS_ROBUST=str(ROBUST))).stdout
    os.remove(cf)
    if fix: os.remove(cf + '.fix')
    lines = o.strip().split('\n')
    best = float([l for l in lines if l.startswith('BEST')][0].split()[1])
    key = list(map(int, [l for l in lines if l.startswith('KEY')][0].split()[1:]))
    rs = [float(l.split()[2]) for l in lines if l.startswith('R ')]
    return best, key, rs


def make_control(stream, seed, noise=0.0, xnull=False):
    rng = random.Random(seed)
    txt = letters(body(CTRL_FILE)) if not SPACE else re.sub(r'[^a-z]+', ' ', body(CTRL_FILE).lower()).replace(' ', '{')
    nongap = [s for s in stream if s is not None and not (xnull and s == 'X')]
    n = len(nongap)
    st = rng.randrange(0, len(txt) - n - 1); plain = txt[st:st + n]
    prof = Counter(nongap)
    need = Counter(plain)
    # greedy: largest sign count to the letter with the largest remaining need
    alloc = {}; rem = dict(need)
    if SPACE:
        alloc['X'] = '{'; rem.pop('{', None)
    for s, c in sorted(prof.items(), key=lambda x: -x[1]):
        if s in alloc: continue
        l = max(rem, key=lambda k: rem[k]); alloc[s] = l; rem[l] -= c
    for l in need:  # any letter left without a sign gets the smallest unused... reuse: give it a fresh sign
        if not any(v == l for v in alloc.values()):
            alloc[f'EXTRA-{l}'] = l; prof[f'EXTRA-{l}'] = 1
    by = {}
    for s, l in alloc.items(): by.setdefault(l, []).append(s)
    quota = dict(prof)
    signs = []
    for ch in plain:
        cand = by[ch]; w = [max(quota[s], 0) + 0.01 for s in cand]
        s = rng.choices(cand, w)[0]; quota[s] -= 1; signs.append(s)
    allsigns = sorted(prof)
    if noise:
        for i in range(len(signs)):
            if rng.random() < noise: signs[i] = rng.choice(allsigns)
    # rebuild with gaps (and X nulls) at the target's own positions
    out, truth, k = [], [], 0
    for s in stream:
        if s is None: out.append(None); truth.append(None)
        elif xnull and s == 'X': out.append('NULLX'); truth.append('#')
        else: out.append(signs[k]); truth.append(plain[k]); k += 1
    return out, truth


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode'); ap.add_argument('--text', default='c2'); ap.add_argument('--test'); ap.add_argument('--xnull', action='store_true')
    ap.add_argument('--solve-xnull', action='store_true', help='drop X before solving (on a control made with --xnull)')
    ap.add_argument('--noise', type=float, default=0.0); ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--restarts', type=int, default=40); ap.add_argument('--iters', type=int, default=3000000)
    ap.add_argument('--beta', type=float, default=1.0); ap.add_argument('--t0', type=float, default=1.5)
    ap.add_argument('--tag', default=''); ap.add_argument('--order', default=5, type=lambda v: v if v == 's' else int(v)); ap.add_argument('--show', action='store_true')
    ap.add_argument('--robust', type=float, default=0.0); ap.add_argument('--xspace', action='store_true'); ap.add_argument('--reverse', action='store_true'); ap.add_argument('--drop-pict', action='store_true'); ap.add_argument('--ctrl-file', help='control plaintext (repo-relative), e.g. a French text for the wrong-language control')
    a = ap.parse_args()
    global ROBUST, SPACE, CTRL_FILE, CTRL_FOLD, REVERSE, DROP_PICT; ROBUST = a.robust; SPACE = a.xspace; REVERSE = a.reverse; DROP_PICT = a.drop_pict
    if a.ctrl_file: CTRL_FILE = a.ctrl_file; CTRL_FOLD = True
    if a.xspace: a.order = 's'
    if a.mode == 'model': return build_model(os.path.join(HERE, 'model_en.bin'))
    stream = target_stream(a.text)
    if a.mode == 'control':
        cs, truth = make_control(stream, a.seed, a.noise, a.xnull)
        if a.solve_xnull:
            keep = [i for i, s in enumerate(cs) if s != 'NULLX']; cs = [cs[i] for i in keep]; truth = [truth[i] for i in keep]
        signs, seq = encode(cs)
        best, key, rs = run_solver(seq, len(signs), a.restarts, a.iters, a.seed, a.beta, a.t0, model=MODELS[a.order], fix=({signs.index('X'): 26} if SPACE and 'X' in signs else None))
        ok = tot = sp = 0
        for c, t in zip(seq, truth):
            if c < 0 or t is None or t == '#': continue
            tot += 1; ok += chr(97 + key[c]) == t; sp += t == '{'
        rs.sort(reverse=True)
        print(json.dumps({'control': a.text, 'seed': a.seed, 'noise': a.noise, 'xnull': a.xnull, 'N': tot, 'K': len(signs),
                          'recovery': round(ok / tot, 4), 'recovery_letters': round((ok - sp) / max(1, tot - sp), 4) if SPACE else None, 'best': best, 'per_window5': round(best / max(1, sum(1 for i in range(len(seq) - 4) if min(seq[i:i + 5]) >= 0)), 4), 'top_restarts': rs[:5]}))
        if a.show:
            print(''.join(chr(97 + key[c]) if c >= 0 else '_' for c in seq)[:300])
    elif a.mode == 'control2':
        # held-out stepping stone: one planted key over c2 then c1 (joint shape), fit on --text's part only,
        # applied to the other part; reports recovery on both parts and writes both parts as cipher-only files
        fit, test = a.text, (a.test or ('c1' if a.text == 'c2' else 'c2'))
        s1, s2 = target_stream(fit), target_stream(test)
        cs, truth = make_control(s1 + [None] * 5 + s2, a.seed, a.noise, a.xnull)
        cut = len(s1)
        parts = {fit: (cs[:cut], truth[:cut]), test: (cs[cut:], truth[cut:])}
        signs = sorted({s for s in parts[fit][0] if s is not None}); idx = {x: i for i, x in enumerate(signs)}
        seq = [idx[s] if s is not None else -1 for s in parts[fit][0]]
        best, key, rs = run_solver(seq, len(signs), a.restarts, a.iters, a.seed, a.beta, a.t0, model=MODELS[a.order], fix=({signs.index('X'): 26} if SPACE and 'X' in signs else None))
        kmap = {x: chr(97 + key[i]) for x, i in idx.items()}
        nwin = sum(1 for i in range(len(seq) - 4) if min(seq[i:i + 5]) >= 0)
        res = {'control2': True, 'ctrl_file': os.path.basename(CTRL_FILE), 'per_window5': round(best / nwin, 4), 'fit': fit, 'seed': a.seed, 'noise': a.noise, 'xnull': a.xnull, 'K_fit': len(signs)}
        for p in (fit, test):
            ok = tot = 0
            for c, t in zip(*parts[p]):
                if c is None or t is None or t == '#': continue
                tot += 1; ok += kmap.get(c) == t
            res['recovery_' + p] = round(ok / tot, 4)
        # write the test part as a pseudo-text and the key, for heldout.py --stream
        kf = os.path.join(HERE, f'_ctrl2_key_s{a.seed}.tsv')
        with open(kf, 'w') as f:
            f.write('sign\tvalue\n' + ''.join(f'{x}\t{v}\n' for x, v in kmap.items()))
        with open(os.path.join(HERE, f'_ctrl2_test_s{a.seed}.txt'), 'w') as f:
            f.write('\n'.join('_' if c is None else c for c in parts[test][0]))
        res['key'] = kf
        print(json.dumps(res))
    elif a.mode in ('target', 'shuffled'):
        if a.xnull: stream = [s for s in stream if s != 'X']
        if a.mode == 'shuffled': stream = shuffled_stream(stream, 1000 + a.seed); a.tag = (a.tag or ('xnull' if a.xnull else 'xletter')) + '_SHUF'
        signs, seq = encode(stream)
        best, key, rs = run_solver(seq, len(signs), a.restarts, a.iters, a.seed, a.beta, a.t0, model=MODELS[a.order], fix=({signs.index('X'): 26} if SPACE and 'X' in signs else None))
        rs.sort(reverse=True)
        tag = a.tag or ('xnull' if a.xnull else 'xletter')
        kf = os.path.join(HERE, f'key_{a.text}_{tag}_s{a.seed}.tsv')
        with open(kf, 'w') as f:
            f.write('sign\tvalue\n')
            for s, v in zip(signs, key): f.write(f'{s}\t{chr(97 + v)}\n')
        nwin = sum(1 for i in range(len(seq) - 4) if min(seq[i:i + 5]) >= 0)
        print(json.dumps({'mode': a.mode, 'target': a.text, 'per_window5': round(best / nwin, 4), 'noise_note': None, 'xnull': a.xnull, 'N': sum(1 for c in seq if c >= 0), 'K': len(signs),
                          'best': best, 'per_window': None, 'top_restarts': rs[:5], 'key': kf}))



def truth_score(seq, truth, beta, model='model_en.bin'):
    """score (same formula as hsolve) of the planted key -- control diagnostics only, prints no plaintext."""
    raw = open(os.path.join(HERE, model), 'rb').read()
    Q = struct.unpack('456976f', raw[:456976 * 4]); U = struct.unpack('26f', raw[456976 * 4:])
    lk = {}
    for c, t in zip(seq, truth):
        if c >= 0 and t and t != '#': lk.setdefault(c, Counter())[t] += 1
    key = {c: ord(v.most_common(1)[0][0]) - 97 for c, v in lk.items()}
    p = [key.get(c, 4) if c >= 0 else -1 for c in seq]
    s = sum(Q[((p[i] * 26 + p[i + 1]) * 26 + p[i + 2]) * 26 + p[i + 3]] for i in range(len(p) - 3) if min(p[i:i + 4]) >= 0)
    cnt = Counter(x for x in p if x >= 0); tot = sum(cnt.values())
    kl = sum(c / tot * math.log(c / tot / U[l]) for l, c in cnt.items()) * tot / math.log(10)
    return s - beta * kl


def shuffled_stream(stream, seed):
    """rule-3 control for a target solve: the same tokens with order permuted inside each run between gaps is too
    weak (runs are long); permute all non-gap tokens globally, gaps stay in place. Sign counts identical, sequence
    structure destroyed -- the solver's best score on this is what 'no language' reaches at this N and K."""
    rng = random.Random(seed)
    toks = [s for s in stream if s is not None]; rng.shuffle(toks); it = iter(toks)
    return [None if s is None else next(it) for s in stream]


if __name__ == '__main__':
    main()
