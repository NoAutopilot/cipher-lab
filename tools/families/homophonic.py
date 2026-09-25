"""homophonic: homophonic substitution, wrapping tools/homophonic_anneal.py with the spec's K.

Control design: homophonic_anneal.make_control (K signs allotted to letters by corpus frequency, each occurrence
drawing a homophone at random) on a plaintext window cut from the corpus and held out of the solver's model.
Solver: homophonic_anneal.solve. params: iters (40000), order (3), uni_weight (1.0).

profile=target (GOLD-D1, 25 Sept 2026): allot the K homophones so the control's own sign-count profile matches
the TARGET's sorted sign counts (from params["target_msgs"], always supplied by family_run.py), not corpus
letter frequency alone -- so a control at the target's K also carries the same lopsided top sign (Debosnys' X
at 16.1 pct of N). Letters (ranked by the solver's own corpus frequency) are walked in order and handed buckets
from the target's own counts, largest first, until each letter's bucket sum reaches about its corpus share of
N; a letter's occurrences then draw among its own bucket-sized signs with probability proportional to the
bucket sizes, so the marginal sign-count distribution this produces is the target's own shape. Default (no
profile param) is unchanged: homophonic_anneal.make_control's frequency-proportional allotment.

noise=p (the Salviati recipe, ciphers/fr2933-salviati-1525/control/codemark_curve.py, LANE R6 CM): after the
control cipher is built (either allotment above), a share p of its tokens are redrawn -- weighted by the
target's own type-frequency profile, mapped by rank onto the control's own K sign labels -- standing in for a
transcription error rate on the real page. Default 0 leaves the control untouched."""
import random
import homophonic_anneal as ha
from families import draw_window
from collections import Counter

DESCRIPTION = ("homophonic substitution (homophonic_anneal.py, control = make_control at the target's N and K; "
               "--param profile=target matches the target's own sign-count profile; --param noise=p redraws a "
               "share p of control tokens at the target's own type frequencies)")


def _p(params, k, d):
    return type(d)(params.get(k, d))


def _target_sign_counts(params):
    """The target's own sign counts (params["target_msgs"], always set by family_run.py), sorted descending."""
    toks = [t for m in params.get("target_msgs") or [] for t in m]
    return sorted(Counter(toks).values(), reverse=True)


def _make_control_profile(plain_text, K, N, model, seed, target_counts):
    """profile=target: see module docstring. target_counts: the target's own sorted sign counts.

    Fair-share greedy, not a fixed per-letter homophone count: (1) reserve the L smallest target buckets (L =
    number of distinct plaintext letters in the window), one per letter, rarest letter <- smallest bucket, so
    every letter is covered and K is never short; (2) hand out the remaining K-L buckets largest-first, each to
    whichever letter's allocation-so-far is furthest below its corpus share (min of got/want) -- so the single
    biggest bucket goes to the most frequent letter, and once that letter's running total approaches its own
    share, further big buckets go to the next most under-served letter instead of piling onto the first. This is
    what lets ONE control sign end up carrying close to the target's own top share (e.g. Debosnys' X at 16.1 pct
    of N): splitting a letter's homophones by the plain largest-remainder rule (proportional to K, not to the
    target's own lumpy counts) would spread that letter's occurrences over many similar-sized signs instead."""
    rng = random.Random(seed + 1000)
    p = ha.fold(plain_text)[:N]
    cnt = Counter(p)
    letters = [a for a, _ in cnt.most_common()]  # present letters, most frequent first
    L = len(letters)
    counts = list(target_counts) if target_counts else []
    counts = (counts + [1] * K)[:K] if len(counts) < K else counts[:K]
    counts_desc = sorted(counts, reverse=True)
    reserve = counts_desc[-L:] if L <= len(counts_desc) else counts_desc + [1] * (L - len(counts_desc))
    remaining = counts_desc[:len(counts_desc) - L] if L <= len(counts_desc) else []
    letters_asc = list(reversed(letters))  # rarest first, paired with the smallest reserved buckets
    alloc = {a: [reserve[i]] for i, a in enumerate(letters_asc)}
    want = {a: model.freq[a] * N for a in letters}
    got = {a: alloc[a][0] for a in letters}
    for b in remaining:  # largest bucket first
        a = min(letters, key=lambda a: got[a] / want[a] if want[a] > 0 else float("inf"))
        alloc[a].append(b)
        got[a] += b
    homs, i = {}, 0
    for a in letters:
        homs[a] = [f"s{i + j}" for j in range(len(alloc[a]))]
        i += len(alloc[a])
    seq = [rng.choices(homs[a], weights=alloc[a])[0] for a in p]
    truth = {s: a for a, ss in homs.items() for s in ss}
    return seq, p, truth


def _inject_noise(seq, noise, target_counts, seed):
    """noise=p: see module docstring (the Salviati recipe). Redraws a share p of seq's own tokens, weighted by
    the target's own counts mapped by rank onto seq's own labels (its most frequent label gets the target's
    largest count as weight, and so on)."""
    if not noise:
        return seq
    rng = random.Random(seed + 9000)
    cnt = Counter(seq)
    labels = sorted(cnt, key=lambda s: -cnt[s])
    weights = list(target_counts)[:len(labels)] if target_counts else []
    weights = (weights + [1] * len(labels))[:len(labels)]
    return [rng.choices(labels, weights)[0] if rng.random() < noise else s for s in seq]


def make_control(spec, seed, corpora, params):
    N, K = params["N"], params["K"]
    text = ha.fold("\n".join(corpora))
    plain, rest = draw_window(text, N, seed, lambda w: len(set(w)) <= K)
    model = ha.Model([rest], _p(params, "order", 3))
    noise = float(params.get("noise", 0) or 0)
    profile = params.get("profile", "")
    target_counts = _target_sign_counts(params) if (profile == "target" or noise) else None
    if profile == "target":
        seq, p, truth = _make_control_profile(plain, K, N, model, seed, target_counts)
    else:
        seq, p, truth = ha.make_control(plain, K, N, model, seed)
    if noise:
        seq = _inject_noise(seq, noise, target_counts, seed)
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
