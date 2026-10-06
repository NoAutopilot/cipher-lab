"""cycling_homophonic: homophonic substitution whose homophones for each letter are used in one fixed cyclic order
(R11-SCORPCYC, 6 Oct 2026, scorpion-1991; the design Pelling 2020 proposed for the Scorpion and Zodiac-style ciphers).

Design: letter a has m_a homophones h_a[0..m_a-1]; the i-th occurrence of a in the text writes h_a[(off_a + i) mod m_a].
So, under the true key, the signs a letter receives, read in text order, repeat with period m_a = the number of
distinct signs mapped to it (each sign recurs exactly m_a occurrences of its letter later).

Control (rule 3's matched control): a window of the corpus, held out of the solver's model (families.draw_window), K
homophones allotted by the window's letter frequency exactly as homophonic_anneal.make_control (at least one per letter,
then largest-remainder), each letter's homophones then used cyclically from a random offset. The realized K can fall
below the nominal K when a letter occurs fewer times than it has homophones (as in the `homophonic` control).

Solver: an n-gram anneal over the sign -> letter key (homophonic_anneal's incremental n-gram and unigram-KL terms) whose
objective adds -lam * V, V = cycle violations: for each letter, take its sign sequence in text order; between two
consecutive occurrences of one sign no other sign may appear twice (in a strict cycle each appears exactly once), and
every extra appearance is one violation (letter_violations). A true key has V = 0; lam large (e.g. 50) makes the
cycle a near-hard constraint. Note what the constraint can and cannot see: a letter whose signs are all hapax has V = 0
under any key, so on a hapax-heavy text (S1: 39 of 53 signs hapax) the cycle term has little to bite on -- the control
measures exactly that.
params: lam (2.0), iters (40000), order (3), uni_weight (1.0), t0 (4.0).
Must catch: a control that is not cyclic, a violation count that is not zero on the true key, and a solver that cannot
read an easy (N=400, K=40) cycling control. Must NOT change: any other family (tools/tests/test_cycling_homophonic.py)."""
import bisect
import math
import random
from collections import Counter

import homophonic_anneal as ha
from families import draw_window

DESCRIPTION = ("homophonic with each letter's homophones used in a fixed cyclic order (Pelling 2020); anneal with a "
               "-lam x cycle-violation term (--param lam=2.0, lam=50 near-hard; R11-SCORPCYC 6 Oct 2026)")


def _p(params, k, d):
    return type(d)(params.get(k, d))


def encipher(plain, K, seed):
    """Cyclic homophonic encipherment of folded plain text with K homophones allotted by its own letter frequency.
    Returns (seq, truth_key {sign: letter}, homs {letter: [signs in cycle order]})."""
    rng = random.Random(seed + 1000)
    cnt = Counter(plain)
    letters = [a for a, _ in cnt.most_common()]
    if K < len(letters):
        raise SystemExit(f"cycling_homophonic: K={K} is below the {len(letters)} letters in the window")
    alloc = {a: 1 for a in letters}
    for _ in range(K - len(letters)):
        a = max(letters, key=lambda a: cnt[a] / alloc[a])
        alloc[a] += 1
    homs, i = {}, 0
    for a in letters:
        homs[a] = [f"s{i + j}" for j in range(alloc[a])]
        i += alloc[a]
    off = {a: rng.randrange(alloc[a]) for a in letters}
    seen = Counter()
    seq = []
    for a in plain:
        seq.append(homs[a][(off[a] + seen[a]) % alloc[a]])
        seen[a] += 1
    return seq, {s: a for a, ss in homs.items() for s in ss}, homs


def make_control(spec, seed, corpora, params):
    N, K = params["N"], params["K"]
    text = ha.fold("\n".join(corpora))
    plain, rest = draw_window(text, N, seed, lambda w: len(set(w)) <= K)
    seq, truth, _ = encipher(plain, K, seed)
    print("cycling_homophonic control (seed %d): N=%d nominal K=%d realized K=%d hapax %d" % (
        seed, N, K, len(set(seq)), sum(1 for v in Counter(seq).values() if v == 1)))
    return [seq], plain, [rest]


