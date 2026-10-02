"""phased_homophonic: two-digit homophonic substitution written as unsegmented digit runs with stray single digits,
the phase (where each pair starts) resampled jointly with the key (BIRAGO-NUM3, 2 Oct 2026, birago-nevers-1571).

Why a separate family: `homophonic` needs the cipher already cut into signs. On a stream of figures with no group
separators and stray single digits, a cut fixed beforehand by a pair-frequency hard-EM (ciphers/birago-fr3252-1571-72/
num/phase.py) is 66-78% right at ~60 cells, and the fixed-phase homophonic control falls from 0.90 to 0.25 at that phase
error (BIRAGO-NUM). This family never fixes the phase: each restart starts from the same hard-EM cut, then alternates
  (a) homophonic_anneal.anneal on the current pair tokens, seeded with the last key (strays dropped), and
  (b) a Viterbi re-cut of every run under the current key: a pair token scores the n-gram log-prob of its letter in
      context + lam * log P(pair | its letter) (homophone choice, re-estimated from the last cut); a stray digit scores `stray` and is a
      null (the letter context runs on across it).
Best restart by the joint objective (homophonic_anneal.score of the letters + lam * log P(pair | letter) + stray * strays).

Input: one run per message, each a list of single digits (family_run.py --cipher FILE --tokens space, one run per line,
digits space-separated). N is the digit count, K the digit alphabet (10).
Control: a window of the corpus enciphered with a random key of `cells` two-digit cells (default 40; the cells use only
the digits that make up >= 2% of the target's digits -- Birago: no 6/7), one cell per letter then the rest by
frequency/size; each token is a stray single digit with probability `strays` (default 0.05), else the next letter's
pair; runs are filled to the target's own run lengths and a pair never straddles a break (a run with one digit left
takes a stray). Truth and decode are per-digit strings: a letter where a pair starts, '.' on its second digit, '-' on
a stray; recovery = share of true pair starts whose decoded pair starts there and reads the right letter.
params: cells (40), strays (0.05), rounds (4), iters (30000 first anneal), iters2 (10000 later), order (3), lam (1.0),
stray (-9.0), uni_weight (1.0), em_iters (30).
Must catch: a solver that reads a clean pre-cut homophonic stream but cannot recover the phase. Must NOT change: any
other family (this module is new; tools/tests/test_phased_homophonic.py)."""
import math
import random
from collections import Counter

import homophonic_anneal as ha
from families import draw_window

DESCRIPTION = ("two-digit homophonic in unsegmented digit runs with stray single digits; phase resampled jointly with "
               "the key (Viterbi re-cut under the key's n-gram score, alternating with homophonic_anneal; --param cells=40 "
               "strays=0.05 rounds=4; BIRAGO-NUM3 2 Oct 2026)")


def _p(params, k, d):
    return type(d)(params.get(k, d))


def _digits(params):
    toks = [t for m in params.get("target_msgs") or [] for t in m]
    c = Counter(toks)
    tot = max(1, sum(c.values()))
    ds = sorted(d for d, v in c.items() if v / tot >= 0.02 and len(d) == 1)
    return ds or list("0123456789")


def make_control(spec, seed, corpora, params):
    ncell, srate = _p(params, "cells", 40), _p(params, "strays", 0.05)
    lengths = params["lengths"]
    rng = random.Random(seed * 101 + ncell)
    text = ha.fold("\n".join(corpora))
    need = sum(lengths) // 2 + 50
    window, rest = draw_window(text, need, seed)
    ds = _digits(params)
    cells = [a + b for a in ds for b in ds]
    rng.shuffle(cells)
    fr = Counter(window)
    letters = sorted(fr)
    if ncell < len(letters) or ncell > len(cells):
        raise SystemExit(f"phased_homophonic: cells={ncell} must lie in {len(letters)}..{len(cells)}")
    key = {a: [cells.pop()] for a in letters}
    for _ in range(ncell - len(letters)):
        a = max(letters, key=lambda a: fr[a] / len(key[a]))
        key[a].append(cells.pop())
    msgs, truth, wi = [], [], 0
    for L in lengths:
        run, tr = [], []
        while len(run) < L:
            if rng.random() < srate or L - len(run) == 1 or wi >= len(window):
                run.append(rng.choice(ds)); tr.append("-")
            else:
                c = rng.choice(key[window[wi]])
                run += list(c); tr += [window[wi], "."]
                wi += 1
        msgs.append(run); truth.append("".join(tr))
    return msgs, "".join(truth), [rest]


def _em_cut(runs, rng, stray=-7.0, iters=30):
    """Hard-EM pair cut by pair frequency alone (the num/phase.py start): random initial phase per run."""
    toks = []
    for r in runs:
        s = rng.randrange(2) if len(r) > 1 else 1
        toks.append(([r[0]] if s and r else []) + [r[i:i + 2] for i in range(s, len(r) - 1, 2)] +
                    ([r[-1]] if (len(r) - s) % 2 and len(r) > s else []))
    for _ in range(iters):
        lp = _prior(toks)
        toks = [_viterbi_prior(r, lp, stray) for r in runs]
    return toks


def _prior(toks):
    c = Counter(x for t in toks for x in t if len(x) == 2)
    tot = sum(c.values())
    return {k: math.log((v + 0.1) / (tot + 10)) for k, v in c.items()}, math.log(0.1 / (tot + 10))


