"""Decoy-null joint-consistency crib test over the pooled f.119 + f.100r pair stream (BIRAGO-NUM4, 3 Oct 2026; rules in PREREG.md).

python3 joint_crib.py control [--trials 20] [--ncell 40] [--seed 4001]  -> power on synthetic it16dip text, 3 cribs planted
python3 joint_crib.py target  [--decoys 200]                            -> target_out.txt
A placement = a crib laid on consecutive pair tokens of one run, admissible if no code stands for two letters.
Two placements (different cribs, or the same crib at two places) AGREE when they do not overlap in the stream, no code is
given two letters across them, and they give the same letter to >= K shared codes (K=2). Statistic J(set) = number of
agreeing placement pairs. Null = J of decoy sets: each crib replaced by a random it16dip word of the same length.
Reuses ../crib/crib_drag.py (corpus, read_runs) and ../phase.py (em)."""
import sys, random, re, glob, gzip, argparse
import numpy as np
HERE = __file__.rsplit('/', 1)[0] or '.'
sys.path.insert(0, HERE + '/..'); sys.path.insert(0, HERE + '/../crib')
import crib_drag as cd
import phase, analyze

CRIBS = ['carmagnola', 'bellagarda', 'ualletta', 'sauoia', 'turino', 'saluzzo', 'monsignore', 'maesta', 'neuers',
         'birago', 'ceppo', 'centurione', 'maresciale', 'ugonotti', 'regina']
AL = cd.AL; LIX = {a: i for i, a in enumerate(AL)}
K = 2
STAT = 'max'

_W = None
def words():
    global _W
    if _W is None:
        raw = ''.join(gzip.open(f, 'rt', errors='ignore').read() for f in sorted(glob.glob(HERE + '/../../../../tools/data/it16dip/*.txt.gz')))
        ws = [cd.clean(w) for w in re.split(r'[^A-Za-zÀ-ÿ]+', raw)]
        _W = {}
        for w in ws:
            if 4 <= len(w) <= 12: _W.setdefault(len(w), []).append(w)
    return _W

def decoy_set(cribs, rng):
    W = words(); return [rng.choice(W[len(c)]) for c in cribs]

def placements(runs, crib, codes, offs):
    """Return (onehot [n, ncode*20], presence [n, ncode], posmask [n, ntok])."""
    L = len(crib); oh, pr, ps = [], [], []
    nc = len(codes); nt = offs[-1]
    for ri, r in enumerate(runs):
        for p in range(len(r) - L + 1):
            m = {}; ok = True
            for c, ch in zip(r[p:p + L], crib):
                if m.setdefault(c, ch) != ch: ok = False; break
            if not ok: continue
            o = np.zeros(nc * 20, np.float32); q = np.zeros(nc, np.float32); s = np.zeros(nt, np.float32)
            for c, ch in m.items(): o[codes[c] * 20 + LIX[ch]] = 1; q[codes[c]] = 1
            s[offs[ri] + p: offs[ri] + p + L] = 1
            oh.append(o); pr.append(q); ps.append(s)
    if not oh: return None
    return np.array(oh), np.array(pr), np.array(ps)

_PM = None
def pmi():
    global _PM
    if _PM is None: _PM = cd.pmi_matrix()[0]
    return _PM

def Jmax(runs, cribs, codes, offs):
    """Statistic S (primary): max over consistent, non-overlapping placement pairs (any two cribs, or one crib twice)
    of the it16dip bigram PMI summed over every adjacent token pair in both letters whose codes the pair's joint key
    fixes, each crib's own internal bigrams removed (a constant per crib). Shared agreeing codes count twice."""
    P = [placements(runs, c, codes, offs) for c in cribs]
    nc = len(codes); A = np.zeros((nc, nc), np.float32)
    for r in runs:
        for x, y in zip(r, r[1:]): A[codes[x], codes[y]] += 1
    Pm = pmi().astype(np.float32)
    Q = np.einsum('xy,lm->xlym', A, Pm).reshape(nc * 20, nc * 20); Qs = Q + Q.T
    self_s = []
    for c, p in zip(cribs, P):
        if p is None: self_s.append(None); continue
        internal = sum(Pm[LIX[x], LIX[y]] for x, y in zip(c, c[1:]))
        self_s.append(np.einsum('nd,nd->n', p[0] @ Q, p[0]) - internal)
    PQ = [None if p is None else p[0] @ Qs for p in P]
    best = -1e9
    for a in range(len(P)):
        if P[a] is None: continue
        for b in range(a, len(P)):
            if P[b] is None: continue
            agree = P[a][0] @ P[b][0].T; share = P[a][1] @ P[b][1].T; ovl = P[a][2] @ P[b][2].T
            ok = (share == agree) & (ovl == 0)
            if a == b: ok = np.triu(ok, 1)
            if not ok.any(): continue
            S = self_s[a][:, None] + self_s[b][None, :] + PQ[a] @ P[b][0].T
            best = max(best, float(S[ok].max()))
    return best