def letter_violations(signs):
    """Cycle violations in one letter's sign sequence (text order). In a strict cycle, between two consecutive
    occurrences of a sign every other sign of the letter appears exactly once, so no sign appears twice inside such a
    gap; each extra appearance counts one violation. This is a necessary condition only (zero on the true key) and,
    unlike a period-m check, does not depend on m: one wrong sign added to a letter costs only the gaps it upsets,
    not every comparison (a period-m count rescored the whole letter and stalled the anneal, R11-SCORPCYC dev)."""
    last, v = {}, 0
    for k, x in enumerate(signs):
        p = last.get(x)
        if p is not None and k - p > 2:
            c = Counter(signs[p + 1:k])
            v += sum(n - 1 for n in c.values())
        last[x] = k
    return v


def violations(seq, key):
    by = {}
    for x in seq:
        by.setdefault(key[x], []).append(x)
    return sum(letter_violations(v) for v in by.values())


def anneal(seq, model, iters, rng, uni_w, lam, t0=4.0):
    o = model.order
    signs = sorted(set(seq))
    letters = list(ha.ALPHA)
    weights = [model.freq[a] for a in letters]
    lf = {a: math.log(model.freq[a]) for a in letters}
    pos = {s: [i for i, x in enumerate(seq) if x == s] for s in signs}
    n = len(seq)
    starts = {s: sorted({j for i in pos[s] for j in range(max(0, i - o + 1), min(i, n - o) + 1)}) for s in signs}
    key = {s: rng.choices(letters, weights)[0] for s in signs}
    pl = [key[x] for x in seq]
    lpos = {a: [] for a in letters}            # positions decoded as each letter, sorted
    for i, a in enumerate(pl):
        lpos[a].append(i)
    lp = model.logp

    def part(js):
        return sum(lp("".join(pl[j:j + o])) for j in js)

    def lv(a):
        return letter_violations([seq[i] for i in lpos[a]])

    cnt = Counter(pl)
    xlx = lambda c: c * math.log(c) if c > 0 else 0.0
    viol = {a: lv(a) for a in letters}
    cur = ha.score(model, "".join(pl), uni_w) - lam * sum(viol.values())
    best, bestkey = cur, dict(key)
    for it in range(iters):
        T = t0 * (1 - it / iters) + 0.02
        s = rng.choice(signs)
        old, new = key[s], rng.choice(letters)
        if new == old:
            continue
        js = starts[s]
        before = part(js)
        for i in pos[s]:
            pl[i] = new
        m = len(pos[s])
        du = m * (lf[new] - lf[old]) - (xlx(cnt[new] + m) - xlx(cnt[new]) + xlx(cnt[old] - m) - xlx(cnt[old]))
        dr = part(js) - before
        for i in pos[s]:
            lpos[old].remove(i)
            bisect.insort(lpos[new], i)
        vo, vn = lv(old), lv(new)
        dv = vo + vn - viol[old] - viol[new]
        d = dr + uni_w * du - lam * dv
        if d >= 0 or rng.random() < math.exp(d / T):
            key[s] = new
            cnt[new] += m
            cnt[old] -= m
            viol[old], viol[new] = vo, vn
            cur += d
            if cur > best:
                best, bestkey = cur, dict(key)
        else:
            for i in pos[s]:
                pl[i] = old
                lpos[new].remove(i)
                bisect.insort(lpos[old], i)
    return best, bestkey


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    model = ha.Model(corpora, _p(params, "order", 3))
    seq = [s for m in cipher_msgs for s in m]
    lam, uw = _p(params, "lam", 2.0), _p(params, "uni_weight", 1.0)
    rng = random.Random(seed)
    res = [anneal(seq, model, _p(params, "iters", 40000), rng, uw, lam, _p(params, "t0", 4.0)) for _ in range(restarts)]
    res.sort(key=lambda r: -r[0])
    sc, key = res[0]
    return "".join(key[x] for x in seq), sc, {"restart_scores": [round(r[0], 1) for r in res], "lam": lam,
                                             "violations": violations(seq, key), "key": key}


def score_recovery(plain, truth):
    n = max(1, len(truth))
    return sum(1 for a, b in zip(plain, truth) if a == b) / n
