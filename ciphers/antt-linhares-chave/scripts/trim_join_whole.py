#!/usr/bin/env python3
"""Trim/join enumeration re-scored by a whole-string pt18 character 5-gram (LIN-TRIM, 9 Oct 2026).

Pre-registered in PREREG-LINTRIM2.md (pushed before any scored run). Inputs and margin rule as trim_join_enum.py
(D22-LINTRIM); the scorer is one Witten-Bell character 5-gram over a-z + ' ' trained on running pt18 text (minus each
file's last 10% of words, held out), so context crosses word boundaries. Exact Viterbi, state = (last 4 chars, tokens
in current word).

Gates, in order: 1 worked example exact; 2 gluing check (DA1 windows) <= 5%; 3 planted trim/join control on held-out
windows. Exits 3 without scoring the target if any fails.

Usage: python3 scripts/trim_join_whole.py [--out trim_join_whole_result.tsv] [--windows 100] [--perms 50]
"""
import argparse, glob, gzip, math, os, random, re, sys
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import trim_join_enum as E  # noqa: E402

ORDER = 5
HOLDOUT = 0.10
THRESH = math.log(10)
MAXSPAN = 4
TARGET_TRIMS = [2, 3, 3, 4, 4, 4, 5, 6]


def load():
    train, held = [], []
    for f in sorted(glob.glob(os.path.join(E.ROOT, "tools", "data", "pt18", "*.gz"))):
        ws = re.findall(r"[a-z]+", E.fold(gzip.open(f, "rt", errors="ignore").read()))
        cut = int(len(ws) * (1 - HOLDOUT))
        train.append(ws[:cut])
        held.append(ws[cut:])
    return train, held


def build(train):
    counts = defaultdict(lambda: defaultdict(int))
    for ws in train:
        s = " " + " ".join(ws) + " "
        for i in range(1, len(s)):
            for k in range(0, ORDER):
                if i - k < 0:
                    break
                counts[s[i - k:i]][s[i]] += 1
    tot = {c: sum(d.values()) for c, d in counts.items()}
    typ = {c: len(d) for c, d in counts.items()}
    V = 27
    cache = {}

    def prob(ctx, ch):
        key = (ctx, ch)
        r = cache.get(key)
        if r is not None:
            return r
        lower = 1.0 / V if ctx == "" else prob(ctx[1:], ch)
        d = counts.get(ctx)
        p = (d.get(ch, 0) + typ[ctx] * lower) / (tot[ctx] + typ[ctx]) if d else lower
        cache[key] = p
        return p

    lcache = {}

    def extend(ctx, s):
        """log prob of appending string s after 4-char context ctx; returns (lp, new ctx)."""
        key = (ctx, s)
        r = lcache.get(key)
        if r is not None:
            return r
        lp = 0.0
        c = ctx
        for ch in s:
            lp += math.log(prob(c, ch))
            c = (c + ch)[-(ORDER - 1):]
        lcache[key] = (lp, c)
        return lp, c
    return extend


def best(vs, extend, force_var=None, force_bound=None):
    """Viterbi. Returns (total, list of (direction per token), set of joined boundaries)."""
    force_var = force_var or {}
    force_bound = force_bound or {}
    n = len(vs)
    # state key: (ctx, k tokens in current word) -> (score, back)
    states = {(" ", 0): (0.0, None)}
    for i in range(n):
        new = {}
        opts = [v for v in vs[i] if force_var.get(i, v[0]) == v[0]]
        for (ctx, k), (sc, back) in states.items():
            if i == 0:
                seps = [("", 1)]
            else:
                seps = []
                fb = force_bound.get(i - 1)
                if fb is not True:
                    seps.append((" ", 1))
                if fb is not False and k < MAXSPAN:
                    seps.append(("", k + 1))
            for sep, nk in seps:
                for d, s in opts:
                    lp, nc = extend(ctx, sep + s)
                    key = (nc, nk)
                    tot = sc + lp
                    if key not in new or tot > new[key][0]:
                        new[key] = (tot, (back, d, sep == "" and i > 0))
        states = new
    bestv = None
    for (ctx, k), (sc, back) in states.items():
        lp, _ = extend(ctx, " ")
        if bestv is None or sc + lp > bestv[0]:
            bestv = (sc + lp, back)
    tot, back = bestv
    dirs, joins = [], set()
    i = n - 1
    while back is not None:
        prev, d, j = back
        dirs.append(d)
        if j:
            joins.add(i - 1)
        back = prev
        i -= 1
    dirs.reverse()
    return tot, dirs, joins


def reading_of(vs, dirs, joins):
    out = ""
    for i, (v, d) in enumerate(zip(vs, dirs)):
        if i > 0 and (i - 1) not in joins:
            out += " "
        out += dict(v)[d]
    return out


