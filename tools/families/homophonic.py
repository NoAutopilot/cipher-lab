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
transcription error rate on the real page. Default 0 leaves the control untouched.

units=syl (bMALN, 26 Sept 2026, malsburg-hessen-1636): a letter+syllable homophonic design -- a sign stands for a
letter OR a common syllable/bigram (period German tables of the 1600s mix both). The corpus is cut into units by
greedy longest match over `syl` (--param syl=und,der,sch,... ; default SYL_DE below), each unit becomes one private
character, and the SAME annealer (homophonic_anneal.anneal, whose alphabet now follows model.alpha) assigns one unit
per sign under a unit n-gram model (order param, default 2 for units: on a 48-unit alphabet the unit trigram is
too sparse for the anneal to find the true key even when it scores it higher -- measured bMALN, clean N=1500 K=60:
order 3 recovered 0.00-0.26, order 2 0.16-0.87 per restart; use --param iters=150000 and >= 8 restarts). The control is
a unit window of N units under the same profile/noise options; recovery = share of unit positions read correctly.
The target decode is written expanded back to letters (split_decode), so the judge reads ordinary text.

merge=k nulls=p (H22, 28 Sept 2026, spinelli-beinecke-c1515): a "merged-symbol + nulls" design -- a substitution in
which the signs of k plaintext letters have collapsed into ONE cipher symbol (a family of small hook shapes two blind
readers cannot tell apart, or a table whose several letters share a sign) and a share p of the N cipher tokens are
nulls drawn from `null_types` (default 6) null signs, carrying no letter. The control window is M = N - round(N*p)
letters long (so the control's N is the target's N, nulls included); the k merged letters are the random k-subset
of the window's own letters (2000 draws) whose combined share of the window is nearest `merge_share` (default: the
target's own top sign count over its letter tokens, N - round(N*p) -- Spinelli: HOOK 54 of 218 = 0.248); the
remaining letters get the remaining K - 1 - null_types signs by the ordinary at-least-one-then-largest-remainder
allotment (ha.make_control's rule); nulls are placed at random positions and drawn uniformly over the null signs.
The plain string returned carries '-' at null positions and score_recovery skips them, so recovery is the share of
LETTER positions read correctly; the merged symbol can read at most one of its k letters right, so make_control
prints the design's recovery ceiling (1 - (merged count - largest member count)/M) beside the merged letters --
compare the control's recovery with that ceiling, not only with the gate. Must catch: a solver that reads a clean
homophonic control but not this design (a control under the gate then says the design, not the length, is the
limit -- rule 3's Salviati lesson). Must NOT change: merge=0 nulls=0 (or absent) is byte-for-byte the old
behaviour (tools/tests/test_homophonic_merge.py checks both). --param noise=p applies to this design too (GAPS50,
3 Oct 2026: before then it was silently ignored here, so a merge/nulls control "at the measured error" was clean);
profile=target is still not applied to the merge/nulls allotment.

wild=<sign>[,<sign>] (H25, 28 Sept 2026, spinelli-beinecke-c1515): solver side of the same design -- every occurrence of
a wild sign is annealed as its own pseudo-sign, i.e. a per-position free letter chosen by the n-gram model with the
unigram KL term keeping the letter distribution honest, so a family sign standing for several letters (Spinelli's HOOK)
has a recovery ceiling of 1.0 instead of the merge= control's 1 - (merged - top)/M. The same param reaches the control
and the target, so name both signs: --param wild=sM,HOOK (sM is the merge= control's merged sign). The info dict's
`wild_letters` gives the letters each wild sign was read as, with counts. Test: tools/tests/test_homophonic_wild.py.

alphabet=NAME|CHARS (A2P4-KAL4, 3 Oct 2026, kaliningrad-2015): the plaintext alphabet, passed to
homophonic_anneal.set_alphabet before the control and the solve -- a name from homophonic_anneal.ALPHABETS
(ru-s3p-soft 35 letters, ru-s3-soft 37: Russian with each softened consonant its own letter) or a literal string.
The corpus must already be written in that alphabet (tools/data/ru19_soft); fold keeps only its characters,
case-sensitive. Absent (or "default") is byte-for-byte the old 24-letter behaviour. The judge needs the same
alphabet in the spec's judge block ("alphabet": the same NAME or CHARS). Test: tools/tests/test_homophonic_alphabet.py.

crib=drag (RUN3-SANG, 4 Oct 2026, sanguszkow-mniszech-dunin-1714): a crib-assisted run seeded from the cipher's own
exact sign repeats. Solver: R6 = the most frequent sign 6-gram (count >= 3), R2 = the most frequent sign bigram
(count >= 3) with no sign in R6; the top m6 (200) corpus 6-letter strings are pinned on R6 one at a time (short anneal,
drag_iters 8000), the best `keep` (5) are crossed with the top m2 (40) corpus bigrams on R2, and the best-scoring pair
is pinned for the full anneal. Control: the window is redrawn (up to 2000 tries) until it holds a 6-letter string x>=3
and a bigram x>=8, and those occurrences are given identical signs (one 6-sign repeat x3, one 2-sign repeat x8 planted),
so the control carries the target's crib count and kind. crib_oracle=1 (control-only diagnostic, never a gate for a
target) appends the planted strings to the candidate lists, separating "truth not in the list" from "scoring cannot
pick it". info carries the chosen cribs, and for a control
`crib_right`. Must catch: a crib-drag whose wrong pin pulls the anneal off (control recovery falls). Must NOT change:
crib absent is byte-for-byte the old behaviour. Test: tools/tests/test_homophonic_cribdrag.py."""
import json
import math
import random
import re
import homophonic_anneal as ha
from families import draw_window
from collections import Counter

DESCRIPTION = ("homophonic substitution (homophonic_anneal.py, control = make_control at the target's N and K; "
               "--param profile=target matches the target's own sign-count profile; --param noise=p redraws a "
               "share p of control tokens at the target's own type frequencies; --param merge=k nulls=p collapses "
               "k letters' signs into one symbol and makes a share p of the tokens nulls, H22 28 Sept 2026; --param wild=SIGN,... "
               "anneals every occurrence of a wild sign as its own letter, H25 28 Sept 2026; --param alphabet=NAME|CHARS sets the "
               "plaintext alphabet, A2P4-KAL4 3 Oct 2026)")


SYL_DE = "und,der,die,das,sch,ein,ch,en,er,ei,ie,st,ge,be,in,an,te,de,nd,ss,ck,au,ng,re"
_UCH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def _units(params):
    syl = [u for u in str(params.get("syl", SYL_DE)).split(",") if u]
    if len(syl) > len(_UCH):
        raise SystemExit(f"homophonic units=syl: at most {len(_UCH)} syllables")
    return sorted(syl, key=len, reverse=True), {u: _UCH[i] for i, u in enumerate(syl)}


def encode_units(text, params):
    """Folded letters -> unit string (one char per unit, greedy longest match over the syllable list)."""
    syl, code = _units(params)
    t, out, i = ha.fold(text), [], 0
    while i < len(t):
        for u in syl:
            if t.startswith(u, i):
                out.append(code[u]); i += len(u); break
        else:
            out.append(t[i]); i += 1
    return "".join(out)


def expand_units(s, params):
    _, code = _units(params)
    inv = {c: u for u, c in code.items()}
    return "".join(inv.get(c, c) for c in s)


class UnitModel:
    """homophonic_anneal.Model's interface over a unit alphabet (letters + one private char per syllable)."""
    def __init__(self, unit_texts, order=3, k=0.5, alpha=None):
        s = "".join(unit_texts)
        self.alpha = alpha
        self.order = order
        self.n = Counter(s[i:i + order] for i in range(len(s) - order + 1))
        self.c = Counter(s[i:i + order - 1] for i in range(len(s) - order + 2))
        self.uni = Counter(s)
        tot = sum(self.uni.values())
        self.freq = {a: (self.uni[a] + 0.5) / (tot + 0.5 * len(alpha)) for a in alpha}
        self.k, self.V = k, len(alpha)
        self.cache = {}

    def logp(self, g):
        v = self.cache.get(g)
        if v is None:
            v = math.log((self.n[g] + self.k) / (self.c[g[:-1]] + self.k * self.V))
            self.cache[g] = v
        return v


def _unit_model(unit_texts, params):
    _, code = _units(params)
    return UnitModel(unit_texts, _p(params, "order", 2), alpha=ha.ALPHA + "".join(code.values()))


def _is_units(params):
    return params.get("units", "") == "syl"


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
    ha.set_alphabet(params.get("alphabet"))  # A2P4-KAL4: default (absent) restores the 24-letter fold exactly
    if _is_units(params):
        return _make_control_units(corpora, N, K, seed, params)
    text = ha.fold("\n".join(corpora))
    merge, nulls = int(params.get("merge", 0) or 0), float(params.get("nulls", 0) or 0)
    if merge or nulls:
        seq, plain, truth, info = _make_control_merged(text, N, K, seed, params, _target_sign_counts(params))
        noise = float(params.get("noise", 0) or 0)
        if noise:  # GAPS50 3 Oct 2026: noise was silently ignored on this branch; same redraw rule as the plain design
            seq = _inject_noise(seq, noise, _target_sign_counts(params), seed)
        print("homophonic merge/nulls control (seed %d): merged letters %s (share %.3f of %d letter tokens), "
              "%d null tokens over %d null signs, %d signs in all, recovery ceiling %.3f" % (
                  seed, "".join(info["merged"]) or "-", info["merged_share"], info["M"], info["n_null"],
                  info["null_types"], len(set(seq)), info["ceiling"]))
        return [seq], plain, [info["rest"]]
    if params.get("crib", "") == "drag":
        plain, rest = draw_window(text, N, seed, lambda w: len(set(w)) <= K and _plant_targets(w) is not None,
                                  tries=2000)
    else:
        plain, rest = draw_window(text, N, seed, lambda w: len(set(w)) <= K)
    model = ha.Model([rest], _p(params, "order", 3))
    noise = float(params.get("noise", 0) or 0)
    profile = params.get("profile", "")
    target_counts = _target_sign_counts(params) if (profile == "target" or noise) else None
    if profile == "target":
        seq, p, truth = _make_control_profile(plain, K, N, model, seed, target_counts)
    else:
        seq, p, truth = ha.make_control(plain, K, N, model, seed)
    if params.get("crib", "") == "drag":
        global _LAST_PLANT
        seq = _plant(seq, p)
        g, _, b, _ = _plant_targets(p)
        _LAST_PLANT = (g, b, seq, p)
    if noise:
        seq = _inject_noise(seq, noise, target_counts, seed)
    return [seq], p, [rest]


def _plant_targets(w, n6=3, n2=8):
    """crib=drag control: (6-gram, its start positions, bigram, its positions outside the 6-gram occurrences) when
    the window holds a 6-letter string >= n6 times (non-overlapping) and a bigram >= n2 times outside it, else None."""
    c6 = Counter(w[i:i + 6] for i in range(len(w) - 5))
    for g, _ in c6.most_common(5):
        starts, last = [], -6
        for i in range(len(w) - 5):
            if w[i:i + 6] == g and i >= last + 6:
                starts.append(i); last = i
        if len(starts) < n6:
            continue
        cover = {j for i in starts for j in range(i, i + 6)}
        c2 = Counter(w[i:i + 2] for i in range(len(w) - 1) if i not in cover and i + 1 not in cover
                     and not set(w[i:i + 2]) & set(g))
        for b, _ in c2.most_common(3):
            ps, last = [], -2
            for i in range(len(w) - 1):
                if w[i:i + 2] == b and i not in cover and i + 1 not in cover and i >= last + 2:
                    ps.append(i); last = i
            if len(ps) >= n2:
                return g, starts[:n6], b, ps[:n2]
    return None


def _plant(seq, plain):
    g, s6, b, s2 = _plant_targets(plain)
    seq = list(seq)
    for i in s6[1:]:
        seq[i:i + 6] = seq[s6[0]:s6[0] + 6]
    for i in s2[1:]:
        seq[i:i + 2] = seq[s2[0]:s2[0] + 2]
    return seq


def _top_repeat(seq, n, exclude=()):
    c = Counter(tuple(seq[i:i + n]) for i in range(len(seq) - n + 1))
    for g, k in c.most_common():
        if k < 3:
            return None
        if not set(g) & set(exclude):
            return g
    return None


def _consistent(signs, word):
    m = {}
    for s, a in zip(signs, word):
        if m.setdefault(s, a) != a:
            return False
    return True


def _crib_drag(seq, model, corp, seed, restarts, params):
    """crib=drag solver (module docstring). Returns (score, key, info)."""
    rng = random.Random(seed + 77)
    it_s, keep = _p(params, "drag_iters", 8000), _p(params, "keep", 5)
    uw = _p(params, "uni_weight", 1.0)
    r6 = _top_repeat(seq, 6)
    r2 = _top_repeat(seq, 2, exclude=r6 or ())
    alpha = set(model.freq)
    c6 = Counter(corp[i:i + 6] for i in range(len(corp) - 5))
    c2 = Counter(corp[i:i + 2] for i in range(len(corp) - 1))
    info = {"R6": " ".join(r6) if r6 else None, "R2": " ".join(r2) if r2 else None}
    stage1 = []
    if r6:
        cands = [w for w, _ in c6.most_common(4 * _p(params, "m6", 200)) if set(w) <= alpha and _consistent(r6, w)]
        cands = cands[:_p(params, "m6", 200)]
        if params.get("crib_oracle") and _LAST_PLANT is not None and _LAST_PLANT[2] == seq and _LAST_PLANT[0] not in cands:
            cands.append(_LAST_PLANT[0])  # diagnostic only (control): is the candidate list or the scoring the limit?
        for w in cands:
            fx = dict(zip(r6, w))
            sc, _ = ha.anneal(seq, model, it_s, rng, uw, fixed=fx)
            stage1.append((sc, w))
        stage1.sort(reverse=True)
    best6 = [w for _, w in stage1[:keep]] or [None]
    stage2 = []
    c2l = [b for b, _ in c2.most_common(4 * _p(params, "m2", 40)) if set(b) <= alpha]
    if params.get("crib_oracle") and _LAST_PLANT is not None and _LAST_PLANT[2] == seq and _LAST_PLANT[1] not in c2l:
        c2l.insert(0, _LAST_PLANT[1])
    for w in best6:
        base = dict(zip(r6, w)) if w else {}
        if not r2:
            stage2.append((stage1[0][0] if stage1 else 0.0, w, None)); continue
        n2 = 0
        for b in c2l:
            if not _consistent(r2, b):
                continue
            n2 += 1
            if n2 > _p(params, "m2", 40):
                break
            fx = dict(base); fx.update(zip(r2, b))
            sc, _ = ha.anneal(seq, model, it_s, rng, uw, fixed=fx)
            stage2.append((sc, w, b))
    stage2.sort(key=lambda x: -x[0])
    _, w, b = stage2[0]
    fx = {}
    if w:
        fx.update(zip(r6, w))
    if b:
        fx.update(zip(r2, b))
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, uw, fixed=fx)
    info.update({"crib6": w, "crib2": b, "stage1_top": [(round(x, 1), y) for x, y in stage1[:keep]],
                 "stage2_top": [(round(x, 1), y, z) for x, y, z in stage2[:5]], "n_pinned_tokens":
                 sum(1 for x in seq if x in fx)})
    return res[0][0], res[0][1], info


def _make_control_merged(text, N, K, seed, params, target_counts):
    """merge=k nulls=p: see module docstring. Returns (seq of N tokens, plain of N chars with '-' at null
    positions, truth sign -> letter or '-', info dict with merged letters, shares, ceiling and the training rest)."""
    merge, nulls = int(params.get("merge", 0) or 0), float(params.get("nulls", 0) or 0)
    null_types = int(params.get("null_types", 6) or 0) if nulls > 0 else 0
    n_null = int(round(N * nulls)) if nulls > 0 else 0
    M = N - n_null
    if M < 10:
        raise SystemExit(f"homophonic merge/nulls: nulls={nulls} leaves only {M} letter tokens of N={N}")
    K_letters = K - (1 if merge else 0) - null_types
    if K_letters < 1:
        raise SystemExit(f"homophonic merge/nulls: K={K} too small for merge={merge} null_types={null_types}")
    # the window's distinct letters, less the k merged into one sign, must fit the K_letters remaining signs
    plain, rest = draw_window(text, M, seed, lambda w: len(set(w)) - max(0, merge - 1) <= K_letters)
    rng = random.Random(seed + 4000)
    cnt = Counter(plain)
    letters = [a for a, _ in cnt.most_common()]
    merged = []
    if merge:
        merge = min(merge, len(letters))
        share = params.get("merge_share")
        if share is None or share == "":
            share = (target_counts[0] / M) if target_counts else None
        else:
            share = float(share)
        best, best_d = None, None
        for _ in range(2000):
            sub = rng.sample(letters, merge)
            if share is None:
                best = sub
                break
            d = abs(sum(cnt[a] for a in sub) / M - share)
            if best_d is None or d < best_d:
                best, best_d = sub, d
        merged = sorted(best)
    others = [a for a in letters if a not in merged]
    alloc = {a: 1 for a in others}
    extra = K_letters - len(others)
    while extra > 0 and others:
        a = max(others, key=lambda a: cnt[a] / alloc[a])
        alloc[a] += 1
        extra -= 1
    homs, i = {}, 0
    for a in others:
        homs[a] = [f"s{i + j}" for j in range(alloc[a])]
        i += alloc[a]
    for a in merged:
        homs[a] = ["sM"]
    letter_seq = [rng.choice(homs[a]) for a in plain]
    null_labels = [f"n{j}" for j in range(null_types)]
    seq, out_plain = list(letter_seq), list(plain)
    if n_null:
        for pos in sorted(rng.sample(range(N), n_null)):
            seq.insert(pos, rng.choice(null_labels))
            out_plain.insert(pos, "-")
    truth = {s: a for a, ss in homs.items() for s in ss}
    truth.update({n: "-" for n in null_labels})
    merged_count = sum(cnt[a] for a in merged)
    top_member = max((cnt[a] for a in merged), default=0)
    info = {"merged": merged, "merged_share": merged_count / M if M else 0.0, "M": M, "n_null": n_null,
            "null_types": null_types, "ceiling": 1.0 - (merged_count - top_member) / M, "rest": rest}
    return seq, "".join(out_plain), truth, info


def _make_control_units(corpora, N, K, seed, params):
    """units=syl control: an N-unit window (held out of training), K homophones over the units, same profile /
    noise options as the letter design. Returns plain as the unit string; training text as a unit string too."""
    u = encode_units("\n".join(corpora), params)
    plain, rest = draw_window(u, N, seed, lambda w: len(set(w)) <= K)
    model = _unit_model([rest], params)
    noise = float(params.get("noise", 0) or 0)
    target_counts = _target_sign_counts(params) if (params.get("profile", "") == "target" or noise) else None
    if params.get("profile", "") == "target":
        seq, p, truth = _make_control_profile_units(plain, K, N, model, seed, target_counts)
    else:
        seq, p, truth = _make_control_profile_units(plain, K, N, model, seed, None)
    if noise:
        seq = _inject_noise(seq, noise, target_counts, seed)
    return [seq], p, [rest]


def _make_control_profile_units(plain, K, N, model, seed, target_counts):
    """_make_control_profile's fair-share allotment on a unit string (no fold). target_counts None: K split by
    frequency (every present unit gets >= 1)."""
    rng = random.Random(seed + 1000)
    p = plain[:N]
    cnt = Counter(p)
    units = [a for a, _ in cnt.most_common()]
    L = len(units)
    if target_counts:
        counts = sorted((list(target_counts) + [1] * K)[:K], reverse=True)
    else:
        counts = sorted([max(1, round(N / K))] * K, reverse=True)
    reserve = counts[-L:] if L <= len(counts) else counts + [1] * (L - len(counts))
    remaining = counts[:len(counts) - L] if L <= len(counts) else []
    alloc = {a: [reserve[i]] for i, a in enumerate(reversed(units))}
    want = {a: model.freq[a] * N for a in units}
    got = {a: alloc[a][0] for a in units}
    for b in remaining:
        a = min(units, key=lambda a: got[a] / want[a] if want[a] > 0 else float("inf"))
        alloc[a].append(b)
        got[a] += b
    homs, i = {}, 0
    for a in units:
        homs[a] = [f"s{i + j}" for j in range(len(alloc[a]))]
        i += len(alloc[a])
    seq = [rng.choices(homs[a], weights=alloc[a])[0] for a in p]
    return seq, p, {s: a for a, ss in homs.items() for s in ss}


def split_decode(dec, msgs):
    """Only for units=syl (set by solve through _LAST_UNITS): one expanded-letter line per message."""
    if _LAST_UNITS is None:
        return None
    lines, pos = [], 0
    for m in msgs:
        lines.append(expand_units(dec[pos:pos + len(m)], _LAST_UNITS)); pos += len(m)
    return lines


_LAST_UNITS = None
_LAST_PLANT = None


def solve(cipher_msgs, spec, seed, restarts, corpora, params):
    global _LAST_UNITS
    _LAST_UNITS = None
    ha.set_alphabet(params.get("alphabet"))
    if _is_units(params):
        # corpora arrive as raw text for the target and as unit strings (the control's held-out rest) for a control
        # a unit string has no whitespace or punctuation; raw corpus text always has spaces
        texts = [c if re.fullmatch(r"[a-zA-Z0-9]*", c[:5000]) else encode_units(c, params) for c in corpora]
        model = _unit_model(texts, params)
        seq = [s for m in cipher_msgs for s in m]
        res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
        sc, key = res[0]
        _LAST_UNITS = dict(params)
        return "".join(key[x] for x in seq), sc, {"restart_scores": [round(r[0], 1) for r in res],
                                                 "key": {k: expand_units(v, params) for k, v in key.items()}}
    model = ha.Model(corpora, _p(params, "order", 3))
    seq = [s for m in cipher_msgs for s in m]
    wild = {w for w in str(params.get("wild", "")).split(",") if w}
    if wild:
        # H25 (28 Sept 2026): every occurrence of a wild sign is its own pseudo-sign, so the anneal gives it a
        # per-position letter under the n-gram model and the unigram KL term (ceiling 1.0 for a family sign)
        seq_w = [f"{x}#{i}" if x in wild else x for i, x in enumerate(seq)]
        res = ha.solve(seq_w, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
        sc, key = res[0]
        dec = "".join(key[x] for x in seq_w)
        wl = {w: dict(Counter(key[f"{w}#{i}"] for i, x in enumerate(seq) if x == w)) for w in wild if w in seq}
        return dec, sc, {"restart_scores": [round(r[0], 1) for r in res],
                         "key": {k: v for k, v in key.items() if "#" not in k}, "wild_letters": wl}
    if params.get("crib", "") == "drag":
        corp = ha.fold("\n".join(corpora))
        global _LAST_PLANT
        sc, key, info = _crib_drag(seq, model, corp, seed, restarts, params)
        if _LAST_PLANT is not None and _LAST_PLANT[2] == seq:  # a control: report whether the drag found the plant
            g, b, _, p = _LAST_PLANT
            fx = {x for x in seq if (info["R6"] and x in info["R6"].split()) or (info["R2"] and x in info["R2"].split())}
            info["planted"] = (g, b)
            info["crib_right"] = (info["crib6"] == g, info["crib2"] == b)
            un = [(key[x], a) for x, a in zip(seq, p) if x not in fx]
            info["unpinned_recovery"] = round(sum(1 for u, v in un if u == v) / max(1, len(un)), 3)
        _LAST_PLANT = None
        print("crib=drag:", json.dumps({k: v for k, v in info.items()}, ensure_ascii=False, default=str)[:900])
        info["key"] = key
        return "".join(key[x] for x in seq), sc, info
    res = ha.solve(seq, model, restarts, _p(params, "iters", 40000), seed, _p(params, "uni_weight", 1.0))
    sc, key = res[0]
    return "".join(key[x] for x in seq), sc, {"restart_scores": [round(r[0], 1) for r in res], "key": key}


def score_recovery(plain, truth):
    """Share of positions read correctly; a '-' in truth marks a null token (merge/nulls control) and is skipped,
    so the figure is over LETTER positions only."""
    pairs = [(a, b) for a, b in zip(plain, truth) if b != "-"]
    n = max(1, len(pairs))
    return sum(1 for a, b in pairs if a == b) / n
