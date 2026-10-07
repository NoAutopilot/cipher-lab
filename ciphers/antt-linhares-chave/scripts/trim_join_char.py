#!/usr/bin/env python3
"""Trim/join enumeration re-scored by a pt18 letter 5-gram (DA1-LIN, 7 Oct 2026).

Pre-registered in NOTES.md "Front-trim and adjacent-join enumeration, letter n-gram scorer (DA1-LIN, 7 Oct 2026)".
The enumerator (variants, exact DP, margins) is imported unchanged from trim_join_enum.py; only the scorer differs:
an interpolated Witten-Bell character 5-gram over a-z + '#' (word boundary), trained on tools/data/pt18 minus the
last 10% of words of each file (held out). A word w scores log P('#w#').

Gate 1: worked-example known-answer control. Gate 2: gluing check, 100 held-out windows of 26 fixed words,
false-join rate <= 5%. Exits 3 without scoring the target if either fails.

Usage: python3 scripts/trim_join_char.py [--out trim_join_char_result.tsv]
"""
import argparse, glob, gzip, math, os, random, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import trim_join_enum as E  # noqa: E402

ORDER = 5
HOLDOUT = 0.10
GLUE_MAX = 0.05
GLUE_WINDOWS, GLUE_LEN, GLUE_SEED = 100, 26, 20261007


def load_words():
    train, held = [], []
    for f in sorted(glob.glob(os.path.join(E.ROOT, "tools", "data", "pt18", "*.gz"))):
        ws = re.findall(r"[a-z]+", E.fold(gzip.open(f, "rt", errors="ignore").read()))
        cut = int(len(ws) * (1 - HOLDOUT))
        train += ws[:cut]
        held.append(ws[cut:])
    return train, held


def build(words):
    # counts[ctx][ch], ctx length 0..ORDER-1
    counts = defaultdict(lambda: defaultdict(int))
    for w in words:
        s = "#" + w + "#"
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
        if key in cache:
            return cache[key]
        if ctx == "":
            lower = 1.0 / V
        else:
            lower = prob(ctx[1:], ch)
        if ctx in counts:
            t, u = tot[ctx], typ[ctx]
            p = (counts[ctx].get(ch, 0) + u * lower) / (t + u)
        else:
            p = lower
        cache[key] = p
        return p

    wcache = {}

    def score(w):
        if w in wcache:
            return wcache[w]
        s = "#" + w + "#"
        lp = 0.0
        for i in range(1, len(s)):
            ctx = s[max(0, i - ORDER + 1):i]  # first char: '#' alone
            lp += math.log(prob(ctx, s[i]))
        wcache[w] = lp
        return lp
    return score


def glue_check(held, score):
    rng = random.Random(GLUE_SEED)
    joined = bounds = 0
    for _ in range(GLUE_WINDOWS):
        ws = held[rng.randrange(len(held))]
        i = rng.randrange(len(ws) - GLUE_LEN)
        toks = [(w, 0) for w in ws[i:i + GLUE_LEN]]
        _, words = E.best(E.variants(toks), score)
        joined += GLUE_LEN - len(words)
        bounds += GLUE_LEN - 1
    return joined / bounds


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "..", "trim_join_char_result.tsv"))
    ap.add_argument("--perms", type=int, default=20)
    a = ap.parse_args()
    train, held = load_words()
    score = build(train)
    print(f"pt18 train words={len(train)}, held-out words={sum(map(len, held))}, order={ORDER}")
    out = [("set", "kind", "idx", "item", "chosen", "chosen_str", "alt", "alt_str", "margin", "resolved")]
    tot, reading, rows = E.analyse(E.WORKED, score)
    ok1 = reading == E.WORKED_ANSWER
    print(f"GATE 1 worked example: {reading!r} score {tot:.2f} -> {'PASS' if ok1 else 'FAIL'}")
    for r in rows:
        out.append(("control",) + tuple(r[:-1]) + (f"{r[-1]:.3f}", str(r[-1] >= E.THRESH)))
    if not ok1:
        print("non-test: letter-n-gram scorer fails gate 1")
        E.write(a.out, out)
        return 3
    fj = glue_check(held, score)
    ok2 = fj <= GLUE_MAX
    print(f"GATE 2 gluing check: false-join rate {fj:.4f} ({GLUE_WINDOWS} windows x {GLUE_LEN - 1} boundaries) -> {'PASS' if ok2 else 'FAIL'}")
    out.append(("glue", "summary", "", f"{GLUE_WINDOWS}x{GLUE_LEN}", f"false_join_rate={fj:.4f}", "", "", "", "", str(ok2)))
    if not ok2:
        print("non-test: letter-n-gram scorer fails gate 2")
        E.write(a.out, out)
        return 3
    tot, reading, rows = E.analyse(E.TARGET, score)
    print(f"TARGET: {reading!r} score {tot:.2f}")
    for r in rows:
        out.append(("target",) + tuple(r[:-1]) + (f"{r[-1]:.3f}", str(r[-1] >= E.THRESH)))
        if r[0] == "trim" or r[3] == "join" or r[-1] < E.THRESH:
            print("  " + "\t".join(str(x) for x in r[:-1]) + f"\t{r[-1]:.3f}\t{r[-1] >= E.THRESH}")
    rng = random.Random(20261006)
    tr = jr = 0
    for _ in range(a.perms):
        toks = E.TARGET[:]
        rng.shuffle(toks)
        _, _, prow = E.analyse(toks, score)
        tr += sum(1 for r in prow if r[0] == "trim" and r[-1] >= E.THRESH)
        jr += sum(1 for r in prow if r[0] == "join" and r[-1] >= E.THRESH and r[3] == "join")
    print(f"NULL scrambled order ({a.perms} perms): mean resolved trim decisions {tr / a.perms:.2f}, mean resolved joins {jr / a.perms:.2f}")
    out.append(("null", "summary", "", f"{a.perms} perms", f"trim_resolved_mean={tr / a.perms:.2f}", f"join_resolved_mean={jr / a.perms:.2f}", "", "", "", ""))
    E.write(a.out, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
