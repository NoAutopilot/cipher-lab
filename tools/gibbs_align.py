#!/usr/bin/env python3
"""Gibbs-sampled segmentation of cipher-group runs against an interlinear gloss (RUN1-PAG, 4 Oct 2026).

A different instrument from tools/interlinear_align.py (hard-EM dynamic programming, which commits to the single
best chunking each iteration and so lets an early wrong boundary feed itself): this one SAMPLES every pair's
chunk boundaries from their posterior given all other pairs, under a Bayesian model, and reads code values off
the posterior averaged over many sweeps.

Model (per pair: a run of codes c_1..c_n under a gloss of letters g):
  - each code c has its own distribution over chunks (strings of 0..--max-chunk letters), drawn from a Dirichlet
    process DP(alpha, G0); G0(s) = P_len(|s|) * prod_letters u(x), u = letter unigrams of the gloss material itself,
    P_len = --len-weights over lengths 0..max (length 0 is a null: the code adds nothing to the gloss);
  - the gloss is the concatenation of the chunks in order, except that the decipherer may write letters no code
    carries (an added "de Parme" for clarity): each such inserted letter costs --ins x u(letter);
  - collapsed Gibbs: remove the pair's counts, compute P(chunk | c) = (n_c[chunk] + alpha G0(chunk)) / (n_c + alpha)
    from all OTHER pairs, forward-filter over the (code index, gloss position) lattice, backward-sample one chunking,
    add its counts back. Temperature anneals from --t0 to 1 over the first half of --iters; the second half's
    samples are kept.
Tokens: interlinear_align.classify_token; 'num' and 'code' tokens are codes; a doubtful token is a code of its own
(never pooled); a clear token (a parenthesised numeral) carries no letters. Folding: interlinear_align.fold plus
y -> i (French manuscript spelling), applied to the gloss letters before sampling.

Output per code: counts of each chunk over kept sweeps and tokens; per token: its modal chunk over kept sweeps and
that chunk's share. Library use: sample(pairs, ...) -> (prep, tok_counts); token_modes(...); code_key(...).
    python3 tools/gibbs_align.py PAIRS.tsv --out KEY.tsv [--iters 200] [--seed 0] [--alpha 1] [--max-chunk 4]
           [--ins 0.02] [--len-weights 0.05,0.3,0.4,0.18,0.07] [--t0 3]
Scale-free settings: every default is a probability or count of sweeps, not a pixel or a corpus size.
Offline test: tools/tests/test_gibbs_align.py (a synthetic homophonic syllabary with nulls and inserted gloss
words; the sampler recovers the planted values well above a shuffled-pairing run).
"""
import argparse, collections, csv, math, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import interlinear_align as ia

DEFAULTS = dict(iters=200, alpha=1.0, max_chunk=4, ins=0.02, len_weights=(0.05, 0.3, 0.4, 0.18, 0.07), t0=3.0)


def fold(s):
    return ia.fold(s).replace('y', 'i')


def prepare(pairs):
    """-> list of (pair, codes, letters); codes is a list of hashable code ids or None (clear token)."""
    out = []
    for k, p in enumerate(pairs):
        codes = []
        for j, t in enumerate(p['cipher_raw'].split()):
            kind, val = ia.classify_token(t)
            if kind in ('num', 'code'):
                codes.append(val)
            elif kind == 'doubtful':
                codes.append(('doubtful', k, j))
            else:
                codes.append(None)
        out.append((p, codes, fold(ia.plain_letters(p['plain_raw'])[0])))
    return out