def analyse(tokens, extend):
    vs = E.variants(tokens)
    tot, dirs, joins = best(vs, extend)
    rows = []
    for k, v in enumerate(vs):
        if len(v) < 2:
            continue
        other = [d for d, _ in v if d != dirs[k]][0]
        t2, _, _ = best(vs, extend, force_var={k: other})
        rows.append(("trim", k, tokens[k][0], dirs[k], dict(v)[dirs[k]], other, dict(v)[other], tot - t2))
    for b in range(len(vs) - 1):
        joined = b in joins
        t2, _, _ = best(vs, extend, force_bound={b: not joined})
        rows.append(("join", b, tokens[b][0] + "|" + tokens[b + 1][0], "join" if joined else "split", "", "", "", tot - t2))
    return tot, reading_of(vs, dirs, joins), rows


def glue_check(held, extend, windows=100, length=26, seed=20261007):
    # identical window draw to DA1's glue_check (held is a list of per-file word lists)
    rng = random.Random(seed)
    joined = bounds = 0
    for _ in range(windows):
        ws = held[rng.randrange(len(held))]
        i = rng.randrange(len(ws) - length)
        vs = E.variants([(w, 0) for w in ws[i:i + length]])
        _, _, joins = best(vs, extend)
        joined += len(joins)
        bounds += length - 1
    return joined / bounds


def plant_index(vocab):
    pre, suf = defaultdict(list), defaultdict(list)
    for W in vocab:
        for n in range(1, 7):
            if len(W) > n:
                pre[W[:-n]].append((W, n))   # W = w + s: end-trim gives w
                suf[W[n:]].append((W, n))    # W = s + w: front-trim gives w
    return pre, suf


def plant(w, rng, pre, suf):
    """Return (W, n, direction) for fragment w, or None."""
    dirs = ["end", "front"]
    rng.shuffle(dirs)
    for d in dirs:
        pool = pre.get(w, []) if d == "end" else suf.get(w, [])
        ok = [(W, n) for W, n in pool if W[:-n] != W[n:]]
        if not ok:
            continue
        want = rng.choice(TARGET_TRIMS)
        pref = [x for x in ok if x[1] == want]
        W, n = rng.choice(pref or ok)
        return W, n, d
    return None


def make_window(held, rng, pre, suf, length=26):
    while True:
        ws = held[rng.randrange(len(held))]
        i = rng.randrange(len(ws) - length)
        words = ws[i:i + length]
        order = list(range(length))
        rng.shuffle(order)
        trims, join_word = {}, None
        for j in order:
            if len(trims) < 8:
                p = plant(words[j], rng, pre, suf)
                if p:
                    trims[j] = p
            elif join_word is None and len(words[j]) >= 4:
                cut = rng.randrange(1, len(words[j]))
                a, b = words[j][:cut], words[j][cut:]
                pa, pb = plant(a, rng, pre, suf), plant(b, rng, pre, suf)
                if pa and pb:
                    join_word = (j, pa, pb)
            if len(trims) == 8 and join_word:
                break
        if len(trims) < 8 or not join_word:
            continue
        toks, truth_dir, truth_join = [], {}, set()
        for j, w in enumerate(words):
            if j in trims:
                W, n, d = trims[j]
                truth_dir[len(toks)] = d
                toks.append((W, n))
            elif join_word and j == join_word[0]:
                for k, (W, n, d) in enumerate(join_word[1:]):
                    truth_dir[len(toks)] = d
                    if k == 0:
                        truth_join.add(len(toks))
                    toks.append((W, n))
            else:
                toks.append((w, 0))
        return toks, truth_dir, truth_join


