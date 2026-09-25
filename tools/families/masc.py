"""masc: monoalphabetic simple substitution, wrapping tools/homophonic_anneal.py with signs = alphabet size.

Control design: a plaintext window with exactly K distinct letters (K = the target's sign count) under a random
one-sign-per-letter key, so the control is a true simple substitution of the target's N and K, not a homophonic
one (that is the `homophonic` family). Solver: homophonic_anneal.solve, the same call the target gets.
params: iters (default 40000), order (3), uni_weight (1.0)."""
import random
import homophonic_anneal as ha
from families import draw_window, letters

DESCRIPTION = "simple substitution (homophonic_anneal.py, one sign per letter; control has the target's K distinct letters)"


def _p(params, k, d):
    return type(d)(params.get(k, d))


def make_control(spec, seed, corpora, params):
    N, K = params["N"], params["K"]
    text = ha.fold("\n".join(corpora))
    accept = lambda w: len(set(w)) == K
    plain, rest = draw_window(text, N, seed, accept)
    rng = random.Random(seed + 1000)
    distinct = sorted(set(plain))
    signs = [f"s{i}" for i in range(len(distinct))]
    rng.shuffle(signs)
    key = dict(zip(distinct, signs))
    return [[key[a] for a in plain]], plain, [rest]


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    seq = [s for m in cipher_msgs for s in m]
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
    sc, key = res[0]
    return "".join(key[x] for x in seq), sc, {"restart_scores": [round(r[0], 1) for r in res], "key": key}


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n
