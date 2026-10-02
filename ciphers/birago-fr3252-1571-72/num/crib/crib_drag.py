"""Pre-registered crib drag over the pooled f.119 + f.100r pair stream (BIRAGO-NUM2, 2 Oct 2026; rules in PREREG.md).

python3 crib_drag.py target   [--perms 200]   -> crib_target.tsv
python3 crib_drag.py control  [--trials 5] [--ncell 40] [--copies 1]   -> power on synthetic it16dip text
A placement = the crib laid on consecutive pair tokens of one run; admissible if no code stands for two letters.
Score = sum of bigram PMI over adjacent token pairs elsewhere in both letters whose two codes the placement fixes.
Null = the same max over placements with pair tokens permuted across positions (run structure kept)."""
import sys, math, random, glob, gzip, re, argparse
import numpy as np
sys.path.insert(0, '..')
HERE = __file__.rsplit('/', 1)[0] or '.'
CRIBS = ['carmagnola', 'bellagarda', 'bellegarda', 'ualletta', 'sauoia', 'turino', 'duca', 'regina', 'ugonotti',
         'centurione', 'maresciale', 'maesta']
AL = 'abcdefghilmnopqrstuz'


def clean(t):
    t = t.lower()
    for a, b in (('j', 'i'), ('k', 'c'), ('w', 'u'), ('y', 'i'), ('x', 's'), ('v', 'u')):
        t = t.replace(a, b)
    return re.sub('[^' + AL + ']', '', t)


_C = None
def corpus():
    global _C
    if _C is None:
        _C = clean(''.join(gzip.open(f, 'rt', errors='ignore').read()
                           for f in sorted(glob.glob(HERE + '/../../../../tools/data/it16dip/*.txt.gz'))))
    return _C


def pmi_matrix():
    c = corpus(); ix = {a: i for i, a in enumerate(AL)}; n = len(AL)
    big = np.full((n, n), 0.5); uni = np.full(n, 0.5)
    a = np.frombuffer(c.encode(), dtype=np.uint8)
    lut = np.full(256, -1); [lut.__setitem__(ord(ch), i) for ch, i in ix.items()]
    v = lut[a]
    np.add.at(big, (v[:-1], v[1:]), 1); np.add.at(uni, v, 1)
    pb = big / big.sum(1, keepdims=True); pu = uni / uni.sum()
    return np.log(pb) - np.log(pu)[None, :], ix


def read_runs(path):
    runs = []
    for line in open(path):
        t = line.split()
        if t == ['76'] or not t: continue
        cur = []
        for x in t:
            if len(x) == 2: cur.append(x)
            else:
                if cur: runs.append(cur)
                cur = []
        if cur: runs.append(cur)
    return runs


def adjacency(runs, codes):
    A = np.zeros((len(codes), len(codes)))
    for r in runs:
        for a, b in zip(r, r[1:]): A[codes[a], codes[b]] += 1
    return A


def drag(runs, crib, codes, A, P, lix):
    """Return list of (score, run, pos, mapping) over admissible placements."""
    L = len(crib); out = []
    li = [lix[ch] for ch in crib]
    for ri, r in enumerate(runs):
        for p in range(len(r) - L + 1):
            seg = r[p:p + L]; m = {}
            ok = True
            for c, ch in zip(seg, crib):
                if m.setdefault(c, ch) != ch: ok = False; break
            if not ok: continue
            cs = list(m); ci = np.array([codes[c] for c in cs]); lv = np.array([lix[m[c]] for c in cs])
            sub = A[np.ix_(ci, ci)].copy()
            for a, b in zip(seg, seg[1:]):              # exclude the crib's own adjacencies
                sub[cs.index(a), cs.index(b)] -= 1
            s = float((sub * P[np.ix_(lv, lv)]).sum())
            out.append((s, ri, p, m))
    return out


def permute(runs, rng):
    flat = [x for r in runs for x in r]; rng.shuffle(flat); out, k = [], 0
    for r in runs: out.append(flat[k:k + len(r)]); k += len(r)
    return out


def test_crib(runs, crib, P, lix, perms, rng, full=False):
    codes = {c: i for i, c in enumerate(sorted({x for r in runs for x in r}))}
    pl = drag(runs, crib, codes, adjacency(runs, codes), P, lix)
    if not pl: return (None, [], 0, []) if full else (None, [], 0)
    best = max(pl, key=lambda t: t[0])
    null = []
    for _ in range(perms):
        pr = permute(runs, rng); q = drag(pr, crib, codes, adjacency(pr, codes), P, lix)
        null.append(max(t[0] for t in q) if q else -1e9)
    return (best, null, len(pl), pl) if full else (best, null, len(pl))


