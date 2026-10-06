#!/usr/bin/env python3
"""Front-trim / end-trim and adjacent-join enumeration for antt-linhares-chave (D22-LINTRIM, 6 Oct 2026).

Pre-registered in NOTES.md "Front-trim and adjacent-join enumeration (D22-LINTRIM, 6 Oct 2026)".
Each trimmed token has {W[:-n], W[n:]}; a word is 1-4 consecutive tokens joined; scorer S1 is an
accent-folded pt18 word unigram (in-vocab ln(c/N), OOV ln(0.1/N) - len). The best configuration is
an exact DP maximum; margins are best-with-choice minus best-with-opposite-forced.

Usage: python3 scripts/trim_join_enum.py [--out trim_join_result.tsv]
Runs the worked-example known-answer control first; exits 3 without scoring the target if it fails.
"""
import argparse, glob, gzip, math, os, random, re, sys, unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
THRESH = math.log(10)
MAXSPAN = 4

# (headword, trim); trim 0 = fixed token
WORKED = [("aba", 2), ("guerra", 0), ("de", 0), ("franco", 1), ("anao", 3), ("com", 0), ("abicar", 5),
          ("rustico", 4), ("sillaba", 5), ("acaso", 4), ("parecer", 1), ("inevitavel", 0)]
WORKED_ANSWER = "a guerra de franca com a russia parece inevitavel"
TARGET = [("para", 0), ("supprir", 0), ("ovo", 2), ("seu", 0), ("lugar", 0), ("junto", 0), ("com", 0),
          ("mando", 2), ("ouros", 4), ("d", 0), ("justa", 0), ("hernia", 4), ("segredo", 0), ("ate", 0),
          ("paralisia", 5), ("odio", 3), ("ministerio", 0), ("pela", 0), ("memoria", 0), ("dormitar", 6),
          ("cagar", 0), ("lhe", 0), ("pauperrimo", 3), ("venablo", 4), ("habil", 3), ("logo", 0)]


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


def load_model():
    cnt = Counter()
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", "data", "pt18", "*.gz"))):
        cnt.update(re.findall(r"[a-z]+", fold(gzip.open(f, "rt", errors="ignore").read())))
    n = sum(cnt.values())
    oov = math.log(0.1 / n)

    def score(w):
        c = cnt.get(w, 0)
        return math.log(c / n) if c else oov - len(w)
    return score, cnt, n


def variants(tokens):
    out = []
    for w, t in tokens:
        if t == 0:
            out.append([("fixed", w)])
        else:
            v = [("end", w[:-t])]
            if w[t:] != w[:-t]:
                v.append(("front", w[t:]))
            out.append(v)
    return out


def best(vs, score, force_var=None, force_bound=None):
    """Exact max. force_var: {i: direction}; force_bound: {b: True(join)/False(split)} for boundary b between i and i+1."""
    force_var = force_var or {}
    force_bound = force_bound or {}
    n = len(vs)
    allowed = [[v for v in vs[i] if force_var.get(i, v[0]) == v[0]] for i in range(n)]
    dp = [(-1e18, None)] * (n + 1)
    dp[0] = (0.0, [])
    for j in range(1, n + 1):
        for i in range(max(0, j - MAXSPAN), j):
            if dp[i][1] is None:
                continue
            # word spans tokens i..j-1: internal boundaries joined, boundary i-1 and j-1 split
            if any(force_bound.get(b) is False for b in range(i, j - 1)):
                continue
            if j < n and force_bound.get(j - 1) is True:
                continue
            # build best choice of variants for the span (product, small)
            combos = [("", [])]
            for k in range(i, j):
                combos = [(s + v[1], ch + [v[0]]) for s, ch in combos for v in allowed[k]]
            if not combos:
                continue
            w, ch = max(combos, key=lambda c: score(c[0]))
            tot = dp[i][0] + score(w)
            if tot > dp[j][0]:
                dp[j] = (tot, dp[i][1] + [(i, j, w, ch)])
    return dp[n]


def analyse(tokens, score):
    vs = variants(tokens)
    tot, words = best(vs, score)
    reading = " ".join(w for _, _, w, _ in words)
    chosen = {}
    for i, j, w, ch in words:
        for k, d in zip(range(i, j), ch):
            chosen[k] = d
    splits = {j - 1 for (_, j, _, _) in words[:-1]}
    rows = []
    for k, v in enumerate(vs):
        if len(v) < 2:
            continue
        other = [d for d, _ in v if d != chosen[k]][0]
        t2, _ = best(vs, score, force_var={k: other})
        rows.append(("trim", k, tokens[k][0], chosen[k], dict(v)[chosen[k]], other, dict(v)[other], tot - t2))
    for b in range(len(vs) - 1):
        joined = b not in splits
        t2, _ = best(vs, score, force_bound={b: not joined})
        rows.append(("join", b, tokens[b][0] + "|" + tokens[b + 1][0], "join" if joined else "split", "", "", "", tot - t2))
    return tot, reading, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(HERE, "..", "trim_join_result.tsv"))
    ap.add_argument("--perms", type=int, default=20)
    a = ap.parse_args()
    score, cnt, n = load_model()
    print(f"pt18 tokens N={n}, vocab={len(cnt)}")
    tot, reading, rows = analyse(WORKED, score)
    ok = reading == WORKED_ANSWER
    print(f"CONTROL worked example: {reading!r} score {tot:.2f} -> {'PASS' if ok else 'FAIL'}")
    out = [("set", "kind", "idx", "item", "chosen", "chosen_str", "alt", "alt_str", "margin", "resolved")]
    for r in rows:
        out.append(("control",) + tuple(r[:-1]) + (f"{r[-1]:.3f}", str(r[-1] >= THRESH)))
    if not ok:
        print("non-test: enumerator fails its known-answer control")
        write(a.out, out)
        return 3
    tot, reading, rows = analyse(TARGET, score)
    print(f"TARGET: {reading!r} score {tot:.2f}")
    for r in rows:
        out.append(("target",) + tuple(r[:-1]) + (f"{r[-1]:.3f}", str(r[-1] >= THRESH)))
    rng = random.Random(20261006)
    tr = jr = 0
    for p in range(a.perms):
        toks = TARGET[:]
        rng.shuffle(toks)
        _, _, prow = analyse(toks, score)
        tr += sum(1 for r in prow if r[0] == "trim" and r[-1] >= THRESH)
        jr += sum(1 for r in prow if r[0] == "join" and r[-1] >= THRESH and r[3] == "join")
    print(f"NULL scrambled order ({a.perms} perms): mean resolved trim decisions {tr / a.perms:.2f}, mean resolved joins {jr / a.perms:.2f}")
    out.append(("null", "summary", "", f"{a.perms} perms", f"trim_resolved_mean={tr / a.perms:.2f}", f"join_resolved_mean={jr / a.perms:.2f}", "", "", "", ""))
    write(a.out, out)
    return 0


def write(path, rows):
    with open(path, "w") as f:
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")


if __name__ == "__main__":
    sys.exit(main())
