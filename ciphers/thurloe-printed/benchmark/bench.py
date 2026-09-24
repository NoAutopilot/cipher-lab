#!/usr/bin/env python3
"""Fauconberg benchmark (LANE T worker F, 24 Sept 2026): how well do our two ciphertext-only solvers read a real
1658 homophonic letter cipher, scored against Birch's printed decipherment, and a synthetic control of the
same length and homophone structure?

  python3 bench.py            run everything, write results.tsv, groundtruth_key.tsv, synth_key.tsv
  python3 bench.py --check    rerun and exit 1 if results.tsv differs (the seconds column is ignored)
  python3 bench.py --quick    fewer restarts/iterations, prints only (smoke test)

Solvers, fed the group sequences only (no crib, no fixed values):
  hillclimb  tools/subst_hillclimb.py anneal(), its defaults (40 restarts x 6000 iters, max 2 homophones),
             24-letter alphabet (i=j, u=v), 4-gram model from corpus.lm_texts().
  anneal     tools/nomenclator_anneal.py solve(), its defaults (8 restarts x 100000 iters, homo cap 4) with
             syllable, word and null values switched off (the Fauconberg system has none); 5-gram model built
             with tools/italian_ngram.build() from the same corpus. That model folds y->i, w->u, k->c, so this
             solver is scored against the truth folded the same way (21 letters).
Data: real = data.groups() (P16-P24 cipher lines, 3,024 groups in 243 fragments); synth = corpus.control_plain()
enciphered with the ground-truth key's homophone sets, each group drawn with its real relative frequency, cut
into the same fragment lengths. Sizes 300, 600, 1200 (contiguous fragments from a seeded start, last one cut)
and all; seeds 1-3 choose the subset and seed the solver.
truth_score_per_tok (hillclimb only): the same model's score for the true key on the same input; above
score_per_tok means the search missed a better key, below it means the model prefers a wrong key.
Scores: tok_acc = share of scored tokens read right; dist_acc = share of distinct scored groups read right.
Real tokens are scored only where data.truth() gives the group a letter (39 of 45 groups).
"""
import argparse, csv, io, json, os, random, sys, tempfile, time
from collections import Counter, defaultdict
from multiprocessing import Pool
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[2] / "tools"))
import data, corpus  # noqa: E402
import subst_hillclimb as sh  # noqa: E402

SIZES = [300, 600, 1200, "all"]
SEEDS = [1, 2, 3]
AFOLD = str.maketrans({"y": "i", "w": "u", "k": "c", "j": "i", "v": "u"})


def synth(frags, key):
    inv = defaultdict(list)
    for g, c in key.items():
        inv[c].append(g)
    cnt = Counter(g for f in frags for g in f)
    nxt = 61
    for c in sh.ALPHA:
        if c not in inv:
            inv[c] = [nxt]; nxt += 1
    n = sum(map(len, frags))
    text, span = corpus.control_plain(n + 50)
    plain = sh.norm(text)[:n]
    rng = random.Random(1658)
    out, k = [], 0
    for f in frags:
        seg = []
        for ch in plain[k:k + len(f)]:
            gs = inv[ch]
            seg.append(rng.choices(gs, weights=[cnt.get(g, 0) + 1 for g in gs])[0])
        out.append(seg); k += len(f)
    tkey = {g: c for c, gs in inv.items() for g in gs}
    return out, tkey, span


def subset(frags, size, seed):
    if size == "all":
        return frags
    rng = random.Random(1000 * size + seed)
    tot = [sum(map(len, frags[i:])) for i in range(len(frags))]
    i = rng.choice([j for j, t in enumerate(tot) if t >= size])
    out, n = [], 0
    while n < size:
        f = frags[i][:size - n]
        out.append(f); n += len(f); i += 1
    return out


def score(frags, got, truth, fold=None):
    fx = (lambda c: c.translate(AFOLD)) if fold else (lambda c: c)
    toks = [g for f in frags for g in f if g in truth]
    ok = sum(fx(got.get(g, "?")) == fx(truth[g]) for g in toks)
    ds = sorted(set(toks))
    dok = sum(fx(got.get(g, "?")) == fx(truth[g]) for g in ds)
    return len(toks), ok / max(1, len(toks)), len(ds), dok / max(1, len(ds))


_M = None


