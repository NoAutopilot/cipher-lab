#!/usr/bin/env python3
"""Matched controls (rule 3) and ciphertext-only target runs for bowes-walsingham-1583, 23 Sept 2026.

Shape: the target's eleven fragment lengths [14,7,10,26,1,10,7,9,9,3,5] (101 tokens). Controls:
 a  one-to-one substitution, running English cut from Surtees vol.14 (letters before CLXXXVII) at word bounds
 b  as a, with two homophones each for e and a (the target's own doubled vowels)
 c  as a, with F5 and F10 replaced by code-name signs (fresh symbols; excluded from the accuracy count)
 d  the target's real design: every fragment is a proper name or name phrase from Surtees vol.14 (other letters)
Model: 4-grams from tools/data (Holmes, Moby Dick) + Surtees vol.14 text up to line 15000 (disjoint from the
control plaintext, which is drawn from lines 15000-22500, and from the target letters, lines 22900+).
Writes control/results.tsv and appends target/baseline rows to runs.tsv.
"""
import json, random, re, sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import subst_hillclimb as sh

LENS = [14, 7, 10, 26, 1, 10, 7, 9, 9, 3, 5]
RESTARTS, ITERS = 100, 20000
surt = open(os.path.join(HERE, "..", "corpus", "correspondenceof00bowerich_djvu.txt"), encoding="utf-8", errors="replace").read().split("\n")
train = "\n".join(surt[:15000])
pool = "\n".join(surt[15000:22500])
model = sh.Model([open(os.path.join(ROOT, "tools/data", f), encoding="utf-8").read() for f in ("pg1661_holmes.txt", "pg2701_mobydick.txt")] + [train])

words = [sh.norm(w) for w in re.findall(r"[A-Za-z]+", pool)]
words = [w for w in words if w]
names = [sh.norm(w) for w in re.findall(r"(?<![.!?]\s)\b[A-Z][a-z]{3,}", pool)]
nc = Counter(names)
common = {"that", "this", "with", "which", "your", "majesty", "bowes", "correspondence", "king", "queen", "therefore", "thus", "whereupon", "besides", "sir", "lord", "earl", "letter", "from", "edinburgh"}
namelist = [n for n, c in nc.items() if c >= 2 and n not in common]


def running_text(rng, n):
    """Consecutive words from the pool whose letters total exactly n (retry until a fit)."""
    while True:
        i = rng.randrange(len(words) - 50)
        s = ""
        for w in words[i:i + 40]:
            s += w
            if len(s) >= n:
                break
        if len(s) == n:
            return s


def name_text(rng, n):
    for _ in range(20000):
        s = ""
        while len(s) < n:
            s += rng.choice(namelist)
        if len(s) == n:
            return s
    return running_text(rng, n)


def make(design, seed):
    rng = random.Random(seed)
    plain = [(name_text if design == "d" else running_text)(rng, L) for L in LENS]
    syms = [f"{i:02d}" for i in range(2, 60)]
    rng.shuffle(syms)
    it = iter(syms)
    key = {c: [next(it)] for c in sh.ALPHA}
    if design == "b":
        for c in "ea":
            key[c].append(next(it))
    frags, truth = [], []
    for k, p in enumerate(plain):
        if design == "c" and k in (4, 9):
            frags.append([next(it) for _ in p]); truth.append([None] * len(p)); continue
        frags.append([rng.choice(key[c]) for c in p]); truth.append(list(p))
    return frags, truth, plain


def accuracy(res, frags, truth):
    ok = n = 0
    for f, t in zip(frags, truth):
        for s, c in zip(f, t):
            if c is None:
                continue
            n += 1; ok += res["key"][s] == c
    return ok, n


if __name__ == "__main__":
    rows = ["design\tseed\ttrue_key_score\tsymbols\ttokens_scored\ttokens_correct\tpct\tscore_per_token\tbest_restart\trestarts\titers\tplaintext\treading"]
    for design in "abcd":
        for seed in (11, 12, 13):
            frags, truth, plain = make(design, seed)
            tr = sum(model.score_frags([sh.np.array([sh.IDX[x] for x in q])]) for q in plain) / 101
            res = sh.anneal(frags, model, RESTARTS, ITERS, seed=seed)
            ok, n = accuracy(res, frags, truth)
            nsym = len({t for f in frags for t in f})
            rows.append(f"{design}\t{seed}\t{tr:.3f}\t{nsym}\t{n}\t{ok}\t{100*ok/n:.1f}\t{res['score_per_token']:.3f}\t{res['best_restart']}\t{RESTARTS}\t{ITERS}\t{'|'.join(plain)}\t{'|'.join(res['reading'])}")
            print(rows[-1], flush=True)
    open(os.path.join(HERE, "results.tsv"), "w").write("\n".join(rows) + "\n")
    # target and shuffled baseline, same settings
    tf = sh.load_cipher(os.path.join(HERE, "..", "ciphertext.txt"))
    out = []
    res = sh.anneal(tf, model, RESTARTS, ITERS, seed=1)
    out.append(("T1", "target, ciphertext-only, control settings", res))
    for s in (101, 102, 103):
        r = sh.anneal(sh.shuffle_frags(tf, s), model, RESTARTS, ITERS, seed=s)
        out.append((f"B{s-100}", f"target tokens shuffled seed {s}, same settings", r))
    json.dump({k: v for k, _, v in out}, open(os.path.join(HERE, "target_runs.json"), "w"), indent=1)
    for k, d, r in out:
        print(k, d, f"{r['score_per_token']:.3f}", "|".join(r["reading"]), flush=True)