def J(runs, cribs, codes, offs):
    if STAT == 'max': return Jmax(runs, cribs, codes, offs)
    P = [placements(runs, c, codes, offs) for c in cribs]
    tot = 0
    for a in range(len(P)):
        if P[a] is None: continue
        for b in range(a, len(P)):
            if P[b] is None: continue
            agree = P[a][0] @ P[b][0].T; share = P[a][1] @ P[b][1].T; ovl = P[a][2] @ P[b][2].T
            good = (agree >= K) & (share == agree) & (ovl == 0)
            tot += int(np.triu(good, 1).sum()) if a == b else int(good.sum())
    return tot

def prep(runs):
    codes = {c: i for i, c in enumerate(sorted({x for r in runs for x in r}))}
    offs = [0]
    for r in runs: offs.append(offs[-1] + len(r))
    return codes, offs

def rank_test(runs, cribs, ndec, rng):
    codes, offs = prep(runs); real = J(runs, cribs, codes, offs)
    null = [J(runs, decoy_set(cribs, rng), codes, offs) for _ in range(ndec)]
    ge = sum(x >= real for x in null)
    return real, null, (ge + 1) / (ndec + 1)

def synth(rng, ncell, planted, npairs=476, stray=0.05):
    """it16dip running text of ~npairs letters with the planted cribs inserted at word boundaries, one homophonic key,
    stray digits, cut into runs, re-phased by phase.em (best of 5 seeds by entropy) -> pair runs, as crib_drag.synth_runs."""
    c = cd.corpus(); n = npairs - sum(map(len, planted))
    s = rng.randrange(0, len(c) - n); txt = c[s:s + n]
    pos = sorted(rng.sample(range(20, n - 20), len(planted)), reverse=True)
    for p, w in zip(pos, planted): txt = txt[:p] + w + txt[p:]
    letters = sorted(set(txt)); fr = {l: txt.count(l) for l in letters}; cells = analyze.CELLS[:]; rng.shuffle(cells)
    key = {l: [cells.pop()] for l in letters}; extra = ncell - len(letters)
    while extra > 0:
        l = max(letters, key=lambda l: fr[l] / len(key[l])); key[l].append(cells.pop()); extra -= 1
    toks = []
    for ch in txt:
        if rng.random() < stray: toks.append(rng.choice('0123456789'))
        toks.append(rng.choice(key[ch]))
    runs, cur = [], ''
    for t in toks:
        cur += t
        if len(cur) > 40 and rng.random() < 0.15: runs.append(cur); cur = ''
    if cur: runs.append(cur)
    got, bh = None, 9e9
    for sd in range(5):
        g = phase.em(runs, seed=sd); h = phase.summary(g)['H']
        if h < bh: bh, got = h, g
    out = []
    for toksr in got:
        cur = []
        for t in toksr:
            if len(t) == 2: cur.append(t)
            else:
                if cur: out.append(cur)
                cur = []
        if cur: out.append(cur)
    return out

def control(a):
    rng = random.Random(a.seed); hits = 0
    for t in range(a.trials):
        planted = rng.sample(CRIBS, 3)
        runs = synth(rng, a.ncell, planted)
        real, null, p = rank_test(runs, CRIBS, a.decoys, rng)
        hit = p <= 0.05; hits += hit
        print(f'trial {t} ncell={a.ncell} planted={",".join(planted)} J={real:.2f} null_mean={np.mean(null):.2f} '
              f'p95={sorted(null)[int(.95*len(null))]:.2f} p={p:.3f} found={hit}', flush=True)
    print(f'CONTROL ncell={a.ncell} stat={STAT} K={K}: found {hits}/{a.trials} (gate >= 15/20)')

def target(a):
    rng = random.Random(20261003)
    runs = cd.read_runs(HERE + '/../pooled_tokens.txt')
    real, null, p = rank_test(runs, CRIBS, a.decoys, rng)
    ns = sorted(null)
    print(f'TARGET runs={len(runs)} pairs={sum(map(len, runs))} K={K} J_real={real} null_mean={np.mean(null):.2f} '
          f'p50={ns[len(ns)//2]} p95={ns[int(.95*len(ns))]} max={ns[-1]} rank={sum(x > real for x in null)+1}/{len(null)+1} p={p:.3f}')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('mode'); ap.add_argument('--trials', type=int, default=20)
    ap.add_argument('--ncell', type=int, default=40); ap.add_argument('--seed', type=int, default=4001)
    ap.add_argument('--decoys', type=int, default=200); ap.add_argument('--K', type=int, default=2); ap.add_argument('--stat', default='max')
    a = ap.parse_args(); K = a.K; STAT = a.stat
    control(a) if a.mode == 'control' else target(a)