def target(args):
    P, lix = pmi_matrix(); runs = read_runs(HERE + '/../pooled_tokens.txt'); rng = random.Random(20261002)
    print('runs', len(runs), 'pairs', sum(map(len, runs)))
    rows = ['crib\tadmissible\treal_max\tnull_mean\tnull_p95\tnull_max\tp\taccept\trun\tpos\tmapping']
    for crib in CRIBS:
        best, null, n = test_crib(runs, crib, P, lix, args.perms, rng)
        if best is None:
            rows.append(f'{crib}\t0\t\t\t\t\t\tno\t\t\t'); print(crib, 'no admissible placement'); continue
        ge = sum(x >= best[0] for x in null); p = (ge + 1) / (len(null) + 1); ns = sorted(null)
        acc = 'yes' if ge == 0 else 'no'
        mp = ' '.join(f'{c}={l}' for c, l in sorted(best[3].items()))
        rows.append(f'{crib}\t{n}\t{best[0]:.2f}\t{np.mean(null):.2f}\t{ns[int(.95 * len(ns))]:.2f}\t{ns[-1]:.2f}\t{p:.3f}\t{acc}\t{best[1]}\t{best[2]}\t{mp}')
        print(rows[-1])
    open(HERE + '/crib_target.tsv', 'w').write('\n'.join(rows) + '\n')


def synth_runs(rng, ncell, crib, copies, npairs=476, stray=0.05):
    import phase, analyze
    c = corpus(); n = npairs - copies * len(crib)
    s = rng.randrange(0, len(c) - n); txt = c[s:s + n]
    pos = sorted(rng.sample(range(20, n - 20), copies))
    for k, p in enumerate(reversed(pos)): txt = txt[:p] + crib + txt[p:]
    starts = [p + i * len(crib) for i, p in enumerate(pos)]
    letters = sorted(set(txt)); fr = {l: txt.count(l) for l in letters}; cells = analyze.CELLS[:]; rng.shuffle(cells)
    key = {l: [cells.pop()] for l in letters}; extra = ncell - len(letters)
    while extra > 0:
        l = max(letters, key=lambda l: fr[l] / len(key[l])); key[l].append(cells.pop()); extra -= 1
    toks, idx = [], []                    # idx: plaintext index of each pair token
    for i, ch in enumerate(txt):
        if rng.random() < stray: toks.append(rng.choice('0123456789')); idx.append(None)
        toks.append(rng.choice(key[ch])); idx.append(i)
    runs, cur = [], ''
    digit_src = []                        # plaintext index per digit position (first digit of a pair)
    for t, i in zip(toks, idx):
        for k in range(len(t)): digit_src.append(i if (len(t) == 2 and k == 0) else None)
    for t in toks:
        cur += t
        if len(cur) > 40 and rng.random() < 0.15: runs.append(cur); cur = ''
    if cur: runs.append(cur)
    got = None; bh = 9e9
    for sd in range(5):
        g = phase.em(runs, seed=sd); h = phase.summary(g)['H']
        if h < bh: bh, got = h, g
    # true crib placements in recovered token coordinates: crib start digit -> (run, token index) if phase right
    truth = set(); off = 0
    starts_digit = {}
    for d, i in enumerate(digit_src):
        if i is not None: starts_digit[i] = d
    want = {starts_digit[s0] for s0 in starts if s0 in starts_digit}
    pr = []; ri = 0
    for r, toksr in zip(runs, got):
        d = off; cur = []
        for t in toksr:
            if len(t) == 2:
                if d in want: truth.add((len(pr), len(cur)))
                cur.append(t)
            else:
                if cur: pr.append(cur)
                cur = []
            d += len(t)
        if cur: pr.append(cur)
        off += len(r)
    return pr, truth


def control(args):
    sys.path.insert(0, HERE + '/..')
    P, lix = pmi_matrix(); rng = random.Random(args.seed)
    for crib in args.cribs.split(','):
        acc = 0; found = 0; phased = 0; wrong = 0
        for t in range(args.trials):
            runs, truth = synth_runs(rng, args.ncell, crib, args.copies)
            best, null, n, pl = test_crib(runs, crib, P, lix, args.perms, rng, full=True)
            truth = {k for k in truth if any((x[1], x[2]) == k for x in pl)}   # whole crib intact in recovered phase
            phased += bool(truth)
            hit = best is not None and (best[1], best[2]) in truth
            found += hit
            acc += hit and all(x < best[0] for x in null)
            wrong += best is not None and not hit and all(x < best[0] for x in null)
        print(f'control ncell={args.ncell} copies={args.copies} crib={crib} L={len(crib)}: crib intact after phasing '
              f'{phased}/{args.trials}, top-scoring {found}/{args.trials}, accepted {acc}/{args.trials}, wrong placement accepted {wrong}/{args.trials}', flush=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('mode'); ap.add_argument('--perms', type=int, default=200)
    ap.add_argument('--trials', type=int, default=5); ap.add_argument('--ncell', type=int, default=40)
    ap.add_argument('--copies', type=int, default=1); ap.add_argument('--seed', type=int, default=7)
    ap.add_argument('--cribs', default='carmagnola,ualletta,turino,duca')
    a = ap.parse_args(); target(a) if a.mode == 'target' else control(a)
