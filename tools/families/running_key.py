"""running_key: book-key Vigenere family, wrapping tools/running_key.py (LANE GOLD's two-stream beam decoder).

Control design: as running_key.py --control: a plaintext window from one corpus book enciphered under a window of
a different book as key (both books held out of the models), one message per target message length.
Solver: running_key.build_models + decode_message, the same call the target gets. Needs at least three corpus
texts (plain book, key book, one to train on): give the family a directory corpus such as tools/data/de20.
params: tabula (vig), order (6), beam (3000), per_hyp (10), polish (0/1), discount (0.9). Slow: a 924-letter
target at beam 3000 runs for minutes; use beam 200 for a smoke test."""
import random, types
import running_key as rk
from families import draw_window

DESCRIPTION = "running key / book key (running_key.py two-stream beam decoder; control = plain book x key book)"


def _args(params, pcorpus=(), kcorpus=()):
    return types.SimpleNamespace(pcorpus=list(pcorpus), kcorpus=list(kcorpus), order=int(params.get("order", 6)),
                                 discount=float(params.get("discount", 0.9)), spaces=False,
                                 beam=int(params.get("beam", 3000)), per_hyp=int(params.get("per_hyp", 10)),
                                 polish=bool(int(params.get("polish", 0))), tabula=params.get("tabula", "vig"))


def make_control(spec, seed, corpora, params):
    if len(corpora) < 3:
        raise SystemExit("running_key control needs at least three corpus texts (plain book, key book, training)")
    rng = random.Random(seed)
    tab = params.get("tabula", "vig")
    idx = list(range(len(corpora)))
    rng.shuffle(idx)
    pi, ki = idx[0], idx[1]
    ptext, ktext = rk.fold(corpora[pi]), rk.fold(corpora[ki])
    lengths = params.get("lengths") or [params["N"]]
    msgs, plains = [], []
    for n in lengths:
        P, _ = draw_window(ptext, n, rng.randrange(10 ** 6))
        K, _ = draw_window(ktext, n, rng.randrange(10 ** 6))
        msgs.append([rk.A[rk.encipher(tab, rk.IDX[a], rk.IDX[b])] for a, b in zip(P, K)])
        plains.append(P)
    train = [corpora[i] for i in idx[2:]]
    return msgs, "".join(plains), train


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    tab = params.get("tabula", "vig")
    a = _args(params)
    lm = rk.LM([rk.fold(t) for t in corpora], a.order, a.discount, rk.A)
    out, ll = [], 0.0
    n = 0
    for m in cipher_msgs:
        c = "".join(m)
        r = rk.decode_message(c, lm, lm, tab, a.beam, a.per_hyp, a.polish, False)
        out.append(r["plain"])
        ll += (r["ll_p"] + r["ll_k"]) * len(c)
        n += len(c)
    return "".join(out), ll / max(1, n), {"tabula": tab, "beam": a.beam, "order": a.order}


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n