def run_hill(job):
    global _M
    name, size, seed, frags, truth, quick = job
    if _M is None:
        _M = sh.Model(corpus.lm_texts())
    t = time.time()
    r = sh.anneal([[str(g) for g in f] for f in frags], _M, restarts=6 if quick else 40,
                  iters=2000 if quick else 6000, seed=seed)
    got = {int(k): v for k, v in r["key"].items()}
    tk = {g: truth.get(g, got[g]) for g in got}  # the true key, solver's letter where truth has none
    ts = _M.score_frags([sh.np.array([sh.IDX[tk[g]] for g in f]) for f in frags]) / sum(map(len, frags))
    return ("hillclimb", name, size, seed, sum(map(len, frags))) + score(frags, got, truth) + \
        (round(r["score_per_token"], 4), round(ts, 4), round(time.time() - t))


def run_anneal(job, model_path):
    import nomenclator_anneal as na
    name, size, seed, frags, truth, quick = job
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
        fh.write(" .\n".join(" ".join(f"g{g}" for g in f) for f in frags) + "\n")
    t = time.time()
    r = na.solve([fh.name], model_path, restarts=4 if quick else 8, iters=20000 if quick else 100000,
                 caps=dict(syl=0, word=0, null=0, homo=4), syl="none", words=[], dots=True, seed=seed, procs=4)
    os.unlink(fh.name)
    got = {int(k[1:]): v for k, v in r["best"]["key"].items()}
    return ("anneal", name, size, seed, sum(map(len, frags))) + score(frags, got, truth, fold=True) + \
        (round(r["per_token"], 4), "", round(time.time() - t))


def build_anneal_model(path):
    import numpy as np, italian_ngram as ing
    lines = [ing.norm(p) for t in corpus.lm_texts() for p in t.split("\n\n") if p.strip()]
    llr, p1 = ing.build([l for l in lines if len(l) > 20], 5)
    np.savez_compressed(path, llr=llr, p1=p1, order=5, syms=ing.SYMS)


COLS = ["solver", "data", "size", "seed", "ntok", "scored_tok", "tok_acc", "scored_groups", "dist_acc",
        "score_per_tok", "truth_score_per_tok", "seconds"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true"); ap.add_argument("--quick", action="store_true")
    ap.add_argument("--only", choices=["hillclimb", "anneal"])
    a = ap.parse_args()
    real = data.groups()
    tkey, votes, _, _ = data.truth()
    sfr, skey, span = synth(real, tkey)
    jobs = []
    for name, fr, tr in (("real", real, tkey), ("synth", sfr, skey)):
        for size in SIZES:
            for seed in SEEDS:
                jobs.append((name, size, seed, subset(fr, size, seed), tr, a.quick))
    rows = []
    if a.only != "anneal":
        with Pool(4) as p:
            rows += p.map(run_hill, jobs)
    if a.only != "hillclimb":
        mp = str(HERE / "anneal_model.npz")
        if not os.path.exists(mp):
            build_anneal_model(mp)
        for j in jobs:
            rows.append(run_anneal(j, mp)); print(rows[-1], file=sys.stderr)
    rows = [tuple(round(x, 4) if isinstance(x, float) else x for x in r) for r in rows]
    buf = io.StringIO(); w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(COLS); w.writerows(rows)
    out = buf.getvalue()
    if a.quick:
        print(out); return
    res = HERE / "results.tsv"
    if a.check:
        strip = lambda s: [l.rsplit("\t", 1)[0] for l in s.strip().split("\n")]
        same = strip(res.read_text()) == strip(out)
        print("results.tsv " + ("up to date" if same else "STALE")); sys.exit(0 if same else 1)
    res.write_text(out)
    with open(HERE / "groundtruth_key.tsv", "w") as fh:
        fh.write("# group\tletter\tvotes (data.truth(): Birch's printed decipherment, exact lines + offset-aligned +-3 lines)\n")
        for g in sorted(votes):
            fh.write(f"{g}\t{tkey.get(g, '-')}\t" + " ".join(f"{c}:{n}" for c, n in votes[g].most_common()) + "\n")
    with open(HERE / "synth_key.tsv", "w") as fh:
        fh.write(f"# synthetic control key; plaintext = vol. 7 djvu lines {span[0]}-{span[1]} (English, windows excluded)\n")
        for g in sorted(skey):
            fh.write(f"{g}\t{skey[g]}\n")
    print(out)


if __name__ == "__main__":
    main()