def _cond(toks, key):
    """log P(pair | its letter) under the current cut and key -- the homophone-choice term of the generative model
    (letters from the n-gram model, then a homophone per letter). A plain log P(pair) would count the letter's own
    frequency twice and favours a wrong cut with fewer pair types (BIRAGO-NUM3 dev: true cut scored below a wrong one)."""
    c = Counter(x for t in toks for x in t if len(x) == 2)
    nl = Counter()
    for x, v in c.items():
        nl[key[x]] += v
    lp = {x: math.log((v + 0.1) / (nl[key[x]] + 1.0)) for x, v in c.items()}
    return lp, math.log(0.1 / (max(nl.values() or [1]) + 1.0))


def _viterbi_prior(run, lpd, stray):
    lp, floor = lpd
    n = len(run)
    best, back = [0.0] + [-1e18] * n, [0] * (n + 1)
    for i in range(1, n + 1):
        c = best[i - 1] + stray
        if c > best[i]:
            best[i], back[i] = c, 1
        if i >= 2:
            c = best[i - 2] + lp.get(run[i - 2:i], floor - 4)
            if c > best[i]:
                best[i], back[i] = c, 2
    out, i = [], n
    while i > 0:
        out.append(run[i - back[i]:i]); i -= back[i]
    return out[::-1]


def _viterbi_key(run, key, model, lpd, lam, stray):
    """Re-cut one run under a fixed key: states = (digit position, last order-1 letters)."""
    lp, floor = lpd
    o = model.order
    lf = {a: math.log(model.freq[a]) for a in model.freq}
    n = len(run)
    layers = [dict() for _ in range(n + 1)]
    layers[0][""] = (0.0, None)
    for i in range(n):
        for ctx, (sc, _) in layers[i].items():
            c = sc + stray                         # stray: null, context unchanged
            if c > layers[i + 1].get(ctx, (-1e18,))[0]:
                layers[i + 1][ctx] = (c, (i, ctx, run[i]))
            if i + 2 <= n:
                t = run[i:i + 2]
                a = key.get(t)
                if a is None:
                    continue
                g = ctx + a
                lm = model.logp(g) if len(g) == o else lf[a]
                c = sc + lm + lam * lp.get(t, floor)
                nctx = g[-(o - 1):]
                if c > layers[i + 2].get(nctx, (-1e18,))[0]:
                    layers[i + 2][nctx] = (c, (i, ctx, t))
    ctx = max(layers[n], key=lambda k: layers[n][k][0])
    out, i = [], n
    while i > 0:
        _, (pi, pctx, tok) = layers[i][ctx]
        out.append(tok); i, ctx = pi, pctx
    return out[::-1]


def _objective(toks, key, model, lam, stray, uni_w):
    seq = [x for t in toks for x in t if len(x) == 2]
    lp, floor = _cond(toks, key)
    return (ha.score(model, "".join(key[x] for x in seq), uni_w) + lam * sum(lp.get(x, floor) for x in seq)
            + stray * sum(1 for t in toks for x in t if len(x) == 1))


def _render(toks, key):
    """per-digit string: letter at a pair start, '.' on its second digit, '-' on a stray."""
    out = []
    for t in toks:
        for x in t:
            out.append(key[x] + "." if len(x) == 2 else "-")
    return "".join(out)


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    runs = ["".join(m) for m in cipher_msgs]
    rounds, it1, it2 = _p(params, "rounds", 4), _p(params, "iters", 30000), _p(params, "iters2", 10000)
    lam, stray, uw = _p(params, "lam", 1.0), _p(params, "stray", -9.0), _p(params, "uni_weight", 1.0)
    letters = list(ha.ALPHA)
    weights = [model.freq[a] for a in letters]
    rng = random.Random(seed)
    results = []
    for r in range(restarts):
        toks = _em_cut(runs, rng, iters=_p(params, "em_iters", 30))
        key = None
        hist = []
        for rd in range(rounds + 1):
            seq = [x for t in toks for x in t if len(x) == 2]
            _, k2 = ha.anneal(seq, model, it1 if rd == 0 else it2, rng, uw, init=key)
            allp = {a + b for a in "0123456789" for b in "0123456789"}
            key = {p: k2.get(p) or (key or {}).get(p) or rng.choices(letters, weights)[0] for p in allp}
            obj = _objective(toks, key, model, lam, stray, uw)
            hist.append(round(obj, 1))
            if rd == rounds:
                break
            lpd = _cond(toks, key)
            new = [_viterbi_key(rn, key, model, lpd, lam, stray) for rn in runs]
            if new == toks:
                break
            toks = new
        results.append((obj, toks, key, hist))
    results.sort(key=lambda x: -x[0])
    obj, toks, key, hist = results[0]
    used = Counter(x for t in toks for x in t if len(x) == 2)
    return _render(toks, key), obj, {"restart_objectives": [round(x[0], 1) for x in results], "rounds": hist,
                                    "pairs": sum(used.values()), "types": len(used),
                                    "strays": sum(1 for t in toks for x in t if len(x) == 1),
                                    "key": {p: key[p] for p in sorted(used)},
                                    "cut": [" ".join(t) for t in toks]}


def score_recovery(plain, truth):
    pos = [i for i, b in enumerate(truth) if b not in ".-"]
    return sum(1 for i in pos if i < len(plain) and plain[i] == truth[i]) / max(1, len(pos))


def split_decode(dec, msgs):
    out, p = [], 0
    for m in msgs:
        out.append("".join(c for c in dec[p:p + len(m)] if c not in ".-")); p += len(m)
    return out