def _ffbs(codes, g, prob, maxc, ins_cost, temp, rng):
    """Sample one chunking: list of (start, end) per code (None for clear tokens). prob(code, chunk) -> P."""
    n, m = len(codes), len(g)
    f = [[0.0] * (m + 1) for _ in range(n + 1)]
    f[0][0] = 1.0
    scale = [1.0] * (n + 1)
    for j in range(1, m + 1):
        f[0][j] = f[0][j - 1] * ins_cost[j - 1]
    for i in range(1, n + 1):
        c = codes[i - 1]
        fi, fp = f[i], f[i - 1]
        for j in range(m + 1):
            if c is None:
                s = fp[j]
            else:
                s = 0.0
                for L in range(0, min(maxc, j) + 1):
                    if fp[j - L]:
                        s += fp[j - L] * prob(c, g[j - L:j]) ** (1.0 / temp)
            if j:
                s += fi[j - 1] * ins_cost[j - 1]
            fi[j] = s
        # rescale row to avoid underflow
        mx = max(fi) or 1.0
        scale[i] = mx
        for j in range(m + 1):
            fi[j] /= mx
    if f[n][m] == 0:
        return None
    seg = [None] * n
    j = m
    i = n
    while i > 0:
        c = codes[i - 1]
        # choices: an inserted letter at j (stay at row i) or code i's chunk ending at j
        opts = []
        if j:
            # row i is stored divided by scale[i] relative to row i-1's units
            opts.append(('ins', f[i][j - 1] * scale[i] * ins_cost[j - 1]))
        if c is None:
            opts.append((0, f[i - 1][j]))
        else:
            for L in range(0, min(maxc, j) + 1):
                if f[i - 1][j - L]:
                    opts.append((L, f[i - 1][j - L] * prob(c, g[j - L:j]) ** (1.0 / temp)))
        tot = sum(w for _, w in opts)
        r = rng.random() * tot
        for ch, w in opts:
            r -= w
            if r <= 0:
                break
        if ch == 'ins':
            j -= 1
            continue
        seg[i - 1] = None if c is None else (j - ch, j)
        j -= ch
        i -= 1
    return seg