def score_control(windows, extend, scramble_seed=None):
    st = Counter()
    rng = random.Random(scramble_seed) if scramble_seed is not None else None
    for toks, tdir, tjoin in windows:
        if rng:
            idx = list(range(len(toks)))
            rng.shuffle(idx)
            toks = [toks[i] for i in idx]
            tdir = {idx.index(k): d for k, d in tdir.items()}
            tjoin = set()  # order destroyed: no true joins remain
        _, _, rows = analyse(toks, extend)
        for r in rows:
            m = r[-1]
            if r[0] == "trim":
                st["trims"] += 1
                if m >= THRESH:
                    st["trim_res"] += 1
                    st["trim_res_ok"] += r[3] == tdir[r[1]]
                st["trim_ok_any"] += r[3] == tdir[r[1]]
            else:
                planted = r[1] in tjoin
                st["planted_joins" if planted else "other_bounds"] += 1
                if r[3] == "join":
                    if planted:
                        st["join_hit"] += 1
                    else:
                        st["false_join"] += 1
                    if m >= THRESH:
                        st["join_res"] += 1
                        st["join_res_ok"] += planted
    return st


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "..", "trim_join_whole_result.tsv"))
    ap.add_argument("--windows", type=int, default=100)
    ap.add_argument("--perms", type=int, default=50)
    a = ap.parse_args()
    train, held = load()
    extend = build(train)
    print(f"pt18 train words={sum(map(len, train))}, held-out words={sum(map(len, held))}, order={ORDER}, whole-string")
    out = [("set", "kind", "idx", "item", "chosen", "chosen_str", "alt", "alt_str", "margin", "resolved")]

    tot, reading, rows = analyse(E.WORKED, extend)
    ok1 = reading == E.WORKED_ANSWER
    print(f"GATE 1 worked example: {reading!r} score {tot:.2f} -> {'PASS' if ok1 else 'FAIL'}")
    for r in rows:
        out.append(("control",) + tuple(r[:-1]) + (f"{r[-1]:.3f}", str(r[-1] >= THRESH)))
    if not ok1:
        print("non-test: whole-string scorer fails gate 1")
        E.write(a.out, out)
        return 3

    fj = glue_check(held, extend)
    ok2 = fj <= 0.05
    print(f"GATE 2 gluing check: false-join rate {fj:.4f} (100 x 25 boundaries) -> {'PASS' if ok2 else 'FAIL'}")
    out.append(("glue", "summary", "", "100x26", f"false_join_rate={fj:.4f}", "", "", "", "", str(ok2)))
    if not ok2:
        print("non-test: whole-string scorer fails gate 2")
        E.write(a.out, out)
        return 3

    vocab = Counter(w for ws in train for w in ws)
    pre, suf = plant_index([w for w, c in vocab.items() if c >= 3])
    rng = random.Random(20261009)
    wins = [make_window(held, rng, pre, suf) for _ in range(a.windows)]
    st = score_control(wins, extend)
    tprec = st["trim_res_ok"] / st["trim_res"] if st["trim_res"] else 0.0
    tres = st["trim_res"] / st["trims"]
    jprec = st["join_res_ok"] / st["join_res"] if st["join_res"] else 0.0
    frate = st["false_join"] / st["other_bounds"]
    ok3 = tprec >= 0.90 and tres >= 0.30 and jprec >= 0.80 and frate <= 0.05
    print(f"GATE 3 planted control ({a.windows} windows): trim resolved {st['trim_res']}/{st['trims']} ({tres:.3f}), "
          f"resolved precision {tprec:.3f}, any-margin accuracy {st['trim_ok_any'] / st['trims']:.3f}; "
          f"joins resolved {st['join_res']} precision {jprec:.3f}, planted-join recall (argmax) {st['join_hit']}/{st['planted_joins']}; "
          f"false-join rate {st['false_join']}/{st['other_bounds']} = {frate:.4f} -> {'PASS' if ok3 else 'FAIL'}")
    out.append(("planted", "summary", "", f"{a.windows} windows", f"trim_res={st['trim_res']}/{st['trims']}",
                f"trim_res_prec={tprec:.3f}", f"join_res_prec={jprec:.3f} ({st['join_res']})",
                f"join_recall={st['join_hit']}/{st['planted_joins']}", f"false_join={frate:.4f}", str(ok3)))
    ss = score_control(wins, extend, scramble_seed=20261010)
    sp = ss["trim_res_ok"] / ss["trim_res"] if ss["trim_res"] else 0.0
    print(f"  scrambled-order control: trim resolved {ss['trim_res']}/{ss['trims']}, precision {sp:.3f}; "
          f"joins resolved {ss['join_res']}, false joins {ss['false_join']}/{ss['other_bounds']}")
    out.append(("planted_scrambled", "summary", "", "", f"trim_res={ss['trim_res']}/{ss['trims']}", f"trim_res_prec={sp:.3f}",
                f"join_res={ss['join_res']}", "", f"false_join={ss['false_join'] / ss['other_bounds']:.4f}", ""))
    if not ok3:
        print("non-test: whole-string scorer fails gate 3")
        E.write(a.out, out)
        return 3

    tot, reading, rows = analyse(E.TARGET, extend)
    print(f"TARGET: {reading!r} score {tot:.2f}")
    rng = random.Random(20261006)
    null_trim = defaultdict(list)
    null_join = []
    for _ in range(a.perms):
        toks = E.TARGET[:]
        rng.shuffle(toks)
        _, _, prow = analyse(toks, extend)
        for r in prow:
            if r[0] == "trim":
                null_trim[r[2]].append(r[-1])
            elif r[3] == "join":
                null_join.append(r[-1])

    def p95(xs):
        xs = sorted(xs)
        return xs[min(len(xs) - 1, int(math.ceil(0.95 * len(xs))) - 1)] if xs else float("-inf")
    jp95 = p95(null_join)
    print(f"NULL ({a.perms} perms): pooled join-margin p95 {jp95:.3f} over {len(null_join)} chosen joins")
    for r in rows:
        m = r[-1]
        if r[0] == "trim":
            np95 = p95(null_trim[r[2]])
            res = m >= THRESH and m > np95
            call = ("context-resolved, = committed" if r[3] == "end" else "context-resolved, S candidate") if res else "M"
            extra = f"null_p95={np95:.3f};{call}"
        else:
            res = r[3] == "join" and m >= THRESH and m > jp95
            extra = f"join_p95={jp95:.3f};{'I candidate' if res else ''}"
        out.append(("target",) + tuple(r[:-1]) + (f"{m:.3f}", f"{res};{extra}"))
        if r[0] == "trim" or r[3] == "join" or m < THRESH:
            print("  " + "\t".join(str(x) for x in r[:-1]) + f"\t{m:.3f}\t{extra}")
    out.append(("null", "summary", "", f"{a.perms} perms", f"join_p95={jp95:.3f}", "", "", "", "", ""))
    E.write(a.out, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
