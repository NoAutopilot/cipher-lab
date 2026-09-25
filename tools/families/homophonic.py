"""homophonic: homophonic substitution, wrapping tools/homophonic_anneal.py with the spec's K.

Control design: homophonic_anneal.make_control (K signs allotted to letters by corpus frequency, each occurrence
drawing a homophone at random) on a plaintext window cut from the corpus and held out of the solver's model.
Solver: homophonic_anneal.solve. params: iters (40000), order (3), uni_weight (1.0)."""
import homophonic_anneal as ha
from families import draw_window

DESCRIPTION = "homophonic substitution (homophonic_anneal.py, control = make_control at the target's N and K)"


def _p(params, k, d):
    return type(d)(params.get(k, d))


def make_control(spec, seed, corpora, params):
    N, K = params["N"], params["K"]
    text = ha.fold("\n".join(corpora))
    plain, rest = draw_window(text, N, seed, lambda w: len(set(w)) <= K)
    model = ha.Model([rest], _p(params, "order", 3))
    seq, p, truth = ha.make_control(plain, K, N, model, seed)
    return [seq], p, [rest]


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    seq = [s for m in cipher_msgs for s in m]
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
    sc, key = res[0]
    return "".join(key[x] for x in seq), sc, {"restart_scores": [round(r[0], 1) for r in res], "key": key}


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n