def sample(pairs, iters=None, seed=0, alpha=None, max_chunk=None, ins=None, len_weights=None, t0=None, prep=None):
    """Run the sampler. -> (prep, tok_counts): tok_counts[pair_index][token_index] = Counter(chunk -> kept sweeps)."""
    o = dict(DEFAULTS)
    for k, v in dict(iters=iters, alpha=alpha, max_chunk=max_chunk, ins=ins, len_weights=len_weights, t0=t0).items():
        if v is not None:
            o[k] = v
    rng = random.Random(seed)
    prep = prep or prepare(pairs)
    allg = ''.join(g for _, _, g in prep)
    uc = collections.Counter(allg)
    u = {ch: (uc[ch] + 0.5) / (len(allg) + 0.5 * 26) for ch in 'abcdefghijklmnopqrstuvwxyz'}
    lw = list(o['len_weights'])[:o['max_chunk'] + 1]
    zl = sum(lw)
    lw = [x / zl for x in lw]
    g0cache = {}

    def g0(s):
        v = g0cache.get(s)
        if v is None:
            v = lw[len(s)]
            for ch in s:
                v *= u.get(ch, 1e-3)
            g0cache[s] = v
        return v

    cnt = collections.defaultdict(collections.Counter)
    tot = collections.Counter()
    a = o['alpha']

    def prob(c, s):
        if isinstance(c, tuple):  # doubtful: never pooled
            return g0(s)
        return (cnt[c][s] + a * g0(s)) / (tot[c] + a)

    segs = [None] * len(prep)
    keep = [[collections.Counter() for _ in codes] for _, codes, _ in prep]
    half = max(1, o['iters'] // 2)
    order = list(range(len(prep)))
    for it in range(o['iters']):
        temp = o['t0'] + (1.0 - o['t0']) * min(1.0, it / half)
        rng.shuffle(order)
        for k in order:
            _, codes, g = prep[k]
            if segs[k] is not None:
                for c, sg in zip(codes, segs[k]):
                    if c is not None and sg is not None and not isinstance(c, tuple):
                        cnt[c][g[sg[0]:sg[1]]] -= 1
                        tot[c] -= 1
            ins_cost = [o['ins'] * u.get(ch, 1e-3) for ch in g]
            sg = _ffbs(codes, g, prob, o['max_chunk'], ins_cost, temp, rng)
            segs[k] = sg
            if sg is None:
                continue
            for c, s in zip(codes, sg):
                if c is not None and s is not None and not isinstance(c, tuple):
                    cnt[c][g[s[0]:s[1]]] += 1
                    tot[c] += 1
        if it >= half:
            for k, (_, codes, g) in enumerate(prep):
                if segs[k] is None:
                    continue
                for t, (c, s) in enumerate(zip(codes, segs[k])):
                    if c is not None and s is not None:
                        keep[k][t][g[s[0]:s[1]]] += 1
    return prep, keep


def token_modes(prep, keep):
    """-> list of (pair_index, token_index, code, modal_chunk, share) for every code token with kept samples."""
    out = []
    for k, (_, codes, _) in enumerate(prep):
        for t, c in enumerate(codes):
            if c is None or isinstance(c, tuple) or not keep[k][t]:
                continue
            ch, n = keep[k][t].most_common(1)[0]
            out.append((k, t, c, ch, n / sum(keep[k][t].values())))
    return out


def code_key(modes, nulls=False):
    """code -> (top modal chunk, its token count, token total), kept only when the top is unique.
    nulls=False: empty modal chunks are left out of both counts (a null is never a key value)."""
    per = collections.defaultdict(list)
    for _, _, c, ch, _ in modes:
        if ch or nulls:
            per[c].append(ch)
    k = {}
    for c, xs in per.items():
        mc = collections.Counter(xs).most_common()
        if len(mc) == 1 or mc[0][1] > mc[1][1]:
            k[c] = (mc[0][0], mc[0][1], len(xs))
    return k


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('pairs', help='TSV with columns plain_raw and cipher_raw (interlinear_align.py pairs format)')
    ap.add_argument('--out', required=True, help='key TSV: code, top chunk, top tokens, tokens, posterior chunk counts')
    ap.add_argument('--iters', type=int, default=DEFAULTS['iters'])
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--alpha', type=float, default=DEFAULTS['alpha'])
    ap.add_argument('--max-chunk', type=int, default=DEFAULTS['max_chunk'])
    ap.add_argument('--ins', type=float, default=DEFAULTS['ins'], help='per-letter weight of a gloss letter no code carries')
    ap.add_argument('--len-weights', default=','.join(map(str, DEFAULTS['len_weights'])), help='P_len for lengths 0..max')
    ap.add_argument('--t0', type=float, default=DEFAULTS['t0'], help='starting temperature (anneals to 1 over half the sweeps)')
    a = ap.parse_args()
    pairs = ia.load_pairs(a.pairs)
    prep, keep = sample(pairs, iters=a.iters, seed=a.seed, alpha=a.alpha, max_chunk=a.max_chunk, ins=a.ins,
                        len_weights=tuple(float(x) for x in a.len_weights.split(',')), t0=a.t0)
    modes = token_modes(prep, keep)
    key = code_key(modes)
    post = collections.defaultdict(collections.Counter)
    for k, (_, codes, _) in enumerate(prep):
        for t, c in enumerate(codes):
            if c is not None and not isinstance(c, tuple):
                post[c].update(keep[k][t])
    with open(a.out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['code', 'top', 'top_tokens', 'tokens', 'posterior'])
        for c in sorted(post, key=lambda x: (str(type(x)), x)):
            top = key.get(c, ('', 0, sum(1 for m in modes if m[2] == c)))
            w.writerow([c, top[0], top[1], top[2],
                        ','.join('%s:%d' % (s or '-', n) for s, n in post[c].most_common(6))])
    print('codes %d, keyed (unique non-empty top) %d -> %s' % (len(post), len(key), a.out))


if __name__ == '__main__':
    main()
